from flask import Flask
import cmath
import random
app = Flask(__name__)
def calculate_earth_circumference():#function to calculate the circumference of earth
    radius_of_earth = 6371 
    circumference = 2 * 3.14 * radius_of_earth
    print(f"The circumference of the Earth is: {circumference} kilometers")
@app.route('/')
def index():
        return(calculate_earth_circumference())

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
