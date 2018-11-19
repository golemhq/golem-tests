from golem import actions

from projects.golem_integration.utils import expected_exception


description = 'Verify webdriver.close_window_by_partial_title method'

def test(data):
    actions.navigate(data.env.url+'tabs/')
    actions.send_keys('#urlInput', '/elements/')
    actions.click("#goButton")
    actions.clear_element('#urlInput')
    actions.send_keys('#urlInput', '/alert/')
    actions.click("#goButton")
    actions.switch_to_window_by_index(0)
    first_title = actions.get_window_title()
    first_title_partial = first_title[:-2]
    actions.switch_to_window_by_index(1)
    second_title = actions.get_window_title()
    actions.switch_to_window_by_index(2)
    third_title = actions.get_window_title()
    third_title_partial = third_title[:-2]
    actions.switch_to_window_by_index(0)
    browser = actions.get_browser()
    # close third window by partial title
    browser.close_window_by_partial_title(third_title_partial)
    actions.verify_amount_of_windows(2)
    actions.verify_title(first_title)
    # close first window by partial title, from the first window
    browser.close_window_by_partial_title(first_title_partial)
    # second window is now active
    actions.verify_amount_of_windows(1)
    actions.verify_title(second_title)
    # try to close a window that is not present
    msg = "a window with partial title 'Incorrect Title' was not found"
    with expected_exception(Exception, msg):
        browser.close_window_by_partial_title('Incorrect Title')
