from golem import actions

from projects.golem_integration.pages import golem_steps


description = 'Verify switch_to_frame action'


def test_switch_to_frame(data):
    # switch to frame by frame name
    actions.navigate(data.env.url+'frames/')
    actions.switch_to_frame('frame-top')
    actions.verify_page_contains_text('Top')
    actions.verify_page_not_contains_text('Bottom Right')
    actions.click('#button-top')
    actions.verify_element_text('#button-top-result', 'Clicked!')
    # switch to frame by index
    actions.navigate(data.env.url + 'frames/')
    actions.switch_to_frame(0)
    golem_steps.assert_last_step_message('Switch to frame 0')
    actions.verify_page_contains_text('Top')
    actions.verify_page_not_contains_text('Bottom Right')
    actions.click('#button-top')
    actions.verify_element_text('#button-top-result', 'Clicked!')
    # switch to frame by webelement
    actions.navigate(data.env.url + 'frames/')
    frame_element = actions.get_browser().find('#frameTop')
    actions.switch_to_frame(frame_element)
    actions.verify_page_contains_text('Top')
    actions.verify_page_not_contains_text('Bottom Right')
    actions.click('#button-top')
    actions.verify_element_text('#button-top-result', 'Clicked!')


def test_switch_to_frame_iframe(data):
    # switch to iframe by frame name
    actions.navigate(data.env.url+'iframes/')
    actions.switch_to_frame('iframe-top')
    actions.verify_page_contains_text('IFrame Top')
    actions.verify_page_not_contains_text('IFrames')
    actions.click('#button-top')
    actions.verify_element_text('#button-top-result', 'Clicked!')
    # switch to iframe by index
    actions.navigate(data.env.url + 'iframes/')
    actions.switch_to_frame(1)
    actions.verify_page_contains_text('IFrame Bottom')
    actions.verify_page_not_contains_text('IFrames')
    actions.click('#button-bottom')
    actions.verify_element_text('#button-bottom-result', 'Clicked!')
    # switch to iframe by webelement
    actions.navigate(data.env.url + 'iframes/')
    frame_element = actions.get_browser().find('#iframeBottom')
    actions.switch_to_frame(frame_element)
    actions.verify_page_contains_text('IFrame Bottom')
    actions.verify_page_not_contains_text('IFrames')
    actions.click('#button-bottom')
    actions.verify_element_text('#button-bottom-result', 'Clicked!')
