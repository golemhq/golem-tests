from golem import actions
from golem.browser import elements

from projects.golem_gui.pages import list_common


error_modal = ('id', 'errorModal', 'Error modal')


def add_suite(name):
    list_common._add_tree_element('suite', name)
    

def suite_exists(fullpath):
    return list_common._elem_exists('suite', fullpath)


def assert_suite_exists(fullpath):
    assert suite_exists(fullpath), 'suite {} does not exist'.format(fullpath)


def assert_error_message(error_message):
    actions.step('Verify that the error {} is displayed'.format(error_message))
    actions.wait_for_element_displayed(error_modal)
    errors = elements(css='#errorList>li')
    for error in errors:
        if error.text == error_message:
            return
    raise AssertionError('Error message {} was not found'.format(error_message))


def access_suite(name):
    list_common._access_elem('suite', name)


def create_access_suite(fullpath):
    """Access a page from the list, create it if it does not exist"""
    if not suite_exists(fullpath):
        add_suite(fullpath)
    access_suite(fullpath)


def create_access_random_suite():
    suite_name = 'test_' + actions.random('dddddd')
    add_suite(suite_name)
    access_suite(suite_name)


def rename_suite(old_full_name, new_full_name):
    list_common._rename_elem('suite', old_full_name, new_full_name)