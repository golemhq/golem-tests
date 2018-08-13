from golem import actions


description = 'Verify switch_to_first_window action'

def test(data):
    actions.navigate(data.env.url+'tabs/')
    actions.click('#openTab')
    actions.wait_for_window_present_by_title('Tab')
    actions.switch_to_window_by_index(1)
    assert actions.get_window_index() == 1
    actions.verify_title('Tab')
    actions.switch_to_first_window()
    assert actions.get_window_index() == 0
    actions.verify_title('Tabs')