#réalisé par Alexandre Wilbue en 2023
import arcade, random, time, colorama #importer quelques modules

#Dimensions de l'écran

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

#Couleurs que les Objets vont prendre

COLORS = [arcade.csscolor.RED, arcade.csscolor.BROWN, arcade.csscolor.PINK, arcade.csscolor.BLUE, arcade.csscolor.GREEN, arcade.csscolor.BLACK, arcade.csscolor.ORANGE, arcade.csscolor.YELLOW]

class Boule: #La class, qui va représenter chaque balle 

    #La méthode __init__ qui sera appelé une fois pour chaque cercle
    #Elle contient les attributs de la classe Boule

    def __init__(self, x, y, chx, chy, rayon, color):
        print("Boule is initializing. ")
        self.cercle_x = x
        self.cercle_y = y
        self.cercle_change_x = chx # Nombre d'unité pour le déplacement sur l'axe des X
        self.cercle_change_y = chy # Nombre d'unité pour le déplacement sur l'axe des Y
        self.rayon_cercle = rayon
        self.cercle_color = color

    #Les méthodes update et draw qui seront appelés constament

    def update(self):

        #Bouger le rectangle en changeant ses coordonnés

        self.cercle_x += self.cercle_change_x
        self.cercle_y += self.cercle_change_y

        #Corriger le mouvement du cercle pour éviter qu'il sorte de la fenêtre

        if self.cercle_x < 0 + self.rayon_cercle: #Le cercle est à gauche de la fenêtre
            self.cercle_x += 1
            self.cercle_change_x *= -1

        if self.cercle_x > SCREEN_WIDTH - self.rayon_cercle: #Le cercle est à droite de la fenêtre
            self.cercle_x -= 1
            self.cercle_change_x *= -1

        if self.cercle_y < 0 + self.rayon_cercle: #Le cercle est en bas de la fenêtre
            self.cercle_y += 1
            self.cercle_change_y *= -1

        if self.cercle_y > SCREEN_HEIGHT - self.rayon_cercle: #Le cercle est en haut de la fenêtre
            self.cercle_y -= 1
            self.cercle_change_y *= -1

    def draw(self):
        #print(str(self))
        arcade.draw_circle_filled(self.cercle_x, self.cercle_y, self.rayon_cercle, self.cercle_color, num_segments=16) #Dessiner le cercle au nouvel endroit
    
class Rectangle: #La classe qui va représenter chaque rectangle

    #La méthode __init__ qui sera appelé une fois pour chaque rectangle
    #Elle contient les attributs de la classe Rectangle

    def __init__(self, x, y, chx, chy, width, height, color):
        print("Rectangle is initializing. ")
        self.rectangle_x = x
        self.rectangle_y = y
        self.rectangle_change_x = chx # Nombre d'unité pour le déplacement sur l'axe des X
        self.rectangle_change_y = chy # Nombre d'unité pour le déplacement sur l'axe des Y
        self.rectangle_width = width
        self.rectangle_height = height
        self.rectangle_color = color

        #Les méthodes update et draw qui seront appelés constament

    def update(self):
        
        #Bouger le rectangle en changeant ses coordonnés

        self.rectangle_x += self.rectangle_change_x
        self.rectangle_y += self.rectangle_change_y

        #Corriger le mouvement du cercle pour éviter qu'il sorte de la fenêtre
        
        if self.rectangle_x < 0 + self.rectangle_width / 2: #Le rectangle est à gauche de la fenêtre
            self.rectangle_x += 1
            self.rectangle_change_x *= -1

        if self.rectangle_x > SCREEN_WIDTH - self.rectangle_width / 2: #Le rectangle est à droite de la fenêtre
            self.rectangle_x -= 1
            self.rectangle_change_x *= -1

        if self.rectangle_y < 0 + self.rectangle_height / 2: #Le rectangle est en bas de la fenêtre
            self.rectangle_y += 1
            self.rectangle_change_y *= -1

        if self.rectangle_y > SCREEN_HEIGHT - self.rectangle_height / 2: #Le rectangle est en haut de la fenêtre
            self.rectangle_y -= 1
            self.rectangle_change_y *= -1

    def draw(self):
        #print(str(self))
        arcade.draw_rectangle_filled(self.rectangle_x, self.rectangle_y, self.rectangle_width, self.rectangle_height, self.rectangle_color) #Dessiner le rectangle au nouvel endroit

class MyGame(arcade.Window): #La classe qui va controller le jeu au complet et qui va ouvrir la fenêtre dans Windows

    #La méthode __init__ qui sera appelé une fois

    def __init__(self):
        print("MyGame is Initializing. ")
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "TP4") #Ouvrir la nouvelle fenêtre avec les bons paramètre
        arcade.set_background_color(arcade.color.SKY_BLUE) #Couleur de l'arrière plan

        #La liste qui va contenir tous les Instances (en Anglais) des classes Rectangles et Boule
        #Chaque Instance réprésente un objet qui bouge dans la fenêtre Windows
        #À travers le programme, le paramètre self fait référence à une Instance de la classe
        #On commence déja avec une boule qui bouge quand on démarre le programme

        self.clist = [Boule(random.randint(1, 800), random.randint(1, 600), random.randint(-5,5), random.randint(-5,5), random.randint(10,30), random.choice(COLORS))]

    def on_draw(self): #La méthode on_draw() qui sera appelée constamment par le arcarde.run()
        arcade.start_render() #Faire apparaitre l'arrière plan et enlever les anciens objets (classes)

        for obj in self.clist: #Dessiner et faire bouger chaque Instance de classe
            #print("Attempting to load balls")
            obj.draw()
            obj.update()

    #Ajouter un objet à la liste de Rectangles et de Cercles à chaque fois qu'on appuie sur la fenêtre
    #Cet objet aura des attributs aléatoires, mais sera créé à la place de l'appuie sur la fenêtre 

    def on_mouse_press(self,x, y, button, modifiers): #La méthode qui est appelé quand on appuie sur la fenêtre
        if button == arcade.MOUSE_BUTTON_LEFT: #Condition pour le bouton de gauche

            self.clist.append(Boule(x, y, random.randint(-5,5), random.randint(-5,5), random.randint(10,30), random.choice(COLORS)))

        if button == arcade.MOUSE_BUTTON_RIGHT: #Condition pour le boutton de droite

            self.clist.append(Rectangle(x, y, random.randint(-5,5), random.randint(-5,5), random.randint(20,50), random.randint(20,50), random.choice(COLORS)))

def main(): #La fonction qui va faire rouler le jeu
    my_game = MyGame()
    my_game.on_mouse_press
    
    arcade.run() #Faire rouler on_draw, on_mouse_press on_update(Je l'ai enlevé)
main()