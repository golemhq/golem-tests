from golem import execution


def project(project):
    return '{}project/{}/'.format(execution.data.env.url, project)


def test(project, test):
    return '{}project/{}/test/{}/'.format(execution.data.env.url, project, test)


def page(project, page):
    return '{}project/{}/page/{}/'.format(execution.data.env.url, project, page)


def suite(project, suite):
    return '{}project/{}/suite/{}/'.format(execution.data.env.url, project, suite)


def environments(project):
    return '{}project/{}/environments/'.format(execution.data.env.url, project)


def users_new():
    return '{}users/new'.format(execution.data.env.url)
