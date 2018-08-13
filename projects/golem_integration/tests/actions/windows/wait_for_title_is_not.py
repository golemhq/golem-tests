from golem import actions


description = 'Verify webdriver.wait_for_title_is_not method'

def test(data):
    actions.navigate(data.env.url+'dynamic-elements/?delay=3')
    actions.verify_title('Dynamic Elements')
    actions.click('#change-title-button')
    actions.get_browser().wait_for_title_is_not('Dynamic Elements', 5)
    actions.verify_title_is_not('Dynamic Elements')
    actions.navigate(data.env.url + 'dynamic-elements/?delay=5')
    try:
        actions.click('#change-title-button')
        actions.get_browser().wait_for_title_is_not('Dynamic Elements', 5)
        assert False, 'Expected Exception'
    except Exception as e:
        assert "Timeout waiting for title to not be \'Dynamic Elements\'" in e.args[0]
