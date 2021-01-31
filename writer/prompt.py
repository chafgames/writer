from asciimatics.scene import Scene

from writer.promptframe import PromptFrame


class Prompt(Scene):
    def __init__(self, screen, effects=[], duration=-1, clear=True, name='Prompt',
                 title='Prompt', prompt="???",
                 responses=['', '', ''], buttons=['', '', ''], closing_scenes=['', '', '']):
        super().__init__(effects, duration, clear, name)
        self._title = title
        effects = [
            PromptFrame(screen, height=screen.height, width=screen.width,
                        prompt=prompt, responses=responses, buttons=buttons, closing_scenes=closing_scenes,
                        x=0, y=0, name='text', title=self._title),

            ]
        for fx in effects:
            self.add_effect(fx)

    def reset(self, old_scene=None, screen=None):
        pass

    def process_event(self, event):
        super(Prompt, self).process_event(event)
