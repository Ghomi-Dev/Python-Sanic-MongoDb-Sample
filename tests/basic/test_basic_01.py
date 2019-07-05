import pytest
from sanic import response, Sanic
from sanic.websocket import WebSocketProtocol


def test_fixture_unused_port(unused_port):
    assert unused_port > 1024 and unused_port < 65535

@pytest.yield_fixture
def app():
    app = Sanic("test_sanic_app")

    @app.route("/test_get", methods=['GET'])
    async def test_get(request):
        return response.json({"GET": True})

    @app.route("/test_post", methods=['POST'])
    async def test_post(request):
        return response.json({"POST": True})

    yield app

@pytest.fixture
def test_cli(loop, app, test_client):
    return loop.run_until_complete(test_client(app, protocol=WebSocketProtocol))

async def test_fixture_test_client_get(test_cli):
    """
    GET request
    """
    resp = await test_cli.get('/test_get')
    assert resp.status == 200
    resp_json = await resp.json()
    assert resp_json == {"GET": True}


async def test_fixture_test_client_post(test_cli):
    """
    POST request
    """
    resp = await test_cli.post('/test_post')
    assert resp.status == 200
    resp_json = await resp.json()
    assert resp_json == {"POST": True}