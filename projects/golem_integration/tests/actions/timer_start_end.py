import time

from golem import actions


description = 'Verify timers can be started and stopped'


def test(data):
    actions.timer_start()
    time.sleep(0.5)
    assert actions.timer_stop() > 0.5
    # start a timer already started
    actions.timer_start('foo')
    current_time = actions.timer_start('foo')
    assert current_time is None
    # stop a timer that does not exist
    elapsed_time = actions.timer_stop('bar')
    assert elapsed_time is None
