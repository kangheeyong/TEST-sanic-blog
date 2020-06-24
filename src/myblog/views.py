import os

from sanic.response import redirect
from sanic_jinja2 import SanicJinja2
from sanic_session import InMemorySessionInterface

from . import app
from .models import Post
from .forms import LoginForm, RegistrationForm

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

jinja = SanicJinja2(app)
render_template = jinja.render


app.static('css/', os.path.join(BASE_DIR, 'static', 'css'), name='css')


@app.route('/')
@app.route('/home')
async def home(request):
    posts = Post.query.all()
    return render_template('home.html', request, posts=posts)


@app.route('/about')
async def about(request):
    return render_template('about.html', request, title='about')


@app.route("/register", methods=["GET", "POST"])
def register(request):
    form = RegistrationForm()
    #if form.validate():
#        flash('Acount created for {}!'.format(form.username.data), 'success')
    #    return redirect(app.url_for('home'))
    return render_template('register.html', request, title='Register', form=form)


@app.route("/login", methods=["GET", "POST"])
def login(request):
    form = LoginForm()
#    if form.validate():
#        if form.email.data == 'admin@blog.com' and form.password.data == '123':
#            flash('You have been logged in!', 'success')
#            return redirect(app.url_for('home'))
#        else:
#            flash('Login Unsuccessful. Please check username and password', 'danger')

    return render_template('login.html', request, title='Login', form=form)


