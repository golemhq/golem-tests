
description = 'Verify the application shows the correct error message when creating a project with the name too short (less than 3 chars long)'

pages = ['common',
         'index']

def setup(data):
    common.access_golem(data.env.url, data.env.admin)

def test(data):
    click(index.create_project_button)
    store('project_name', random('cc'))
    send_keys(index.project_name_input, data.project_name)
    click(index.create_button)
    common.assert_error_message('Project name is too short')
