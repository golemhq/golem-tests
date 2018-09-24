from golem import actions

from projects.golem_integration.pages import golem_steps


description = 'Verify select_option_by_text action'

def test(data):
    actions.navigate(data.env.url+'elements/')
    select = ('id', 'select-1')
    actions.select_option_by_text(select, 'Saab')
    golem_steps.assert_last_step_message("Select option 'Saab' from element select-1")
    actions.verify_selected_option_by_text(select, 'Saab')
