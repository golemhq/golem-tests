

browsers = [
    'chrome-headless'
]

environments = [
    'test'
]

workers = 5

tests = [
    'project_suites.add_suite',
    'page_builder.add_element_to_page',
    'suite_builder.*',
    'project_pages.add_page',
    'index.create_project',
    'project_tests.add_test',
    'test_builder.add_action_to_test',
    'login.login'
]
