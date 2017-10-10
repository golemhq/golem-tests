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


def click_pages_add_new(path=''):
    split_path = []
    if len(path):
        split_path = path.split('.')
    selector = '#pagesTree >'
    for i in range(len(split_path)):
        branch = split_path[i]
        this_branch_selector += 'li[data-branch-name=\'{}\'] > a'.format(branch)
        element(css=this_branch_selector).click()
        selector = selector +'li[data-branch-name=\'{}\'] ul '.format(branch)
    selector += ' li > span > a'
    element(css=selector).click()


def add_page(full_path):
    pages_tree_ul = element(id='pagesTree')
    split_path = full_path.split('/')
    page_name = split_path.pop()
    if split_path:
        _expand_tree_path(pages_tree_ul, list(split_path))
    dot_path = '.'.join(split_path) if split_path else '.'
    form_container = pages_tree_ul.find("li.form-container[fullpath='{}']".format(dot_path))
    form_container.find('a.new-element-link').click()
    add_page_input = form_container.find('input.new-element-input')
    actions.send_keys(add_page_input, page_name)
    actions.press_key(add_page_input, 'ENTER')


def add_test(full_path):
    tests_tree_ul = element(id='testCasesTree')
    split_path = full_path.split('/')
    page_name = split_path.pop()
    if split_path:
        _expand_tree_path(tests_tree_ul, list(split_path))
    dot_path = '.'.join(split_path) if '.'.join(split_path) else '.' 
    form_container = tests_tree_ul.find("li.form-container[fullpath='{}']".format(dot_path))
    form_container.find('a.new-element-link').click()
    add_test_input = form_container.find('input.new-element-input')
    actions.send_keys(add_test_input, page_name)
    actions.press_key(add_test_input, 'ENTER')


def add_page_directory(full_path):
    pages_tree_ul = element(id='pagesTree')
    split_path = full_path.split('/')
    page_name = split_path.pop()
    if split_path:
        _expand_tree_path(pages_tree_ul, list(split_path))
    dot_path = '.'.join(split_path) if '.'.join(split_path) else '.' 
    form_container = pages_tree_ul.find("li.form-container[fullpath='{}']".format(dot_path))
    form_container.find('a.new-element-link').click()
    add_page_input = form_container.find('input.new-element-input')
    actions.send_keys(add_page_input, page_name+'/')
    actions.press_key(add_page_input, 'ENTER')


def verify_page_exists(full_path):
    pages_tree_ul = element(id='pagesTree')
    split_path = full_path.split('/')
    page_name = split_path.pop()
    if split_path:
        _expand_tree_path(pages_tree_ul, list(split_path))
    full_dot_path = full_path.replace('/', '.')
    page_selector = "li.tree-element[fullpath='{}']".format(full_dot_path) 
    try:
        tree_element = pages_tree_ul.find(page_selector, timeout=1)
    except:
        raise Exception('Page {} does not exist'.format(full_path))


def verify_page_directory_exists(full_path):
    pages_tree_ul = element(id='pagesTree')
    split_path = full_path.split('/')
    page_name = split_path.pop()
    if split_path:
        _expand_tree_path(pages_tree_ul, list(split_path))
    full_dot_path = full_path.replace('/', '.')
    dir_selector = "li.branch[fullpath='{}']".format(full_dot_path)
    try:
        tree_element = pages_tree_ul.find(dir_selector, timeout=1)
    except:
        raise Exception('Page directory {} does not exist'.format(full_path))


def verify_test_exists(full_path):
    test_tree_ul = element(id='testCasesTree')
    split_path = full_path.split('/')
    page_name = split_path.pop()
    if split_path:
        _expand_tree_path(test_tree_ul, list(split_path))
    full_dot_path = full_path.replace('/', '.') 
    test_selector = "li.tree-element[fullpath='{}']".format(full_dot_path)
    try:
        tree_element = test_tree_ul.find(test_selector, timeout=1)
    except:
        raise Exception('Test {} does not exist'.format(full_path))


# def verify_test_exists(full_path):
#     split_path = []
#     if len(full_path):
#         split_path = full_path.split('.')
#     dir_name = split_path.pop()
#     selector = 'ul#testCasesTree >'
#     for i in range(len(split_path)):
#         branch = split_path[i]
#         this_branch_selector += 'li[data-branch-name=\'{}\'] > a'.format(branch)
#         element(css=this_branch_selector).click()
#         selector = selector +'li[data-branch-name=\'{}\'] ul '.format(branch)

#     list_of_lis_selector = selector + ' li.tree-element'
#     list_of_lis = elements(css=list_of_lis_selector)
#     if not dir_name in [x.text for x in list_of_lis]:
#         raise Exception('Test {} was not found'.format(dir_name))


def verify_error_message(error_message):
    actions.step('Verify that the error {} is displayed'.format(error_message))
    actions.wait_for_element_visible(error_modal)
    errors = elements(css='#errorList>li')
    for error in errors:
        if error.text == error_message:
            return
    raise Exception('Error message {} was not found'.format(error_message))


def access_test(full_path):
    test_tree_ul = element(id='testCasesTree')
    split_path = full_path.split('/')
    page_name = split_path.pop()
    if split_path:
        _expand_tree_path(test_tree_ul, list(split_path))
    full_dot_path = full_path.replace('/', '.') 
    test_selector = "li.tree-element[fullpath='{}']".format(full_dot_path)
    tree_element = test_tree_ul.find(test_selector)
    actions.click(tree_element.find('a'))


def create_access_test(full_path):
    """Access a test from the list, create it if it does not exist"""
    try:
        verify_test_exists(full_path)
    except:
        add_test(full_path)
    access_test(full_path)


def add_page_directory_if_not_exists(full_path):
    try:
        verify_page_exists(full_path)
    except:
        add_page_directory(full_path)    

