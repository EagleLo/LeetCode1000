# LeetCode 3484. Design Spreadsheet
# Difficulty: Medium
# Topic: Object-Oriented Programming, String Parsing, 2D Array

"""
Problem Description:
------------------
A spreadsheet is a grid with 26 columns (labeled from 'A' to 'Z') and a given number of rows. 
Each cell in the spreadsheet can hold an integer value between 0 and 10^5.

Implement the Spreadsheet class:
- Spreadsheet(int rows): Initializes a spreadsheet with 26 columns (labeled 'A' to 'Z') and 
  the specified number of rows. All cells are initially set to 0.
- void setCell(String cell, int value): Sets the value of the specified cell. The cell 
  reference is provided in the format "AX" (e.g., "A1", "B10"), where the letter represents 
  the column (from 'A' to 'Z') and the number represents a 1-indexed row.
- void resetCell(String cell): Resets the specified cell to 0.
- int getValue(String formula): Evaluates a formula of the form "=X+Y", where X and Y are 
  either cell references or non-negative integers, and returns the computed sum.

Note: If getValue references a cell that has not been explicitly set using setCell, 
its value is considered 0.

Example 1:
Input:
["Spreadsheet", "getValue", "setCell", "getValue", "setCell", "getValue", "resetCell", "getValue"]
[[3], ["=5+7"], ["A1", 10], ["=A1+6"], ["B2", 15], ["=A1+B2"], ["A1"], ["=A1+B2"]]

Output: [null, 12, null, 16, null, 25, null, 15]

Explanation:
Spreadsheet spreadsheet = new Spreadsheet(3); // Initializes a spreadsheet with 3 rows and 26 columns
spreadsheet.getValue("=5+7"); // returns 12 (5+7)
spreadsheet.setCell("A1", 10); // sets A1 to 10
spreadsheet.getValue("=A1+6"); // returns 16 (10+6)
spreadsheet.setCell("B2", 15); // sets B2 to 15
spreadsheet.getValue("=A1+B2"); // returns 25 (10+15)
spreadsheet.resetCell("A1"); // resets A1 to 0
spreadsheet.getValue("=A1+B2"); // returns 15 (0+15)

Constraints:
* 1 <= rows <= 10^3
* 0 <= value <= 10^5
* The formula is always in the format "=X+Y", where X and Y are either valid cell references 
  or non-negative integers with values less than or equal to 10^5.
* Each cell reference consists of a capital letter from 'A' to 'Z' followed by a row number 
  between 1 and rows.
* At most 10^4 calls will be made in total to setCell, resetCell, and getValue.
"""

class Spreadsheet(object):
    def __init__(self, rows):
        """
        Initialize a spreadsheet with 26 columns and specified number of rows.
        
        Args:
            rows (int): Number of rows in the spreadsheet
        """
        # Don't do this: self.spst = [[0] * 26] * rows
        # This creates shallow copies - all rows point to the same list!
        # Right way to init a 2D Array: [[0] * columns for _ in range(rows)]
        self.spst = [[0] * 26 for _ in range(rows)]
    
    def parseCell(self, cell):
        """
        Parse cell reference string to get row and column indices.
        
        Args:
            cell (str): Cell reference in format "AX" (e.g., "A1", "B10")
            
        Returns:
            tuple: (row, col) - 0-indexed row and column indices
        """
        col = ord(cell[0]) - ord('A')  # Convert 'A'->0, 'B'->1, etc.
        row = int(cell[1:]) - 1        # Convert 1-indexed row to 0-indexed
        return row, col

    def setCell(self, cell, value):
        """
        Set the value of the specified cell.
        
        Args:
            cell (str): Cell reference in format "AX"
            value (int): Value to set in the cell
        """
        row, col = self.parseCell(cell)
        self.spst[row][col] = value

    def resetCell(self, cell):
        """
        Reset the specified cell to 0.
        
        Args:
            cell (str): Cell reference in format "AX"
        """
        row, col = self.parseCell(cell)
        self.spst[row][col] = 0
    
    def getCellValue(self, num):
        """
        Get the value of a cell reference or return the integer value.
        
        Args:
            num (str): Either a cell reference (e.g., "A1") or a number string (e.g., "5")
            
        Returns:
            int: The value of the cell or the parsed integer
        """
        if num[0].isalpha():
            # It's a cell reference
            row, col = self.parseCell(num)
            num = self.spst[row][col]
        return int(num)

    def getValue(self, formula):
        """
        Evaluate a formula of the form "=X+Y" and return the sum.
        
        Args:
            formula (str): Formula in format "=X+Y" where X and Y are cell references or numbers
            
        Returns:
            int: The computed sum
        """
        result = 0
        # Remove the '=' and split by '+'
        for num in formula[1:].split('+'):
            result += self.getCellValue(num)
        return result

