from flask import Flask, render_template
from astral import LocationInfo
from astral.sun import sun
import datetime


app = Flask(__name__)


def is_day():
    now = datetime.datetime.now()
    # now = now + datetime.timedelta(hours=14)
    city = LocationInfo("Moscow")
    s = sun(city.observer, date=datetime.datetime.now())
    if s["sunrise"].time() < now.time() <  s["dusk"].time():
        return True
    else:
        return False   


def calculate_suntimes():
    city = LocationInfo("Moscow")
    s = sun(city.observer, date=datetime.datetime.now())
    time_data = {
        'Sunrise': s["sunrise"].time().strftime("%H:%M:%S"),
        'Dusk': s["dusk"].time().strftime("%H:%M:%S")
    }
    if is_day():
        return time_data['Dusk']
    else:
        return time_data['Sunrise']  

 
@app.route('/')
def home():
    obj = {
        'time_to': calculate_suntimes(),
        'is_day': is_day()
    }
    return render_template('home_template.html', data=obj)


app.run(host='0.0.0.0', port=88)