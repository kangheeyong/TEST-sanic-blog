from .. import app


def test_url_for():
    assert app.url_for('index') == '/'
    assert app.url_for('about') == '/about'
    assert app.url_for('static', filename='layout.css', name='css') == '/css/layout.css'
    assert app.url_for('static', filename='default.png', name='profile_imgs') == '/profile_imgs/default.png'



def test_response_200():
    request, response = app.test_client.get('/')
    assert response.status == 200

    request, response = app.test_client.get('/about')
    assert response.status == 200

    request, response = app.test_client.get('/css/layout.css')
    assert response.status == 200

    request, response = app.test_client.get('/profile_imgs/default.png')
    assert response.status == 200



