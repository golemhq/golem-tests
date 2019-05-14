import requests

from golem import execution

from projects.golem_api.pages import utils


DELETE_PAGE_ENDPOINT = 'api/page/delete'
DUPLICATE_PAGE_ENDPOINT = 'api/page/duplicate'
RENAME_PAGE_ENDPOINT = 'api/page/rename'
PAGE_ELEMENTS_ENDPOINT = 'api/page/elements'
SAVE_PAGE_ENDPOINT = 'api/page/save'
SAVE_PAGE_CODE_ENDPOINT = 'api/page/code/save'


def delete_page_url(base_url):
    return '{}{}'.format(base_url, DELETE_PAGE_ENDPOINT)


def duplicate_page_url(base_url):
    return '{}{}'.format(base_url, DUPLICATE_PAGE_ENDPOINT)


def rename_page_url(base_url):
    return '{}{}'.format(base_url, RENAME_PAGE_ENDPOINT)


def page_elements_url(base_url):
    return '{}{}'.format(base_url, PAGE_ELEMENTS_ENDPOINT)


def save_page_url(base_url):
    return '{}{}'.format(base_url, SAVE_PAGE_ENDPOINT)


def save_page_code_url(base_url):
    return '{}{}'.format(base_url, SAVE_PAGE_CODE_ENDPOINT)


def delete_page(project_name, page_name, user=None):
    return requests.delete(delete_page_url(execution.data.env.url),
                           headers=utils.common_headers(user),
                           json={'project': project_name, 'fullPath': page_name})


def duplicate_page(project_name, page_name, new_page_name, user=None):
    json_ = {
        'project': project_name,
        'fullPath': page_name,
        'newFileFullPath': new_page_name
    }
    return requests.post(duplicate_page_url(execution.data.env.url),
                         headers=utils.common_headers(user), json=json_)


def rename_page(project_name, page_name, new_page_name, user=None):
    json_ = {
        'project': project_name,
        'fullFilename': page_name,
        'newFullFilename': new_page_name
    }
    return requests.post(rename_page_url(execution.data.env.url),
                         headers=utils.common_headers(user), json=json_)


def get_page_elements(project_name, page_name, user=None):
    return requests.get(page_elements_url(execution.data.env.url),
                        headers=utils.common_headers(user),
                        params={'project': project_name, 'page': page_name})


def save_page(project_name, page_name, elements, functions, import_lines, user=None):
    json_ = {
        'project': project_name,
        'pageName': page_name,
        'elements': elements,
        'functions': functions,
        'importLines': import_lines
    }
    return requests.put(save_page_url(execution.data.env.url),
                        headers=utils.common_headers(user), json=json_)


def save_page_code(project_name, page_name, content, user=None):
    json_ = {
        'project': project_name,
        'pageName': page_name,
        'content': content
    }
    return requests.put(save_page_code_url(execution.data.env.url),
                        headers=utils.common_headers(user), json=json_)
