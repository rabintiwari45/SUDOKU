board =  [
  [7,8,0,4,0,0,1,2,0],
  [6,0,0,0,7,5,0,0,9],
  [0,0,0,6,0,1,0,7,8],
  [0,0,7,0,4,0,2,6,0],
  [0,0,1,0,5,0,9,3,0],
  [9,0,4,0,6,0,0,0,5],
  [0,7,0,3,0,0,0,1,2],
  [1,2,0,0,0,7,4,0,0],
  [0,4,9,2,0,6,0,0,7]
]

def display_board(board):
  """
  Takes list of list and print out the
  board with vertical and horizontal lines.
  
  * Print horizontal line after every third iteration.
  
  * Print vertical line after every third iteration.
  """
  for i in range(0,len(board)):
      if i % 3 == 0 and i != 0:
          print("----------------------")
      for j in range(0,len(board[0])):
          if j % 3 == 0 and j != 0:
              print("| ",end="")
          print(str(board[i][j]) + " ",end="")    
      print("\n")
        
def find_empty(board):
  """
  Finds the empty position on the board if present
  otherwise return None
  """
  for i in range(0,len(board)):
      for j in range(0,len(board[0])):
          if board[i][j] == 0:
              return (i,j)
                      
  return None
                
def is_valid(board,number,position):
  """
  Checks if the number that is inserted
  in position is valid or not.
  
  * First checks the row.
  * Second checks the column.
  * Third checks the small grid of 3x3.
  """
  for i in range(0,len(board)):
      if board[position[0]][i] == number:
          return False
  for j in range(0,len(board[0])):
      if board[j][position[1]] == number:
          return False
  row = (position[0]//3) * 3
  column = (position[1]//3) * 3
  for i in range(row,row+3):
      for j in range(column,column+3):
          if board[i][j] == number:
              return False
  return True

def solve_sudoku(board):
  """
  Solves the sudoku using backtracking.
  
  * Finds the empty position, if not present we're done.
  * Insert number between 1 to 9 and check if it's valid or not.
  * If valid insert into the position.
  * Recurselively call the solver.
  """
  position = find_empty(board)
  if not position:
      return True
  else:
      position = position
  for i in range(0,10):
      if is_valid(board,i,position):
          board[position[0]][position[1]] = i
          if solve_sudoku(board):
              return True
          board[position[0]][position[1]] = 0
  return False
    
if __name__ == "__main__":
  display_board(board)
  solve_sudoku(board)
  print("The solved solution is:\n")
  display_board(board)
    
                