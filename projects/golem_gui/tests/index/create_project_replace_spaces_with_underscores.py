
description = 'Verify that spaces are replaced with underscores when creating a test'

pages = ['common',
         'index']


def setup(data):
    common.access_golem(data.env.url, data.env.admin)


def test(data):
    store('project_name', 'project ' + random('cccc'))
    click(index.create_project_button)
    wait_for_element_displayed(index.project_name_input)
    send_keys(index.project_name_input, data.project_name)
    click(index.create_button)
    wait_for_element_not_displayed(index.create_button)
    index.assert_project_exists(data.project_name.replace(' ', '_'))
