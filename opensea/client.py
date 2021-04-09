import requests
import pandas as pd


class OpenseaClient:

    def __init__(self):
        self.key = ""
        self.base_url = "https://api.opensea.io/api/v1"
        self._format = pd.DataFrame

    def _build_url(self, endpoint, query):
        url = f"{self.base_url}/{endpoint}"

        query_list = []
        for key, value in query.items():
            if type(value) == list:
                for item in value:
                    query_list.append(
                        f"{key}={item}"
                    )
            else:
                query_list.append(
                    f"{key}={value}"
                )

        if query_list:
            url += f"?{'&'.join(query_list)}"

        return url

    def _call_get_api(self, endpoint, querystring):
        url = self._build_url(endpoint, querystring)
        try:
            response = requests.get(url)
            # response = requests.request(
            #     "GET",
            #     self._build_url(endpoint),
            #     params=querystring
            # )
            return response.json()
        except Exception as e:
            pass
        return

    def retrieve_assets(self, **kwargs):
        querystring = {
            "order_direction": "desc",
            "offset": "0",
            "limit": "20"
        }
        querystring.update(kwargs)

        return self._call_get_api("assets", querystring)

    def retrieve_bundles(self, **kwargs):
        querystring = {
            "offset": "0",
            "limit": "20"
        }
        querystring.update(kwargs)

        return self._call_get_api("bundles", querystring)
