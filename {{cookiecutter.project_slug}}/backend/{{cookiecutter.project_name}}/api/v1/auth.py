from flask import (
    Blueprint
)
from {{cookiecutter.project_name}}.api.v1 import API_PREFIX

bp = Blueprint('auth', __name__, url_prefix=API_PREFIX)