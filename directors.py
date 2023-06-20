from flask_restx import Namespace, Resource

director_namespace = Namespace('directors', description='Directors API')


@director_namespace.route('/')
class DirectorResource(Resource):
    def get(self):
        # Логика для получения списка всех режиссеров
        pass


@director_namespace.route('/<int:id>')
class DirectorDetailResource(Resource):
    def get(self, id):
        # Логика для получения подробной информации о режиссере по идентификатору
        pass


@director_namespace.route('/')
class DirectorResource(Resource):
    def post(self):
        # Логика для создания нового режиссера
        pass


@director_namespace.route('/<int:id>')
class DirectorDetailResource(Resource):
    def put(self, id):
        # Логика для обновления информации о режиссере по идентификатору
        pass

    def delete(self, id):
        # Логика для удаления режиссера по идентификатору
        pass
