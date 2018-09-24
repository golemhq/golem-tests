from golem import actions

from projects.golem_integration.pages import golem_steps


description = 'clear_element action'

def test(data):
    actions.navigate(data.env.url + 'elements/')
    input = '#input-one'
    text_area = '#textarea-1'
    # clear input
    actions.send_keys(input, 'foo')
    actions.assert_element_attribute(input, 'value', 'foo')
    actions.clear_element(input)
    golem_steps.assert_last_step_message('Clear element {}'.format(input))
    actions.assert_element_attribute(input, 'value', '')
    # clear text area
    actions.send_keys(text_area, 'bar')
    actions.assert_element_attribute(text_area, 'value', 'bar')
    actions.clear_element(text_area)
    actions.assert_element_attribute(text_area, 'value', '')
