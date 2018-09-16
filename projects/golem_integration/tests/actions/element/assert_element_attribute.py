from golem import actions

from projects.golem_integration.pages import golem_steps


description = 'assert_element_attribute action'

def test(data):
    actions.navigate(data.env.url+'elements/')
    actions.verify_element_attribute('#button-one', 'id', 'button-one')
    expected = "Assert the element #button-one attribute id value is 'button-one'"
    assert golem_steps.get_last_step_message() == expected
    try:
        actions.assert_element_attribute('#button-one', 'id', 'not-this-one')
    except AssertionError as e:
        expected = ("expected element #button-one attribute id "
                    "value to be 'not-this-one' was 'button-one'")
        assert expected in e.args[0]
