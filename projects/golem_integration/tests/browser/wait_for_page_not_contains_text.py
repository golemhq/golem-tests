from golem import actions


description = 'Verify webdriver.wait_for_page_not_contains_text method'

def test(data):
    actions.navigate(data.env.url+'dynamic-elements/?delay=3')
    actions.get_browser().wait_for_page_not_contains_text('<button id="button-six"', timeout=5)
    # wait times out waiting for text to be present in page
    actions.navigate(data.env.url + 'dynamic-elements/?delay=5')
    try:
        actions.get_browser().wait_for_page_not_contains_text('<button id="button-six"', timeout=3)
        assert False, 'Expected Exception'
    except Exception as e:
        assert "Timeout waiting for page to not contain '<button id=\"button-six\"'" in e.args[0]
