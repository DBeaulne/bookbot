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



def character_sort(character_dict):
  def sort_on(items):
    return items["num"]
  
  list_of_characters = []

  for key, value in character_dict.items():
    new_dict = {'char': key, 'num': value}
    list_of_characters.append(new_dict)

  # print(f"Unsorted List: ", list_of_characters)
  list_of_characters.sort(reverse=True, key=sort_on)

  return list_of_characters



