from projects.golem_api.pages import drivers


def test_delete_driver_files_does_not_exist(data):
    response = drivers.delete_driver('nonexistent.file')
    assert response.status_code == 200
    assert response.json() == ['File nonexistent.file does not exist']
