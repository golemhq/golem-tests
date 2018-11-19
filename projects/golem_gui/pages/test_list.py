from golem import actions
from golem.browser import elements

from projects.golem_gui.pages import list_common


error_modal = ('id', 'errorModal', 'Error modal')


def add_test(fullpath):
    list_common._add_tree_element('test', fullpath)


def add_directory(fullpath):
    list_common._add_directory('test', fullpath)


def assert_test_exists(fullpath):
    assert test_exists(fullpath), 'test {} does not exist'.format(fullpath)


def test_exists(fullpath):
    return list_common._elem_exists('test', fullpath)


def directory_exists(fullpath):
    return list_common._directory_exists('test', fullpath)


def assert_error_message(error_message):
    actions.step('Verify that the error {} is displayed'.format(error_message))
    actions.wait_for_element_displayed(error_modal)
    errors = elements(css='#errorList>li')
    for error in errors:
        if error.text == error_message:
            return
    raise Exception('Error message {} was not found'.format(error_message))


def access_test(fullpath):
    list_common._access_elem('test', fullpath)


def create_access_test(fullpath):
    """Access a test from the list, create it if it does not exist"""
    if not test_exists(fullpath):
        add_test(fullpath)
    access_test(fullpath)


def create_access_random_test():
    test_name = 'test_' + actions.random('dddddd')
    add_test(test_name)
    access_test(test_name)


def add_test_directory_if_not_exists(fullpath):
    if not directory_exists(fullpath):
        add_directory(fullpath)


def rename_test(old_full_name, new_full_name):
    list_common._rename_elem('test', old_full_name, new_full_name)


