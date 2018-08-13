from golem import actions

description = 'Verify error action'

def test(data):
    try:
        actions.error('hey!, an error')
        assert False, 'Expected Exception'
    except Exception as e:
        assert 'hey!, an error' in e.args[0]
