#1. include pygame
import pygame

#from math module(in python) gets fabs method
from math import fabs
#2. init pygame
##in order to use pygame must run init method
pygame.init()

#3. creat screen with size
##the screen size must be a tuple
screen_size = (512, 480)
##actually tell python to set screen up and store it
pygame_screen = pygame.display.set_mode(screen_size)
##set a caption
pygame.display.set_caption("Goblin Chase")
##set up a variable with our image
background_image = pygame.image.load('background2.png')
hero_image = pygame.image.load('hero.png')
goblin_image = pygame.image.load('goblin.png')
#make a font so we can write on the screen


##3a set up a hero location
hero = {
	"x": 100,
	"y": 100,
	"speed": 20,
	"wins": 0
}


#font = pygame.font.Font(None, 25)
#wins_text = font.render("Wins: %d" % (hero['wins']), True, (0,0,0))

goblin = {
	"x": 200,
	"y": 200,
	"speed": 15
}

keys = {
	"up": 273,
	"down": 274,
	"right": 275,
	"left": 276
}

keys_down = {
	"up": False,
	"down": False,
	"left": False,
	"right": False
}

#4. create game loop (while)
##create a boolean for whether the game should be going or not
game_on = True
while game_on:   
#we are inside the main game loop. will keep running as long as bool is true

#5. add quit event (python needs an escape)
##pygame comes with an event loop (kind of like JS)
	for event in pygame.event.get():
		if (event.type == pygame.QUIT): ##means the user cliked the red X to exit
			game_on = False
		elif event.type == pygame.KEYDOWN:
			#print "User pressed a key!"
			if event.key == keys["up"]: ##273 is the up arrow key
				#hero['y'] -= hero['speed']
				keys_down["up"] == True
			elif event.key == keys["down"]:
				#hero ['y'] += hero ["speed"]
				keys_down["down"] == True
			elif event.key == keys["right"]:
				#hero ['x'] += hero['speed']
				keys_down["left"] == True
			elif event.key == keys["left"]:
				#hero['x'] -= hero['speed']
				keys_down["right"] == True

		elif event.type == pygame.KEYUP: ##the use let go of a key see if its one that matters
			if event.key == keys["up"]:
				keys_down['up'] = False
			if event.key == keys["down"]:
				keys_down['down'] = False
			if event.key == keys["right"]:
				keys_down['right'] = False
			if event.key == keys["left"]:
				keys_down['left'] = False


	if keys_down["up"]:
		hero['y'] -= hero['speed']
	elif keys_down["down"]:
		hero['y'] += hero['speed']
	if keys_down["left"]:
		hero['x'] -= hero['speed']
	elif keys_down["right"]:
		hero ['x'] += hero['speed']

	##COLLISION DETECTION
	distance_between = fabs(hero['x'] - goblin['x']) + fabs(hero['y'] - goblin['y'])
	if distance_between < 32: ##hero and goblin are touching
		print "collision"
	else:
		print "not touching"



#6. fill in the screen with a color (or image)
##blie takes 2 arguments
##1 what do you want to draw? and where to you want it to draw
##[0,0] starts in the top left corner
	pygame_screen.blit(background_image, [0,0])
	
	font = pygame.font.Font(None, 25)
	wins_text = font.render("Wins: %d" % (hero['wins']), True, (0,0,0))
	pygame_screen.blit(wins_text, [40,40])

	pygame_screen.blit(hero_image, [hero["x"], hero["y"]])
	pygame_screen.blit(goblin_image, [goblin['x'], goblin['y']])
 #background image it what. [0,0] is where

#7. repeat 6 over and over and over
	pygame.display.flip()