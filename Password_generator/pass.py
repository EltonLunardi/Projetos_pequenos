import random
import string


def gen_low():
    length = int(input('\nInsira o tamanho da senha: '))
    lower = string.ascii_lowercase
    all = lower
    temp = random.sample(all, length)
    password = "".join(temp)
    print(password)


def gen_upe():
    length = int(input('\nInsira o tamanho da senha: '))
    upper = string.ascii_uppercase
    all = upper
    temp = random.sample(all, length)
    password = "".join(temp)
    print(password)


def gen_num():
    length = int(input('\nInsira o tamanho da senha: '))
    num = string.digits
    all = num
    temp = random.sample(all, length)
    password = "".join(temp)
    print(password)


def gen_sym():
    length = int(input('\nInsira o tamanho da senha: '))
    symbols = string.punctuation
    all = symbols
    temp = random.sample(all, length)
    password = "".join(temp)
    print(password)


def gen_char():
    length = int(input('\nInsira o tamanho da senha: '))
    char = string.ascii_letters
    all = char
    temp = random.sample(all, length)
    password = "".join(temp)
    print(password)


def gen_completo():
    length = int(input('\nInsira o tamanho da senha: '))

    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    num = string.digits
    symbols = string.punctuation
    char = string.ascii_letters

    # Uniao dos caracteres
    all = lower + upper + num + symbols + char

    # Embaralho dos caracteres
    temp = random.sample(all, length)

    # Gerador
    password = "".join(temp)

    print(password)


def menu():
    while True:
        try:
            menu0 = ' |   Gerador de senha aleatória   |'
            menu1 = ' |[1] Senha completa              |'
            menu2 = ' |[2] Senha com letra minuscula   |'
            menu3 = ' |[3] Senha com letra maiuscula   |'
            menu4 = ' |[4] Senha com numeros           |'
            menu5 = ' |[5] Senha com simbolos          |'
            menu6 = ' |[6] Senha com letras            |'
            menu7 = ' |[7] Sair                        |'
            menu = ' ----------------------------------'
            print('\n\n')
            print(menu0.center(80, ' '))
            print(menu1.center(80, ' '))
            print(menu2.center(80, ' '))
            print(menu3.center(80, ' '))
            print(menu4.center(80, ' '))
            print(menu5.center(80, ' '))
            print(menu6.center(80, ' '))
            print(menu7.center(80, ' '))
            print(menu.center(80, ' '))

            option = int(input(' Escolha a opção: '))
            if option == 1:
                gen_completo()
            elif option == 2:
                gen_low()
            elif option == 3:
                gen_upe()
            elif option == 4:
                gen_num()
            elif option == 5:
                gen_sym()
            elif option == 6:
                gen_char()
            elif option == 7:
                print('Fim do Programa')
                exit()
            else:
                print('Escolha Inválida. Escolha entre 1 e 7!')
        except ValueError:
            print('Escolha um numero menor por favor!')


menu()
