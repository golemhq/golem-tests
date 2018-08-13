from golem import actions


description = 'verify_element_not_displayed action'

def test(data):
    actions.navigate(data.env.url+'special-elements/')
    actions.verify_element_not_displayed('#hidden-input')
    try:
        actions.verify_element_not_displayed('#double-click-one')
        assert False, 'Expected Exception'
    except Exception as e:
        assert 'element #double-click-one is displayed' in e.args[0]
