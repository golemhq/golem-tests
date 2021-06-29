from projects.golem_api.pages import project


def test_project_has_tests(data):
    project_name = project.create_random_project()
    response = project.get_project_has_tests(project_name)
    assert response.json() is False
    project.create_test(project_name)
    response = project.get_project_has_tests(project_name)
    assert response.json() is True
