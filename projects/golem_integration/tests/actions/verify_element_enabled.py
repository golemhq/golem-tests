from golem import actions


description = 'verify_element_enabled action'

def test(data):
    actions.navigate(data.env.url+'elements/')
    actions.verify_element_enabled('#input-one')
    actions.navigate(data.env.url+'disabled-elements/')
    try:
        actions.verify_element_enabled('#text')
        assert False, 'Expected Exception'
    except Exception as e:
        assert 'Element is not enabled' in e.args[0]
