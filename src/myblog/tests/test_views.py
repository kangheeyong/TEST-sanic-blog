from .. import app


def test_url_for():
    assert app.url_for('home') == '/'
    assert app.url_for('about') == '/about'
    assert app.url_for('static', filename='main.css', name='css') == '/css/main.css'


def test_response_200():
    request, response = app.test_client.get('/')
    assert response.status == 200

    request, response = app.test_client.get('/about')
    assert response.status == 200

    request, response = app.test_client.get('/css/main.css')
    assert response.status == 200




