

browsers = [
    'chrome-headless'
]

environments = [
    'test'
]

workers = 5

tests = [
    'index.create_project',
    'login.login',
    'login.login_incorrect_password',
    'page_builder.*',
    'project.add_page',
    'project.add_suite',
    'project.add_test',
    'test_builder.add_action_to_test'
]
