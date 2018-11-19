from golem import actions
from golem.browser import element


def _expand_tree_path(root_element, path):
    this_dir = path.pop()
    this_dir_elem = root_element.find("li.branch[name='{}']".format(this_dir))
    this_dir_elem.click()
    if path:
        new_root_element = this_dir_elem.find('ul')
        _expand_tree_path(new_root_element, path)


def _add_tree_element(elem_type, fullpath):
    if elem_type == 'test':
        tree_ul = element(id='testCasesTree')
    elif elem_type == 'page':
        tree_ul = element(id='pagesTree')
    elif elem_type == 'suite':
        tree_ul = element(id='suitesTree')
    else:
        raise ValueError('Error: elem_type must be in {}'.format(['test', 'page', 'suite']))
    split_path = fullpath.split('/')
    elem_name = split_path.pop()
    if split_path:
        _expand_tree_path(tree_ul, list(split_path))
    dot_path = '.'.join(split_path) if split_path else '.'
    form_container = tree_ul.find("li.form-container[fullpath='{}']".format(dot_path))
    form_container.find('a.new-element-link').click()
    add_elem_input = form_container.find('input.new-element-input')
    actions.send_keys(add_elem_input, elem_name)
    actions.press_key(add_elem_input, 'ENTER')
    actions.wait(0.5)


def _add_directory(elem_type, fullpath):
    if elem_type == 'test':
        tree_ul = element(id='testCasesTree')
    elif elem_type == 'page':
        tree_ul = element(id='pagesTree')
    else:
        raise('Error: elem_type must be in {}'.format(['test', 'page']))
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


def _elem_exists(elem_type, fullpath):
    if elem_type == 'test':
        tree_ul = element(id='testCasesTree')
    elif elem_type == 'page':
        tree_ul = element(id='pagesTree')
    elif elem_type == 'suite':
        tree_ul = element(id='suitesTree')
    else:
        raise ValueError('Error: elem_type must be in {}'.format(['test', 'page', 'suite']))
    split_path = fullpath.split('/')
    elem_name = split_path.pop()
    if split_path:
        _expand_tree_path(tree_ul, list(split_path))
    full_dot_path = fullpath.replace('/', '.')
    selector = "li.tree-element[fullpath='{}']".format(full_dot_path) 
    try:
        tree_element = tree_ul.find(selector, timeout=1)
        return True
    except:
        return False


def _directory_exists(elem_type, fullpath):
    if elem_type == 'test':
        tree_ul = element(id='testCasesTree')
    elif elem_type == 'page':
        tree_ul = element(id='pagesTree')
    elif elem_type == 'suite':
        tree_ul = element(id='suitesTree')
    else:
        raise ValueError('Error: elem_type must be in {}'.format(['test', 'page', 'suite']))
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

def _access_elem(elem_type, fullpath):
    if elem_type == 'test':
        tree_ul = element(id='testCasesTree')
    elif elem_type == 'page':
        tree_ul = element(id='pagesTree')
    elif elem_type == 'suite':
        tree_ul = element(id='suitesTree')
    else:
        raise('Error: elem_type must be in {}'.format(['test', 'page', 'suite']))
    split_path = fullpath.split('/')
    elem_name = split_path.pop()
    if split_path:
        _expand_tree_path(tree_ul, list(split_path))
    full_dot_path = fullpath.replace('/', '.') 
    selector = "li.tree-element[fullpath='{}']".format(full_dot_path)
    tree_elem = tree_ul.find(selector)
    actions.click(tree_elem.find('a'))


def _rename_elem(elem_type, old_fullpath, new_fullpath):
    if elem_type == 'test':
        tree_ul = element(id='testCasesTree')
    elif elem_type == 'page':
        tree_ul = element(id='pagesTree')
    elif elem_type == 'suite':
        tree_ul = element(id='suitesTree')
    else:
        raise ValueError('Error: elem_type must be in {}'.format(['test', 'page', 'suite']))
    split_path = old_fullpath.split('/')
    elem_name = split_path.pop()
    if split_path:
        _expand_tree_path(tree_ul, list(split_path))
    full_dot_path = old_fullpath.replace('/', '.')
    selector = "li.tree-element[fullpath='{}']".format(full_dot_path)
    tree_elem = tree_ul.find(selector)
    rename_button = tree_elem.find('.tree-element-buttons > button.rename-button')
    actions.click(rename_button)
    prompt_input = element('#promptModal #promptModalInput', wait_displayed=5)
    actions.clear_element(prompt_input)
    actions.send_keys(prompt_input, new_fullpath)
    actions.click('#promptModal #prompSaveButton')
    actions.wait_for_element_displayed('#toast-container')
