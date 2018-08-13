from golem import actions


description = 'Verify wait_for_page_contains_text action'

def test(data):
    actions.navigate(data.env.url+'dynamic-elements/?delay=3')
    actions.wait_for_page_contains_text('<div id="button-five-container">', timeout=5)
    # wait times out waiting for text to be present in page
    actions.navigate(data.env.url + 'dynamic-elements/?delay=5')
    try:
        actions.wait_for_page_contains_text('<div id="button-five-container">', timeout=3)
        assert False, 'Expected Exception'
    except Exception as e:
        assert "Timeout waiting for page to contain '<div id=\"button-five-container\">'" in e.args[0]
