from flask import Flask, render_template
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    actual_year = datetime.datetime.today().year
    #Actual anniversary
    countdown = datetime.date(actual_year, 1, 21) - datetime.date.today()
    if countdown.days == 0:
        return render_template('index.html')
    #Next Anniversary countdown
    countdown = datetime.date(actual_year + 1, 1, 21) - datetime.date.today()
    return render_template('wait.html', countdown=countdown.days)