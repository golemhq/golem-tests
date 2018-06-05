from golem import actions
from golem.browser import element


description = 'Verify drag_and_drop action'

def test(data):
    actions.navigate(data.env.url+'drag-and-drop/')
    actions.drag_and_drop(('id', 'airplane'), ('id', 'target2'))
    actions.wait(5)
    # assert element(('id', 'double-click-one-result')).text == 'Double Clicked!'
