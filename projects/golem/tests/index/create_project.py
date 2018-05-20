
description = 'Verify the user can create a new project in the index page'

pages = ['common',
         'index']

def setup(data):
    common.access_golem(data.env.url, data.env.admin)

def test(data):
    store('project_name', 'project_' + random('cccc'))
    click(index.create_project_button)
    wait_for_element_visible(index.project_name_input)
    send_keys(index.project_name_input, data.project_name)
    click(index.create_button)
    wait_for_element_not_visible(index.create_button)
    index.verify_project_exists(data.project_name)
