from golem import actions
from golem.browser import element, elements


error_modal = ('id', 'errorModal', 'Error modal')


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
        raise('Error: elem_type must be in {}'.format(['test', 'page', 'suite']))
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


def add_page(fullpath):
    _add_tree_element('page', fullpath)


def add_test(fullpath):
    _add_tree_element('test', fullpath)


def add_suite(name):
    _add_tree_element('suite', name)
    

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
    form_container.find('a.new-element-link').click()
    add_elem_input = form_container.find('input.new-element-input')
    actions.send_keys(add_elem_input, elem_name+'/')
    actions.press_key(add_elem_input, 'ENTER')


def add_page_directory(fullpath):
    _add_directory('page', fullpath)


def add_test_directory(fullpath):
    _add_directory('test', fullpath)


def _verify_elem_exists(elem_type, fullpath):
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
    try:
        tree_element = tree_ul.find(selector, timeout=1)
    except:
        raise Exception('Page {} does not exist'.format(fullpath))


def verify_page_exists(fullpath):
    _verify_elem_exists('page', fullpath)


def verify_page_directory_exists(fullpath):
    pages_tree_ul = element(id='pagesTree')
    split_path = fullpath.split('/')
    page_name = split_path.pop()
    if split_path:
        _expand_tree_path(pages_tree_ul, list(split_path))
    full_dot_path = fullpath.replace('/', '.')
    dir_selector = "li.branch[fullpath='{}']".format(full_dot_path)
    try:
        tree_element = pages_tree_ul.find(dir_selector, timeout=1)
    except:
        raise Exception('Page directory {} does not exist'.format(fullpath))


def verify_test_exists(fullpath):
    _verify_elem_exists('test', fullpath)


def verify_suite_exists(name):
    _verify_elem_exists('suite', name)


def verify_error_message(error_message):
    actions.step('Verify that the error {} is displayed'.format(error_message))
    actions.wait_for_element_visible(error_modal)
    errors = elements(css='#errorList>li')
    for error in errors:
        if error.text == error_message:
            return
    raise Exception('Error message {} was not found'.format(error_message))


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


def access_test(fullpath):
    _access_elem('test', fullpath)


def access_page(fullpath):
    _access_elem('page', fullpath)


def access_suite(name):
    _access_elem('suite', name)


def create_access_test(fullpath):
    """Access a test from the list, create it if it does not exist"""
    try:
        verify_test_exists(fullpath)
    except:
        add_test(fullpath)
    access_test(fullpath)


def create_access_page(fullpath):
    """Access a page from the list, create it if it does not exist"""
    try:
        verify_page_exists(fullpath)
    except:
        add_page(fullpath)
    access_page(fullpath)


def create_access_suite(fullpath):
    """Access a page from the list, create it if it does not exist"""
    try:
        verify_suite_exists(fullpath)
    except:
        add_suite(fullpath)
    access_suite(fullpath)


def add_page_directory_if_not_exists(fullpath):
    try:
        verify_page_exists(fullpath)
    except:
        add_page_directory(fullpath)


def add_test_directory_if_not_exists(fullpath):
    try:
        verify_test_exists(fullpath)
    except:
        add_test_directory(fullpath)

