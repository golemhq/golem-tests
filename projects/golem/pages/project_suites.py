from golem import actions
from golem.browser import element, elements

from projects.golem.pages import project_common


error_modal = ('id', 'errorModal', 'Error modal')


def add_suite(name):
    project_common._add_tree_element('suite', name)
    

def verify_suite_exists(name):
    project_common._verify_elem_exists('suite', name)


def verify_error_message(error_message):
    actions.step('Verify that the error {} is displayed'.format(error_message))
    actions.wait_for_element_visible(error_modal)
    errors = elements(css='#errorList>li')
    for error in errors:
        if error.text == error_message:
            return
    raise Exception('Error message {} was not found'.format(error_message))


def access_suite(name):
    project_common._access_elem('suite', name)


def create_access_suite(fullpath):
    """Access a page from the list, create it if it does not exist"""
    try:
        verify_suite_exists(fullpath)
    except:
        add_suite(fullpath)
    access_suite(fullpath)
