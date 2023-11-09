import arcade, random, time, colorama

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

COLORS = []



class MyGame(arcade.Window):
   def __init__(self):
       super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Exercice #1")
       pass

   def setup(self):
       
       pass

   def on_draw(self):
       arcade.start_render()

       pass


def main():
   my_game = MyGame()
   my_game.setup()

   arcade.run()


main()

