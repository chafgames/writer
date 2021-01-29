from asciimatics.widgets import Frame,  Layout, Label


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
                                        has_border=has_border)

        layout = Layout([width])
        self.add_layout(layout)
        layout.add_widget(Label(data['text'], height=height))
        # layout.add_widget(WrappedText(f"{self.name}", dummydata['text'], width))

        self.fix()
