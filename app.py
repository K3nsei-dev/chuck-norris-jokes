from flask import Flask, render_template
import requests


app = Flask(__name__)


@app.route('/', methods=['GET'])
def get_chuck_norris_jokes():
    api_url = "https://api.chucknorris.io/jokes/random"
    response = requests.get(api_url).json()

    return render_template('home.html', api_url=api_url, response=response['value'])


@app.route('/apidata')
def api():
    api_url = "https://api.chucknorris.io/jokes/random"
    response = requests.get(api_url).json()

    return render_template('api.html', api_url=api_url, response=response)


if __name__ == '__main__':
    app.run(debug=True)
