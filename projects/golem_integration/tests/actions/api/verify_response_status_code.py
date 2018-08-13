from golem import actions


description = 'Verify verify_response_status_code action'

def test(data):
    url = data.env.url + 'ajax-request-process/'
    params = {'numberOne': '1', 'numberTwo': '1', 'delay': '0'}
    actions.http_post(url, data=params)
    actions.verify_response_status_code(data.last_response, 200)
