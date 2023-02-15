class Task:
    def __init__(self, id, description):
        self.id = id
        self.description = description


class TaskList:
    def __init__(self, file_name):
        self.file_name = file_name
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        try:
            with open(self.file_name, 'r') as f:
                for line in f:
                    id, description = line.strip().split('|')
                    self.tasks.append(Task(id, description))
        except FileNotFoundError:
            pass

    def save_tasks(self):
        with open(self.file_name, 'w') as f:
            for task in self.tasks:
                f.write(f"{task.id}|{task.description}\n")

    def create_task(self, description):
        id = len(self.tasks) + 1
        task = Task(id, description)
        self.tasks.append(task)
        self.save_tasks()
        return task

    def read_tasks(self):
        return self.tasks

    def update_task(self, id, description):
        for task in self.tasks:
            if task.id == id:
                task.description = description
                self.save_tasks()
                return task

    def delete_task(self, id):
        for i, task in enumerate(self.tasks):
            if task.id == id:
                del self.tasks[i]
                self.save_tasks()
                return


# Exemplo de uso:
task_list = TaskList('tasks.txt')

while True:
    # Imprime o menu de opções
    print('\nEscolha uma opção:')
    print('1. Ver tarefas')
    print('2. Adicionar tarefa')
    print('3. Atualizar tarefa')
    print('4. Remover tarefa')
    print('0. Sair')

    # Lê a opção escolhida pelo usuário
    option = input('> ')

    if option == '1':
        # Ler todas as tarefas
        tasks = task_list.read_tasks()
        for task in tasks:
            print(task.id, task.description)

    elif option == '2':
        # Criar uma nova tarefa
        description = input('Digite a descrição da tarefa: ')
        task = task_list.create_task(description)
        print(f'Tarefa {task.id} adicionada com sucesso!')

    elif option == '3':
        # Atualizar uma tarefa existente
        id = input('Digite o ID da tarefa que deseja atualizar: ')
        description = input('Digite a nova descrição da tarefa: ')
        task = task_list.update_task(int(id), description)
        if task:
            print(f'Tarefa {task.id} atualizada com sucesso!')
        else:
            print('Tarefa não encontrada')

    elif option == '4':
        # Remover uma tarefa existente
        id = input('Digite o ID da tarefa que deseja remover: ')
        task_list.delete_task(int(id))
        print(f'Tarefa {id} removida com sucesso!')

    elif option == '0':
        # Sai do programa
        break

    else:
        print('Opção inválida, tente novamente')
