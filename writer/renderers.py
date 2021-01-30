from asciimatics.renderers import StaticRenderer


class Dull(StaticRenderer):

    def __init__(self, screen, renderer):
        super(Dull, self).__init__()
        palette = [19, 20, 21, 25, 26, 27, 31, 32, 33]
        palette = range(51, 255, 36)

        for image in renderer.images:
            new_image = ""
            for y, line in enumerate(image):
                for x, c in enumerate(line):
                    colour = (x + y) % len(palette)
                    new_image += '${%d,1}%s' % (palette[colour], c)
                if y < len(image) - 1:
                    new_image += "\n"
            self._images.append(new_image)

class Jenny(StaticRenderer):

    def __init__(self, screen, renderer):
        super(Jenny, self).__init__()
        palette = range(196, 201)
                    
        for image in renderer.images:
            new_image = "" 
            for y, line in enumerate(image):
                for x, c in enumerate(line):
                    colour = (x + y) % len(palette)
                    new_image += '${%d,1}%s' % (palette[colour], c)
                if y < len(image) - 1: 
                    new_image += "\n" 
            self._images.append(new_image)
