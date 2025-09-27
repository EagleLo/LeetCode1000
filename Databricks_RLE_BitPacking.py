# Databricks Run-Length Encoding (RLE) and Bit-Packing (BP)
# Difficulty: Medium-Hard
# Topic: Data Compression, Bit Manipulation, Encoding/Decoding

"""
Problem Description:
------------------
Implement a hybrid compression scheme that combines Run-Length Encoding (RLE) and Bit-Packing (BP).

### Run-Length Encoding (RLE)
Encoding scheme where integers that have the same value can be represented as a single value 
with a count, e.g. `1, 1, 1, 1, 1` can be written as `1 (5)`.

### Bit-Packing (BP)
Encoding scheme where smaller integer values can be represented without using the full 4 bytes 
of data. For example, all numbers in `2, 3, 4, 5` fit within 3 bits, so we can encode ("pack") 
them into 12 bits or at most 2 bytes, thus reducing data 8x.

### Run
A sequence of values that are encoded using RLE or BP. All values in a run have the same 
encoding but runs themselves can interleave, e.g. `[RLE, BP, RLE, RLE, BP, ...]`.

Rules:
1. All values have to be placed into runs, and value order cannot change.
2. A Run-Length encoded run has at least 8 values (only the last run can have fewer values).
3. Once started, a Run-Length encoded run should extend as far as possible.
4. A Bit-Packing encoded run has exactly 8 values (only the last run can have fewer values).
5. Run-Length encoding is our default scheme. We only use Bit-Packing when we cannot apply RLE.

Examples:
- `[1, 1, 1]` will be encoded as `RLE[1, 3]`.
- `[1, 1, 1, 1, 2, 3, 4, 5]` will be encoded as `BP[1, 1, 1, 1, 2, 3, 4, 5]`.
- `[1, 1, 1, 1, 1, 1, 1, 1, 2, 3, 4, 5]` will be encoded as `RLE[1, 8], BP[2, 3, 4, 5]`.
- `[1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 3, 4, 5]` will be encoded as `RLE[1, 9], BP[2, 3, 4, 5]`.
"""

from typing import List
from math import ceil, log2

# --------------------------- Bit I/O ---------------------------------

class BitWriter:
    """
    Helper class for writing bits to a byte stream.
    Handles bit-level operations and byte alignment.
    """
    
    def __init__(self):
        pass

    def write_bits(self, value: int, nbits: int) -> None:
        """
        Write the lower nbits of value, LSB-first into the stream.
        
        Args:
            value: The value to write
            nbits: Number of bits to write (0-32)
        """
        pass

    def write_u8(self, x: int) -> None:
        """Write an 8-bit unsigned integer."""
        pass

    def write_u32le(self, x: int) -> None:
        """Write a 32-bit unsigned integer in little-endian format."""
        # little-endian 4 bytes
        pass

    def finish(self) -> bytes:
        """Finalize the bit stream and return the complete byte array."""
        pass


class BitReader:
    """
    Helper class for reading bits from a byte stream.
    Handles bit-level operations and byte alignment.
    """
    
    def __init__(self, data: bytes):
        pass

    def read_bits(self, nbits: int) -> int:
        """
        Read nbits (LSB-first) and return value as int.
        
        Args:
            nbits: Number of bits to read
            
        Returns:
            The read value
            
        Raises:
            ValueError: If end of stream is reached unexpectedly
        """
        pass

    def read_u8(self) -> int:
        """Read an 8-bit unsigned integer."""
        pass

    def read_u32le(self) -> int:
        """Read a 32-bit unsigned integer in little-endian format."""
        pass

# --------------------------- Encoder ---------------------------------

# Run tags
TAG_RLE = 0  # [tag=0][value:u32][count:u32]
TAG_BP  = 1  # [tag=1][L:u8][w:u8][payload bits = L*w, LSB-first per value]

def _bit_width(max_val: int) -> int:
    """
    Calculate the minimum number of bits needed to represent max_val.
    
    Args:
        max_val: The maximum value to represent
        
    Returns:
        Number of bits needed (minimum 1, maximum 32)
    """
    pass

def encode(values: List[int]) -> bytes:
    """
    Encode a list of integers using RLE and Bit-Packing compression.
    
    Algorithm:
    1. Scan the input for runs of equal values
    2. If a run has >= 8 equal values, use RLE (extend maximally)
    3. Otherwise, use Bit-Packing for exactly 8 values (or remaining if < 8)
    4. Repeat until all values are processed
    
    Args:
        values: List of non-negative integers (0 <= x < 2^32)
        
    Returns:
        Compressed byte array
        
    Raises:
        ValueError: If values are negative or exceed 32-bit range
    """
    pass

# --------------------------- Decoder ---------------------------------

def decode(data: bytes) -> List[int]:
    """
    Decode a compressed byte array back to the original list of integers.
    
    Algorithm:
    1. Read run tags from the stream
    2. For RLE runs: read value and count, repeat value count times
    3. For BP runs: read length and bit width, unpack values
    4. Continue until stream ends
    
    Args:
        data: Compressed byte array
        
    Returns:
        Original list of integers
        
    Raises:
        ValueError: If data format is invalid or stream ends unexpectedly
    """
    pass

# --------------------------- Test Cases ---------------------------------

