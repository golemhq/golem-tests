from golem import actions


description = 'verify_element_present action'

def test(data):
    actions.navigate(data.env.url+'special-elements/')
    actions.verify_element_present('#double-click-one')
    try:
        actions.verify_element_present('#does-not-exist')
        assert False, 'Expected Exception'
    except Exception as e:
        assert 'element #does-not-exist is not present' in e.args[0]
