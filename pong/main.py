#!/usr/bin/env python3
# coding=utf-8

"""
Basic Kivy Pong Example.

    https://kivy.org/docs/tutorials/pong.html
"""

from random import randint


import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.scatter import Scatter
from kivy.vector import Vector
from kivy.clock import Clock
from kivy.properties import (
    NumericProperty,
    ReferenceListProperty,
    ObjectProperty
)
from kivy.graphics import (
    Color,
    Ellipse,
    Line
)

kivy.require('1.9.0')

##########################################


##########################################
class RelativeCollide(Widget):
    """Adds relative Aware collide functions."""

    def collide_widget_relative(self, widget):
        """Collide Widget test that takes into account relative layouts."""
        # w_x, w_y = self.to_widget(*widget.pos)
        w_x, w_y = widget.pos
        w_right = w_x + widget.width
        w_top = (w_y + widget.height)
        # widget_pos now is in the same coordinate space as self.pos
        # really?
        # simple rectangular boundingbox check:
        result = True
        flag_left = False
        flag_right = False
        flag_bottom = False
        flag_top = False
        # check if widget is outside of self
        # check horizontal intersections
        # check if self left side is > as widget right side
        if self.x > w_right:
            result = False
            flag_left = True
        # check if self right side is < as widget left side
        if self.right < w_x:
            result = False
            flag_right = True
        # check vertical intersections
        # check if self bottom side is > as widget top side
        if self.y > w_top:
            result = False
            flag_bottom = True
        # check if self top side is < as widget bottom side
        if self.top < w_y:
            result = False
            flag_top = True
        if result:
            print(
                "x: {:>+12f} y: {:>+12f};  "
                "right: {:>+12f} top: {:>+12f};  "
                "w_pos_x: {:>+12f} w_y: {:>+12f}  "
                "w_right: {:>+12f} w_top: {:>+12f} "
                "".format(
                    self.x,
                    self.y,
                    self.right,
                    self.top,
                    w_x,
                    w_y,
                    w_right,
                    w_top
                )
            )
        # if self.parent.myname == "Player Left":
        #     print(
        #         "x: {:>+12f} y: {:>+12f};  "
        #         "right: {:>+12f} top: {:>+12f};  "
        #         "w_pos_x: {:>+12f} w_y: {:>+12f}  "
        #         "w_right: {:>+12f} w_top: {:>+12f} "
        #         "left {:<1} right {:<1} bottom {:<1} top {:<1}"
        #         "".format(
        #             self.x,
        #             self.y,
        #             self.right,
        #             self.top,
        #             w_x,
        #             w_y,
        #             w_right,
        #             w_top,
        #             flag_left,
        #             flag_right,
        #             flag_bottom,
        #             flag_top
        #         )
        #     )
        return result

    def collide_position_relative(self, x, y):
        """Collide Position test that takes into account relative layouts."""
        pass


##########################################
class PongGate(Widget):
    """A Gate."""

    def check_ball(self, ball):
        """Check if ball is in the gate."""
        # if self.collide_widget(ball):
        #     self.parent.score += 1
        #     return True