def test_case_1():
    """
    Test Case 1: Basic RLE encoding
    """
    print("Running Test Case 1: Basic RLE encoding")
    
    values = [1, 1, 1]
    encoded = encode(values)
    decoded = decode(encoded)
    
    print(f"Original: {values}")
    print(f"Encoded: {list(encoded)}")
    print(f"Decoded: {decoded}")
    
    assert decoded == values, f"Expected {values}, got {decoded}"
    print("✓ Test Case 1 passed")

def test_case_2():
    """
    Test Case 2: Bit-Packing encoding
    """
    print("Running Test Case 2: Bit-Packing encoding")
    
    values = [1, 1, 1, 1, 2, 3, 4, 5]
    encoded = encode(values)
    decoded = decode(encoded)
    
    print(f"Original: {values}")
    print(f"Encoded: {list(encoded)}")
    print(f"Decoded: {decoded}")
    
    assert decoded == values, f"Expected {values}, got {decoded}"
    print("✓ Test Case 2 passed")

def test_case_3():
    """
    Test Case 3: Mixed RLE and BP encoding
    """
    print("Running Test Case 3: Mixed RLE and BP encoding")
    
    values = [1, 1, 1, 1, 1, 1, 1, 1, 2, 3, 4, 5]
    encoded = encode(values)
    decoded = decode(encoded)
    
    print(f"Original: {values}")
    print(f"Encoded: {list(encoded)}")
    print(f"Decoded: {decoded}")
    
    assert decoded == values, f"Expected {values}, got {decoded}"
    print("✓ Test Case 3 passed")

def test_case_4():
    """
    Test Case 4: Extended RLE run
    """
    print("Running Test Case 4: Extended RLE run")
    
    values = [1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 3, 4, 5]
    encoded = encode(values)
    decoded = decode(encoded)
    
    print(f"Original: {values}")
    print(f"Encoded: {list(encoded)}")
    print(f"Decoded: {decoded}")
    
    assert decoded == values, f"Expected {values}, got {decoded}"
    print("✓ Test Case 4 passed")

def test_case_5():
    """
    Test Case 5: Complex mixed case
    """
    print("Running Test Case 5: Complex mixed case")
    
    values = [0] * 20 + list(range(8)) + [7] * 16 + [0, 0, 0, 0, 0, 0, 0]
    encoded = encode(values)
    decoded = decode(encoded)
    
    print(f"Original length: {len(values)}")
    print(f"Encoded length: {len(encoded)}")
    print(f"Compression ratio: {len(encoded) / (len(values) * 4):.2f}")
    print(f"Decoded matches: {decoded == values}")
    
    assert decoded == values, f"Decoded values don't match original"
    print("✓ Test Case 5 passed")

def test_case_6():
    """
    Test Case 6: Edge cases
    """
    print("Running Test Case 6: Edge cases")
    
    # Empty list
    values = []
    encoded = encode(values)
    decoded = decode(encoded)
    assert decoded == values, f"Empty list failed: {decoded}"
    
    # Single value
    values = [42]
    encoded = encode(values)
    decoded = decode(encoded)
    assert decoded == values, f"Single value failed: {decoded}"
    
    # All zeros
    values = [0] * 10
    encoded = encode(values)
    decoded = decode(encoded)
    assert decoded == values, f"All zeros failed: {decoded}"
    
    # Large values
    values = [2**31 - 1] * 5
    encoded = encode(values)
    decoded = decode(encoded)
    assert decoded == values, f"Large values failed: {decoded}"
    
    print("✓ Test Case 6 passed")

def run_all_tests():
    """
    Run all test cases and print success message if all pass.
    """
    print("=" * 60)
    print("Running Databricks RLE + Bit-Packing Test Suite")
    print("=" * 60)
    
    try:
        test_case_1()
        test_case_2()
        test_case_3()
        test_case_4()
        test_case_5()
        test_case_6()
        
        print("=" * 60)
        print("🎉 ALL TESTS PASSED! SUCCESS! 🎉")
        print("=" * 60)
        
    except AssertionError as e:
        print(f"❌ Test failed: {e}")
        import traceback
        traceback.print_exc()
        return False
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        import traceback
        traceback.print_exc()
        return False
    
    return True

if __name__ == "__main__":
    run_all_tests()

"""
Implementation Notes:
====================

1. **RLE Encoding**:
   - Used when >= 8 consecutive equal values
   - Format: [tag=0][value:u32][count:u32]
   - Extends maximally to capture all equal values

2. **Bit-Packing Encoding**:
   - Used when < 8 consecutive equal values
   - Format: [tag=1][length:u8][bit_width:u8][packed_values]
   - Exactly 8 values (or remaining if < 8)
   - Bit width calculated from maximum value in block

3. **Bit I/O**:
   - LSB-first bit ordering
   - Handles byte alignment automatically
   - Supports 0-32 bit values

4. **Compression Strategy**:
   - Prefer RLE for long runs (>= 8)
   - Use BP for short runs (< 8)
   - Maintain original order of values

5. **Time Complexity**: O(n) where n is number of values
6. **Space Complexity**: O(n) for output (compressed size varies)

Key Insights:
- RLE is most efficient for long runs of equal values
- BP is most efficient for short runs with small values
- Hybrid approach optimizes for different data patterns
- Bit-level operations enable fine-grained control over compression
"""
