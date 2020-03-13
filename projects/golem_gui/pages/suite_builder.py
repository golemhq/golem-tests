from golem import actions
from golem.browser import element, get_browser

from projects.golem_gui.pages import common


save_button = ('css', 'button#save', 'Save button')
run_suite_button = ('css', 'button#runTest', 'Run Suite button')
browsers_input = ('id', 'browsers', 'Browsers input')
processes_input = ('id', 'processes', 'Processes input')
environments_input = ('id', 'environments', 'Environments input')
tags_input = ('id', 'tags', 'Tags input')
suite_name = ('id', 'suiteName', 'Suite name')
all_tests_checkbox = ('id', 'allTestCasesCheckbox')


def save_suite():
    actions.click(save_button)
    actions.wait_for_element_present('#toast-container', timeout=5)


def assert_processes_value(expected_value):
    actual_value = element(processes_input).value
    if not actual_value == str(expected_value):
        msg = ('Error: expected Processes value to be: {}, but was {}'
               .format(expected_value, actual_value))
        raise Exception(msg)


def get_test_checkbox(test_name):
    li = element("li[data-type='test'][full-name='{}']".format(test_name))
    return li.find('label>input')


def assert_suite_was_run(suite_name):
    msg = 'Running suite {} - open'.format(suite_name)
    common.assert_toast_message_is_displayed(msg)


def run_suite():
    element(run_suite_button).click()
    assert common.get_toast_with_message('Running suite') is not None


def access_suite_execution_from_toast():
    msg = 'Running suite'
    toast = common.get_toast_with_message(msg)
    toast.find('a').click()


def assert_browser_suggestions(expected_list):
    suggestion_divs = get_browser().find_all('div.autocomplete-suggestions > div.autocomplete-suggestion')
    actual_suggestions = [s.text for s in suggestion_divs]
    for suggestion in expected_list:
        if suggestion not in actual_suggestions:
            actions.fail('Expected {} to be in browser suggestion list'.format(suggestion))


def assert_test_not_selected(test_name):
    checkbox = get_test_checkbox(test_name)
    assert not checkbox.is_selected(), 'expected {} to be not selected'.format(test_name)


def assert_test_selected(test_name):
    checkbox = get_test_checkbox(test_name)
    assert checkbox.is_selected(), 'expected {} to be selected'.format(test_name)


def select_test(test_name):
    checkbox = get_test_checkbox(test_name)
    checkbox.check()


def assert_test_counter(selected=None, total=None):
    counter_text = element('#testCount').text
    actual_selected = counter_text.split('/')[0]
    actual_total = counter_text.split('/')[1]
    if selected:
        assert actual_selected == str(selected), 'expected selected tests to be {} but was {}'.format(selected, actual_selected)
    if total:
        assert actual_total == str(total), 'expected total tests to be {} but was {}'.format(total, actual_total)
