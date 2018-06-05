from golem import actions


description = 'verify_element_has_focus action'

def test(data):
    actions.navigate(data.env.url+'elements/')
    actions.focus_element('#input-one')
    actions.verify_element_has_focus('#input-one')
    actions.focus_element('#textarea-1')
    actions.verify_element_has_focus('#textarea-1')
    try:
        actions.verify_element_has_focus('#input-one')
    except Exception as e:
        assert 'element #input-one does not have focus' in e.args[0]
