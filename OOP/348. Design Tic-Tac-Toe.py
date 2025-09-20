# LeetCode 348. Design Tic-Tac-Toe
# Difficulty: Medium
# Topic: Object-Oriented Programming, Design, Array

"""
Problem Description:
------------------
Assume the following rules are for the tic-tac-toe game on an n x n board between two players:

1. A move is guaranteed to be valid and is placed on an empty block.
2. Once a winning condition is reached, no more moves are allowed.
3. A player who succeeds in placing n of their marks in a horizontal, vertical, or diagonal row wins the game.

Implement the TicTacToe class:
- TicTacToe(int n): Initializes the object the size of the board n.
- int move(int row, int col, int player): Indicates that the player with id player plays at the cell (row, col) of the board. The move is guaranteed to be a valid move, and the two players alternate in making moves. Return:
  * 0 if there is no winner after the move,
  * 1 if player 1 is the winner after the move, or
  * 2 if player 2 is the winner after the move.

Example 1:
Input:
["TicTacToe", "move", "move", "move", "move", "move", "move", "move"]
[[3], [0, 0, 1], [0, 2, 2], [2, 2, 1], [1, 1, 2], [2, 0, 1], [1, 0, 2], [2, 1, 1]]

Output: [null, 0, 0, 0, 0, 0, 0, 1]

Explanation:
TicTacToe ticTacToe = new TicTacToe(3);
Assume that player 1 is "X" and player 2 is "O" in the board.

ticTacToe.move(0, 0, 1); // return 0 (no one wins)
|X| | |
| | | |    // Player 1 makes a move at (0, 0).
| | | |

ticTacToe.move(0, 2, 2); // return 0 (no one wins)
|X| |O|
| | | |    // Player 2 makes a move at (0, 2).
| | | |

ticTacToe.move(2, 2, 1); // return 0 (no one wins)
|X| |O|
| | | |    // Player 1 makes a move at (2, 2).
| | |X|

ticTacToe.move(1, 1, 2); // return 0 (no one wins)
|X| |O|
| |O| |    // Player 2 makes a move at (1, 1).
| | |X|

ticTacToe.move(2, 0, 1); // return 0 (no one wins)
|X| |O|
| |O| |    // Player 1 makes a move at (2, 0).
|X| |X|

ticTacToe.move(1, 0, 2); // return 0 (no one wins)
|X| |O|
|O|O| |    // Player 2 makes a move at (1, 0).
|X| |X|

ticTacToe.move(2, 1, 1); // return 1 (player 1 wins)
|X| |O|
|O|O| |    // Player 1 makes a move at (2, 1).
|X|X|X|

Constraints:
* 2 <= n <= 100
* player is 1 or 2.
* 0 <= row, col < n
* (row, col) are unique for each different call to move.
* At most n^2 calls will be made to move.

Follow-up: Could you do better than O(n^2) per move() operation?
"""

class TicTacToe(object):
    def __init__(self, n):
        """
        Initialize the tic-tac-toe game with an n x n board.
        
        Data Structure Choice:
        - Instead of storing the entire board, track counts for each row, column, and diagonal
        - This allows O(1) move() operation instead of O(n^2)
        
        Args:
            n (int): Size of the board (n x n)
        """
        self.mv_count = 0  # Track number of moves (not used in this solution)
        self.n = n
        
        # Track counts for each row (n rows)
        self.row = [0] * self.n
        
        # Track counts for each column (n columns)
        self.col = [0] * self.n
        
        # Track count for main diagonal (top-left to bottom-right)
        self.dia = 0
        
        # Track count for anti-diagonal (top-right to bottom-left)
        self.anti_dia = 0
        
    def move(self, row, col, player):
        """
        Make a move on the board and check for winner.
        
        Algorithm:
        1. Convert player to +1 or -1 for easy counting
        2. Update row, column, and diagonal counts
        3. Check if any count equals n (winning condition)
        
        Args:
            row (int): Row index (0 to n-1)
            col (int): Column index (0 to n-1)
            player (int): Player ID (1 or 2)
            
        Returns:
            int: 0 if no winner, 1 if player 1 wins, 2 if player 2 wins
        """
        # Convert player to +1 or -1 for easy counting
        cur_player = 1 if player == 1 else -1
        
        # Update row count
        self.row[row] += cur_player
        
        # Update column count
        self.col[col] += cur_player
        
        # Update main diagonal count (row == col)
        if row == col:
            self.dia += cur_player
            
        # Update anti-diagonal count (row + col == n - 1)
        if row + col == self.n - 1:
            self.anti_dia += cur_player

        # Check for winning condition
        # If any count equals n (for player 1) or -n (for player 2), that player wins
        win_cond = cur_player * self.n
        
        if (self.row[row] == win_cond or 
            self.col[col] == win_cond or 
            self.dia == win_cond or 
            self.anti_dia == win_cond):
            return player

        return 0

