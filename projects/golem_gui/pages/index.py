from golem import actions
from golem.browser import elements


create_project_button = ('css', "#projectCreationButton button", 'Create Project button')
title = ('css', "h4", 'Title')
project_name_input = ('id', "newProjectName", 'Project Name input')
create_button = ('id', "createProjectCreate", 'Create button')
project_list_item = ('css', '#projectList>a')
error_list_items = ('css', '#errorList li', 'error_list_item')
error_modal = ('id', 'errorModal', 'error_modal')


def _project_exists(project_name):
    items = elements(project_list_item)
    project_names = [x.text for x in items]
    return project_name in project_names


def assert_project_exists(project_name):
    actions.take_screenshot('verify the project exists in the list')
    assert _project_exists(project_name), 'Project {} does not exists'.format(project_name)


def assert_error_message(error_message):
    actions.wait_for_element_displayed(error_modal)
    items = elements(error_list_items)
    error_messages = [x.text for x in items]
    msg = 'verify the application shows the error message: {}'.format(error_message)
    actions.take_screenshot(msg)
    assert error_message in error_messages, 'Error message {} is not present'.format(error_message)


def access_project(project_name):
    actions.step('Access project {}'.format(project_name))
    items = elements(project_list_item)
    for item in items:
        if item.text == project_name:
            item.click()
            return
    raise Exception('Project {} not found'.format(project_name))


def create_project(project_name):
    actions.click(create_project_button)
    actions.wait_for_element_displayed(project_name_input)
    actions.send_keys(project_name_input, project_name)
    actions.click(create_button)
    actions.wait_for_element_displayed(create_project_button)


def create_access_project(project_name):
    if not _project_exists(project_name):
        create_project(project_name)
    access_project(project_name)

