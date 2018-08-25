# Django specific settings
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_star.settings")

from apistar import App, Route
from django_orm.views import *

# Ensure settings are read
from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()


def welcome(name=None):
    if name is None:
        return {'message': 'Welcome to API Star!'}
    return {'message': 'Welcome to API Star, %s!' % name}


routes = [
    Route('/', method='GET', handler=welcome),
    Route('/users/', method='GET', handler=list_users),
    Route('/users/', method='POST', handler=create_users),
    Route('/products/', method='GET', handler=list_products),
    Route('/products/', method='POST', handler=create_product),
]

app = App(routes=routes)

if __name__ == '__main__':
    app.serve('127.0.0.1', 8000, use_debugger=True, use_reloader=True)
