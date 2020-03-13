from golem import actions

from projects.golem_gui.pages import common
from projects.golem_gui.pages import index
from projects.golem_gui.pages import urls


description = 'Verify a correct message is displayed when the test does not exist'


def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    index.create_access_project('test')


def test(data):
    actions.navigate(urls.test('test', 'not_existent_test'))
    actions.assert_page_contains_text('The test not_existent_test does not exist')