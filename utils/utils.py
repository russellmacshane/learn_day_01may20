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

    def sensor(self):
        """ Function for test purposes. """
        print("Scheduler is alive!")

    def save_confirmed(self, confirmed):
        f = open("assets/stats", "a")
        f.write(f'{str(confirmed)}\n')
        f.close()

    def all_confirmed(self):
        f = open("assets/stats", "r")
        return f.read()

