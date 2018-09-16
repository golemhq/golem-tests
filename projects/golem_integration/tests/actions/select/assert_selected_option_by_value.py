from golem import actions

from projects.golem_integration.pages import golem_steps


description = 'assert_selected_option_by_value action'

def test(data):
    actions.navigate(data.env.url+'elements/')
    select = ('id', 'select-1')
    actions.select_option_by_value(select, 'option-saab')
    actions.assert_selected_option_by_value(select, 'option-saab')
    expected = 'Assert selected option value of element select-1 is option-saab'
    golem_steps.assert_last_step_message(expected)
    try:
        actions.assert_selected_option_by_value(select, 'NOT')
    except AssertionError as e:
        expected = 'expected selected option in element select-1 to be NOT but was option-saab'
        assert expected in e.args[0]
