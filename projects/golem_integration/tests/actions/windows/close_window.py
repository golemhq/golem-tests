from golem import actions


description = 'Verify close_window action'

def test(data):
    actions.navigate(data.env.url+'tabs/')
    actions.send_keys('#urlInput', '/elements/')
    actions.click("#goButton")
    actions.clear_element('#urlInput')
    actions.send_keys('#urlInput', '/alert/')
    actions.click("#goButton")
    actions.verify_amount_of_windows(3)
    actions.switch_to_window_by_title('Elements')
    actions.close_window()
    actions.verify_amount_of_windows(2)
    actions.verify_title('Tabs')
    actions.switch_to_window_by_title('Alert')
    actions.close_window()
    actions.verify_amount_of_windows(1)
    actions.verify_title('Tabs')

