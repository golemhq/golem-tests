from golem import actions


description = 'Verify refresh_page action'

def test(data):
    actions.navigate(data.env.url + 'elements/')
    checkbox = ('id', 'unselected-checkbox')
    actions.click(checkbox)
    actions.verify_is_selected(checkbox)
    actions.refresh_page()
    actions.verify_is_not_selected(checkbox)
