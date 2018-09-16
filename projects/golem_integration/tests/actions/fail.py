from golem import actions


description = 'Verify fail action'

def test(data):
    try:
        actions.fail('I have failed you Anakin')
    except AssertionError as e:
        assert 'I have failed you Anakin' in e.args[0]
