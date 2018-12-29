import os

from golem import actions
from golem import execution

from projects.golem_integration.utils import expected_exception


description = 'Verify _capture_screenshot'

def test(data):
    original_screenshot_settings = execution.settings['screenshots']
    reportdir = execution.report_directory
    imgpath = lambda filename: os.path.join(reportdir, filename)

    actions.navigate(data.env.url)

    # no screenshot settings
    execution.settings['screenshots'] = {}
    actions._capture_screenshot('no_settings')
    assert os.path.isfile(imgpath('no_settings.png'))

    # validate format is 'png' or 'jpg'
    execution.settings['screenshots'] = {'format': 'foo'}
    with expected_exception(ValueError, "settings screenshots format should be 'jpg' or 'png'"):
        actions._capture_screenshot('validate_format')

    # validate quality is int
    execution.settings['screenshots'] = {'quality': 'foo'}
    with expected_exception(ValueError, 'settings screenshots quality should be int'):
        actions._capture_screenshot('validate_quality_not_int')

    # validate quality correct range jpg
    execution.settings['screenshots'] = {
        'format': 'jpg',
        'quality': 96
    }
    msg = 'settings screenshots quality should be in 1..95 range for jpg files'
    with expected_exception(ValueError, msg):
        actions._capture_screenshot('validate_quality_incorrect_range_jpg')

    # validate width is int
    execution.settings['screenshots'] = {'width': 'foo'}
    with expected_exception(ValueError, 'settings screenshots width should be int'):
        actions._capture_screenshot('validate_width_not_int')

    # validate width greater than 0
    execution.settings['screenshots'] = {'width': -1}
    with expected_exception(ValueError, 'settings screenshots width should be greater than 0'):
        actions._capture_screenshot('validate_width_greater_than_0')

    # validate height is int
    execution.settings['screenshots'] = {'height': 'foo'}
    with expected_exception(ValueError, 'settings screenshots height should be int'):
        actions._capture_screenshot('validate_height_not_int')

    # validate height greater than 0
    execution.settings['screenshots'] = {'height': -1}
    with expected_exception(ValueError, 'settings screenshots height should be greater than 0'):
        actions._capture_screenshot('validate_height_greater_than_0')

    # validate resize is int
    execution.settings['screenshots'] = {'resize': 'foo'}
    with expected_exception(ValueError, 'settings screenshots resize should be int'):
        actions._capture_screenshot('validate_resize_not_int')

    # validate resize greater than 0
    execution.settings['screenshots'] = {'resize': -1}
    with expected_exception(ValueError, 'settings screenshots resize should be greater than 0'):
        actions._capture_screenshot('validate_resize_greater_than_0')

    # save screenshot as jpg
    execution.settings['screenshots'] = {'format': 'jpg'}
    actions._capture_screenshot('jpg_all_settings_default')
    filename = imgpath('jpg_all_settings_default.jpg')
    assert os.path.isfile(filename)
    default_jpg_size = os.path.getsize(filename)

    # save screenshot as jpg with reduced quality
    execution.settings['screenshots'] = {
        'format': 'jpg',
        'quality': 50
    }
    actions._capture_screenshot('jpg_reduced_quality')
    filename = imgpath('jpg_reduced_quality.jpg')
    assert os.path.isfile(filename)
    # size should be smaller than the default quality jpg
    assert os.path.getsize(filename) < default_jpg_size

    # save screenshot as jpg with set width and height
    execution.settings['screenshots'] = {
        'format': 'jpg',
        'width': 400,
        'height': 250
    }
    actions._capture_screenshot('jpg_set_width_height')
    filename = imgpath('jpg_set_width_height.jpg')
    assert os.path.isfile(filename)
    # size should be smaller than the default quality jpg
    assert os.path.getsize(filename) < default_jpg_size

    # save screenshot as png
    execution.settings['screenshots'] = {'format': 'png'}
    actions._capture_screenshot('png_all_settings_default')
    filename = imgpath('png_all_settings_default.png')
    assert os.path.isfile(filename)
    default_png_size = os.path.getsize(filename)

    # save screenshot as png with set width and height
    execution.settings['screenshots'] = {
        'format': 'png',
        'width': 400,
        'height': 250
    }
    actions._capture_screenshot('png_set_width_height')
    filename = imgpath('png_set_width_height.png')
    assert os.path.isfile(filename)
    # size should be smaller than the default quality jpg
    assert os.path.getsize(filename) < default_png_size

    # reset settings
    execution.settings['screenshots'] = original_screenshot_settings
