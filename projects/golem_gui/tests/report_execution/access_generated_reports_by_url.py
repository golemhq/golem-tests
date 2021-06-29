from golem import actions

from projects.golem_gui.pages import common
from projects.golem_gui.pages import api
from projects.golem_gui.pages import utils
from projects.golem_gui.pages import suite_builder
from projects.golem_gui.pages import report_execution


description = 'Verify that the user can access the "HTML", "JUnit" and JSON reports by url'


def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    api.project.using_project('report_execution')
    utils.create_access_simple_suite()


def test(data):
    suite_builder.run_suite()
    suite_builder.access_suite_execution_from_toast()
    report_execution.wait_until_execution_end()
    current_url = actions.get_current_url()
    actions.navigate(current_url + 'html/')
    actions.assert_element_text_contains(report_execution.title, 'report execution - simple suite')
    actions.navigate(current_url + 'html-no-images/')
    actions.assert_element_text_contains(report_execution.title, 'report execution - simple suite')
    actions.navigate(current_url + 'json/')
    assert '"totals_by_result"' in actions.get_browser().page_source
    actions.navigate(current_url + 'junit/')
    actions.assert_url_contains('/junit')
