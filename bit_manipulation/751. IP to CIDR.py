# LeetCode 751. IP to CIDR
# Difficulty: Medium
# Topic: Bit Manipulation, String, Greedy

"""
Problem Description:
------------------
An IP address is a formatted 32-bit unsigned integer where each group of 8 bits is 
printed as a decimal number and the dot character '.' splits the groups.

For example, the binary number 00001111 10001000 11111111 01101011 (spaces added for clarity) 
formatted as an IP address would be "15.136.255.107".

A CIDR block is a format used to denote a specific set of IP addresses. It is a string 
consisting of a base IP address, followed by a slash, followed by a prefix length k. 
The addresses it covers are all the IPs whose first k bits are the same as the base IP address.

For example, "123.45.67.89/20" is a CIDR block with a prefix length of 20. Any IP address 
whose binary representation matches 01111011 00101101 0100xxxx xxxxxxxx, where x can be 
either 0 or 1, is in the set covered by the CIDR block.

You are given a start IP address ip and the number of IP addresses we need to cover n. 
Your goal is to use as few CIDR blocks as possible to cover all the IP addresses in the 
inclusive range [ip, ip + n - 1] exactly. No other IP addresses outside of the range 
should be covered.

Return the shortest list of CIDR blocks that covers the range of IP addresses. If there 
are multiple answers, return any of them.

Example 1:
Input: ip = "255.0.0.7", n = 10
Output: ["255.0.0.7/32","255.0.0.8/29","255.0.0.16/32"]
Explanation:
The IP addresses that need to be covered are:
- 255.0.0.7  -> 11111111 00000000 00000000 00000111
- 255.0.0.8  -> 11111111 00000000 00000000 00001000
- 255.0.0.9  -> 11111111 00000000 00000000 00001001
- 255.0.0.10 -> 11111111 00000000 00000000 00001010
- 255.0.0.11 -> 11111111 00000000 00000000 00001011
- 255.0.0.12 -> 11111111 00000000 00000000 00001100
- 255.0.0.13 -> 11111111 00000000 00000000 00001101
- 255.0.0.14 -> 11111111 00000000 00000000 00001110
- 255.0.0.15 -> 11111111 00000000 00000000 00001111
- 255.0.0.16 -> 11111111 00000000 00000000 00010000

The CIDR block "255.0.0.7/32" covers the first address.
The CIDR block "255.0.0.8/29" covers the middle 8 addresses (binary format of 11111111 00000000 00000000 00001xxx).
The CIDR block "255.0.0.16/32" covers the last address.

Example 2:
Input: ip = "117.145.102.62", n = 8
Output: ["117.145.102.62/31","117.145.102.64/30","117.145.102.68/31"]

Constraints:
* 7 <= ip.length <= 15
* ip is a valid IPv4 on the form "a.b.c.d" where a, b, c, and d are integers in the range [0, 255].
* 1 <= n <= 1000
* Every implied address ip + x (for x < n) will be a valid IPv4 address.
"""

class Solution(object):
    def ip_to_int(self, ip):
        """
        Convert IP address string to 32-bit integer.
        
        Args:
            ip (str): IP address in format "a.b.c.d"
            
        Returns:
            int: 32-bit integer representation
        """
        ans = 0
        for x in ip.split('.'):
            ans = 256 * ans + int(x)
        return ans

    def int_to_ip(self, x):
        """
        Convert 32-bit integer to IP address string.
        
        Args:
            x (int): 32-bit integer
            
        Returns:
            str: IP address in format "a.b.c.d"
        """
        ip = []
        for i in [24, 16, 8, 0]:  # Extract bytes from left to right
            ip.append(str((x >> i) & 0xFF))
        return '.'.join(ip)
        
    def ipToCIDR(self, ip, n):
        """
        Convert IP range to minimum number of CIDR blocks.
        
        Approach: Greedy algorithm
        - Start from the given IP address
        - At each step, find the largest possible CIDR block that starts at current IP
        - The size of the block is limited by the number of remaining IPs and alignment
        
        Args:
            ip (str): Starting IP address
            n (int): Number of IP addresses to cover
            
        Returns:
            List[str]: List of CIDR blocks
        """
        start = self.ip_to_int(ip)
        result = []
        
        while n > 0:
            # Find the largest possible CIDR block starting at current IP
            # The block size is limited by:
            # 1. The number of remaining IPs (n)
            # 2. The alignment of the current IP (lowest set bit)
            
            # Get the lowest set bit of start IP
            lowest_bit = start & -start
            
            # Calculate how many IPs we can cover with this block
            # Block size = 2^(32 - mask_length)
            # We want the largest block that doesn't exceed remaining IPs
            max_block_size = min(lowest_bit, n)
            
            # Find the largest power of 2 that doesn't exceed max_block_size
            block_size = 1
            while block_size * 2 <= max_block_size:
                block_size *= 2
            
            # Calculate mask length
            mask_length = 32 - block_size.bit_length() + 1
            
            # Add CIDR block to result
            result.append(self.int_to_ip(start) + '/' + str(mask_length))
            
            # Update start IP and remaining count
            start += block_size
            n -= block_size
        
        return result

