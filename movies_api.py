from flask import Flask
from flask_restx import Api

from movies import movie_namespace
from directors import director_namespace
from genres import genre_namespace

app = Flask(__name__)
api = Api(app)

api.add_namespace(movie_namespace)
api.add_namespace(director_namespace)
api.add_namespace(genre_namespace)

if __name__ == '__main__':
    app.run(debug=True)
