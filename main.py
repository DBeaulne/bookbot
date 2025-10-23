from stats import get_word_count, count_each_character

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
  # print(text)
  word_count = get_word_count(text)
  print(f"Found {word_count} total words")

  char_count = count_each_character(text.lower())
  print(char_count)
  

main()