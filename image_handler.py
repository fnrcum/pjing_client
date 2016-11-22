import pygame


class ImageHandler:

    def displayImage(self, screen, px, topleft, prior):
        # ensure that the rect always has positive width, height
        x, y = topleft
        width = pygame.mouse.get_pos()[0] - topleft[0]
        height = pygame.mouse.get_pos()[1] - topleft[1]
        if width < 0:
            x += width
            width = abs(width)
        if height < 0:
            y += height
            height = abs(height)

        # eliminate redundant drawing cycles (when mouse isn't moving)
        current = x, y, width, height
        if not (width and height):
            return current
        if current == prior:
            return current

        # draw transparent box and blit it onto canvas
        screen.blit(px, px.get_rect())
        im = pygame.Surface((width, height))
        im.fill((128, 128, 128))
        pygame.draw.rect(im, (32, 32, 32), im.get_rect(), 1)
        im.set_alpha(128)
        screen.blit(im, (x, y))
        pygame.display.flip()

        # return current box extents
        return x, y, width, height

    def setup(self, path):
        px = pygame.image.load(path)
        rect = px.get_rect()
        wg = rect[2]
        hg = rect[3]
        pygame.font.SysFont("Arial", 16)
        screen = pygame.display.set_mode([wg, hg], pygame.FULLSCREEN)
        screen.blit(px, px.get_rect())
        pygame.display.flip()
        return screen, px

    def mainLoop(self, screen, px):
        topleft = bottomright = prior = None
        end = False
        while not end:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONUP:
                    if not topleft:
                        topleft = event.pos
                    else:
                        bottomright = event.pos
                        end = True
            if topleft:
                prior = self.displayImage(screen, px, topleft, prior)
        return topleft + bottomright
