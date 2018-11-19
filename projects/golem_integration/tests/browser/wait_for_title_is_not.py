from golem import actions

from projects.golem_integration.utils import expected_exception


description = 'Verify wait_for_title_is_not action'

def test(data):
    actions.navigate(data.env.url+'dynamic-elements/?delay=3')
    actions.verify_title('Dynamic Elements')
    actions.click('#change-title-button')
    actions.wait_for_title_is_not('Dynamic Elements', 5)
    actions.verify_title_is_not('Dynamic Elements')
    actions.navigate(data.env.url + 'dynamic-elements/?delay=5')
    msg = "Timeout waiting for title to not be 'Dynamic Elements'"
    with expected_exception(Exception, msg):
        actions.click('#change-title-button')
        actions.wait_for_title_is_not('Dynamic Elements', 5)
