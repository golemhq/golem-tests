from golem import actions

from projects.golem_gui.pages import list_common


def add_page_to_current_folder(page_name):
    list_common.add_file_to_current_folder(page_name)


def add_page(page_name):
    actions.step('Add page {}'.format(page_name))
    page_name_split = page_name.split('.')
    if len(page_name_split) > 1:
        list_common.add_file_to_folder(page_name_split, create_folders=True)
    else:
        add_page_to_current_folder(page_name)


def page_exists(page_name):
    return list_common.file_exists(page_name)


def assert_page_exists(page_name):
    actions.step('Assert page {} exists'.format(page_name))
    assert page_exists(page_name)


def folder_exists(folder_name):
    return list_common.folder_exists(folder_name)


def add_folder(folder_name):
    actions.step('Add folder {}'.format(folder_name))
    folder_name_split = folder_name.split('.')
    if len(folder_name_split) > 1:
        list_common.add_folder(folder_name_split)
    else:
        list_common.add_folder_to_current_folder(folder_name)


def rename_page(name, new_name):
    actions.step('Rename page {} to {}'.format(name, new_name))
    list_common.rename_file(name, new_name)


def duplicate_page(name, new_name):
    actions.step('Duplicate page {} with name {}'.format(name, new_name))
    list_common.duplicate_file(name, new_name)


def delete_page(name):
    actions.step('Delete page {}'.format(name))
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


def access_page(name):
    actions.step('Access page {}'.format(name))
    list_common.access_file(name)
