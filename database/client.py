#!/usr/bin/python

from .config import config
import logging

import pandas as pd
import psycopg2
from psycopg2.extras import execute_values

logger = logging.getLogger()


class DBClient:

    def __init__(self):
        self.conn = self.connect_to_db()
        self.keys = {}
        self.get_keys()

    @staticmethod
    def connect_to_db():
        """ Connect to the PostgreSQL database server """
        conn = None
        try:
            # read connection parameters
            params = config()

            # connect to the PostgreSQL server
            logger.info("Connecting to the PostgreSQL database...")
            print("Connecting to the PostgreSQL database...")
            conn = psycopg2.connect(**params)

            # create a cursor
            with conn.cursor() as cur:
                # execute a statement
                logger.info("PostgreSQL database version:")
                cur.execute("SELECT version()")

                # display the PostgreSQL database server version
                db_version = cur.fetchone()
                logger.info(db_version)
                print(db_version)

        except (Exception, psycopg2.DatabaseError) as error:
            logger.error(error)
            print(error)

        return conn

    def get_keys(self):
        query = """
        SELECT table_name, column_name
        FROM information_schema.constraint_column_usage
        """
        key_records = self.select_from_db(query)
        for table_name, column_name in key_records:
            if table_name not in self.keys:
                self.keys[table_name] = [column_name]
            else:
                self.keys[table_name].append(column_name)

    def reset_keys(self):
        self.keys = {}

    def insert_many_to_db(self, table_name, dataframe):
        dataset = [tuple(x) for x in dataframe.to_numpy()]
        columns = ",".join(list(dataframe.columns))
        query = """
            INSERT INTO %s (%s) 
            VALUES %%s
        """ % (table_name, columns)

        keys = ",".join(self.keys.get(table_name))
        if keys != "":
            query += """
                ON CONFLICT (%s)
                DO NOTHING
            """ % keys

        try:
            with self.conn.cursor() as cursor:
                execute_values(cursor, query, dataset)
            self.conn.commit()

        except (Exception, psycopg2.Error) as error:
            logger.error(error)

    def update_many_to_db(self, table_name, dataframe):
        dataset = [tuple(x) for x in dataframe.to_numpy()]
        columns = ",".join(list(dataframe.columns))
        query = """
            INSERT INTO %s (%s) 
            VALUES %%s
        """ % (table_name, columns)

        value_columns = list(set(dataframe.columns) - set(self.keys.get(table_name)))
        value_columns_in_query = [
            f" {v} = EXCLUDED.{v} " for v in value_columns
        ]
        keys = ",".join(self.keys.get(table_name))
        if len(value_columns_in_query) > 0:
            query += """
                ON CONFLICT (%s)
                DO UPDATE
                SET
                %s
            """ % (keys, ",".join(value_columns_in_query))

        try:
            with self.conn.cursor() as cursor:
                execute_values(cursor, query, dataset)
            self.conn.commit()

        except (Exception, psycopg2.Error) as error:
            logger.error(error)

    def insert_to_db(self, table_name, dataframe):
        pass

    def select_from_db(self, query, output="list"):
        with self.conn.cursor() as cur:
            cur.execute(query)
            records = cur.fetchall()
            columns = [item[0] for item in cur.description]

        if output == "pandas":
            return pd.DataFrame(records, columns=columns)
        return records
