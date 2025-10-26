from stats import get_word_count, count_each_character, character_sort

""" 
## This was my solution for Bookbot, Chapter 2, Lesson 3
def get_book_text(filepath):
  contents = filepath.read()
  return contents

def main():
  filepath = "books/frankenstein.txt"
  with open(filepath) as f:
    print(get_book_text(f))
"""

# Boot.dev solution

def get_book_text(path):
  with open(path) as f:
    return f.read()
   
def main():
  filepath = "books/frankenstein.txt"
  text = get_book_text(filepath)
  print("============= BOOKBOT =============")
  print(f"Analyzing book fount at", filepath,"...")

  word_count = get_word_count(text)
  print("------------ Word Count -----------")
  print(f"Found {word_count} total words")

  char_count = count_each_character(text.lower())

  sorted_list = character_sort(char_count)
  print("--------- Character Count ---------")
  for char in sorted_list:
    if char['char'].isalpha() == True:
      print(f"{char['char']}: {char['num']}")

main()