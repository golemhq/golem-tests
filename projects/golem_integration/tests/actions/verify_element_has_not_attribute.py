from golem import actions


description = 'verify_verify_element_has_not_attribute action'

def test(data):
    actions.navigate(data.env.url+'elements/')
    actions.verify_element_has_not_attribute('#button-one', 'not-this-one')
    try:
        actions.verify_element_has_attribute('#button-one', 'onclick')
    except Exception as e:
        assert 'element #button-one has attribute onclick' in e.args[0]
