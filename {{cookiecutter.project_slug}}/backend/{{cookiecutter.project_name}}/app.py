from flask import Flask

from {{cookiecutter.project_name}}.api.v1 import auth

def create_app(test_config=None):
    """Application factory, used to create application."""
    app = Flask("{{cookiecutter.project_name}}", instance_relative_config=True)

    if test_config is None:
        # load the instance config, it it exists, when not in testing mode.
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load test config if passed in
        app.config.from_mapping(test_config)

    
    register_blueprints(app)

    return app



def register_blueprints(app: Flask):
    """Register all blueprints for application."""
    app.register_blueprint(auth.bp)


if __name__ == "__main__":
    create_app()

