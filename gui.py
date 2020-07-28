import pygame
import numpy as np
from solver import *

pygame.init()

#taille de la fenetre
hauteur = 540
largeur = 480

#la police
myfont = pygame.font.SysFont("Arial",30,True)

#la grille en fond
background = pygame.image.load("sudoku_grid.png")

grid = np.array([[5,3,0,0,7,0,0,0,0],
	[6,0,0,1,9,5,0,0,0],
	[0,9,8,0,0,0,0,6,0],
	[8,0,0,0,6,0,0,0,3],
	[4,0,0,8,0,3,0,0,1],
	[7,0,0,0,2,0,0,0,6],
	[0,6,0,0,0,0,2,8,0],
	[0,0,0,4,1,9,0,0,5],
	[0,0,0,0,8,0,0,7,9]])

class Jeu():
	def __init__(self,grid):
		self.gagne = False
		self.grid = grid

	def maj_ecran(self,ecran): #l'affichage

		#le fond blanc et la grille
		ecran.fill((255,255,255))
		ecran.blit(background,(0,0))

		#les nombres
		for i in range(9):
			for j in range(9):
				if self.grid[i][j] != 0:
					texte_nbre = myfont.render(str(self.grid[i][j]),1,(0,0,0))
					ecran.blit(texte_nbre,(25+50*j,25+50*i))

		#les boutons
		pygame.draw.rect(ecran,(202,204,206),(20,480,100,50))
		texte_solve = myfont.render("Solve",1,(0,0,0))
		ecran.blit(texte_solve,(25,490))

		pygame.display.update()

	def backtracking(self,test,i,j,grid):
		x,y = dernier_zero(grid)
		if test[x][y] != 0:
			self.grid = np.copy(test)
		else:
			for k in range(1,10):
				autre_grid = np.copy(test)
				autre_grid[i][j] = k
				if check_juste(autre_grid):
					if (i,j) != (x,y):
						i_bis,j_bis = suivant(i,j,grid)
						self.backtracking(autre_grid,i_bis,j_bis,grid)
					else:
						self.backtracking(autre_grid,i,j,grid)

	def run(self):
		screen = pygame.display.set_mode((largeur,hauteur))
		pygame.display.set_caption("Sudoku")

		cont = True

		while cont:

			pygame.time.delay(30)

			#pour fermer la fenetre
			events = pygame.event.get()
			for event in events:
				if event.type == pygame.QUIT:
					cont = False

			#lorsqu'on appuie sur le bouton
			if pygame.mouse.get_pressed()[0]:
				x,y = pygame.mouse.get_pos()

				if x >= 20 and x <= 120 and y >= 480 and y <= 530:

					texte_solving = myfont.render("Solving...",1,(0,0,0))
					screen.blit(texte_solving,(200,490))
					pygame.display.update()

					test = np.copy(grid)
					self.backtracking(test,premier_zero(grid)[0],premier_zero(grid)[1],grid)

			self.maj_ecran(screen)


if __name__ == "__main__":
	jeu = Jeu(grid)
	jeu.run()
	pygame.quit()

