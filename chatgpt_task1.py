"""
✅ Task 1: String Compression
Difficulty: Junior
Category: String manipulation, logic

Problem:
Write a function compress_string(s: str) -> str that compresses a string by replacing sequences 
of the same character with that character followed by the count of repetitions.
If the compressed string is not shorter than the original, return the original string.

Example:

compress_string("aabcccccaaa")  # "a2b1c5a3"
compress_string("abc")         # "abc"
"""

def compress_string(s: str) -> str:
    final_string = []
    current_symbol = s[0]
    current_symbol_num = 1
    
    for i in s[1:]:
        if i == current_symbol:
            current_symbol_num += 1
        else:
            final_string.append(f"{current_symbol}{current_symbol_num}")
            current_symbol = i
            current_symbol_num = 1
    final_string.append(current_symbol)
    
    finished_str = ''.join(final_string)
    return finished_str if len(finished_str) < len(s) else s
        
print(compress_string('aabcccccaaa'))