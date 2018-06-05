from golem import actions


description = 'Verify select_option_by_value action'

def test(data):
    actions.navigate(data.env.url+'elements/')
    select = ('id', 'select-1')
    actions.select_option_by_value(select, 'option-saab')
    actions.verify_selected_option(select, 'Saab')