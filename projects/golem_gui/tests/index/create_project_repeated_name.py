
description = 'Verify the application shows the correct error message when the user tries to create a project with non unique name'

pages = ['common',
         'index']

def setup(data):
    common.access_golem(data.env.url, data.env.admin)

def test(data):
    click(index.create_project_button)
    store('project_name', 'project_' + random('ddddd'))
    send_keys(index.project_name_input, data.project_name)
    click(index.create_button)
    click(index.create_project_button)
    send_keys(index.project_name_input, data.project_name)
    click(index.create_button)
    common.assert_error_message('A project with that name already exists')
