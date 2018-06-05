from golem import actions


description = 'verify_element_has_not_focus action'

def test(data):
    actions.navigate(data.env.url+'elements/')
    actions.verify_element_has_not_focus('#input-one')
    actions.focus_element('#input-one')
    try:
        actions.verify_element_has_not_focus('#input-one')
    except Exception as e:
        assert 'element #input-one has focus' in e.args[0]
