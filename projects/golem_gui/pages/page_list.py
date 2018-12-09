import time

from golem import actions

from projects.golem_gui.pages import list_common, common


def add_page(fullpath):
    list_common._add_tree_element('page', fullpath)


def add_directory(fullpath):
    list_common._add_directory('page', fullpath)


def assert_page_exists(fullpath):
    assert page_exists(fullpath), 'page {} does not exist'.format(fullpath)


def assert_directory_exists(fullpath):
    msg = 'directory {} does not exist'.format(fullpath)
    assert directory_exists(fullpath), msg


def page_exists(fullpath):
    return list_common._elem_exists('page', fullpath)


def directory_exists(fullpath):
    return list_common._directory_exists('page', fullpath)


def access_page(fullpath):
    list_common._access_elem('page', fullpath)


def create_access_page(fullpath):
    """Access a page from the list, create it if it does not exist"""
    if not page_exists(fullpath):
        add_page(fullpath)
    access_page(fullpath)


def create_access_random_page():
    page_name = 'test_' + actions.random('dddddd')
    add_page(page_name)
    access_page(page_name)


def add_directory_if_not_exists(fullpath):
    if not directory_exists(fullpath):
        add_directory(fullpath)


def rename_page(old_full_name, new_full_name):
    list_common._rename_elem('page', old_full_name, new_full_name)


def wait_for_page_exists(fullpath, timeout=5):
    for _ in range(timeout):
        if page_exists(fullpath):
            return
        time.sleep(timeout)
    raise AssertionError('Timeout waiting for page {} to exist'.format(fullpath))