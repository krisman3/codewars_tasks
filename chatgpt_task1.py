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
    current_symbol = ''
    current_symbol_num = 0
    for i in s:
        if i == current_symbol:
            current_symbol_num += 1
        else:
            final_string.append(current_symbol_num)
            current_symbol_num = 0
            current_symbol = i
            current_symbol_num += 1
            final_string.append(current_symbol)
    
    finished_str = ''.join(str(x) for x in final_string[1:len(final_string)])
    return finished_str
        
print(compress_string('aabcccccaaa'))