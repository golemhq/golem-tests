import requests

from projects.golem_api.pages.utils import url, headers


DELETE_PAGE_ENDPOINT = '/page/delete'
DUPLICATE_PAGE_ENDPOINT = '/page/duplicate'
RENAME_PAGE_ENDPOINT = '/page/rename'
PAGE_COMPONENTS_ENDPOINT = '/page/components'
SAVE_PAGE_ENDPOINT = '/page/save'
SAVE_PAGE_CODE_ENDPOINT = '/page/code/save'
RENAME_PAGE_DIRECTORY_ENDPOINT = '/page/directory/rename'
DELETE_PAGE_DIRECTORY_ENDPOINT = '/page/directory/delete'


def delete_page(project_name, page_name, user=None):
    return requests.delete(url(DELETE_PAGE_ENDPOINT), headers=headers(user),
                           json={'project': project_name, 'fullPath': page_name})


def duplicate_page(project_name, page_name, new_page_name, user=None):
    json_ = {
        'project': project_name,
        'fullPath': page_name,
        'newFileFullPath': new_page_name
    }
    return requests.post(url(DUPLICATE_PAGE_ENDPOINT), headers=headers(user), json=json_)


def rename_page(project_name, page_name, new_page_name, user=None):
    json_ = {
        'project': project_name,
        'fullFilename': page_name,
        'newFullFilename': new_page_name
    }
    return requests.post(url(RENAME_PAGE_ENDPOINT), headers=headers(user), json=json_)


def get_page_components(project_name, page_name, user=None):
    return requests.get(url(PAGE_COMPONENTS_ENDPOINT), headers=headers(user),
                        params={'project': project_name, 'page': page_name})


def save_page(project_name, page_name, elements, functions, import_lines, user=None):
    json_ = {
        'project': project_name,
        'pageName': page_name,
        'elements': elements,
        'functions': functions,
        'importLines': import_lines
    }
    return requests.put(url(SAVE_PAGE_ENDPOINT), headers=headers(user), json=json_)


def save_page_code(project_name, page_name, content, user=None):
    json_ = {
        'project': project_name,
        'pageName': page_name,
        'content': content
    }
    return requests.put(url(SAVE_PAGE_CODE_ENDPOINT), headers=headers(user), json=json_)


def rename_page_directory(project_name, dir_name, new_dir_name, user=None):
    json_ = {
        'project': project_name,
        'fullDirname': dir_name,
        'newFullDirname': new_dir_name
    }
    return requests.post(url(RENAME_PAGE_DIRECTORY_ENDPOINT), headers=headers(user), json=json_)


def delete_page_directory(project_name, dir_name, user=None):
    return requests.delete(url(DELETE_PAGE_DIRECTORY_ENDPOINT), headers=headers(user),
                           json={'project': project_name, 'fullDirname': dir_name})
