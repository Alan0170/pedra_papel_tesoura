import random

pedra = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

papel = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

tesoura = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images = [pedra, papel, tesoura]

user_choice = int(input("Qual sua escolha? Digite 0 para PEDRA, 1 para papel e 2 para Tesoura.\n"))
if user_choice >= 3 or user_choice < 0:
  print("Você digitiou um valor inválido, Você Perdeu!")
else:
  print(game_images[user_choice])
  

  computer_choice = random.randint(0, 2)
  print("." * 15)
  print(f"Computador escolheu:")
  print(game_images[computer_choice])



  if computer_choice == user_choice:
    print("Deu empate!")
  elif (user_choice == 0 and computer_choice == 2) or (user_choice == 1 and computer_choice == 0) or (user_choice == 2 and computer_choice == 1):
    print("Você Ganhou!")
  else:
    print("Você Perdeu!")

