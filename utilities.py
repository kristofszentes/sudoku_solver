import numpy as np

def contient_double(vec): #checks if a vector contains one element twice
	reste = np.array(vec)
	for i in range(len(vec)):
		reste = np.delete(reste,0)
		if vec[i] in reste and vec[i] != 0:
			return True

	return False

def check_juste(grid):#checks if the given grid is valid
	
	#checking every line
	for i in range(9):
		if contient_double(grid[i]):
			return False

	#checking every column
	for j in range(9):
		if contient_double(grid[:,j]):
			return False

	#checking every square
	for k in range(3):
		for l in range(3):
			petit_carre = []
			for i in range(3):
				for j in range(3):
					petit_carre.append(grid[k*3+i][l*3+j])

			if contient_double(petit_carre):
				return False

	return True

def suivant(i,j,grid):#returns the next 0 in the grid
	if j < 8 and grid[i][j+1] == 0:
		return (i,j+1)
	elif j < 8:
		return suivant(i,j+1,grid)
	elif grid[i+1][0] == 0:
		return (i+1,0)
	else:
		return suivant(i+1,0,grid)

def premier_zero(grid):#returns the first 0 in the grid
	for i in range(9):
		for j in range(9):
			if grid[i][j] == 0:
				return i,j

def dernier_zero(grid):#returns the last 0 in the grid
	k,l = 0,0
	for i in range(9):
		for j in range(9):
			if grid[i][j] == 0:
				k,l = i,j
	return k,l


