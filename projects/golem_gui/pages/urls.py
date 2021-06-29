from golem import execution


def project(project_name):
    return '{}project/{}/'.format(execution.data.env.url, project_name)


def test(project_name, test_name):
    return '{}project/{}/test/{}/'.format(execution.data.env.url, project_name, test_name)


def test_code(project_name, test_name):
    return '{}project/{}/test/{}/code/'.format(execution.data.env.url, project_name, test_name)


def page(project_name, page_name):
    return '{}project/{}/page/{}/'.format(execution.data.env.url, project_name, page_name)


def suite(project_name, suite_name):
    return '{}project/{}/suite/{}/'.format(execution.data.env.url, project_name, suite_name)


def environments(project_name):
    return '{}project/{}/environments/'.format(execution.data.env.url, project_name)


def users_new():
    return '{}users/new'.format(execution.data.env.url)
