from golem import actions
from golem.browser import element, elements, get_browser

from projects.golem.pages import project_common


error_modal = ('id', 'errorModal', 'Error modal')


def add_test(fullpath):
    project_common._add_tree_element('test', fullpath)


def add_test_directory(fullpath):
    project_common._add_directory('test', fullpath)


def verify_test_exists(fullpath):
    project_common._verify_elem_exists('test', fullpath)


def verify_error_message(error_message):
    actions.step('Verify that the error {} is displayed'.format(error_message))
    actions.wait_for_element_visible(error_modal)
    errors = elements(css='#errorList>li')
    for error in errors:
        if error.text == error_message:
            return
    raise Exception('Error message {} was not found'.format(error_message))


def access_test(fullpath):
    project_common._access_elem('test', fullpath)


def create_access_test(fullpath):
    """Access a test from the list, create it if it does not exist"""
    try:
        verify_test_exists(fullpath)
    except:
        add_test(fullpath)
    access_test(fullpath)


def create_access_random_test():
    test_name = 'test_' + actions.random('dddddd')
    add_test(test_name)
    access_test(test_name)


def add_test_directory_if_not_exists(fullpath):
    try:
        verify_test_exists(fullpath)
    except:
        add_test_directory(fullpath)


def rename_test(old_full_name, new_full_name):
    project_common._rename_elem('test', old_full_name, new_full_name)


