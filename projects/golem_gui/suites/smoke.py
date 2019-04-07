

browsers = [
    'chrome-headless'
]

environments = [
    'test'
]

processes = 5

tests = [
    'index.create_project',
    'login.login',
    'page_builder.add_element_to_page',
    'page_list.add_page',
    'suite_list.add_suite',
    'test_builder.add_action_to_test',
    'test_list.add_test'
]
