from asciimatics.widgets import Frame,  Layout, Label

from writer.gamestate import STATE

import logging
logger = logging.getLogger(__name__)


class TextFrame(Frame):
    def __init__(self, screen, height, width, data={}, x=0, y=0, name="FRAME", title="FRAME", has_border=True):
        self.x = x
        self.y = y
        self.name = name
        super(TextFrame, self).__init__(screen,
                                        height,
                                        width,
                                        data=data,
                                        x=x, y=y,
                                        name=name,
                                        title=title,
                                        has_border=has_border,
                                        can_scroll=False)
        self.set_theme('monochrome')
        layout = Layout([width])
        self.add_layout(layout)
        frameinfo = STATE.get_frame_by_name(self.name)
        layout.add_widget(Label(frameinfo['text'], height=height))
        # layout.add_widget(WrappedText(f"{self.name}", dummydata['text'], width))

        self.fix()

    def update(self, frame_no):
        self._update(frame_no)
        label = self._layouts[0]._columns[0][0]
        frameinfo = STATE.get_frame_by_name(self.name)
        label.text = frameinfo['text']
