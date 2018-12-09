
description = 'Verify a correct message is displayed when the test does not exist'

pages = ['common',
         'index']

def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    index.create_access_project('test')

def test(data):
    navigate(data.env.url + 'project/test/test/not_existent/code/')
    assert_page_contains_text('The test not_existent does not exist')
