from golem import actions

description = 'Verify get_data action'

data = [{'foo': 'bar'}]

def test(data):
    actions.store('a', 'b')
    assert actions.get_data().foo == data.foo
    assert actions.get_data().a == 'b'
