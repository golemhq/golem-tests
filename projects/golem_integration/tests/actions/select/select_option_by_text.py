from golem import actions


description = 'Verify select_option_by_text action'

def test(data):
    actions.navigate(data.env.url+'elements/')
    select = ('id', 'select-1')
    actions.select_option_by_text(select, 'Saab')
    actions.verify_selected_option(select, 'Saab')