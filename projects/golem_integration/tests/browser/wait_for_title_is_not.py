from golem import actions

from projects.golem_integration.utils import expected_exception


description = 'Verify wait_for_title_is_not action'

def test(data):
    actions.navigate(data.env.url+'dynamic-elements/?delay=3')
    actions.click('#change-title-button')
    actions.verify_title('Web Playground - Dynamic Elements')
    actions.wait_for_title_is_not('Web Playground - Dynamic Elements', 4)
    actions.verify_title_is_not('Web Playground - Dynamic Elements')
    actions.navigate(data.env.url + 'dynamic-elements/?delay=5')
    msg = "Timeout waiting for title to not be 'Web Playground - Dynamic Elements'"
    with expected_exception(Exception, msg):
        actions.click('#change-title-button')
        actions.wait_for_title_is_not('Web Playground - Dynamic Elements', 3)
