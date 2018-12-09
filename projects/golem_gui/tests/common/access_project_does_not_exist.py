
description = 'Verify that accessing /project/<name>/* when project does not exist a correct message is displayed'

pages = ['common']

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
        'report/project/not_existent/',
        'report/project/not_existent/suite/foo/'
    ]
}

def setup(data):
    common.access_golem(data.env.url, data.env.admin)


def test(data):
    store('project', 'not_existent')
    store('error_msg', 'The project {} does not exist.'.format(data.project))
    for url in data.urls:
        navigate(data.env.url + url)
        assert_page_contains_text(data.error_msg)
