startUp = ord('A')
startlow = ord('a')

def encrypt(text, key):
  result = ''
  for character in text:
    if character.isalpha():
      if character.isupper():
        result += chr((ord(character) + int(key) - startUp) % 26 + startUp)
      elif character.islower():
        result += chr((ord(character) + int(key) - startlow) % 26 + startlow)
  return result
      
message = input('Enter your message:\n')
key = input('Enter number key:\n')

if not key.isdigit():
  print('Invalid key')
else:
  print('Encrypted message: \n' + encrypt(message, key))

input("Press Enter to close...\n")
