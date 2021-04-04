from flask import Flask
from containers import Container
import views
from flask_bootstrap import Bootstrap

def create_app() -> Flask:
	container = Container()
	container.config.from_ini('config.ini')

	app = Flask(__name__)
	app.container = container
	app.add_url_rule('/', 'index', views.index)

	bootstrap = Bootstrap()
	bootstrap.init_app(app)

	return app