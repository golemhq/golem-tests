import time

from golem import actions

from projects.golem_integration.utils import expected_exception


description = 'Verify webelement.send_keys_with_delay method'

def test(data):
    actions.navigate(data.env.url + 'elements/')
    element = actions.get_browser().find('#input-one')
    start = time.time()
    element.send_keys_with_delay('test', delay=0.3)
    end = time.time()
    assert element.value == 'test'
    assert end - start >= 1.2
    element.clear()
    start = time.time()
    element.send_keys_with_delay('ab', delay=1)
    end = time.time()
    assert element.value == 'ab'
    assert end - start >= 2
    # delay is not int or float
    with expected_exception(ValueError, 'delay must be int or float'):
        element.send_keys_with_delay('testing', delay='1')
    # delay is not positive
    with expected_exception(ValueError, 'delay must be a positive number'):
        element.send_keys_with_delay('testing', delay=-1)
