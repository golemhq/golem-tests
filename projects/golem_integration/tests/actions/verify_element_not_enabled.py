from golem import actions


description = 'verify_element_not_enabled action'

def test(data):
    actions.navigate(data.env.url+'disabled-elements/')
    actions.verify_element_not_enabled('#text')
    actions.navigate(data.env.url+'elements/')
    try:
        actions.verify_element_not_enabled('#input-one')
    except Exception as e:
        assert 'Element is enabled' in e.args[0]
