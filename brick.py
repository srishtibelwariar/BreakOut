#!/usr/bin/env python
#BreakOut game
#Srishti Belwariar

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.vector import Vector
from kivy.clock import Clock
from kivy.properties import NumericProperty
from kivy.properties import ReferenceListProperty
from kivy.properties import ObjectProperty
from random import randint

class BBBrick(Widget):
    def bounce_off_brick(self, ball):
        if self.collide_widget(ball) and self.parent!=None:
            vx, vy = ball.v
            offset = (ball.center_x - self.center_x)/ (self.height)
            vy= vy* -1
            rebound = Vector(vx, vy)
            vel = rebound * 1                          
            ball.v = vel.x, vel.y +offset
            #self.size = 0,0
            #self.disabled=True
            self.parent.remove_widget(self)
            
            

class BBPaddle(Widget):
    def bounce_ball(self, ball):
        if self.collide_widget(ball):
            vx, vy = ball.v
            offset = (ball.center_x - self.center_x) / (self.height/ 2)
            vy= vy* -1
            rebound = Vector(vx, vy)
            vel = rebound *1
            ball.v = vel.x, vel.y + offset


class BBBall(Widget):
    v_x=NumericProperty(10);
    v_y=NumericProperty(10);
    v=ReferenceListProperty(v_x, v_y)
    
    def move(self):
        self.pos = Vector(*self.v) + self.pos
            
            
class BBGame(Widget):
    ball = ObjectProperty(None)
    player= ObjectProperty(None)
    
    b10= ObjectProperty(None)
    b20= ObjectProperty(None)
    b30= ObjectProperty(None)
    b40= ObjectProperty(None)
    b50= ObjectProperty(None)
    b60= ObjectProperty(None)
    b70= ObjectProperty(None)
    
    b11= ObjectProperty(None)
    b21= ObjectProperty(None)
    b31= ObjectProperty(None)
    b41= ObjectProperty(None)
    b51= ObjectProperty(None)
    b61= ObjectProperty(None)
    b71= ObjectProperty(None)

    b12= ObjectProperty(None)
    b22= ObjectProperty(None)
    b32= ObjectProperty(None)
    b42= ObjectProperty(None)
    b52= ObjectProperty(None)
    b62= ObjectProperty(None)
    b72= ObjectProperty(None)
   
    b13= ObjectProperty(None)
    b23= ObjectProperty(None)
    b33= ObjectProperty(None)
    b43= ObjectProperty(None)
    b53= ObjectProperty(None)
    b63= ObjectProperty(None)
    b73= ObjectProperty(None)
    
    def serve_ball(self, v=(4,0)):
        self.ball.center_x = self.player.center_x
        self.ball.y = self.y + 100
        self.ball.center=self.ball.center_x, self.ball.y
        v=Vector(v)
        self.ball.velocity = v.rotate(randint(50, 130))

    def update(self, dt):
        self.ball.move()
        self.player.bounce_ball(self.ball)
        
        self.b10.bounce_off_brick(self.ball)
        self.b20.bounce_off_brick(self.ball)
        self.b30.bounce_off_brick(self.ball)
        self.b40.bounce_off_brick(self.ball)
        self.b50.bounce_off_brick(self.ball)
        self.b60.bounce_off_brick(self.ball)
        self.b70.bounce_off_brick(self.ball)
        self.b11.bounce_off_brick(self.ball)
        self.b21.bounce_off_brick(self.ball)
        self.b31.bounce_off_brick(self.ball)
        self.b41.bounce_off_brick(self.ball)
        self.b51.bounce_off_brick(self.ball)
        self.b61.bounce_off_brick(self.ball)
        self.b71.bounce_off_brick(self.ball)
        self.b12.bounce_off_brick(self.ball)
        self.b22.bounce_off_brick(self.ball)
        self.b32.bounce_off_brick(self.ball)
        self.b42.bounce_off_brick(self.ball)
        self.b52.bounce_off_brick(self.ball)
        self.b62.bounce_off_brick(self.ball)
        self.b72.bounce_off_brick(self.ball)
        self.b13.bounce_off_brick(self.ball)
        self.b23.bounce_off_brick(self.ball)
        self.b33.bounce_off_brick(self.ball)
        self.b43.bounce_off_brick(self.ball)
        self.b53.bounce_off_brick(self.ball)
        self.b63.bounce_off_brick(self.ball)
        self.b73.bounce_off_brick(self.ball)
        
        # bounce off top, left and right edges
        if (self.ball.top > self.height):
            self.ball.v_y = self.ball.v_y * -1
        if (self.ball.x < 0) or (self.ball.right > self.width):
            self.ball.v_x = self.ball.v_x * -1
        
        #initiate reserves if ball misses paddle   
        if (self.ball.y<self.y):
            self.serve_ball(v=(4, 0))

    #allows for user control on paddle using mouse (plan to change it to arrow keys)
    def on_touch_move(self, touch):
        self.player.center_x = touch.x
    

class BBApp(App):
    def build(self):
        game = BBGame()
        game.serve_ball()
        Clock.schedule_interval(game.update, 1.0 / 60.0)
        return game


if __name__ == '__main__':
    BBApp().run()
