from asciimatics.widgets import Frame, Layout, Label, Divider, Button, PopUpDialog
from asciimatics.exceptions import NextScene

import logging
logger = logging.getLogger(__name__)


class PromptFrame(Frame):
    def __init__(self, screen, height, width, x=0, y=0,
                 prompt="",
                 buttons=['', '', ''],
                 responses=['', '', ''],
                 closing_scenes=['', '', ''],
                 name="FRAME", title="FRAME", has_border=True):
        self.x = x
        self.y = y
        self.name = name
        self._buttons = buttons
        self._responses = responses
        self._prompt = prompt
        self._closing_scenes = closing_scenes

        super(PromptFrame, self).__init__(screen,
                                          height,
                                          width,
                                          x=x, y=y,
                                          name=name,
                                          title=title,
                                          has_border=has_border,
                                          can_scroll=False)
        self.set_theme('monochrome')

        promptLayout = Layout([width])
        self.add_layout(promptLayout)
        promptLayout.add_widget(Label(self._prompt))
        promptLayout.add_widget(Divider())

        responseLayout = Layout([width])
        self.add_layout(responseLayout)
        responseLayout.add_widget(Button(self._buttons[0], self._response_0), 0)
        responseLayout.add_widget(Button(self._buttons[1], self._response_1), 0)
        responseLayout.add_widget(Button(self._buttons[2], self._response_2), 0)
        self.fix()

    def _response_0(self):
        self._scene.add_effect(PopUpDialog(self._screen,
                                           self._responses[0],
                                           ["continue"],
                                           on_close=self._on_close_0,
                                           theme='warning'))

    def _response_1(self):
        self._scene.add_effect(PopUpDialog(self._screen,
                                           self._responses[1],
                                           ["continue"],
                                           on_close=self._on_close_1,
                                           theme='warning'))

    def _response_2(self):
        self._scene.add_effect(PopUpDialog(self._screen,
                                           self._responses[2],
                                           ["continue"],
                                           on_close=self._on_close_2,
                                           theme='warning'))

    def _on_close(self, name):
        raise NextScene

    def _on_close_0(self, name):
        raise NextScene(self._closing_scenes[0])

    def _on_close_1(self, _):
        raise NextScene(self._closing_scenes[1])

    def _on_close_2(self, _):
        raise NextScene(self._closing_scenes[2])

    def update(self, frame_no):
        self._update(frame_no)
