from golem import actions
from golem.browser import element, elements

from projects.golem.pages import project_common


error_modal = ('id', 'errorModal', 'Error modal')


def add_page(fullpath):
    project_common._add_tree_element('page', fullpath)


def add_page_directory(fullpath):
    project_common._add_directory('page', fullpath)


def verify_page_exists(fullpath):
    project_common._verify_elem_exists('page', fullpath)


def verify_page_directory_exists(fullpath):
    pages_tree_ul = element(id='pagesTree')
    split_path = fullpath.split('/')
    page_name = split_path.pop()
    if split_path:
        project_common._expand_tree_path(pages_tree_ul, list(split_path))
    full_dot_path = fullpath.replace('/', '.')
    dir_selector = "li.branch[fullpath='{}']".format(full_dot_path)
    try:
        tree_element = pages_tree_ul.find(dir_selector, timeout=1)
    except:
        raise Exception('Page directory {} does not exist'.format(fullpath))


def verify_error_message(error_message):
    actions.step('Verify that the error {} is displayed'.format(error_message))
    actions.wait_for_element_visible(error_modal)
    errors = elements(css='#errorList>li')
    for error in errors:
        if error.text == error_message:
            return
    raise Exception('Error message {} was not found'.format(error_message))


def access_page(fullpath):
    project_common._access_elem('page', fullpath)


def create_access_page(fullpath):
    """Access a page from the list, create it if it does not exist"""
    try:
        verify_page_exists(fullpath)
    except:
        add_page(fullpath)
    access_page(fullpath)


def create_access_random_page():
    page_name = 'test_' + actions.random('dddddd')
    add_page(page_name)
    access_page(page_name)


def add_page_directory_if_not_exists(fullpath):
    try:
        verify_page_exists(fullpath)
    except:
        add_page_directory(fullpath)


def rename_page(old_full_name, new_full_name):
    project_common._rename_elem('page', old_full_name, new_full_name)

