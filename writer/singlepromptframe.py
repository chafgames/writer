from asciimatics.widgets import Frame, Layout, Label, Divider, Button, PopUpDialog
from asciimatics.exceptions import NextScene

import logging
logger = logging.getLogger(__name__)


class SinglePromptFrame(Frame):
    def __init__(self, screen, height, width, x=0, y=0,
                 prompt="",
                #  buttons=['', '', ''],
                #  response='Y',
                #  closing_scenes=['', '', ''],
                 name="FRAME", title="FRAME", has_border=True):
        self.x = x
        self.y = y
        self.name = name
        self._prompt = prompt

        super(SinglePromptFrame, self).__init__(screen,
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
        promptLayout.add_widget(Label(self._prompt, height=height-6))
        promptLayout.add_widget(Divider())

        responseLayout = Layout([width])
        self.add_layout(responseLayout)
        responseLayout.add_widget(Button('Continue', self._on_click), 0)
        self.fix()

    def _on_click(self):
        raise NextScene

    def update(self, frame_no):
        self._update(frame_no)
