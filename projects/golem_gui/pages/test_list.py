from golem import actions
from golem.browser import element

from projects.golem_gui.pages import list_common


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


def click_run_test(fullpath):
    tree_ul = element(id='testCasesTree')
    split_path = fullpath.split('/')
    elem_name = split_path.pop()
    if split_path:
        list_common._expand_tree_path(tree_ul, list(split_path))
    full_dot_path = fullpath.replace('/', '.')
    selector = "li.tree-element[fullpath='{}']".format(full_dot_path)
    tree_elem = tree_ul.find(selector)
    run_button = tree_elem.find('.tree-element-buttons > .run-test-button')
    actions.click(run_button)
