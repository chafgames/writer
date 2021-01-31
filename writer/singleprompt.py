from asciimatics.scene import Scene

from writer.singlepromptframe import SinglePromptFrame


class SinglePrompt(Scene):
    def __init__(self, screen, effects=[], duration=-1, clear=True, name='Prompt',
                 title='Prompt', prompt="???"):
        super().__init__(effects, duration, clear, name)
        self._title = title
        effects = [
            SinglePromptFrame(screen, height=screen.height, width=screen.width,
                        prompt=prompt,
                        x=0, y=0, name='text', title=self._title),
            ]
        for fx in effects:
            self.add_effect(fx)

    def reset(self, old_scene=None, screen=None):
        pass

    def process_event(self, event):
        super(SinglePrompt, self).process_event(event)
