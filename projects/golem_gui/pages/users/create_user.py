from golem.browser import element, get_browser
from golem import actions

from projects.golem_gui.pages import urls
from projects.golem_gui.pages import utils
from projects.golem_gui.pages.common import get_autocomplete_suggestions
from projects.golem_gui.pages.users.reset_password_prompt import send_reset_password_prompt as reset_password


username = ('css', 'input#username', 'Username input')
email = ('css', 'input#email', 'Email input')
password = ('css', 'input#password', 'Password input')
superuser_checkbox = ('css', 'input#isSuperuser', 'Super User checkbox')
project_select = ('css', 'input#project', 'Project select input')
permission_select = ('css', 'input#permission', 'Permission select input')
add_permission_button = ('css', 'button#addPermissionButton', 'Add Permission button')
create_user_button = ('css', 'button#createUserButton', 'Create User button')
update_user_button = ('css', 'button#updateUserButton', 'Update User button')
project_permission_table = ('id', 'projectPermissionList', 'Project Permission table')
reset_password_button = ('id', 'resetPassword', 'Reset Password button')


def navigate_to_page():
    actions.step('Navigate to /users/new')
    get_browser().navigate(urls.users_new())


def assert_project_suggestion_list():
    expected_projects = utils.get_projects() + ['all projects']
    project_select_ = element(project_select)
    project_select_.focus()
    suggestions = get_autocomplete_suggestions()
    assert sorted(suggestions) == sorted(expected_projects)


def select_project(project):
    actions.step('Select project {}'.format(project))
    element(project_select).send_keys(project)


def select_permission(permission):
    actions.step('Select permission {}'.format(permission))
    element(permission_select).send_keys(permission)


def project_permission_in_table(project, permission):
    rows = element(project_permission_table).find_all('tr')
    for row in rows:
        tds = row.find_all('td')
        if tds[0].text == project and tds[1].text == permission:
            return row
    return False


def assert_project_permission_in_table(project, permission):
    if not project_permission_in_table(project, permission):
        msg = '{} - {} was not found in Project Permission table'.format(project, permission)
        raise AssertionError(msg)


def add_project_permission(project, permission):
    actions.step('Add project permission: {}, {}'.format(project, permission))
    element(project_select).send_keys(project)
    element(permission_select).send_keys(permission)
    element(add_permission_button).click()


def remove_project_permission(project, permission):
    row = project_permission_in_table(project, permission)
    row.find('button.close').click()


def send_reset_password_prompt(new_password):
    reset_password(new_password)
