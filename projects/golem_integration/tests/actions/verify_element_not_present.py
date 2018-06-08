from golem import actions


description = 'verify_element_not_present action'

def test(data):
    actions.navigate(data.env.url+'special-elements/')
    actions.verify_element_not_present('#does-not-exist')
    try:
        actions.verify_element_not_present('#double-click-one')
    except Exception as e:
        assert 'element #double-click-one is present' in e.args[0]
