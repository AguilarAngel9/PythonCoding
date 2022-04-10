# Reverse to Make Equal

# Instructions:
# Given two arrays A and B of length N, 
# determine if there is a way to make A equal to B 
# by reversing any subarrays from array B any number of times.

def are_they_equal(array_a, array_b):
  # We only want to now if there is posible to make them equal,
  # so we have to review if both list have the same values.
  return all([a in array_b for a in array_a])


a_1 = [1, 2, 3, 4]
b_1 = [1, 4, 3, 2]
output_1 = are_they_equal(a_1, b_1)

# Contiguous Subarrays

# Instructions:
# You are given an array arr of N integers. 
# For each index i, you are required to determine the number of contiguous subarrays that fulfill the following conditions:
# The value at index i must be the maximum element in the contiguous subarrays, and
# These contiguous subarrays must either start from or end on index i.

def count_subarrays(arr):
  # Write your code here
  output = [1] * len(arr)
  for i in range(len(arr)):
    value = arr[i] # Value to compare
    # Forward comparison
    for j in range(i + 1, len(arr)):
      if arr[j] < value:
        output[i] += 1
      elif arr[j] > value:
        break
    # Back comparison
    for g in range(i - 1, -1, -1):
      if arr[g] < value:
        output[i] += 1
      elif arr[g] > value:
        break
  return output

test_1 = [3, 4, 1, 6, 2]
output_1 = count_subarrays(test_1)

# Rotational Cipher

# One simple way to encrypt a string is to "rotate" every alphanumeric character by a certain amount. 
# Rotating a character means replacing it with another character that is a certain number of steps away in normal alphabetic or numerical order.

# Instructions:
# For example, if the string "Zebra-493?" is rotated 3 places, the resulting string is "Cheud-726?". 
# Every alphabetic character is replaced with the character 3 letters higher (wrapping around from Z to A), 
# and every numeric character replaced with the character 3 digits higher (wrapping around from 9 to 0). 
# Note that the non-alphanumeric characters remain unchanged.

def rotationalCipher(input, rotation_factor):
  # Write your code here
  # Make a list of of the string
  password = [char for char in input]
  
  # ASCII number for each number + rotation_factor
  # password_rotated = [chr(ord(char) + rotation_factor) for char in password]
  
  for i in range(len(password)):
    # Identify the letter ones.
    if password[i].isalpha(): #[65, 90] -> 26 [97,122]
      if password[i].isupper():
        if (rotation_factor % 26 + ord(password[i])) <= 90:
          password[i] = chr(ord(password[i]) + rotation_factor % 26)
        else:
          password[i] = chr(64 + ((ord(password[i]) + rotation_factor % 26) - 90))
      else:
        if (rotation_factor % 26 + ord(password[i])) <= 122:
          password[i] = chr(ord(password[i]) + rotation_factor % 26)
        else:
          password[i] = chr(96 + ((ord(password[i]) + rotation_factor % 26) - 122))
    # Identify the numeric ones.
    elif password[i].isnumeric(): #[48, 57] -> 10
      # password[i] = chr(ord(password[i]) + (rotation_factor % 10))
      if (rotation_factor % 10 + ord(password[i])) <= 57:
        password[i] = chr(ord(password[i]) + rotation_factor % 10)
      else:
        password[i] = chr(47 + ((ord(password[i]) + rotation_factor % 10) - 57))
    # Symbols and stuff.
    else:
      password[i] = password[i]     
  
  return ''.join(password)
