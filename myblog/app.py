from sanic import Sanic
from sanic.response import text
from sanic_jinja2 import SanicJinja2


app = Sanic(__name__)

jinja = SanicJinja2(app)
render_template = jinja.render


@app.route('/')
@app.route('index')
async def index(request):
    return render_template('index.html', request)


@app.route('/about')
async def about(request):
    return render_template('about.html', request)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)


