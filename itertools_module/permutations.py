#This function uses the permutations function from the itertools module to generate all possible permutations of the given digits.
# It then checks if each permutation forms a valid time (i.e., the hours are between 0 and 23, and the minutes are between 0 and 59). 
# The result is the count of unique valid times. The function assumes that the input digits are integers between 0 and 9.


from itertools import permutations

def is_valid_time(hours, minutes):
    return 0 <= hours < 23 and 0 <= minutes < 59

def solution(A, B, C, D):
    digits = [A, B, C, D]
    valid_times = set()
    
    for p in permutations(digits):
        hours = p[0] * 10 + p[1]
        minutes = p[2] * 10 + p[3]
        if is_valid_time(hours, minutes):
            valid_times.add((hours, minutes))
            
    return len(valid_times)

#Example usage:
A = 1
B = 2
C = 3
D = 4

result = solution(A, B, C, D)
print(result) # prints 24

#print("Number of valid times: ", result) # prints 24
# print(solution(A, B, C, D)) # prints 24
    
    
  ##  max_time = -1
   # for p in permutations(digits):
       # hours = p[0] * 10 + p[1]
       # minutes = p[2] * 10 + p[3]
      #  if is_valid_time(hours, minutes):
       #     max_time = max(max_time, hours * 60 + minutes)
  #  if max_time == -1:
      #  return "NOT POSSIBLE"
   # else:
     #   return f"{max_time // 60:02d}:{max_time % 60:02d}"