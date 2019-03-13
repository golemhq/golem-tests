from golem import actions

from projects.golem_gui.pages import list_common, common


def add_suite(name):
    list_common._add_tree_element(name)
    

def suite_exists(fullpath):
    return list_common._elem_exists(fullpath)


def add_directory(fullpath):
    list_common._add_directory(fullpath)


def add_directory_if_not_exists(fullpath):
    if not directory_exists(fullpath):
        add_directory(fullpath)


def assert_directory_exists(fullpath):
    msg = 'directory {} does not exist'.format(fullpath)
    assert directory_exists(fullpath), msg


def directory_exists(fullpath):
    return list_common._directory_exists(fullpath)


def assert_suite_exists(fullpath):
    assert suite_exists(fullpath), 'suite {} does not exist'.format(fullpath)


def access_suite(name):
    list_common._access_elem(name)


def create_access_suite(fullpath):
    """Access a suite from the list, create it if it does not exist"""
    if not suite_exists(fullpath):
        add_suite(fullpath)
    access_suite(fullpath)


def create_access_random_suite():
    suite_name = 'test_' + actions.random('dddddd')
    add_suite(suite_name)
    access_suite(suite_name)


def rename_suite(old_full_name, new_full_name):
    list_common.rename_elem(old_full_name, new_full_name)


def click_delete_button(full_name):
    suite_element = list_common.get_tree_item(full_name)
    suite_element.mouse_over()
    button = suite_element.find('.tree-element-buttons button.delete-button')
    button.click()


def duplicate_suite(suite_name, new_suite_name):
    list_common.duplicate_elem(suite_name, new_suite_name)
