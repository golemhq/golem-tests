from projects.golem_api.pages import golem_


def test(data):
    response = golem_.get_default_browser()
    assert response.status_code == 200
