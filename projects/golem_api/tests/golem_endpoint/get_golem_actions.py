from projects.golem_api.pages import golem_


def test(data):
    response = golem_.get_golem_actions()
    assert response.status_code == 200
    assert response.headers['Cache-Control'] == 'max-age=604800, public'
    action = [x for x in response.json() if x['name'] == 'click']
    assert len(action) == 1
