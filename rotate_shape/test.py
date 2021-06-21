
from mygrid import Grid

# fmatrix = [[0, 0], [10, 0], [10, 20], [20, 20], [20, 30], [10, 30], [10, 40], [30, 40], [30, 50], [0, 50]]
amatrix = [[-10, 0], [60, 0], [30, 40]]
transfor_matrix = [[0, -1], [1, 0]]

def multiplication(m1, m2):
	new = [] # m1_row x m2_column
	for i in range(len(m1)):
		row = []
		for j in range(len(m2[0])):
			suma = 0
			for k in range(len(m2)):
				# print(f"{i},{k} - {k}{j}")
				# print(m1[i][k], m2[k][j])
				suma += m1[i][k] * m2[k][j]
			row.append(suma)
		new.append(row)
		print('------------')
	return new

def transpose(m):
	new = []
	for i in range(len(m[0])):
		# new.append([])
		row = []
		for j in range(len(m)):
			# row[i].append(m[j][i])
			row.append(m[j][i])
		new.append(row)
	return new


# newmatrix = transpose(multiplication(transfor_matrix, transpose(fmatrix)))
newmatrix = transpose(multiplication(transfor_matrix, transpose(amatrix)))
g = Grid()

for i in range(len(amatrix)):
	x1, y1 = amatrix[i]
	x2, y2 = amatrix[(i+1) % len(amatrix)]
	# print(x1, y1, x2, y2)
	g.draw_line(x1, y1, x2, y2, 'red')

for i in range(len(newmatrix)):
	x1, y1 = newmatrix[i]
	x2, y2 = newmatrix[(i+1) % len(newmatrix)]
	# print(x1, y1, x2, y2)
	g.draw_line(x1, y1, x2, y2, 'red')


for i in amatrix:
	print(i)

for j in newmatrix:
	print(j)

g.done()


