from flask import Flask
from external.covidapi import CovidAPI
from utils.utils import Utils
from apscheduler.schedulers.background import BackgroundScheduler

app = Flask(__name__)
covid_api = CovidAPI()
utils = Utils()

sched = BackgroundScheduler(daemon=True)
sched.add_job(covid_api.get_world_confirmed, 'interval', minutes=60)
sched.start()
