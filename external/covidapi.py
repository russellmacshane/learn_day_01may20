import requests

from external import utils


class CovidAPI:
    def __init__(self):
        self.endpoint = 'https://api.covid19api.com'

    def get_summary(self):
        return self._get_from_api('summary')

    def get_worldwide(self):
        resp, status_code = self.get_summary()
        return resp['Global'], status_code

    def get_united_states(self):
        resp, status_code = self.get_summary()

        for country in resp['Countries']:
            if country['CountryCode'] == 'US':
                return utils.summary_output(country), status_code

    def _get_from_api(self, endpoint):
        resp = requests.get(f'{self.endpoint}/{endpoint}')
        if resp.status_code == 200:
            return resp.json(), 200
        else:
            return "CovidAPI Exception", resp.status_code
