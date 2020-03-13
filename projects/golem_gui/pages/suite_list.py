from golem import actions
from golem.browser import get_browser

from projects.golem_gui.pages import list_common


no_tests_alert_selector = 'div#infoBarContainer>div'


def add_suite_to_current_folder(suite_name):
    list_common.add_file_to_current_folder(suite_name)


def add_suite(suite_name):
    actions.step('Add suite {}'.format(suite_name))
    suite_name_split = suite_name.split('.')
    if len(suite_name_split) > 1:
        list_common.add_file_to_folder(suite_name_split, create_folders=True)
    else:
        add_suite_to_current_folder(suite_name)


def suite_exists(suite_name):
    return list_common.file_exists(suite_name)


def assert_suite_exists(suite_name):
    actions.step('Assert suite {} exists'.format(suite_name))
    assert suite_exists(suite_name)


def folder_exists(folder_name):
    return list_common.folder_exists(folder_name)


def assert_folder_exists(folder_name):
    actions.step('Assert folder {} exists'.format(folder_name))
    assert folder_exists(folder_name)


def add_folder(folder_name):
    actions.step('Add folder {}'.format(folder_name))
    folder_name_split = folder_name.split('.')
    if len(folder_name_split) > 1:
        list_common.add_folder(folder_name_split)
    else:
        list_common.add_folder_to_current_folder(folder_name)


def rename_suite(name, new_name):
    actions.step('Rename suite {} to {}'.format(name, new_name))
    list_common.rename_file(name, new_name)


def duplicate_suite(name, new_name):
    actions.step('Duplicate suite {} with name {}'.format(name, new_name))
    list_common.duplicate_file(name, new_name)


def delete_suite(name):
    actions.step('Delete suite {}'.format(name))
    list_common.delete_file(name)


def navigate_to_folder(folder):
    actions.step('Navigate to folder {}'.format(folder))
    list_common.navigate_to_folder(folder)


def rename_folder(name, new_name):
    actions.step('Rename folder {} to {}'.format(name, new_name))
    list_common.rename_folder(name, new_name)


def delete_folder(name):
    actions.step('Delete folder {}'.format(name))
    list_common.delete_folder(name)


def wait_for_no_tests_alert_to_appear(timeout=10):
    get_browser().wait_for_element_present(no_tests_alert_selector, timeout)


def dismiss_no_tests_alert_if():
    info_bar = get_browser().element_is_present(no_tests_alert_selector)
    if info_bar:
        info_bar.find('button.close').click()


def access_suite(name):
    actions.step('Access suite {}'.format(name))
    list_common.access_file(name)
