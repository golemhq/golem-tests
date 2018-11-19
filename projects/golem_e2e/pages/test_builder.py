import time

from golem import actions
from golem.browser import get_browser, element, elements


test_name = ('id', 'testName', 'Test Name')
description = ('id', 'description', 'Description input')
save_button = ('id', 'save', 'Save button')
code_button = ('id', 'loadCodeButton', 'Code button')
run_button = ('id', 'runTest', 'Run button')
import_page_input = ('css', 'input.page-objects-autocomplete', 'Import Page input')
new_page_button = ('id', 'newPageButton', 'New Page button')
result_modal_body = ('css', 'div#testRunModal .modal-body #testResultContainer')


def add_action(action_name, params=[], where='test'):
    """adds an action using the autocomplete list"""
    if where == 'test':
        steps_section = element('div#testSteps')
    elif where == 'setup':
        steps_section = element('#setupSteps', wait_displayed=False)
        if not steps_section.is_displayed():
            actions.click('#showSetupLink>a')
            actions.wait(0.5)
    elif where == 'teardown':
        steps_section = element('#teardownSteps', wait_displayed=False)
        if not steps_section.is_displayed():
            actions.click('#showTeardownLink>a')
            actions.wait(0.5)

    # get last step
    steps = steps_section.find_all('div.step')
    step = steps[-1]

    # if the last action input is not empty, add a new one
    if step.find('input.step-first-input').value:
        steps_section.find('button.add-step').click()
        steps = steps_section.find_all('div.step')
        step = steps[-1]

    action_input = step.find('input.step-first-input')
    # actions.send_keys(action_input, action_name)
    for i in range(len(action_name)):
        actions.send_keys(action_input, action_name[i])
        actions.wait(0.1)
    actions.press_key(action_input, 'DOWN')
    actions.press_key(action_input, 'ENTER')

    # fill in each param
    if params:
        param_inputs = step.find_all('input.parameter-input')
        for i, param in enumerate(params):
            param_inputs[i].send_keys(param)


def verify_last_action(action_name, where='test'):
    if where == 'test':
        action_inputs = elements("#testSteps .step-first-input")
    elif where == 'setup':
        action_inputs = elements("#setupSteps .step-first-input")
    elif where == 'teardown':
        action_inputs = elements("#teardownSteps .step-first-input")
    last_input = action_inputs[-1]
    assert last_input.get_attribute('value'), action_name


def verify_description(desc):
    assert element(description).get_attribute('value') == desc


def save_test():
    actions.click(save_button)
    actions.wait_for_element_displayed('#toast-container', timeout=10)


def import_page(page_name):
    for char in page_name:
        actions.send_keys(import_page_input, char)


def verify_page_in_list(page_name):
    actions.step('Verify that page {} is in the list'.format(page_name))
    imported_pages = elements('#pageObjects>div>input.selected-page')
    for page in imported_pages:
        if page.get_attribute('value') == page_name:
            return
    raise Exception('Page {} was not found in the list'.format(page_name))


def add_new_page(page_name):
    actions.click(new_page_button)
    prompt_input = element('#promptModal #promptModalInput')
    actions.send_keys(prompt_input, page_name)
    actions.click('#promptModal #prompSaveButton')
    actions.wait_for_element_not_displayed('#promptModal')


def wait_for_test_to_run(timeout=5):
    loader_icon = element('div#testRunModal div#loaderContainer')
    for _ in range(timeout):
        if not loader_icon.is_displayed():
            return
        else:
            time.sleep(1)
    if loader_icon.is_displayed():
        raise Exception('test is still running')


def assert_result_log_line(index, expected_line):
    test_result_logs = element(result_modal_body).find_all('#testResultLogs>div.log-line')
    actual_line = test_result_logs[index].text
    msg = 'Expected {} in {}'.format(expected_line, actual_line)
    assert expected_line in actual_line, msg


def assert_result_modal_result(expected_result):
    result = element(result_modal_body).find_all('#testResults')[0]
    assert expected_result in result.text


def assert_result_modal_errors(expected_errors):
    if not expected_errors:
        assert not get_browser().element_is_present('#resultErrorList')
    else:
        errors = elements('#resultErrorList>li')
        for i, expected_error in enumerate(expected_errors):
            assert errors[i].text == expected_error


def assert_result_modal_steps_is_empty():
    assert not get_browser().element_is_present('#resultStepsList')


def assert_result_modal_steps(expected_steps):
    if not expected_steps:
        assert not get_browser().element_is_present('#resultStepsList')
    else:
        steps = elements('#resultStepsList>li')
        for i, expected_step in enumerate(expected_steps):
            msg = 'Expected step {} to be {} but was {}'.format(i, expected_step, steps[i].text)
            assert steps[i].text == expected_step, msg