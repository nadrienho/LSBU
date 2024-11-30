from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def index():
    name = "Adrien Ngassam"
    age = 26
    student_id = "S4402831" 
    course = "Computer Science"
    university = "London South Bank University"
    return render_template('index.html',name=name,age=age,student_id=student_id,course=course,university=university)
@app.route('/aboutme')
def myprofile():
    return render_template('aboutme.html')  


@app.route('/printcredit')
def printcredit():
    return f"Print the Profile<br> No more credit left"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
