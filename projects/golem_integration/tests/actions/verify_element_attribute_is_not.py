from golem import actions


description = 'verify_element_attribute_is_not action'

def test(data):
    actions.navigate(data.env.url+'elements/')
    actions.verify_element_attribute_is_not('#input-one', 'class', 'this-is-not-correct')

