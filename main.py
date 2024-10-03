import art
from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(direction, text, shift):
  output_text = []
  text_size = int(len(text))
  
  a = 0
  
  while a < text_size:
    b = 0
    right_letter = False
  
    while right_letter == False:
      if text[a] not in alphabet:
        output_text.append(text[a])
        right_letter = True
      else:  
        if text[a] == alphabet[b]:
          
          if direction == 'encode':
  
            position = (b + shift) % 26
            output_text.append(alphabet[position])
            
          elif direction == 'decode':
            position = (b - shift) % 26
            output_text.append(alphabet[position])
  
          right_letter = True
          
        else: 
          b += 1
    a += 1

  print(f"The {direction}d text is: {(''.join(output_text))}")
  restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
  if restart == "yes":
    cipher_program()
  else:
    print("Goodbye!")

def cipher_program():
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  caesar(direction, text, shift)

print(logo)
cipher_program()