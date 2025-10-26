from stats import (get_word_count, count_each_character, character_sort)
import sys

def get_book_text(path):
  with open(path) as f:
    return f.read()
   
def main():
  if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
  book_path = sys.argv[1]

  text = get_book_text(book_path)
  print("============= BOOKBOT =============")
  print(f"Analyzing book fount at {book_path}...")

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