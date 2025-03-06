import random

def start_game():
    name = input("Введите свое имя: ")
    words = ['пионы', 'орхидея', "хлорофитум", 
             "роза", "акация", "гипсофилы", "фиалка", "тюльпан"]
    random_word = random.choice(words)
    word_letters = []
    attempts = 3
    
    while attempts > 0:
        hidden_word = ''
        for letter in random_word:
            if letter in word_letters:
                hidden_word += letter
            else:
                hidden_word += '_'
        
        print(f"Загаданное слово - {hidden_word}")
        print(f"Осталось {attempts} попыток")
           
        user = input("Введите букву: ").lower()
        
        if  user in word_letters:
            print(f"Откройте букву! {user}")
            continue
        word_letters.append(user)
        
        if user not in random_word:
            attempts -= 1
            print("К сожелению такой буквы нет :(")
            
        if '_' not in hidden_word:
            print('Поздравляем вы выиграли!')
            print(f"И главный приз букет {hidden_word}, вручается {name}")
            
        if attempts == 0:
            print(f'Загаданное слово - {random_word}')
            print("Вы проиграли в этом сезоне, ждем вас на следующем!")
