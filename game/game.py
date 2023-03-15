import random

def choice_option():
  options=('piedra','papel','tijera')
  user_option=input("piedra, papel, tijera: ")
  user_option=user_option.lower()
  computer_option=random.choice(options)
  if not user_option in options:
    print("opcion incorrecta")
    return None, None
  
  return user_option,computer_option

def rules(user_option,computer_option):
  if user_option==computer_option:
    return 0
  elif user_option=='piedra'and computer_option=='papel':
    return 2
  elif user_option=='piedra' and computer_option=='tijera':
    return 1
  elif user_option=='papel' and computer_option=='piedra':
    return 1
  elif user_option=='papel' and computer_option=='tijera':
    return 2
  elif user_option=='tijera'and computer_option=='piedra':
    return 2
  elif user_option=='tijera' and computer_option=='papel':
    return 1
  else :
    return 3


def run():
  user_points=0
  computer_points=0
  round=1
  while True:
    
    print('*'*10)
    print('ROUND NUMBER: '+str(round))
    print('PUNTUACION: ')
    print('USER: '+str(user_points))
    print('COMPUTER: '+str(computer_points))
    if computer_points==3:
      print('GANADOR DE LA PARTIDA COMPUTER!!!')
      break
    elif user_points==3:
      print('GANADOR DE LA PARTIDA USER!!!')
      break
    option1,option2=choice_option()
    winner=rules(option1,option2)
    if winner==0:
      print('EMPATE, INTENTA DE NUEVO')
      continue
    elif winner==1:
      print('GANADOR USER')
      user_points+=1
      round+=1
    elif winner==2:
      print('GANADOR COMPUTER')
      computer_points+=1
      round+=1
    elif winner==3:
      continue
    
if __name__=="__main__":  
    run()

# opcion1,opcion2=choice_option()
# print(opcion1,opcion2)
  
  
  