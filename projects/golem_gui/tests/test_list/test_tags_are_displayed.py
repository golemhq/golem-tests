
description = 'Verify the tags of a test are displayed in the test list'

pages = ['common',
         'index',
         'test_builder',
         'test_list']

def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    index.create_access_project('test_tags')
    common.navigate_menu('Tests')
    store('test_name1', 'test_' + random('ddddd'))
    store('test_name2', 'test_' + random('ddddd'))
    store('tag1', 'foo')
    store('tag2', 'bar')
    # add test 1 with 1 tag
    test_list.create_access_test(data.test_name1)
    send_keys(test_builder.tags_input, data.tag1)
    test_builder.save_test()
    common.navigate_menu('Tests')
    # add test 2 with 2 tags
    test_list.create_access_test(data.test_name2)
    send_keys(test_builder.tags_input, data.tag1 + ', ' + data.tag2)
    test_builder.save_test()
    common.navigate_menu('Tests')

def test(data):
    wait(2)  # wait for tags to load
    test_list.assert_test_tags(data.test_name1, [data.tag1])
    test_list.assert_test_tags(data.test_name2, [data.tag1, data.tag2])
