from golem import actions

from projects.golem_integration.utils import expected_exception


description = 'Verify webdriver.wait_for_page_contains_text method'

def test(data):
    actions.navigate(data.env.url+'dynamic-elements/?delay=3')
    actions.wait_for_page_contains_text('<div id="button-five-container">', timeout=5)
    # wait times out waiting for text to be present in page
    actions.navigate(data.env.url + 'dynamic-elements/?delay=5')
    msg = "Timeout waiting for page to contain '<div id=\"button-five-container\">'"
    with expected_exception(Exception, msg):
        actions.wait_for_page_contains_text('<div id="button-five-container">', timeout=3)
