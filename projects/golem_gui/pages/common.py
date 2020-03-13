import time

from golem.browser import element, elements, get_browser
from golem import actions

from projects.golem_gui.pages import login, left_menu


error_modal = ('id', 'errorModal', 'Error modal')


def access_golem(url, user):
    """navigate to url and log in to Golem GUI"""
    actions.navigate(url)
    login.login(user['username'], user['password'])


def navigate_menu(menu):
    if menu == 'Suites':
        actions.click(left_menu.suites_menu)
    elif menu == 'Tests':
        actions.click(left_menu.tests_menu)
    elif menu == 'Pages':
        actions.click(left_menu.pages_menu)
    elif menu == 'Reports':
        actions.click(left_menu.reports_menu)
    elif menu == 'Project Settings':
        actions.click(left_menu.project_settings_menu)
    elif menu == 'Environments':
        actions.click(left_menu.environments_menu)
    elif menu == 'Global Settings':
        actions.click(left_menu.global_settings_menu)
    elif menu == 'Users':
        actions.click(left_menu.users_menu)
    elif menu == 'User Profile':
        actions.click(left_menu.user_menu)
        actions.click(left_menu.profile_menu)
    else:
        raise Exception('Menu {} not implemented'.format(menu))


def logout():
    actions.click(left_menu.user_menu)
    actions.click(left_menu.logout_menu)


def get_toast_with_message(toast_message):
    for _ in range(6):
        toasts = elements('div.toast>.toast-message')
        for toast in toasts:
            if toast_message in toast.text:
                return toast
        time.sleep(0.5)
    return None


def assert_toast_message_is_displayed(toast_message):
    actions.step('Assert a toast is displayed with message {}'.format(toast_message))
    for _ in range(6):
        toasts = elements('div.toast>.toast-message')
        for toast in toasts:
            if toast.text == toast_message:
                return
        time.sleep(0.5)
    assert False, 'Toast with message "{}" was not found'.format(toast_message)


def wait_for_toast_to_dissapear():
    get_browser().wait_for_element_not_present('div.toast', 10)


def error_modal_is_displayed():
    error_modal_element = get_browser().find(error_modal, timeout=0, wait_displayed=False)
    return error_modal_element.is_displayed()


def dismiss_error_modal():
    error_modal_element = get_browser().find(error_modal, timeout=0, wait_displayed=False)
    error_modal_element.find('button[data-dismiss="modal"]').click()


def assert_error_message(error_message):
    actions.step('Verify that the error {} is displayed'.format(error_message))
    actions.wait_for_element_displayed(error_modal)
    errors = elements(css='#errorList>li')
    for error in errors:
        if error.text == error_message:
            return
    raise Exception('Error message {} was not found'.format(error_message))


def assert_info_bar_message(msg):
    actions.step('Assert an info bar is displayed with msg: {}'.format(msg))
    info_bars = actions.get_browser().find_all('.info-bar')
    if not info_bars:
        time.sleep(1)
        info_bars = actions.get_browser().find_all('.info-bar')
    for bar in info_bars:
        if msg in bar.text:
            return
    info_bars_text = '\n'.join([bar.text for bar in info_bars])
    error = ('expected an info bar with text {}\nInfo Bars found:\n{}'
             .format(msg, info_bars_text))
    actions.fail(error)


def confirm_confirm_modal():
    confirm_button = element('#confirmModal button.confirm')
    confirm_button.click()
    confirm_button.wait_not_displayed(timeout=5)


def wait_confirm_modal_button_enabled(timeout=10):
    element('#confirmModal button.confirm').wait_enabled(timeout)


def submit_prompt_modal(value):
    """Send a value to prompt modal and click Save button"""
    prompt_input = element('#promptModal #promptModalInput', wait_displayed=5)
    prompt_input.clear()
    prompt_input.send_keys(value)
    save_button = element('#promptModal #prompSaveButton')
    save_button.click()
    save_button.wait_not_displayed(5)


def get_autocomplete_suggestions():
    """Get the list of autocomplete suggestions.
    There must be one autocomplete suggestions list displayed
    otherwise it will return None
    """
    suggestions = None
    auto_selector_lists = elements('.autocomplete-suggestions')
    for suggestion_list in auto_selector_lists:
        if suggestion_list.is_displayed():
            suggestions = []
            suggestion_elements = suggestion_list.find_all('div.autocomplete-suggestion')
            for suggestion in suggestion_elements:
                suggestions.append(suggestion.text)
            break
    return suggestions
