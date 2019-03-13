import time

from golem import actions

from projects.golem_gui.pages import list_common, common


def add_page(fullpath):
    list_common._add_tree_element(fullpath)


def add_directory(fullpath):
    list_common._add_directory(fullpath)


def assert_page_exists(fullpath):
    assert page_exists(fullpath), 'page {} does not exist'.format(fullpath)


def assert_directory_exists(fullpath):
    msg = 'directory {} does not exist'.format(fullpath)
    assert directory_exists(fullpath), msg


def page_exists(fullpath):
    return list_common._elem_exists(fullpath)


def directory_exists(fullpath):
    return list_common._directory_exists(fullpath)


def access_page(fullpath):
    list_common._access_elem(fullpath)


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
    list_common.rename_elem(old_full_name, new_full_name)


def duplicate_page(page_name, new_page_name):
    list_common.duplicate_elem(page_name, new_page_name)


def wait_for_page_exists(fullpath, timeout=5):
    for _ in range(timeout):
        if page_exists(fullpath):
            return
        time.sleep(timeout)
    actions.fail('Timeout waiting for page {} to exist'.format(fullpath))


def click_delete_button(full_name):
    test_element = list_common.get_tree_item(full_name)
    test_element.mouse_over()
    button = test_element.find('.tree-element-buttons button.delete-button')
    button.click()
