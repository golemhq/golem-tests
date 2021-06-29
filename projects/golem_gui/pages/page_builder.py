from golem import actions
from golem.browser import elements, get_browser


page_name = ('id', 'fileName', 'page_name')
add_element_button = ('css', 'button[onclick="page.addPageObjectInput();"]', 'Add Element button')
save_button = ('css', 'button#save', 'Save button')
code_button = ('id', 'loadCodeButton', 'Code button')
open_page_code_button = ('link_text', 'Open Page Code', 'Open Page Code button')


def is_displayed(page_name):
    selector = '//h3/span[contains(text(),"{}")]'.format(page_name)
    return get_browser().element_is_present(('xpath', selector))


def add_element(element_def):
    actions.click(add_element_button)
    elemement_rows = elements('#elements>div.element')
    last_element_row = elemement_rows[-1]
    element_name_input = last_element_row.find('input.element-name')
    element_selector_input = last_element_row.find('input.element-selector')
    element_value_input = last_element_row.find('input.element-value')
    element_display_name_input = last_element_row.find('input.element-display-name')
    actions.send_keys(element_name_input, element_def[0])
    actions.send_keys(element_selector_input, element_def[1])
    actions.send_keys(element_value_input, element_def[2])
    actions.clear_element(element_display_name_input)
    actions.send_keys(element_display_name_input, element_def[3])
    actions.press_key(element_display_name_input, 'TAB')


def save_page():
    actions.click(save_button)
    actions.wait_for_element_present('#toast-container', timeout=5)


def assert_element_exists(element_def):
    elemement_rows = elements('#elements>div.element')
    for row in elemement_rows:
        element_name = row.find('input.element-name').get_attribute('value')
        element_selector = row.find('input.element-selector').get_attribute('value')
        element_value = row.find('input.element-value').get_attribute('value')
        element_display_name = row.find('input.element-display-name').get_attribute('value')
        cond1 = element_name == element_def[0]
        cond2 = element_selector == element_def[1]
        cond3 = element_value == element_def[2]
        cond4 = element_display_name == element_def[3]
        if cond1 and cond2 and cond3 and cond4:
            return
    raise AssertionError('The element {} was not found'.format(element_def))


