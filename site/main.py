from flask import Flask, render_template, request
import urllib
import json

app = Flask(__name__)


def get_distance(location_a, location_b):
    params = urllib.urlencode({'origins': location_a, 'destinations': location_b})
    response = urllib.urlopen('https://maps.googleapis.com/maps/api/distancematrix/json?%s' % params)
    return json.loads(response.read())


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
