from golem import actions
from golem.browser import element, elements, get_browser

from projects.golem_gui.pages import test_run_config_modal


test_name = ('id', 'fileName', 'Test Name')
test_name_input = ('css', '#filenameInput>input', 'Test Name input')
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
skip_checkbox = ('id', 'skipCheckbox', 'Skip checkbox')
skip_message_input = ('id', 'skipReason', 'Skip Message input')


def test_function_element(test_function_name):
    selector = "//span[@class='test-function-name' and text()='{}']/../../..".format(test_function_name)
    return element(xpath=selector, timeout=0)


def test_function_steps_element(tfname):
    tfelement = test_function_element(tfname)
    return tfelement.find('div.steps')


def add_action(action_name, params=[], where='test'):
    """adds an action using the autocomplete list"""
    if where == 'setup':
        steps_section = element('#setupSteps', wait_displayed=False)
        if not steps_section.is_displayed():
            actions.click('#showSetupLink>a')
            actions.wait(0.5)
    elif where == 'teardown':
        steps_section = element('#teardownSteps', wait_displayed=False)
        if not steps_section.is_displayed():
            actions.click('#showTeardownLink>a')
            actions.wait(0.5)
    else:
        steps_section = test_function_steps_element(where)

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
    if where == 'setup':
        action_inputs = elements("#setupSteps .step-first-input")
    elif where == 'teardown':
        action_inputs = elements("#teardownSteps .step-first-input")
    else:
        steps_section = test_function_steps_element(where)
        action_inputs = steps_section.find_all('.step-first-input')
    last_input = action_inputs[-1]
    actual_value = last_input.get_attribute('value')
    msg = 'Expected action to be {} but was {}'.format(action_name, actual_value)
    assert actual_value == action_name, msg


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
        assert t in actual_tags, 'tag "{}" is not in Tags input'.format(t)


def steps(where='test'):
    if where == 'setup':
        return elements('#setupSteps>.steps>.step')
    elif where == 'teardown':
        return elements('#teardownSteps>.steps>.step')
    else:
        steps_section = test_function_steps_element(where)
        return steps_section.find_all('.steps>.step')


def remove_steps(where='test'):
    step_elements = steps(where)
    for step in step_elements:
        step.find('.step-remove-icon>a').click()


def get_step(index, where='test'):
    step_elements = steps(where)
    try:
        step = step_elements[index]
    except IndexError:
        raise IndexError('error getting step index {}, total steps: {}'
                         .format(index, len(step_elements)))
    return Step(step)


def open_run_configurations_modal():
    actions.step('Open Run Configurations modal')
    element(run_config_button).click()
    get_browser().wait_for_element_displayed(test_run_config_modal.config_modal, 5)


def add_tag(tag_name):
    actions.step('Add tag {}'.format(tag_name))
    tags_input_element = element(tags_input)
    value = tags_input_element.value
    if value:
        tag_name = ', ' + tag_name
    tags_input_element.send_keys(tag_name)


class Step:

    def __init__(self, element):
        self.element = element
        self.step_type = element.get_attribute('step-type')

    def set_code_value(self, value):
        script = "arguments[0].querySelector('.CodeMirror').CodeMirror.setValue(arguments[1])"
        get_browser().execute_script(script, self.element, value)

    def get_code_value(self):
        script = "return arguments[0].querySelector('.CodeMirror').CodeMirror.getValue()"
        return get_browser().execute_script(script, self.element)
