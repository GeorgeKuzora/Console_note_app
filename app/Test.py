import os
import json

def ListOfNoteTitles():
    directory = os.getcwd() + '/data'
    for file in os.listdir(directory):
        with open(f'{directory}/{file}', 'r') as current_file:
            file_content = json.loads(current_file.read())
            print(file_content['note_title'])

def PrintBodyOfTheChosenNote():
    directory = os.getcwd() + '/data'
    title_from_user = input("Введите название заметки: ")
    for file in os.listdir(directory):
        with open(f'{directory}/{file}', 'r') as current_file:
            dict_from_content = json.loads(current_file.read())
            if title_from_user == dict_from_content['note_title']:
                result = dict_from_content['note_body']
                print(f'Текст выбранной заметки: {result}')
                break
            
def AskUserForAction():
    print('Какое действие вы хотите совершить?')
    print('1. Посмотреть список заметок по названииям')
    print('2. Вывести заметку на экран')
    user_choice = input('Введите номер действия: ')
    if user_choice == '1': ListOfNoteTitles()
    elif user_choice == '2': PrintBodyOfTheChosenNote()
    else:
        print("Введен неправильный номер. Попробуйте еще раз.")
        AskUserForAction()

AskUserForAction()