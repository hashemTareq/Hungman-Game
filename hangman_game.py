import random

words = ['python', 'javascript', 'java', 'slash', 'print']
choosen_word = random.choice(words)
letters_of_word = []
for letter in choosen_word:
  letters_of_word.append(letter)
word_display = ['_' for _ in choosen_word]
tries = 8

while tries > 0 and '_' in word_display:
  print('\n'+''.join(word_display))
  guess = input('Guess 🤔. Type a letter: ').strip().lower()
  if guess in letters_of_word:
    for index, letter in enumerate(letters_of_word):
      if letter == guess:
        word_display[index] = guess
        letters_of_word[index] = ' '
        break
  else:
    print('Wrong letter ❌. Try again.')
    tries -= 1

if '_' not in word_display:
  print('\n' + choosen_word)
  print('Correct guess. You servive 👏')
else:
  print(f'\nYou dead. The word was {choosen_word}')