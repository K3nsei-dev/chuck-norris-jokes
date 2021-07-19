from flask import Flask
import requests

app = Flask(__name__)


@app.route('/', methods=['GET'])
def get_chuck_norris_jokes():
    api_url = "https://api.chucknorris.io/jokes/random"
    response = requests.get(api_url).json()

    return "<strong>Random Joke From Chuck Norris:</strong>" and response['value']


if __name__ == '__main__':
    app.run(debug=True)
