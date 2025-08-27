# # Python3 program to solve N Queen Problem using
# # backtracking
# N = 4

# # ld is an array where its indices indicate row-col+N-1
# # (N-1) is for shifting the difference to store negative
# # indices
# ld = [0] * 30

# # rd is an array where its indices indicate row+col
# # and used to check whether a queen can be placed on
# # right diagonal or not
# rd = [0] * 30

# # Column array where its indices indicates column and
# # used to check whether a queen can be placed in that
# # row or not
# cl = [0] * 30


# # A utility function to print solution
# def printSolution(board):
# 	for i in range(N):
# 		for j in range(N):
# 			print(board[i][j], end=" ")
# 		print()


# # A recursive utility function to solve N
# # Queen problem
# def solveNQUtil(board, col):

# 	# Base case: If all queens are placed
# 	# then return True
# 	if (col >= N):
# 		return True

# 	# Consider this column and try placing
# 	# this queen in all rows one by one
# 	for i in range(N):

# 		# Check if the queen can be placed on board[i][col]

# 		# To check if a queen can be placed on 
# 		# board[row][col] We just need to check 
# 		# ld[row-col+n-1] and rd[row+coln]
# 		# where ld and rd are for left and 
# 		# right diagonal respectively
# 		if ((ld[i - col + N - 1] != 1 and
# 			rd[i + col] != 1) and cl[i] != 1):

# 			# Place this queen in board[i][col]
# 			board[i][col] = 1
# 			ld[i - col + N - 1] = rd[i + col] = cl[i] = 1

# 			# Recur to place rest of the queens
# 			if (solveNQUtil(board, col + 1)):
# 				return True

# 			# If placing queen in board[i][col]
# 			# doesn't lead to a solution,
# 			# then remove queen from board[i][col]
# 			board[i][col] = 0 # BACKTRACK
# 			ld[i - col + N - 1] = rd[i + col] = cl[i] = 0

# 			# If the queen cannot be placed in
# 			# any row in this column col then return False
# 	return False


# # This function solves the N Queen problem using
# # Backtracking. It mainly uses solveNQUtil() to
# # solve the problem. It returns False if queens
# # cannot be placed, otherwise, return True and
# # prints placement of queens in the form of 1s.
# # Please note that there may be more than one
# # solutions, this function prints one of the
# # feasible solutions.
# def solveNQ():
# 	board = [[0, 0, 0, 0],
# 			[0, 0, 0, 0],
# 			[0, 0, 0, 0],
# 			[0, 0, 0, 0],
# 			[0, 0, 0, 0]]
# 	if (solveNQUtil(board, 0) == False):
# 		print("Solution does not exist")
# 		return False
# 	printSolution(board)
# 	return True


# # Driver Code
# if __name__ == '__main__':
# 	solveNQ()

# Python code to for n Queen placement

class GfG:
	def __init__(self):
		self.MAX = 10
		self.arr = [0] * self.MAX
		self.no = 0

	def breakLine(self):
		print("\n------------------------------------------------")

	def canPlace(self, k, i):
		
		# Helper Function to check 
		# if queen can be placed 
		for j in range(1, k):
			if (self.arr[j] == i or
			(abs(self.arr[j] - i) == abs(j - k))):
				return False
		return True

	def display(self, n):
		
		# Function to display placed queen
		self.breakLine()
		self.no += 1
		print("Arrangement No.", self.no, end = " ")
		self.breakLine()

		for i in range(1, n + 1):
			for j in range(1, n + 1):
				if self.arr[i] != j:
					print("\t_", end = " ")
				else:
					print("\tQ", end = " ")
			print()

		self.breakLine()

	def nQueens(self, k, n):
		
		# Function to check queens placement
		for i in range(1, n + 1):
			if self.canPlace(k, i):
				self.arr[k] = i
				if k == n:
					self.display(n)
				else:
					self.nQueens(k + 1, n)

# Driver Code
if __name__ == '__main__':
	n = 8
	obj = GfG()
	obj.nQueens(1, n)
