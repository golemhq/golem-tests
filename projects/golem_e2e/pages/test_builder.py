import time

from golem import actions
from golem.browser import element, elements


test_name = ('id', 'testName', 'Test Name')
description = ('id', 'description', 'Description input')
save_button = ('id', 'save', 'Save button')
code_button = ('id', 'loadCodeButton', 'Code button')
run_button = ('id', 'runTest', 'Run button')
import_page_imput = ('css', 'input.page-objects-autocomplete', 'Import Page input')
new_page_button = ('id', 'newPageButton', 'New Page button')


def add_action(action_name, where='test'):
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

    # get last input in steps section
    inputs = steps_section.find_all('input.form-control.step-first-input')
    last_input = inputs[-1]

    # use the last empty input or add a new one if it's not empty
    new_action_input = None
    if not len(last_input.get_attribute('value')):
        new_action_input = last_input
    else:
        steps_section.find('button.add-step').click()
        inputs = steps_section.find_all('input.form-control.step-first-input')
        new_action_input = inputs[-1]

    actions.send_keys(new_action_input, action_name)
    actions.press_key(new_action_input, 'DOWN')
    actions.press_key(new_action_input, 'ENTER')


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
        actions.send_keys(import_page_imput, char)


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


def verify_empty_test_execution_modal_content(test_name):
    test_result = element('div#testRunModal .modal-body #testResultContainer')
    
    test_result_logs = test_result.find_all('#testResultLogs>div')
    first_log_expected = 'INFO Test execution started: {}'.format(test_name)
    second_log_expected = 'INFO Browser: chrome'
    third_log_expected = 'INFO Test passed'
    assert first_log_expected in test_result_logs[0].text
    assert second_log_expected in test_result_logs[1].text
    assert third_log_expected in test_result_logs[2].text
    assert len(test_result_logs) == 3

    test_results = test_result.find_all('#testResults>.report-result>span')
    assert test_results[0].text == 'Result: pass'
    assert test_results[1].text == 'Error:'
    assert 'Elapsed Time:' in test_results[2].text
    assert test_results[3].text == 'Browser: chrome'
    assert test_results[4].text == 'Steps:'
    assert len(test_results) == 5
