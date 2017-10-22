from golem import actions
from golem.browser import element


save_button = ('css', 'button#save', 'Save button')

workers_input = ('id', 'workers', 'Workers input')


def save_suite():
    actions.click(save_button)
    actions.wait_for_element_not_exist('#toast-container')


def verify_workers_value(expected_value):
    actual_value = element(workers_input).get_attribute('value')
    if not actual_value == str(expected_value):
        msg = ('Error: expected workers value to be: {}, but was {}'
               .format(expected_value, actual_value))
        raise Exception(msg)