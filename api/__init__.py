from flask import Flask
from external.covidapi import CovidAPI

app = Flask(__name__)
covid_api = CovidAPI()
