from datetime import datetime

from sanic import Sanic
from sanic_jinja2 import SanicJinja2


app = Sanic(__name__)

jinja = SanicJinja2(app)
render_template = jinja.render

posts = [
    {
        'author': {
            'username': 'test-user'
        },
        'title': '첫 번째 포스트',
        'content': '첫 번째 포스트 내용입니다.',
        'date_posted': datetime.strptime('2018-08-01', '%Y-%m-%d')
    },
    {
        'author': {
            'username': 'test-user'
        },
        'title': '두 번째 포스트',
        'content': '두 번째 포스트 내용입니다.',
        'date_posted': datetime.strptime('2018-08-03', '%Y-%m-%d')
    },
]

app.static('css/', './static/css/', name='css')


@app.route('/')
@app.route('/index')
async def index(request):
    return render_template('index.html', request, posts=posts)


@app.route('/about')
async def about(request):
    return render_template('about.html', request, title='about')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)


