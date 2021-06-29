from golem import actions

from projects.golem_gui.pages import common
from projects.golem_gui.pages import api


description = 'Verify a correct message is displayed when the test does not exist'


def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    api.project.using_project('test_builder_code')


def test(data):
    actions.navigate(data.env.url + 'project/'+data.project+'/test/not_existent/code/')
    actions.assert_page_contains_text('The test not_existent does not exist')
