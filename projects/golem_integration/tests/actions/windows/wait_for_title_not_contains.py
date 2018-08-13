from golem import actions


description = 'Verify wait_for_title_not_contains action'

def test(data):
    actions.navigate(data.env.url+'dynamic-elements/?delay=3')
    actions.verify_title('Dynamic Elements')
    actions.click('#change-title-button')
    actions.wait_for_title_not_contains('Dynamic', 5)
    actions.verify_title_not_contains('Dynamic')
    actions.navigate(data.env.url + 'dynamic-elements/?delay=5')
    try:
        actions.click('#change-title-button')
        actions.wait_for_title_not_contains('Dynamic', 5)
        assert False, 'Expected Exception'
    except Exception as e:
        assert "Timeout waiting for title to not contain \'Dynamic\'" in e.args[0]