def test():
    """
    Test function to verify solution with various test cases
    """
    # Test case 1: Example from problem
    spreadsheet = Spreadsheet(3)
    
    # Test getValue with numbers
    result1 = spreadsheet.getValue("=5+7")
    assert result1 == 12, f"Test case 1 failed: expected 12, got {result1}"
    
    # Test setCell
    spreadsheet.setCell("A1", 10)
    result2 = spreadsheet.getValue("=A1+6")
    assert result2 == 16, f"Test case 2 failed: expected 16, got {result2}"
    
    # Test setCell and getValue with cell references
    spreadsheet.setCell("B2", 15)
    result3 = spreadsheet.getValue("=A1+B2")
    assert result3 == 25, f"Test case 3 failed: expected 25, got {result3}"
    
    # Test resetCell
    spreadsheet.resetCell("A1")
    result4 = spreadsheet.getValue("=A1+B2")
    assert result4 == 15, f"Test case 4 failed: expected 15, got {result4}"
    
    # Test case 5: Multiple operations
    spreadsheet.setCell("C3", 100)
    result5 = spreadsheet.getValue("=C3+50")
    assert result5 == 150, f"Test case 5 failed: expected 150, got {result5}"
    
    # Test case 6: Unset cell (should be 0)
    result6 = spreadsheet.getValue("=A1+Z1")
    assert result6 == 0, f"Test case 6 failed: expected 0, got {result6}"
    
    print("All test cases passed!")

if __name__ == "__main__":
    test()

"""
What I Learned from This Problem:
================================

1. 2D ARRAY INITIALIZATION:
   - Wrong: [[0] * 26] * rows (creates shallow copies)
   - Right: [[0] * 26 for _ in range(rows)] (creates independent rows)
   - This is a common Python gotcha!

2. STRING PARSING:
   - Parse cell references by extracting column and row
   - Use ord() to convert letters to numbers
   - Handle 1-indexed to 0-indexed conversion

3. CELL REFERENCE FORMAT:
   - Format: "AX" where A is column (A-Z) and X is row (1-indexed)
   - Column: ord(cell[0]) - ord('A') converts A->0, B->1, etc.
   - Row: int(cell[1:]) - 1 converts 1-indexed to 0-indexed

4. FORMULA PARSING:
   - Remove '=' prefix and split by '+'
   - Handle both cell references and direct numbers
   - Use isalpha() to distinguish between cell refs and numbers

5. OBJECT-ORIENTED DESIGN:
   - Separate concerns: parsing, setting, getting, evaluating
   - Helper methods for common operations
   - Clear method responsibilities

6. EDGE CASE HANDLING:
   - Unset cells default to 0
   - Formula always has format "=X+Y"
   - Cell references are always valid

7. DATA STRUCTURE CHOICES:
   - 2D array for spreadsheet grid
   - Simple and efficient for this problem size
   - O(1) access time for cell operations

8. IMPLEMENTATION DETAILS:
   - parseCell: converts "A1" -> (0, 0)
   - getCellValue: handles both cell refs and numbers
   - getValue: splits formula and sums values

This problem taught me about 2D array initialization in Python and how to
design a simple spreadsheet-like data structure with formula evaluation!
"""

"""
Solution Analysis:
----------------
1. Approach:
   - Use 2D array to represent spreadsheet grid
   - Parse cell references to get row/column indices
   - Evaluate formulas by splitting and summing values

2. Data Structure:
   - 2D array: self.spst[row][col] = value
   - 26 columns (A-Z), variable number of rows
   - All cells initialized to 0

3. Time Complexity:
   - setCell: O(1) - direct array access
   - resetCell: O(1) - direct array access
   - getValue: O(k) - where k is number of terms in formula
   - parseCell: O(1) - string parsing

4. Space Complexity: O(rows * 26)
   - 2D array stores all cell values
   - Linear in number of rows

5. Key Methods:
   - parseCell: converts "A1" to (0, 0)
   - getCellValue: gets value from cell ref or number
   - getValue: evaluates "=X+Y" formulas

6. Edge Cases:
   - Unset cells default to 0
   - Formula always has format "=X+Y"
   - Cell references are always valid

7. Implementation Notes:
   - Use list comprehension for 2D array initialization
   - Handle 1-indexed to 0-indexed conversion
   - Split formula by '+' to get terms

8. Why This Works:
   - Simple 2D array representation
   - Direct cell access for O(1) operations
   - String parsing for cell references
   - Formula evaluation by splitting and summing
"""
