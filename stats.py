def get_word_count(text):
  count = len(text.split(sep=None))
  return count

def count_each_character(text):
  char_dict = {}
  
  for char in text:
    if char in char_dict:
      char_dict[char] += 1
    else:
      char_dict[char] = 1
  
  return char_dict