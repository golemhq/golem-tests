from golem import actions


description = 'verify_element_not_present action'

def test(data):
    actions.navigate(data.env.url+'elements/')
    actions.verify_element_not_present('#does-not-exist')
    try:
        actions.verify_element_not_present('#button-one')
        assert False, 'Expected Exception'
    except Exception as e:
        assert 'element #button-one is present' in e.args[0]
