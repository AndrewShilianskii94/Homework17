from flask_restx import Namespace, Resource

movie_namespace = Namespace('movies', description='Movies API')


@movie_namespace.route('/')
class MovieResource(Resource):
    def get(self):
        # Логика для получения списка всех фильмов
        pass


@movie_namespace.route('/<int:id>')
class MovieDetailResource(Resource):
    def get(self, id):
        # Логика для получения подробной информации о фильме по идентификатору
        pass


@movie_namespace.route('/')
class MovieResource(Resource):
    def post(self):
        # Логика для создания нового фильма
        pass


@movie_namespace.route('/<int:id>')
class MovieDetailResource(Resource):
    def put(self, id):
        # Логика для обновления информации о фильме по идентификатору
        pass

    def delete(self, id):
        # Логика для удаления фильма по идентификатору
        pass
