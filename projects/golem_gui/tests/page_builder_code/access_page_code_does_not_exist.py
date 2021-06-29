from golem import actions

from projects.golem_gui.pages import common
from projects.golem_gui.pages import api


description = 'Verify a correct message is displayed when the page does not exist'


def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    api.project.using_project('page_builder_code')


def test(data):
    actions.navigate(data.env.url + 'project/'+data.project+'/page/not_existent/code/')
    actions.assert_page_contains_text('The page not_existent does not exist')
