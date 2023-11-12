import arcade, random, time, colorama

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
rayon_cercle = 20
COLORS = [arcade.csscolor.__package__]
class Boule:
    def __init__(self):
        print("Boule is initializing. ")
        self.cercle_x = random.randint(0, 800)
        self.cercle_y = random.randint(0, 600)
        self.cercle_change_x = 2 # Nombre d'unité pour le déplacement sur l'axe des X
        self.cercle_change_y = 3 # Nombre d'unité pour le déplacement sur l'axe des Y
    def update(self):
        self.cercle_x += self.cercle_change_x
        self.cercle_y += self.cercle_change_y

        if self.cercle_x < 0 + rayon_cercle:
            self.cercle_change_x *= -1

        if self.cercle_x > SCREEN_WIDTH - rayon_cercle:
            self.cercle_change_x *= -1

        if self.cercle_y < 0 + rayon_cercle:
            self.cercle_change_y *= -1

        if self.cercle_y > SCREEN_HEIGHT - rayon_cercle:
            self.cercle_change_y *= -1

    def draw(self):
        #print(str(self))
        arcade.draw_circle_filled(self.cercle_x, self.cercle_y, rayon_cercle, arcade.color.RED, num_segments=16)
    
class MyGame(arcade.Window):
    def __init__(self):
        print("MyGame is Initializing. ")
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Exercice #1")


        arcade.set_background_color(arcade.color.SKY_BLUE)
        arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT / 2, 0, arcade.csscolor.DARK_GREEN)
        
        self.boule1 = Boule()
        self.boule2 = Boule()
    def on_draw(self):
        arcade.start_render()

        self.boule1.draw()
        
        self.boule2.draw()
    def on_update(self,delta_time):
        self.boule1.update()
        
        self.boule2.update()
    def on_mouse_press(self,x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            self.boule2 = Boule()
            
        if button == arcade.MOUSE_BUTTON_RIGHT:
            pass
        self.on_draw()
def main():
   my_game = MyGame()
   my_game.on_mouse_press
   
   arcade.run()

main()