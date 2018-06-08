from golem import actions


description = 'verify_url_is_not action'

def test(data):
    url = data.env.url+'elements/'
    actions.navigate(url)
    actions.verify_url_is_not('http://incorrect')
    try:
        actions.verify_url_is_not(url)
    except Exception as e:
        assert "expected URL to not be '{}'".format(url) in e.args[0]
