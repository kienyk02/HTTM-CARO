import sys
import numpy as np
import copy

ROWS = 20
COLS = 20
class Board:
    def __init__(self):
        self.squares = np.zeros( (ROWS, COLS) ,dtype=int)
        self.marked_sqrs = 0
        
    def final_state(self):
        directions = [(0, 1), (1, 0), (1, 1), (-1, 1)]
        for row in range(ROWS):
            for col in range(COLS):
                if self.squares[row][col] != 0:
                    current_player = self.squares[row][ col]
                    for dr, dc in directions:
                        count = 1
                        for i in range(1, 5):
                            r, c = row + i * dr, col + i * dc
                            if 0 <= r < ROWS and 0 <= c < COLS and self.squares[r][c] == current_player:
                                count += 1
                            else:
                                break
                        for i in range(1, 5):
                            r, c = row - i * dr, col - i * dc
                            if 0 <= r < ROWS and 0 <= c < COLS and self.squares[r][c] == current_player:
                                count += 1
                            else:
                                break
                        if count >= 5:
                            return current_player
        return 0
    
    def mark_sqr(self, row, col, player):
        self.squares[row][col] = player
        self.marked_sqrs += 1
    def empty_sqr(self, row, col):
        return self.squares[row][col] == 0
    def get_empty_sqrs(self):
        empty_sqrs = []
        for row in range(ROWS):
            for col in range(COLS):
                if self.empty_sqr(row, col):
                    empty_sqrs.append( (row, col) )
        return empty_sqrs
    def isfull(self):
        return self.marked_sqrs == ROWS*COLS

def heuristic(board):
        # Tham số đánh giá
        WEIGHTS = {
            "winning": 2000,
            "double_open": 250,
            "single_open": 100,
        }
        score = 0
        player1 = 1
        player2 = 2
        for row in range(ROWS):
            for col in range(COLS):
                if board.squares[row][col] == player1:
                    score += evaluate_position(row, col, player1, board, WEIGHTS)
                elif board.squares[row][col] == player2:
                    score -= evaluate_position(row, col, player2, board, WEIGHTS)
        return score

def evaluate_position( row, col, player, board, weights):
    score = 0
    directions = [(0, 1), (1, 0), (1, 1), (-1, 1), (0,-1), (-1,0), (-1,-1), (1,-1)]
    for dr, dc in directions:
        count = 0  # Số lượng quân cờ liên tiếp
        empty = 0  # Số lượng ô trống sau quân cờ
        blocked = False  # Bị chặn bởi quân cờ đối thủ
        for i in range(1, 5):
            r, c = row + i * dr, col + i * dc
            if 0 <= r < ROWS and 0 <= c < COLS:
                if board.squares[r][c] == player:
                    count += 1
                elif board.squares[r][c] == 0:
                    empty += 1
                else:
                    if board.squares[r][c]==2 and empty==0: # nếu AI chặn người
                        if count==0:   # chặn 1 ô 1 liên tiêp
                            score-=50
                        elif count==1: # chặn 2 ô 1 liên tiêp
                            score-=100
                        elif count==2: # chặn 3 ô 1 liên tiêp
                            score-=600
                        elif count==3: # chặn 4 ô 1 liên tiêp
                            score-=900
                    
                    blocked = True
                    break
            else:
                blocked = True
                break
        if not blocked:
            if count == 1 and empty == 3:
                score += weights["single_open"]
            elif count == 2 and empty == 2:
                score += (weights["double_open"])
            elif count == 3 and empty == 1:
                score += (weights["winning"]/2-200)
            elif count == 4:
                score += weights["winning"]
                
    return score
    
def ClimbingHill(board):    
        best_move = None
        score= float('inf')
        empty_sqrs = board.get_empty_sqrs() 
        for (row, col) in empty_sqrs:
                temp_board = copy.deepcopy(board)
                temp_board.mark_sqr(row, col, 2)
                tmp = heuristic(temp_board)
                if tmp < score:
                    score = tmp
                    best_move = (row, col)
        return score,best_move    

# Đọc dữ liệu đầu vào từ stdin
boardSquares = sys.stdin.read()
# chuyển đổi thành mảng
boardSquares = eval(boardSquares)
# chuyển thành mảng numpy
boardSquares=np.array(boardSquares)
board = Board()
board.squares=boardSquares
board.marked_sqrs=np.count_nonzero(board.squares)
# Tìm kiếm nước đi dựa trên trạng thái bàn cờ
eval, move = ClimbingHill(board)
# In kết quả ra stdout
print(move)