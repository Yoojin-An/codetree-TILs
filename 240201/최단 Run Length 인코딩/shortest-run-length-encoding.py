def run_length_encode(s):
  encoded_string = ""
  i = 0
  while i < len(s):
    char = s[i]
    count = 1
    i += 1
    while i < len(s) and s[i] == char:
      count += 1
      i += 1
    encoded_string += char + str(count)
  return encoded_string

string = input()
encoded_string_lengths = []
for i in range(len(string)):
  string = string[-1]+string[:-1]
  length = len(run_length_encode(string))
  encoded_string_lengths.append(length)
  
print(min(encoded_string_lengths))