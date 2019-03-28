"""Page Object for the test list: /project/<project>/tests/"""
from urllib.parse import urljoin

from golem import actions
from golem.browser import element, elements

from projects.golem_gui.pages import list_common, common


def add_test(fullpath):
    list_common._add_tree_element(fullpath)


def add_test_if_not_exists(fullpath):
    if not test_exists(fullpath):
        list_common._add_tree_element(fullpath)


def add_directory(fullpath):
    list_common._add_directory(fullpath)


def assert_test_exists(fullpath):
    assert test_exists(fullpath), 'test {} does not exist'.format(fullpath)


def test_exists(fullpath):
    return list_common._elem_exists(fullpath)


def directory_exists(fullpath):
    return list_common._directory_exists(fullpath)


def assert_directory_exists(fullpath):
    actions.step('Assert directory {} exists'.format(fullpath))
    assert directory_exists(fullpath), 'directory {} does not exist'.format(fullpath)


def access_test(fullpath):
    list_common._access_elem(fullpath)


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
    list_common.rename_elem(old_full_name, new_full_name)


def duplicate_test(test_name, new_test_name):
    list_common.duplicate_elem(test_name, new_test_name)


def click_run_test(fullpath):
    tree_item = list_common.get_tree_item(fullpath)
    tree_item.mouse_over()
    run_button = tree_item.find('.tree-element-buttons > .run-test-button')
    actions.click(run_button)


def generate_test_url(base_url, project, test):
    rel = '/project/{}/test/{}/'.format(project, test)
    return urljoin(base_url, rel)


def assert_test_tags(full_test_name, expected_tags):
    tag_spans = elements("li.tree-element[fullpath='{}'] > div.tag-container > span.tag"
                         .format(full_test_name))
    msg = ('expected {} tags, but got {} tags for test {}'
           .format(len(expected_tags), len(tag_spans), full_test_name))
    assert len(tag_spans) == len(expected_tags), msg
    actual_tags = [t.text for t in tag_spans]
    for t in expected_tags:
        assert t in actual_tags, '{} tag was not found for test {}'.format(t, full_test_name)


def click_delete_button(full_name):
    test_element = list_common.get_tree_item(full_name)
    test_element.mouse_over()
    button = test_element.find('.tree-element-buttons button.delete-button')
    button.click()
