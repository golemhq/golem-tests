from golem import actions
from golem.browser import element, elements


test_name = ('id', 'testName', 'Test Name')
test_name_input = ('css', '#testNameInput>input', 'Test Name input')
description = ('id', 'description', 'Description input')
save_button = ('id', 'save', 'Save button')
code_button = ('id', 'loadCodeButton', 'Code button')
run_button = ('id', 'runTest', 'Run button')
run_config_button = ('id', 'openRunTestConfig')
import_page_input = ('css', 'input.page-objects-autocomplete', 'Import Page input')
new_page_button = ('id', 'newPageButton', 'New Page button')
new_page_modal_input = ('css', '#promptModal #promptModalInput')
new_page_modal_submit = ('css', '#prompSaveButton')
open_test_code_button = ('link_text', 'Open Test Code', 'Open Test Code button')
tags_input = ('id', 'tags', 'Tag input')
tags_autocomplete_list = ('css', 'div.autocomplete-suggestions')


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
    for i in range(len(action_name)):
        action_input.send_keys(action_name[i])
        actions.wait(0.1)
    actions.press_key(action_input, 'DOWN')
    actions.press_key(action_input, 'ENTER')

    # fill in each param
    if params:
        param_inputs = step.find_all('input.parameter-input')
        for i, param in enumerate(params):
            param_inputs[i].send_keys(param)


def assert_last_action(action_name, where='test'):
    action_inputs = None
    if where == 'test':
        action_inputs = elements("#testSteps .step-first-input")
    elif where == 'setup':
        action_inputs = elements("#setupSteps .step-first-input")
    elif where == 'teardown':
        action_inputs = elements("#teardownSteps .step-first-input")
    last_input = action_inputs[-1]
    assert last_input.get_attribute('value'), action_name


def assert_description(desc):
    assert element(description).get_attribute('value') == desc


def save_test():
    actions.click(save_button)
    actions.wait_for_element_displayed('#toast-container', timeout=5)


def import_page(page_name):
    for char in page_name:
        actions.send_keys(import_page_input, char)


def assert_page_in_list(page_name):
    actions.step('Verify that page {} is in the list'.format(page_name))
    imported_pages = elements('#pageObjects>div>input.page-name')
    for page in imported_pages:
        if page.get_attribute('value') == page_name:
            return
    raise AssertionError('Page {} was not found in the list'.format(page_name))


def add_new_page(page_name):
    actions.click(new_page_button)
    prompt_input = element('#promptModal #promptModalInput')
    actions.send_keys(prompt_input, page_name)
    actions.click('#promptModal #prompSaveButton')
    actions.wait_for_element_not_displayed('#promptModal')


def assert_tags(expected_tags):
    tag_value = element(tags_input).value
    actual_tags = [x.strip() for x in tag_value.split(',')]
    if '' in actual_tags:
        actual_tags.remove('')
    msg = 'expected {} tags but found {}'.format(len(expected_tags), len(actual_tags))
    assert len(actual_tags) == len(expected_tags), msg
    for t in expected_tags:
        assert t in actual_tags, 'tag "{}" is not in Tags input'
