from golem import actions


description = 'Verify webdriver.close_window_switch_back method'

def test(data):
    actions.navigate(data.env.url+'tabs/')
    actions.send_keys('#urlInput', '/elements/')
    actions.click("#goButton")
    actions.switch_to_window_by_index(0)
    browser = actions.get_browser()
    second_handle = browser.window_handles[1]
    browser.close_window_switch_back(second_handle)
    actions.verify_title('Tabs')
    actions.verify_amount_of_windows(1)
