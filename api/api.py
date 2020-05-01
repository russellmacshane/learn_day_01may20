from api import app
from api import covid_api
from api import utils


@app.route('/')
def hello_world():
    return "Welcome to the Covid API - Learning Day May 01, 2020"


@app.route('/summary')
def get_summary():
    return covid_api.get_summary()


@app.route('/worldwide')
def get_worldwide():
    return covid_api.get_worldwide()


@app.route('/usa')
def get_united_states():
    return covid_api.get_united_states()


@app.route('/confirmed')
def all_confirmed():
    return utils.all_confirmed()
