from golem import actions


description = 'Verify wait_for_title action'

def test(data):
    actions.navigate(data.env.url+'dynamic-elements/?delay=3')
    actions.verify_title('Dynamic Elements')
    actions.click('#change-title-button')
    actions.wait_for_title('New Title', 5)
    actions.verify_title('New Title')
    actions.navigate(data.env.url + 'dynamic-elements/?delay=5')
    try:
        actions.click('#change-title-button')
        actions.wait_for_title('New Title', 5)
        assert False, 'Expected Exception'
    except Exception as e:
        assert "Timeout waiting for title to be \'New Title\'" in e.args[0]
