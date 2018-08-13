from golem import actions


description = 'Verify wait_for_title_contains action'

def test(data):
    actions.navigate(data.env.url+'dynamic-elements/?delay=3')
    actions.verify_title('Dynamic Elements')
    actions.click('#change-title-button')
    actions.wait_for_title_contains('New', 5)
    actions.verify_title_contains('New')
    actions.navigate(data.env.url + 'dynamic-elements/?delay=5')
    try:
        actions.click('#change-title-button')
        actions.wait_for_title_contains('New', 5)
        assert False, 'Expected Exception'
    except Exception as e:
        assert "Timeout waiting for title to contain \'New\'" in e.args[0]