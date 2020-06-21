import os
from datetime import datetime

from sanic_jinja2 import SanicJinja2

from . import app
from .models import Post


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

jinja = SanicJinja2(app)
render_template = jinja.render

app.static('css/', os.path.join(BASE_DIR, 'static', 'css'), name='css')
app.static('profile_imgs/', os.path.join(BASE_DIR, 'static', 'profile_imgs'), name='profile_imgs')



@app.route('/')
@app.route('/index')
async def index(request):
    posts = Post.query.all()
    print(posts)
    return render_template('index.html', request, posts=posts)


@app.route('/about')
async def about(request):
    return render_template('about.html', request, title='about')


