from golem.browser import element
from golem import actions


config_modal = ('id', 'runTestConfigModal', 'Config modal')
run_button = ('id', 'TestRunConfigRunTest', 'Run button')
environments_input = ('css', '#runTestConfigModal input#runTestEnvironments', 'Environments input')
browser_input = ('css', '#runTestConfigModal input#runTestBrowsers', 'Browsers input')
processes_input = ('css', '#runTestConfigModal input#runTestProcesses', 'Processes input')


def select_env(env_name):
    input_ = element(environments_input)
    for i in range(len(env_name)):
        actions.send_keys(input_, env_name[i])
        actions.wait(0.1)
    actions.press_key(input_, 'DOWN')
    actions.press_key(input_, 'ENTER')


def select_browser(env_name):
    input_ = element(browser_input)
    for i in range(len(env_name)):
        actions.send_keys(input_, env_name[i])
        actions.wait(0.1)
    actions.press_key(input_, 'DOWN')
    actions.press_key(input_, 'ENTER')
    actions.press_key(input_, 'TAB')
