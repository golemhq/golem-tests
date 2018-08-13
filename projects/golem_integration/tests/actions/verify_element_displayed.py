from golem import actions


description = 'verify_element_displayed action'

def test(data):
    actions.navigate(data.env.url+'special-elements/')
    actions.verify_element_displayed('#double-click-one')
    try:
        actions.verify_element_displayed('#hidden-input')
        assert False, 'Expected Exception'
    except Exception as e:
        assert 'element #hidden-input is not displayed' in e.args[0]
