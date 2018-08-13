from golem import actions


description = 'verify_element_has_attribute action'

def test(data):
    actions.navigate(data.env.url+'elements/')
    actions.verify_element_has_attribute('#button-one', 'onclick')
    try:
        actions.verify_element_has_attribute('#button-one', 'not-this-one')
        assert False, 'Expected Exception'
    except Exception as e:
        assert 'element #button-one does not have attribute not-this-one' in e.args[0]
