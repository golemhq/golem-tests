
pages = ['project']


def setup(data):
    store('project', random('dddddd'))
    project.create_project(data.project)


def test(data):
    response = project.get_project_has_tests(data.project)
    assert not response.json()
    project.create_project_test(data.project, random('dddd'))
    response = project.get_project_has_tests(data.project)
    assert response.json()
