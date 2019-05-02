import os
import sys
import time

import pygame as pg

from objects import GolfBall, BigGolfBall, GolfClub, Golfer
from resources import Colors, Events

FPS = 45
SCREEN_WIDTH = 960
SCREEN_HEIGHT = 640


def rp(relative_path):
    """Get absolute path to a resource."""
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


class App():
    def __init__(self):
        """Initialize the game."""
        pg.init()
        pg.display.set_caption("zOoM ZoOm zOw")
        self.clock = pg.time.Clock()
        self.size = SCREEN_WIDTH, SCREEN_HEIGHT
        self.screen = pg.display.set_mode(self.size)
        self.at_menu = True
        self.running = False
        self.ball = GolfBall(self.screen)
        self.big_ball = BigGolfBall(self.screen)
        self.club = GolfClub(self.screen)
        self.golfer = Golfer(self.screen, self.clock, self.club)

    def display_message(self, text):
        """Display a message on the screen for 2 seconds.

        :param text: The text to display
        """
        # Create the font
        large_text = pg.font.Font(
            rp(os.path.join('resources', 'freesansbold.ttf')),
            int(0.075 * self.screen.get_size()[0])
        )
        # Create the text object
        text_surf, text_rect = self.text_objects(text, large_text)
        # Center the text object
        text_rect.center = (
            self.screen.get_size()[0] / 2,
            self.screen.get_size()[1] / 4
        )
        self.screen.blit(text_surf, text_rect)
        pg.display.flip()
        time.sleep(2)
        self.game_loop()

    @staticmethod
    def text_objects(text, font, color=(0, 0, 0)):
        """Create a text object.

        :param text: The text of the object
        :param font: The font of the object
        :param color: The color of the text
        """
        text_surf = font.render(text, True, color)
        return text_surf, text_surf.get_rect()

    def button(self, text, x, y, w, h, ic, ac, action=None):
        """Create a buton.

        :param text: The button text
        :param x: The X position of top left
        :param y: The Y position of top left
        :param w: The width of the button
        :param h: The height of the button
        :param ic: The color of button when not hovering
        :param ac: The color of button when hovering
        :param action: The action to take when clicked
        """
        mouse = pg.mouse.get_pos()
        click = pg.mouse.get_pressed()
        # If the mouse is inside the button
        if x+w > mouse[0] > x and y+h > mouse[1] > y:
            pg.draw.rect(
                self.screen,
                ac,
                (x, y, w, h)
            )
            # If the mouse is clicked on the button
            if click[0] == 1 and action:
                action()
        else:
            # Normal button
            pg.draw.rect(
                self.screen,
                ic,
                (x, y, w, h)
            )
        # The button text
        small_text = pg.font.Font(
            rp(os.path.join('resources', 'freesansbold.ttf')),
            int(0.02 * self.screen.get_size()[0])
        )
        text_surf, text_rect = self.text_objects(
            text, small_text
        )
        text_rect.center = ((x+(w/2)),
                            (y+(h/2)))
        self.screen.blit(text_surf, text_rect)

    def main_menu(self):
        """The main menu for the game."""

        def begin_game():
            """Close the menu and start the game."""
            self.running = True
            self.at_menu = False
            self.game_loop()

        def quit_menu():
            """Close the menu and quit the app."""
            self.at_menu = False

        while self.at_menu:
            for event in pg.event.get():
                # Quit if escape or 'x' button is pressed
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        quit_menu()
                if event.type == pg.QUIT:
                    quit_menu()
            self.screen.fill(Colors.get('heavy_rough'))
            # Title
            large_text = pg.font.Font(
                rp(os.path.join('resources', 'freesansbold.ttf')),
                int(0.075 * self.screen.get_size()[0])
            )
            text_surf, text_rect = self.text_objects(
                "zOoM ZoOm zOw", large_text, Colors.get('tee_area')
            )
            text_rect.center = (
                self.screen.get_size()[0] / 2,
                self.screen.get_size()[1] / 4
            )
            self.screen.blit(text_surf, text_rect)
            # Begin button
            begin_loc = (250, 450, 100, 50)
            self.button(
                "Begin",
                *begin_loc,
                Colors.get('darkgray'),
                Colors.get('lightgray'),
                action=begin_game
            )
            # Quit button
            quit_loc = (600, 450, 100, 50)
            self.button(
                "Quit",
                *quit_loc,
                Colors.get('darkgray'),
                Colors.get('lightgray'),
                action=quit_menu
            )
            pg.display.flip()
            self.clock.tick(FPS)

    def swing_meter(self, pressed_keys):
        """The swing meter."""
        x = self.screen.get_size()[0] // 2 - 300
        y = self.screen.get_size()[1] - 40
        w, h = 500, 20
        # draw the black outline
        pg.draw.rect(
            self.screen,
            Colors.get('black'),
            (x-2, y-2, w+4, h+4)
        )
        # draw the gray box
        pg.draw.rect(
            self.screen,
            Colors.get('darkdarkgray'),
            (x, y, w, h)
        )
        if self.golfer.is_in_swing:
            pg.draw.rect(
                self.screen,
                Colors.get('water'),
                (x, y, w, h)
            )
        # draw each bar
        for i in range(x, x+w, 10):
            if i == x + w - (w / 5):
                color = Colors.get('flag')
            else:
                color = Colors.get('darkgray')
            pg.draw.rect(
                self.screen,
                color,
                (i+2, y+2, 6, h-2)
            )

    def game_loop(self):
        """The game loop, when Begin is pressed."""

        def quit_game():
            """Quit the game back to the main menu."""
            self.at_menu = True
            self.running = False
            self.main_menu()

        while self.running:
            for event in pg.event.get():
                # Quit to menu on escape
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        quit_game()
                if event.type == pg.QUIT:
                    quit_game()

            pressed_keys = pg.key.get_pressed()
            # If the ball is on the ground and they press T, tee up
            if self.ball.on_ground and pressed_keys[pg.K_t]:
                self.ball.tee_up()

            self.screen.fill(Colors.get('tee_area'))
            # Display the swing meter
            self.swing_meter(pressed_keys)
            # Get power and accuracy from the golfer
            if self.ball.teed_up and pressed_keys[pg.K_SPACE]:
                power, accuracy = self.golfer.update(
                    pressed_keys,
                    start_swing=True
                )
            else:
                power, accuracy = self.golfer.update(pressed_keys)
            #self.club.update()
            if self.ball.on_ground:
                self.ball.update(power, accuracy)
            else:
                self.ball.update()
            self.big_ball.update()
            pg.display.flip()
            #print(self.clock.get_fps())
            self.clock.tick(FPS)


# 'Nameguard' - this starts the game only if called with `python run.py`
if __name__ == '__main__':
    app = App()
    app.main_menu()
    pg.quit()
    sys.exit()

