from golem import actions


description = 'Verify switch_to_default_content action on iframes'

def test(data):
    # switch to iframe by frame name
    actions.navigate(data.env.url+'iframes/')
    actions.switch_to_frame('iframe-bottom')
    actions.switch_to_frame('iframe-bottom-left')
    actions.verify_page_contains_text('IFrame Bottom Left')
    actions.verify_page_not_contains_text('IFrames')
    actions.verify_page_not_contains_text('id="button-bottom"')
    # switch to default content
    actions.switch_to_default_content()
    actions.verify_page_contains_text('IFrames')
    actions.verify_page_not_contains_text('IFrame Bottom')
    actions.verify_page_not_contains_text('IFrame Bottom Left')