class PongPaddle(RelativeCollide):
    """A Paddle."""

    touch_y_offset = 0

    def bounce_ball(self, ball):
        """Bounce ball away."""
        # touch.apply_transform_2d(self.to_local)
        # if self.collide_widget(ball):
        if self.collide_widget_relative(ball):
            # print("bounce..")
            with self.parent.parent.canvas:
                Color(0, 1, 0)
                d = 10.
                Ellipse(
                    pos=(
                        ball.center_x - (d / 2),
                        ball.center_y - (d / 2)
                    ),
                    size=(d, d)
                )
            # vx, vy = ball.velocity
            # offset = (ball.center_y - self.center_y) / (self.height / 2)
            # bounced = Vector(-1 * vx, vy)
            # vel = bounced * 1.1
            # ball.velocity = vel.x, vel.y + offset

    def on_touch_move(self, touch):
        """Move Paddle with touch."""
        # print(self)
        # print(touch)
        # widget_touch_x, widget_touch_y = self.to_widget(
        #     touch.x, touch.y, relative=False
        # )
        # widget_rel_touch_x, widget_rel_touch_y = self.to_widget(
        #     touch.x, touch.y, relative=True
        # )
        # local_touch_x, local_touch_y = self.to_local(
        #     touch.x, touch.y, relative=False
        # )
        # local_rel_touch_x, local_rel_touch_y = self.to_local(
        #     touch.x, touch.y, relative=True
        # )
        # if local_rel_touch_x < 200 and local_rel_touch_x > -10:
        #     print(
        #         "self       x:{:>5} y:{:>5} collide_point:{}\n"
        #         "touch      x:{:>5} y:{:>5} collide_point:{}\n"
        #         "widget     x:{:>5} y:{:>5} collide_point:{}\n"
        #         "widget rel x:{:>5} y:{:>5} collide_point:{}\n"
        #         "local      x:{:>5} y:{:>5} collide_point:{}\n"
        #         "local rel  x:{:>5} y:{:>5} collide_point:{}\n"
        #         "\n".format(
        #             self.x, self.y, self.collide_point(self.x, self.y),
        #             touch.x, touch.y,
        #             self.collide_point(touch.x, touch.y),
        #             widget_touch_x, widget_touch_y,
        #             self.collide_point(widget_touch_x, widget_touch_y),
        #             widget_rel_touch_x, widget_rel_touch_y,
        #             self.collide_point(
        #                 widget_rel_touch_x,
        #                 widget_rel_touch_y
        #             ),
        #             local_touch_x, local_touch_y,
        #             self.collide_point(local_touch_x, local_touch_y),
        #             local_rel_touch_x, local_rel_touch_y,
        #             self.collide_point(local_rel_touch_x, local_rel_touch_y)
        #         )
        #     )

        if self.collide_point(touch.x, touch.y):
            # print("touch: {}".format(touch))
            # print("touch.pos: {}".format(touch.pos))
            # print("touch.ox: {}".format(touch.ox))
            # geht
            touch_center_y = touch.y - self.touch_y_offset
            # does not work - self.center_y will change..
            # we need the positionoffset at touch_down.
            # touch_center_y = touch.y - (touch.oy - self.center_y)
            # self.center_y = touch_center_y
            # print("self.parent.height: {}".format(self.parent.height))
            # print("touch_center_y + (self.height/2): {}".format(
            #     touch.y + (self.height/2)
            # ))
            # print("touch_center_y - (self.height/2): {}".format(
            #     touch.y - (self.height/2)
            # ))
            # return True
            # check bounds of panelmovement.
            if (
                (touch_center_y + (self.height/2) < self.parent.height) and
                (touch_center_y - (self.height/2) > 0)
            ):
                self.center_y = touch_center_y
                return True

    def on_touch_down(self, touch):
        """Move Paddle with touch."""
        if self.collide_point(touch.x, touch.y):
            self.touch_y_offset = touch.y - self.center_y


class PongPlayer(Scatter):
    """A Player."""

    score = NumericProperty(0)


##########################################


class PongBall(Widget):
    """A Ball."""

    # velocity of the ball on x and y axis
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)

    # referencelist property so we can use ball.velocity as
    # a shorthand, just like e.g. w.pos for w.x and w.y
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    def move(self):
        """
        Move the ball one step.

        This will be called in equal intervals to animate the ball
        """
        self.pos = Vector(*self.velocity) + self.pos


##########################################


class PongGame(Widget):
    """The Game."""

    ball = ObjectProperty(None)

    def serve_ball(self, vel=None):
        """Start new Ball."""
        if vel is None:
            vel = Vector(10, 0).rotate(randint(0, 360))
        self.ball.center = self.center
        self.ball.velocity = vel

    def update(self, dt):
        """Call ball.move and other stuff."""
        self.ball.move()

        # bounce of paddles
        self.player1.paddle.bounce_ball(self.ball)
        self.player2.paddle.bounce_ball(self.ball)

        # bounce off top and bottom
        if (self.ball.y < 0) or (self.ball.top > self.height):
            self.ball.velocity_y *= -1

        # bounce off left and right
        if (self.ball.x < 0) or (self.ball.right > self.width):
            self.ball.velocity_x *= -1

        # went of to a side to score point?
        if (
            self.player1.gate.check_ball(self.ball) or
            self.player2.gate.check_ball(self.ball)
        ):
            self.serve_ball()


##########################################


class PongApp(App):
    """My first Pong App."""

    def build(self):
        """Kivy entry point."""
        game = PongGame()
        game.serve_ball()
        Clock.schedule_interval(game.update, 1.0/60.0)
        return game


##########################################
if __name__ == '__main__':
    PongApp().run()
