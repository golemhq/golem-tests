
description = 'Verify a project cannot be created with invalid characters'

pages = ['common',
         'index']

def setup(data):
    common.access_golem(data.env.url, data.env.admin)

def test(data):
    store('project_name', 'project_test_$')
    click(index.create_project_button)
    send_keys(index.project_name_input, data.project_name)
    click(index.create_button)
    common.assert_error_message('Only letters, numbers and underscores are allowed')
