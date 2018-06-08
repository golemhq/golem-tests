from golem import actions


description = 'verify_url action'

def test(data):
    url = data.env.url+'elements/'
    actions.navigate(url)
    actions.verify_url(url)
    try:
        actions.verify_url('http://incorrect_url')
    except Exception as e:
        assert "expected URL to be 'http://incorrect_url' but was '{}'".format(url) in e.args[0]
