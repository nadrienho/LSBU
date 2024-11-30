from flask import Flask,render_template
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('intro.html')

@app.route('/cakes')
def cakes():
    return render_template('intro.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
