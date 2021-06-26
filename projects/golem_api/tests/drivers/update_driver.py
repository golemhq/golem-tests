from projects.golem_api.pages import drivers


def test_update_driver_with_invalid_driver_name(data):
    response = drivers.update_driver('incorrectDriver')
    assert response.status_code == 200
    assert response.json() == 'incorrectDriver is not a valid driver name'