def test():
    """
    Test function to verify solution with various test cases
    """
    solution = Solution()
    
    # Test case 1: Example from problem
    ip1 = "255.0.0.7"
    n1 = 10
    result1 = solution.ipToCIDR(ip1, n1)
    expected1 = ["255.0.0.7/32","255.0.0.8/29","255.0.0.16/32"]
    print(f"Test 1: {result1}")
    assert len(result1) <= len(expected1), f"Test case 1 failed: too many CIDR blocks"
    
    # Test case 2: Example from problem
    ip2 = "117.145.102.62"
    n2 = 8
    result2 = solution.ipToCIDR(ip2, n2)
    expected2 = ["117.145.102.62/31","117.145.102.64/30","117.145.102.68/31"]
    print(f"Test 2: {result2}")
    assert len(result2) <= len(expected2), f"Test case 2 failed: too many CIDR blocks"
    
    # Test case 3: Single IP
    ip3 = "192.168.1.1"
    n3 = 1
    result3 = solution.ipToCIDR(ip3, n3)
    expected3 = ["192.168.1.1/32"]
    print(f"Test 3: {result3}")
    assert result3 == expected3, f"Test case 3 failed: expected {expected3}, got {result3}"
    
    # Test case 4: Power of 2 range
    ip4 = "10.0.0.0"
    n4 = 8
    result4 = solution.ipToCIDR(ip4, n4)
    print(f"Test 4: {result4}")
    assert len(result4) == 1, f"Test case 4 failed: expected 1 CIDR block, got {len(result4)}"
    
    print("All test cases passed!")

if __name__ == "__main__":
    test()

"""
What I Learned from This Problem:
================================

1. IP ADDRESS REPRESENTATION:
   - IP addresses are 32-bit integers
   - Each octet represents 8 bits
   - Conversion: ip = a*256³ + b*256² + c*256¹ + d*256⁰

2. CIDR BLOCK CONCEPTS:
   - CIDR block covers 2^(32-mask_length) IP addresses
   - Mask length determines how many bits are fixed
   - Larger blocks cover more IPs but must be aligned

3. BIT MANIPULATION TECHNIQUES:
   - x & -x gives the lowest set bit
   - This helps find alignment boundaries
   - Powers of 2 are important for block sizes

4. GREEDY ALGORITHM:
   - Always choose the largest possible block at each step
   - This minimizes the total number of CIDR blocks
   - Greedy choice is optimal for this problem

5. ALIGNMENT CONSTRAINTS:
   - CIDR blocks must start at aligned addresses
   - Block size must be a power of 2
   - Alignment is determined by the lowest set bit

6. BLOCK SIZE CALCULATION:
   - Find largest power of 2 ≤ min(remaining_IPs, alignment)
   - This ensures we don't exceed the range
   - This ensures we use the largest possible block

7. EDGE CASES:
   - Single IP address (mask length 32)
   - Power of 2 ranges (single CIDR block)
   - Non-aligned ranges (multiple blocks)

8. OPTIMIZATION GOAL:
   - Minimize number of CIDR blocks
   - Cover exactly the required range
   - No extra IP addresses

This problem taught me about IP addressing, CIDR notation, and how to use
bit manipulation for efficient range covering!
"""

"""
Solution Analysis:
----------------
1. Approach:
   - Convert IP addresses to integers for easier manipulation
   - Use greedy algorithm to find largest possible CIDR blocks
   - Consider both alignment and remaining IP count

2. Algorithm:
   - Start from given IP address
   - Find largest power of 2 that fits in remaining range
   - Create CIDR block and update position
   - Repeat until all IPs are covered

3. Time Complexity: O(log n)
   - Each iteration reduces remaining IPs by at least half
   - Maximum log n iterations

4. Space Complexity: O(log n)
   - Store at most log n CIDR blocks
   - Each block covers at least 2 IPs

5. Key Insights:
   - CIDR blocks must be powers of 2
   - Alignment is determined by lowest set bit
   - Greedy approach is optimal

6. Bit Manipulation:
   - x & -x gives lowest set bit
   - Powers of 2 have exactly one set bit
   - Block size = 2^(32 - mask_length)

7. Edge Cases:
   - Single IP: mask length 32
   - Power of 2 range: single block
   - Non-aligned range: multiple blocks

8. Why Greedy Works:
   - Each CIDR block covers a contiguous range
   - Larger blocks are more efficient
   - No overlap between blocks
   - Optimal substructure property
"""
