from golem import actions

from projects.golem_gui.pages import list_common


def add_test_to_current_folder(test_name):
    list_common.add_file_to_current_folder(test_name)


def add_test(test_name):
    actions.step('Add test {}'.format(test_name))
    test_name_split = test_name.split('.')
    if len(test_name_split) > 1:
        list_common.add_file_to_folder(test_name_split, create_folders=True)
    else:
        add_test_to_current_folder(test_name)


def test_exists(test_name):
    return list_common.file_exists(test_name)


def assert_test_exists(test_name):
    actions.step('Assert test {} exists'.format(test_name))
    assert test_exists(test_name)


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


def rename_test(name, new_name):
    actions.step('Rename test {} to {}'.format(name, new_name))
    list_common.rename_file(name, new_name)


def duplicate_test(name, new_name):
    actions.step('Duplicate test {} with name {}'.format(name, new_name))
    list_common.duplicate_file(name, new_name)


def delete_test(name):
    actions.step('Delete test {}'.format(name))
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


def assert_breadcrumb(breadcrumb_list):
    actions.step('Assert breadcrumb is {}'.format('-'.join(breadcrumb_list)))
    assert breadcrumb_list == list_common.get_breadcrumb_list()


def navigate_to_breadcrumb(folder):
    actions.step('Navigate to breadcrumb folder: {}'.format(folder))
    list_common.navigate_to_breadcrumb_folder(folder)


def access_test(name):
    actions.step('Access test {}'.format(name))
    list_common.access_file(name)


def click_run_test_button(name):
    actions.step('Click test {} run button'.format(name))
    list_common.click_file_menu_button(name, 'run')


def create_access_test(name):
    """Access a test from the list, create it if it does not exist"""
    if not test_exists(name):
        add_test(name)
    access_test(name)
