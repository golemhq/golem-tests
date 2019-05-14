
pages = ['project', 'settings']


def setup(data):
    store('project', random('dddddd'))
    project.create_project(data.project)


def test(data):
    response = settings.save_settings(data.project, '{}', '{}')
    assert response.status_code == 200
    assert response.json() == 'settings-saved'
