import youtube_dl

'''link = ['url']'''
link = [str((input('\n\nURL do video:')))]


with youtube_dl.YoutubeDL() as ydl:
    ydl.download(link)


def menu():
    while True:
        try:
            menu1 = ' |[1] Inserir URL do video   |'
            menu2 = ' |[2] Sair            |'
            menu = '---------------------'
            print('\n\n')
            print(menu1.center(80, ' '))
            print(menu2.center(80, ' '))

            option = int(input(' Escolha a opção: '))
            if option == 1:
                ydl.download(link)
            elif option == 2:
                print('Fim do Programa')
                exit()
            else:
                print('Escolha Inválida. Escolha entre 1 e 2')
        except ValueError:
            print('Escolha Inválida. Escolha entre 1 e 2')


menu()
