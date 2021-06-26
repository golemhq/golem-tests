from projects.golem_api.pages import drivers


def test_get_driver_files(data):
    response = drivers.get_driver_files()
    assert response.status_code == 200
    assert type(response.json()) is list
