import numpy as np

def contient_double(vec): #verifie si un vecteur contient un double (en ne considerant pas les 0 qui sont les cases vides)
	reste = np.array(vec)
	for i in range(len(vec)):
		reste = np.delete(reste,0)
		if vec[i] in reste and vec[i] != 0:
			return True

	return False

def check_juste(grid):#verifie si la grille donnee est valide
	
	#verifie chaque ligne
	for i in range(9):
		if contient_double(grid[i]):
			return False

	#verifie chaque colonne
	for j in range(9):
		if contient_double(grid[:,j]):
			return False

	#verifie chaque petit carre
	for k in range(3):
		for l in range(3):
			petit_carre = []
			for i in range(3):
				for j in range(3):
					petit_carre.append(grid[k*3+i][l*3+j])

			if contient_double(petit_carre):
				return False

	return True

def suivant(i,j,grid):
	if j < 8 and grid[i][j+1] == 0:
		return (i,j+1)
	elif j < 8:
		return suivant(i,j+1,grid)
	elif grid[i+1][0] == 0:
		return (i+1,0)
	else:
		return suivant(i+1,0,grid)

def premier_zero(grid):
	for i in range(9):
		for j in range(9):
			if grid[i][j] == 0:
				return i,j

def dernier_zero(grid):
	k,l = 0,0
	for i in range(9):
		for j in range(9):
			if grid[i][j] == 0:
				k,l = i,j
	return k,l

def backtracking(test,i,j,grid):
	x,y = dernier_zero(grid)
	if test[x][y] != 0:
		print(test)
	else:
		for k in range(1,10):
			autre_grid = np.copy(test)
			autre_grid[i][j] = k
			if check_juste(autre_grid):
				if (i,j) != (x,y):
					i_bis,j_bis = suivant(i,j,grid)
					backtracking(autre_grid,i_bis,j_bis,grid)
				else:
					backtracking(autre_grid,i,j,grid)

					
grid = np.array([[5,3,0,0,7,0,0,0,0],
	[6,0,0,1,9,5,0,0,0],
	[0,9,8,0,0,0,0,6,0],
	[8,0,0,0,6,0,0,0,3],
	[4,0,0,8,0,3,0,0,1],
	[7,0,0,0,2,0,0,0,6],
	[0,6,0,0,0,0,2,8,0],
	[0,0,0,4,1,9,0,0,5],
	[0,0,0,0,8,0,0,7,9]])

"""test = np.copy(grid)
i,j = premier_zero(grid)
backtracking(test,i,j,grid)"""
