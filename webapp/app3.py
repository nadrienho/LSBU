from flask import Flask,render_template
import random
def is_leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False
app = Flask(__name__)

@app.route('/')
def index():
    random_year = random.randint(1, 2021)
    leap_year_status = "is a leap year" if is_leap_year(random_year) else "is not a leap year"
    
    return render_template('leapyear.html', year=random_year, leap_year_status=leap_year_status)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
