from golem import actions

from projects.golem_gui.pages import common, test_list, suite_list, suite_builder



def create_access_simple_suite(suite_name=None, test_name=None):
    """Creates a suite with an empty test if the suite
    does not exist.
    """
    suite_name = suite_name or 'simple_suite'
    test_name = test_name or 'simple_test'
    common.navigate_menu('Tests')
    if not test_list.test_exists(test_name):
        test_list.add_test(test_name)
    common.navigate_menu('Suites')
    if not suite_list.suite_exists(suite_name):
        suite_list.add_suite(suite_name)
        suite_list.access_suite(suite_name)
        suite_builder.select_test(test_name)
        suite_builder.save_suite()
    else:
        suite_list.access_suite(suite_name)
