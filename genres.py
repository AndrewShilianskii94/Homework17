from flask_restx import Namespace, Resource

genre_namespace = Namespace('genres', description='Genres API')


@genre_namespace.route('/')
class GenreResource(Resource):
    def get(self):
        # Логика для получения списка всех жанров
        pass


@genre_namespace.route('/<int:id>')
class GenreDetailResource(Resource):
    def get(self, id):
        # Логика для получения информации о жанре с перечислением списка фильмов по жанру
        pass


@genre_namespace.route('/')
class GenreResource(Resource):
    def post(self):
        # Логика для создания нового жанра
        pass


@genre_namespace.route('/<int:id>')
class GenreDetailResource(Resource):
    def put(self, id):
        # Логика для обновления информации о жанре по идентификатору
        pass

    def delete(self, id):
        # Логика для удаления жанра по идентификатору
        pass
