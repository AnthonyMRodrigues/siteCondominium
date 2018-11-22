import flask
import flask_restful
import resources

apiBp = flask.Blueprint('api', __name__)
api = flask_restful.Api(apiBp)

api.add_resource(resources.Hello, '/hello')

