from projects.golem_api.pages import project


def setup(data):
    project.using_project('general')


def test(data):
    response = project.get_project_tags(data.project)
    assert response.status_code == 200
