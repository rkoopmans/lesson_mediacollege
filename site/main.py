from flask import Flask, render_template, request
from distance import get_distance

app = Flask(__name__)


@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=None):
    name = "World" if not name else name
    return "Hello %s" % name


@app.route('/')
def index():
    return render_template('index.html', title='home')


@app.route('/distance', methods=['POST', 'GET'])
def distance():
    result = None
    if request.method == 'POST':
        location_a = request.form['location_a']
        location_b = request.form['location_b']
        result = get_distance(location_a, location_b)

    return render_template('distance.html', title='Afstand', result=result)

if __name__ == '__main__':
    app.run(debug=True)
