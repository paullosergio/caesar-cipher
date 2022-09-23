alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

from art import logo
print(logo)

def caesar(text, shift, x):

  cipher_text = ''   
    
  if x != "encode": # Change the shift number to negative for decode.
      shift *= -1
  
  for i in text:
    if i in alphabet: # Change only the characters.
      
      if (alphabet.index(i) + shift) > 25: # Restart the index.
        t = (alphabet.index(i) + shift) % 25
        position = t - 1
      else:
        position = alphabet.index(i) + shift   
      
      new_letter = alphabet[position]
      cipher_text += new_letter
    else:
      cipher_text += i
      
  print(f"The {x}d text is {cipher_text}")

  y = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")

  if y == "yes": # Play the code again if the answer is yes.
    menu()
  elif y == "no":
    print("Goodbye")    
  else:
    print("Invalid answer.")


def menu():
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  if direction == "encode" or direction == "decode":
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift %= 25 # Putting number shift in range of the alphabetic list.
    caesar(text, shift, direction)
  else:
    menu()
  

menu()
   