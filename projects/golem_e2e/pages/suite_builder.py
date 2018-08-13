from golem import actions
from golem.browser import element
from projects.golem_e2e.pages import common


save_button = ('css', 'button#save', 'Save button')
run_suite_button = ('css', 'button#runTest', 'Run Suite button')
workers_input = ('id', 'workers', 'Workers input')
suite_name = ('id', 'suiteName', 'Suite name')


def save_suite():
    actions.click(save_button)
    actions.wait_for_element_present('#toast-container', timeout=5)


def verify_workers_value(expected_value):
    actual_value = element(workers_input).get_attribute('value')
    if not actual_value == str(expected_value):
        msg = ('Error: expected workers value to be: {}, but was {}'
               .format(expected_value, actual_value))
        raise Exception(msg)


def select_test(full_path):
    label = element('#suiteTests label[full-name="{}"]'.format(full_path))
    label.find('input[type="checkbox"]').click()


def verify_suite_was_run(suite_name):
    msg = 'Running suite {} - open'.format(suite_name)
    common.verify_toast_message_is_displayed(msg)


def access_suite_execution_from_toast():
    msg = 'Running suite'
    toast = common.get_toast_with_message(msg)
    toast.find('a').click()