def test():
    """
    Test function to verify solution with various test cases
    """
    # Test case 1: Example from problem
    ticTacToe = TicTacToe(3)
    
    assert ticTacToe.move(0, 0, 1) == 0, "Test case 1 failed"
    assert ticTacToe.move(0, 2, 2) == 0, "Test case 2 failed"
    assert ticTacToe.move(2, 2, 1) == 0, "Test case 3 failed"
    assert ticTacToe.move(1, 1, 2) == 0, "Test case 4 failed"
    assert ticTacToe.move(2, 0, 1) == 0, "Test case 5 failed"
    assert ticTacToe.move(1, 0, 2) == 0, "Test case 6 failed"
    assert ticTacToe.move(2, 1, 1) == 1, "Test case 7 failed"
    
    # Test case 2: Player 2 wins
    ticTacToe2 = TicTacToe(3)
    assert ticTacToe2.move(0, 0, 1) == 0, "Test case 8 failed"
    assert ticTacToe2.move(1, 1, 2) == 0, "Test case 9 failed"
    assert ticTacToe2.move(0, 1, 1) == 0, "Test case 10 failed"
    assert ticTacToe2.move(1, 0, 2) == 0, "Test case 11 failed"
    assert ticTacToe2.move(0, 2, 1) == 0, "Test case 12 failed"
    assert ticTacToe2.move(1, 2, 2) == 2, "Test case 13 failed"
    
    # Test case 3: Diagonal win
    ticTacToe3 = TicTacToe(3)
    assert ticTacToe3.move(0, 0, 1) == 0, "Test case 14 failed"
    assert ticTacToe3.move(0, 1, 2) == 0, "Test case 15 failed"
    assert ticTacToe3.move(1, 1, 1) == 0, "Test case 16 failed"
    assert ticTacToe3.move(0, 2, 2) == 0, "Test case 17 failed"
    assert ticTacToe3.move(2, 2, 1) == 1, "Test case 18 failed"
    
    # Test case 4: Anti-diagonal win
    ticTacToe4 = TicTacToe(3)
    assert ticTacToe4.move(0, 2, 1) == 0, "Test case 19 failed"
    assert ticTacToe4.move(0, 0, 2) == 0, "Test case 20 failed"
    assert ticTacToe4.move(1, 1, 1) == 0, "Test case 21 failed"
    assert ticTacToe4.move(1, 0, 2) == 0, "Test case 22 failed"
    assert ticTacToe4.move(2, 0, 1) == 1, "Test case 23 failed"
    
    # Test case 5: No winner
    ticTacToe5 = TicTacToe(2)
    assert ticTacToe5.move(0, 0, 1) == 0, "Test case 24 failed"
    assert ticTacToe5.move(0, 1, 2) == 0, "Test case 25 failed"
    assert ticTacToe5.move(1, 0, 1) == 0, "Test case 26 failed"
    assert ticTacToe5.move(1, 1, 2) == 0, "Test case 27 failed"
    
    print("All test cases passed!")

if __name__ == "__main__":
    test()

"""
What I Learned from This Problem:
================================

1. OPTIMIZATION TECHNIQUE:
   - Instead of storing entire board, track counts for rows/columns/diagonals
   - This reduces space complexity from O(n^2) to O(n)
   - This reduces time complexity from O(n^2) to O(1) per move

2. COUNTING STRATEGY:
   - Use +1 for player 1 and -1 for player 2
   - When count equals n, player 1 wins
   - When count equals -n, player 2 wins
   - This allows checking all conditions with one comparison

3. DIAGONAL DETECTION:
   - Main diagonal: row == col
   - Anti-diagonal: row + col == n - 1
   - Only need to track two diagonal counts instead of checking all cells

4. WINNING CONDITION CHECK:
   - Check if any row, column, or diagonal count equals n or -n
   - Use absolute value to check both players at once
   - Return immediately when winner is found

5. SPACE EFFICIENCY:
   - O(n) space instead of O(n^2)
   - Only store what's necessary for win detection
   - Scales well for large boards

6. TIME EFFICIENCY:
   - O(1) per move instead of O(n^2)
   - No need to scan entire board
   - Constant time operations

7. EDGE CASE HANDLING:
   - Moves are guaranteed to be valid
   - Players alternate turns
   - No need to check for invalid moves

8. FOLLOW-UP ANSWER:
   - Yes, this solution is O(1) per move
   - Much better than O(n^2) naive approach
   - Optimal for this problem

This problem taught me about space-time tradeoffs and how to optimize
data structures for specific use cases!
"""

"""
Solution Analysis:
----------------
1. Approach:
   - Track counts for each row, column, and diagonal
   - Use +1/-1 encoding for easy win detection
   - Check winning condition after each move

2. Data Structure:
   - row[n]: count for each row
   - col[n]: count for each column
   - dia: count for main diagonal
   - anti_dia: count for anti-diagonal

3. Time Complexity:
   - move(): O(1) - constant time operations
   - Much better than O(n^2) naive approach

4. Space Complexity: O(n)
   - Store counts for n rows, n columns, 2 diagonals
   - Much better than O(n^2) board storage

5. Key Insights:
   - Don't need to store actual board state
   - Counts are sufficient for win detection
   - +1/-1 encoding simplifies win checking

6. Winning Conditions:
   - Row win: any row count equals n or -n
   - Column win: any column count equals n or -n
   - Diagonal win: main diagonal count equals n or -n
   - Anti-diagonal win: anti-diagonal count equals n or -n

7. Optimization Benefits:
   - Space: O(n) vs O(n^2)
   - Time: O(1) vs O(n^2)
   - Scalable for large boards

8. Why This Works:
   - Each move affects exactly one row, one column, and possibly one diagonal
   - Counts track the "strength" of each line
   - When count reaches n, that line is complete

9. Follow-up Answer:
   - Yes, this is O(1) per move
   - Optimal solution for this problem
   - No better time complexity possible

10. Edge Cases:
    - Moves are guaranteed valid
    - Players alternate turns
    - No need to handle invalid moves
    - Game ends when winner is found
"""
