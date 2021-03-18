#In this exercise we practice loops, functions and arrays. This exercise is a caesar cypher.

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

import art

def caesar(text, shift, direction):
  finalText = ""
  for letter in text:
    if letter in alphabet:
      index_of_encripted_letter = alphabet.index(letter) + (direction * shift)

      if index_of_encripted_letter < 0 or index_of_encripted_letter  >  (len(alphabet)-1): 
        index_of_encripted_letter = index_of_encripted_letter +  (- direction * (len(alphabet)))

      finalText += alphabet[index_of_encripted_letter]
    else:
      finalText += letter

  print(f"Your result text is: {finalText}")

def checkShift(shift):
  if shift > (len(alphabet)):
    print("Here")
    return shift % len(alphabet)
  else:
    return shift

print(art.logo)
continueCipher = "yes"
while continueCipher == "yes":
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  calculated_shift = checkShift(shift)

  if direction.lower() == "encode":
    caesar(text, calculated_shift, 1)
  elif direction.lower() == "decode":
    caesar(text, calculated_shift, -1)

  continueCipher = input("Do you want to cipher another text? enter yes or not:\n").lower()
