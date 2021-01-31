from asciimatics.widgets import Frame, Layout, Label

from writer.gamestate import STATE

import logging
logger = logging.getLogger(__name__)


class StatusFrame(Frame):
    def __init__(self, screen, height, width, data={}, x=0, y=0, name="FRAME", title="FRAME", has_border=True):
        self.x = x
        self.y = y
        self.name = name
        super(StatusFrame, self).__init__(screen,
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

        # frameinfo = STATE.get_frame_by_name(self.name)
        # STATE.word
        layout.add_widget(Label("", height=1))

        layout.add_widget(Label(self.get_blanked_word(), height=height))
        # layout.add_widget(WrappedText(f"{self.name}", dummydata['text'], width))

        self.fix()

    def get_blanked_word(self):
        blanked = []
        for char in STATE.word:
            if char == ' ':
                blanked.append('/')
            elif char.upper() in STATE.found_letters:
                blanked.append(char)
            else:
                blanked.append('_')
        return ''.join(blanked)

    def update(self, frame_no):
        self._update(frame_no)
        label = self._layouts[0]._columns[0][1]
        label.text = self.get_blanked_word()
