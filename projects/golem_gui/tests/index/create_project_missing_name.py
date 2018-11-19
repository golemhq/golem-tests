
description = 'Verify the application shows the correct error message when creating a project without name'

pages = ['common',
         'index']

def setup(data):
    common.access_golem(data.env.url, data.env.admin)

def test(data):
    click(index.create_project_button)
    click(index.create_button)
    index.assert_error_message('Project name is too short')
