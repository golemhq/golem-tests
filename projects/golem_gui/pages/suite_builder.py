from golem import actions
from golem.browser import element
from projects.golem_gui.pages import common


save_button = ('css', 'button#save', 'Save button')
run_suite_button = ('css', 'button#runTest', 'Run Suite button')
processes_input = ('id', 'processes', 'Processes input')
environments_input = ('id', 'environments', 'Environments input')
tags_input = ('id', 'tags', 'Tags input')
suite_name = ('id', 'suiteName', 'Suite name')


def save_suite():
    actions.click(save_button)
    actions.wait_for_element_present('#toast-container', timeout=5)


def assert_processes_value(expected_value):
    actual_value = element(processes_input).value
    if not actual_value == str(expected_value):
        msg = ('Error: expected Processes value to be: {}, but was {}'
               .format(expected_value, actual_value))
        raise Exception(msg)


def select_test(full_path):
    label = element('#suiteTests label[full-name="{}"]'.format(full_path))
    label.find('input[type="checkbox"]').check()


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