import time

from golem.browser import element, elements, get_browser

from . import common


bottom_new_file_button = ('css', '#bottomMenu>a.new-file-link')
bottom_new_folder_button = ('css', '#bottomMenu>a.new-directory-link')


def _get_child_folder(folder_content, child_folder_name):
    child_folders = folder_content.find_all(xpath='./li[contains(@class, "folder")]')
    for child_folder in child_folders:
        if child_folder.get_attribute('name') == child_folder_name:
            return child_folder
    return None


def _add_folder_to_folder(folder, new_child_folder_name):
    select_from_folder_menu(folder, 'Add New Folder')
    common.submit_prompt_modal(new_child_folder_name)


def _folder_icon(folder):
    return folder.find(xpath='./i[contains(@class, "folder-icon")]')


def _expand_folder(folder):
    folder_icon = _folder_icon(folder)
    if 'glyphicon-folder-close' in folder_icon.get_attribute('class'):
        folder_icon.click()


def _get_folder(folder_path_list, create_folders=False):
    wait_for_render(10)
    current_folder = None
    for node in folder_path_list:
        if current_folder is None:
            folder_content = _root_folder_content()
        else:
            folder_content = current_folder.find('ul.folder-content')
        child_folder = _get_child_folder(folder_content, node)
        if not child_folder and create_folders:
            if current_folder is None:
                add_folder_to_current_folder(node)
            else:
                _add_folder_to_folder(current_folder, node)
            child_folder = _get_child_folder(folder_content, node)
        if child_folder:
            _expand_folder(child_folder)
        current_folder = child_folder
    return current_folder


def _get_folder_content(folder_path_list):
    folder = _get_folder(folder_path_list)
    return folder.find('ul.folder-content')


def _root_folder_content():
    return element('#rootFolderContent')


def file_explorer_container():
    return element('#fileExporerContainer')


def wait_for_render(timeout=10):
    container = file_explorer_container()
    script = 'return arguments[0].FileExplorer.renderFinished'
    for i in range(timeout*4):
        try:
            render_finished = get_browser().execute_script(script, container)
            if render_finished:
                return
        except Exception as e:
            print('EXCEPTION', e)
            pass
        time.sleep(0.25)
    raise TimeoutError


def add_file_to_folder(test_path_list, create_folders=False):
    test_name = test_path_list.pop()
    folder = _get_folder(test_path_list, create_folders=create_folders)
    select_from_folder_menu(folder, 'Add New File')
    common.submit_prompt_modal(test_name)


def add_file_to_current_folder(filename):
    element(bottom_new_file_button).click()
    common.submit_prompt_modal(filename)


def add_folder_to_current_folder(folder_name):
    element(bottom_new_folder_button).click()
    common.submit_prompt_modal(folder_name)


def add_folder(folder_path_list):
    folder_name = folder_path_list.pop()
    folder = _get_folder(folder_path_list, create_folders=True)
    select_from_folder_menu(folder, 'Add New Folder')
    common.submit_prompt_modal(folder_name)


def expand_folder_menu(folder):
    folder.find(xpath='./span[contains(@class,"dropdown-container")]/button').click()


def file_exists(filename):
    return get_file(filename) is not None


def folder_exists(folder_name):
    return _get_folder(folder_name.split('.')) is not None


def get_active_folder_menu():
    menues = elements('ul.dropdown-menu.folder-menu')
    for menu in menues:
        if menu.is_displayed():
            return menu
    return None


def get_file(filename):
    wait_for_render(10)
    filename_split = filename.split('.')
    filename = filename_split.pop()
    if len(filename_split):
        folder_content = _get_folder_content(filename_split)
    else:
        folder_content = _root_folder_content()
    files = folder_content.find_all('li.file')
    for file in files:
        if file.find('a.file-link').text == filename:
            return file
    return None


def select_from_folder_menu(folder, option_text):
    expand_folder_menu(folder)
    menu = get_active_folder_menu()
    if menu is None:
        raise Exception('There is no expanded folder menu')
    options = menu.find_all('li>a')
    for option in options:
        if option.text == option_text:
            option.click()
            return
    raise Exception('Menu option {} was not found'.format(option_text))


def click_file_menu_button(filename, menu):
    file = get_file(filename)
    if not file:
        raise Exception('File {} was not found'.format(filename))
    file.mouse_over()
    if menu == 'rename':
        file.find('.file-menu-button.rename-button').click()
    elif menu == 'duplicate':
        file.find('.file-menu-button.duplicate-button').click()
    elif menu == 'delete':
        file.find('.file-menu-button.delete-button').click()
    elif menu == 'run':
        file.find('.file-menu-button.run-test-button').click()
    else:
        raise Exception('not implemented')


def rename_file(filename, new_filename):
    click_file_menu_button(filename, 'rename')
    common.submit_prompt_modal(new_filename)


def duplicate_file(filename, new_filename):
    click_file_menu_button(filename, 'duplicate')
    common.submit_prompt_modal(new_filename)


def delete_file(filename):
    click_file_menu_button(filename, 'delete')
    common.confirm_confirm_modal()


def navigate_to_folder(folder):
    folder = _get_folder(folder.split('.'))
    folder.find(folder.find(xpath='./a')).click()


def rename_folder(folder_name, new_folder_name):
    folder = _get_folder(folder_name.split('.'))
    if not folder:
        raise Exception('Folder {} does not exist'.format(folder_name))
    select_from_folder_menu(folder, 'Rename Folder')
    common.submit_prompt_modal(new_folder_name)


def delete_folder(folder_name):
    folder = _get_folder(folder_name.split('.'))
    if not folder:
        raise Exception('Folder {} does not exist'.format(folder_name))
    select_from_folder_menu(folder, 'Delete Folder')
    common.wait_confirm_modal_button_enabled()
    common.confirm_confirm_modal()


def get_breadcrumb_elements():
    breadcrumb_elements = []
    breadcrumb = element('#breadcrumb>div')
    breadcrumb_elements += breadcrumb.find_all('a')
    breadcrumb_elements.append(breadcrumb.find('span'))
    return breadcrumb_elements


def get_breadcrumb_list():
    breadcrumb_elements = get_breadcrumb_elements()
    return [e.text for e in breadcrumb_elements]


def assert_breadcrumb(breadcrumb_list):
    assert breadcrumb_list == get_breadcrumb_list()


def navigate_to_breadcrumb_folder(folder):
    for e in get_breadcrumb_elements():
        if e.text == folder:
            e.click()
            return
    raise Exception('Folder {} was not found in breadcrumb'.format(folder))


def access_file(filename):
    file = get_file(filename)
    if not file:
        raise Exception('File {} was not found'.format(filename))
    file.find('.file-link').click()
