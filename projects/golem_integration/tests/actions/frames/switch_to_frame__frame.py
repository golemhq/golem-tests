from golem import actions

from projects.golem_integration.pages import golem_steps


description = 'Verify switch_to_frame action on framesets and frames'

def test(data):
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