class Utils:
    def summary_output(self, json):
        return {
            'NewConfirmed': json['NewConfirmed'],
            'TotalConfirmed': json['TotalConfirmed'],
            'NewDeaths': json['NewDeaths'],
            'TotalDeaths': json['TotalDeaths'],
            'NewRecovered': json['NewRecovered'],
            'TotalRecovered': json['TotalRecovered']
        }

