from sanic import Sanic
app = Sanic(__name__)
from . import views

