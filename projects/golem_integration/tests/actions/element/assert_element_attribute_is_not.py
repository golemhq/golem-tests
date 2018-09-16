from golem import actions

from projects.golem_integration.pages import golem_steps


description = 'assert_element_attribute_is_not action'

def test(data):
    actions.navigate(data.env.url+'elements/')
    actions.verify_element_attribute_is_not('#button-one', 'id', 'incorrect')
    expected = "Assert the element #button-one attribute id value is not 'incorrect'"
    assert golem_steps.get_last_step_message() == expected
    try:
        actions.assert_element_attribute_is_not('#button-one', 'id', 'button-one')
    except AssertionError as e:
        expected = "expected element #button-one attribute id value to not be 'button-one'"
        assert expected in e.args[0]
