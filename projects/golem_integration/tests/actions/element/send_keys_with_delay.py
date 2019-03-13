import time

from golem import actions

from projects.golem_integration.pages import golem_steps


description = 'Verify send_keys_with_delay action'


def test(data):
    actions.navigate(data.env.url + 'elements/')
    start = time.time()
    actions.send_keys_with_delay('#input-one', 'abc', delay=0.5)
    end = time.time()
    golem_steps.assert_last_step_message("Write 'abc' in element #input-one with delay")
    actions.assert_element_value('#input-one', 'abc')
    assert end - start >= 1.5
