import pygame
import numpy as np
from utilities import *

pygame.init()

#dimensions of the window
hauteur = 540
largeur = 480

#the font
myfont = pygame.font.SysFont("Arial",30,True)

#the background image
background = pygame.image.load("background_grid.png")

#the puzzle we want to solve
puzzle = 'grids/grid1.csv'

grid = np.genfromtxt(puzzle, delimiter=',', dtype='int')

class Jeu():
	def __init__(self,grid):
		self.gagne = False
		self.grid_initial = grid
		self.solving = False
		self.grid = np.copy(self.grid_initial)

	def maj_ecran(self,ecran,grille): #the display

		#the black background and the grid background
		ecran.fill((255,255,255))
		ecran.blit(background,(0,0))

		#the numbers
		for i in range(9):
			for j in range(9):
				if grille[i][j] != 0:
					texte_nbre = myfont.render(str(grille[i][j]),1,(0,0,0))
					ecran.blit(texte_nbre,(30+50*j,25+50*i))

		#the buttons
		pygame.draw.rect(ecran,(202,204,206),(20,480,100,50))
		texte_solve = myfont.render("Solve",1,(0,0,0))
		ecran.blit(texte_solve,(25,490))

		#The "Solving..." text
		if self.solving:
			texte_solving = myfont.render("Solving...",1,(0,0,0))
			ecran.blit(texte_solving,(200,490))

		pygame.display.update()

	def backtracking(self,test,i,j,grid,ecran): #the backtracking algorithm
		if self.solving:
			pygame.time.delay(10)
			self.maj_ecran(ecran,test)
			x,y = dernier_zero(grid)
			if test[x][y] != 0:
				print(test)
				self.grid = np.copy(test)
				self.solving = False
			else:
				for k in range(1,10):
					autre_grid = np.copy(test)
					autre_grid[i][j] = k
					if check_juste(autre_grid):
						if (i,j) != (x,y):
							i_bis,j_bis = suivant(i,j,grid)
							self.backtracking(autre_grid,i_bis,j_bis,grid,ecran)
						else:
							self.backtracking(autre_grid,i,j,grid,ecran)

	def run(self): #the main function
		screen = pygame.display.set_mode((largeur,hauteur))
		pygame.display.set_caption("Sudoku")

		cont = True

		while cont:

			pygame.time.delay(30)

			#to close the window
			events = pygame.event.get()
			for event in events:
				if event.type == pygame.QUIT:
					cont = False

			#when we press the "solve" button
			if pygame.mouse.get_pressed()[0]:
				x,y = pygame.mouse.get_pos()

				if x >= 20 and x <= 120 and y >= 480 and y <= 530:
					
					self.solving = True
					test = np.copy(grid)
					self.backtracking(test,premier_zero(grid)[0],premier_zero(grid)[1],self.grid_initial,screen)

			self.maj_ecran(screen,self.grid)


if __name__ == "__main__":
	jeu = Jeu(grid)
	jeu.run()
	pygame.quit()