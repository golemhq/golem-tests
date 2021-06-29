from golem import actions

from projects.golem_gui.pages import index
from projects.golem_gui.pages import common


description = 'Verify the user can create a new project in the index page'

tags = ['smoke']


def setup(data):
    common.access_golem(data.env.url, data.env.admin)


def test_create_project(data):
    actions.navigate(data.env.url)
    project_name = actions.random_str()
    actions.click(index.create_project_button)
    actions.wait_for_element_displayed(index.project_name_input)
    actions.send_keys(index.project_name_input, project_name)
    actions.click(index.create_button)
    actions.wait_for_element_not_displayed(index.create_button)
    assert index.project_is_present(project_name)


def test_create_project_with_invalid_name(data):
    actions.navigate(data.env.url)
    actions.click(index.create_project_button)
    actions.send_keys(index.project_name_input, 'project_test_$')
    actions.click(index.create_button)
    common.assert_error_message('Only letters, numbers and underscores are allowed')


def test_create_project_with_blank_name(data):
    actions.navigate(data.env.url)
    actions.click(index.create_project_button)
    actions.click(index.create_button)
    common.assert_error_message('Project name is too short')


def test_create_project_name_is_too_short(data):
    actions.navigate(data.env.url)
    actions.click(index.create_project_button)
    actions.send_keys(index.project_name_input, actions.random_str(2))
    actions.click(index.create_button)
    common.assert_error_message('Project name is too short')


def test_create_project_name_exists(data):
    actions.navigate(data.env.url)
    actions.click(index.create_project_button)
    project_name = actions.random_str()
    actions.send_keys(index.project_name_input, project_name)
    actions.click(index.create_button)
    actions.click(index.create_project_button)
    actions.send_keys(index.project_name_input, project_name)
    actions.click(index.create_button)
    common.assert_error_message('A project with that name already exists')


def test_create_project_spaces_replaced_with_underscores(data):
    actions.navigate(data.env.url)
    project_name = actions.random_str(prefix='project ')
    actions.click(index.create_project_button)
    actions.wait_for_element_displayed(index.project_name_input)
    actions.send_keys(index.project_name_input, project_name)
    actions.click(index.create_button)
    actions.wait_for_element_not_displayed(index.create_button)
    assert index.project_is_present(project_name.replace(' ', '_'))
