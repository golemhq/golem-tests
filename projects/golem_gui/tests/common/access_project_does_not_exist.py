from golem import actions

from projects.golem_gui.pages import common


description = 'Verify that accessing /project/<name>/* when project does not exist a correct message is displayed'


data = {
    'urls': [
        'project/not_existent/',
        'project/not_existent/suites/',
        'project/not_existent/tests/',
        'project/not_existent/pages/',
        'project/not_existent/settings/',
        'project/not_existent/environments/',
        'project/not_existent/test/foo/',
        'project/not_existent/test/foo/code/',
        'project/not_existent/page/foo/',
        'project/not_existent/page/foo/code/',
        'project/not_existent/suite/foo/',
        'report/not_existent/',
        'report/not_existent/foo/'
    ]
}


def setup(data):
    common.access_golem(data.env.url, data.env.admin)


def test(data):
    error_msg = 'The project not_existent does not exist.'
    for url in data.urls:
        actions.navigate(data.env.url + url)
        actions.assert_page_contains_text(error_msg)
