from heapq import heappop, heappush

filename = 'problemstatement.txt' #'test.txt' #'
file = open(filename, 'r').readlines()

#0 is right, 1 is down, 2 is left, 3 is up
direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
heatMap = [[int(node) for node in row[:-1]] for row in file]
HEIGHT = len(heatMap)
WIDTH = len(heatMap[0])

visited = set()
rankedList = [(0, 0, 0, 0, 0, 0)] #heatloss, row, col, rowchange, colchange, consecutive --> heap sorts by the first element

while rankedList:
	heatloss, row, col, drow, dcol, consecutive = heappop(rankedList)

	if row == HEIGHT-1 and col == WIDTH-1:
		print(heatloss)
		break

	if (row, col, drow, dcol, consecutive) in visited:
		continue
	visited.add((row, col, drow, dcol, consecutive))

	if consecutive < 3 and (drow, dcol) != (0, 0):
		nextRow = drow+row
		nextCol = dcol+col
		if nextRow >= 0 and nextRow < HEIGHT and nextCol >= 0 and nextCol < WIDTH:
			heappush(rankedList, (heatloss+heatMap[nextRow][nextCol], nextRow, nextCol, drow, dcol, consecutive+1))
	
	for turndRow, turndCol in direction:
		if (turndRow, turndCol) == (drow, dcol) or (turndRow, turndCol) == (-drow, -dcol):
			continue
		nextRow = row+turndRow
		nextCol = col+turndCol
		if nextRow >= 0 and nextRow < HEIGHT and nextCol >= 0 and nextCol < WIDTH:
			heappush(rankedList, (heatloss+heatMap[nextRow][nextCol], nextRow, nextCol, turndRow, turndCol, 1))
	


