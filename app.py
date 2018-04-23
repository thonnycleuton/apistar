# Django specific settings
import os
import typing

from apistar import App, Route, types, validators

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_star.settings")

# Ensure settings are read
from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()

# Your application specific
from django_orm.models import User as UserDB


class User(types.Type):
    user_identity = validators.String(max_length=50)
    full_name = validators.String(max_length=100)
    status = validators.String(enum=['active', 'inactive'])


def welcome(name=None):
    if name is None:
        return {'message': 'Welcome to API Star!'}
    return {'message': 'Welcome to API Star, %s!' % name}


def list_users() -> typing.List[User]:
    try:
        queryset = UserDB.objects.all()
        return [User(record) for record in queryset]
    except Exception as e:
        print(e)


def create_users() -> typing.List[User]:
    queryset = None
    return [User(record) for record in queryset]


routes = [
    Route('/', method='GET', handler=welcome),
    Route('/users/', method='GET', handler=list_users),
    Route('/users/', method='POST', handler=create_users)
]

app = App(routes=routes)

if __name__ == '__main__':
    app.serve('127.0.0.1', 5000, use_debugger=True, use_reloader=True)
