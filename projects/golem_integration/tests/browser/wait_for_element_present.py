from golem import actions


description = 'Verify webdriver.wait_for_element_present method'

def test(data):
    actions.navigate(data.env.url+'dynamic-elements/?delay=3')
    actions.get_browser().wait_for_element_present('#button-five', 10)
    actions.verify_element_present('#button-five')
    actions.navigate(data.env.url + 'dynamic-elements/?delay=5')
    try:
        actions.get_browser().wait_for_element_present('#button-five', 3)
        assert False, 'Expected Exception'
    except Exception as e:
        assert "Element #button-five not found using selector css:'#button-five'" in e.args[0]
