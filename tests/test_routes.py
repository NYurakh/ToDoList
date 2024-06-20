import pytest
from src.app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_route_post_empty_list_name(client):
    rv = client.post('/home', data={'list_name': ''}, follow_redirects=True)
    assert b'List name cannot be empty' in rv.data

def test_show_list_route_post_empty_todo_name(client):
    rv = client.post('/list/1', data={'todo_name': ''}, follow_redirects=True)
    assert b'Todo name cannot be empty' in rv.data


# Add more tests as needed for other routes and scenarios

if __name__ == '__main__':
    pytest.main()
