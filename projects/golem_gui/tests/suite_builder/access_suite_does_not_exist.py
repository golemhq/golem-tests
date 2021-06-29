from golem import actions

from projects.golem_gui.pages import common
from projects.golem_gui.pages import api


description = 'Verify a correct message is displayed when the suite does not exist'


def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    api.project.using_project('suite_builder')


def test(data):
    actions.navigate(data.env.url + 'project/'+data.project+'/suite/not_existent/')
    actions.assert_page_contains_text('The suite not_existent does not exist')
