
description = 'Verify the user can add tags to a test'

pages = ['common',
         'index',
         'test_list',
         'test_builder']

def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    index.create_access_project('tags'+random('dddddd'))
    common.navigate_menu('Tests')
    test_list.create_access_random_test()

def test(data):
    store('tag1', 'foo')
    store('tag2', 'bar')
    # add one tag
    send_keys(test_builder.tags_input, data.tag1)
    test_builder.save_test()
    refresh_page()
    test_builder.assert_tags([data.tag1])
    # add two tags
    send_keys(test_builder.tags_input, ','+data.tag2)
    test_builder.save_test()
    refresh_page()
    test_builder.assert_tags([data.tag1, data.tag2])
