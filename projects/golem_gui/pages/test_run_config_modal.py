from golem.browser import element
from golem import actions


config_modal = ('id', 'runTestConfigModal')
run_button = ('id', 'TestRunConfigRunTest')
environments_input = '#runTestConfigModal input#runTestEnvironments'
browser_input = '#runTestConfigModal input#runTestBrowsers'


def select_env(env_name):
    input = element(environments_input)
    for i in range(len(env_name)):
        actions.send_keys(input, env_name[i])
        actions.wait(0.1)
    actions.press_key(input, 'DOWN')
    actions.press_key(input, 'ENTER')


def select_browser(env_name):
    input = element(browser_input)
    for i in range(len(env_name)):
        actions.send_keys(input, env_name[i])
        actions.wait(0.1)
    actions.press_key(input, 'DOWN')
    actions.press_key(input, 'ENTER')
    actions.press_key(input, 'TAB')
