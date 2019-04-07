import time
from golem import actions
from golem.browser import element

from projects.golem_gui.pages import common


tree_root_ul = ('id', 'treeRoot')


def _expand_tree_path(root_element, path):
    this_dir = path.pop()
    this_dir_elem = root_element.find("li.branch[name='{}']".format(this_dir))
    this_dir_elem.click()
    if path:
        new_root_element = this_dir_elem.find('ul')
        _expand_tree_path(new_root_element, path)


def _add_tree_element(fullpath):
    tree_ul = element(tree_root_ul)
    split_path = fullpath.split('/')
    elem_name = split_path.pop()
    if split_path:
        _expand_tree_path(tree_ul, list(split_path))
    dot_path = '.'.join(split_path) if split_path else '.'
    form_container = tree_ul.find("li.form-container[fullpath='{}']".format(dot_path))
    form_container.find('a.new-element-link').click()
    time.sleep(0.5)
    add_elem_input = form_container.find('input.new-element-input')
    actions.send_keys(add_elem_input, elem_name)
    actions.press_key(add_elem_input, 'ENTER')
    actions.wait(0.5)


def _add_directory(fullpath):
    tree_ul = element(tree_root_ul)
    split_path = fullpath.split('/')
    elem_name = split_path.pop()
    if split_path:
        _expand_tree_path(tree_ul, list(split_path))
    dot_path = '.'.join(split_path) if '.'.join(split_path) else '.' 
    form_container = tree_ul.find("li.form-container[fullpath='{}']".format(dot_path))
    form_container.find('a.new-directory-link').click()
    add_elem_input = form_container.find('input.new-element-input')
    actions.send_keys(add_elem_input, elem_name)
    actions.press_key(add_elem_input, 'ENTER')


def _elem_exists(fullpath):
    tree_ul = element(tree_root_ul)
    full_dot_path = fullpath.replace('/', '.')
    selector = "li.tree-element[fullpath='{}']".format(full_dot_path) 
    try:
        tree_element = tree_ul.find(selector, timeout=1, wait_displayed=False)
        return True
    except:
        return False


def _directory_exists(fullpath):
    tree_ul = element(tree_root_ul)
    split_path = fullpath.split('/')
    elem_name = split_path.pop()
    if split_path:
        _expand_tree_path(tree_ul, list(split_path))
    full_dot_path = fullpath.replace('/', '.')
    dir_selector = "li.branch[fullpath='{}']".format(full_dot_path)
    try:
        tree_element = tree_ul.find(dir_selector, timeout=1)
        return True
    except:
        return False


def _access_elem(fullpath):
    tree_ul = element(tree_root_ul)
    split_path = fullpath.split('/')
    elem_name = split_path.pop()
    if split_path:
        _expand_tree_path(tree_ul, list(split_path))
    full_dot_path = fullpath.replace('/', '.') 
    selector = "li.tree-element[fullpath='{}']".format(full_dot_path)
    tree_elem = tree_ul.find(selector)
    actions.click(tree_elem.find('a'))


def rename_elem(old_fullpath, new_fullpath):
    tree_ul = element(tree_root_ul)
    split_path = old_fullpath.split('/')
    elem_name = split_path.pop()
    if split_path:
        _expand_tree_path(tree_ul, list(split_path))
    full_dot_path = old_fullpath.replace('/', '.')
    selector = "li.tree-element[fullpath='{}']".format(full_dot_path)
    tree_elem = tree_ul.find(selector)
    tree_elem.mouse_over()
    rename_button = tree_elem.find('.tree-element-buttons > button.rename-button')
    actions.click(rename_button)
    prompt_input = element('#promptModal #promptModalInput', wait_displayed=5)
    actions.clear_element(prompt_input)
    actions.send_keys(prompt_input, new_fullpath)
    save_button = element('#promptModal #prompSaveButton')
    save_button.click()
    save_button.wait_not_displayed(5)


def get_tree_item(full_path):
    tree_ul = element(tree_root_ul)
    split_path = full_path.split('.')
    elem_name = split_path.pop()
    if split_path:
        _expand_tree_path(tree_ul, list(split_path))
    selector = "li.tree-element[fullpath='{}']".format(full_path)
    return tree_ul.find(selector)


def get_element_buttons(full_path):
    tree_element = get_tree_item(full_path)
    return tree_element.find('.tree-element-buttons')


def duplicate_elem(element_name, new_name):
    tree_item = get_tree_item(element_name)
    tree_item.mouse_over()
    tree_item.find('button.duplicate-button').click()
    common.send_confirm_modal(new_name)
