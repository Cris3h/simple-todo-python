import os #interaccion con el sist operativo. (realiza operaciones de entrada y/o salida)
import pickle #serializa o deserealiza objetos de python.

class Task: 
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.completed = False


# class Task: (single task)
#           
#     def __init__(self, name, description):  <------- constructor y sus propiedades

#         self.name = name                    <------- propiedad y su constructor

#         self.description = description      <------- propiedad y su constructor

#         self.completed = False              <------- propiedad y su constructor


class TodoList:
    def __init__(self):
        self.tasks=[]

    def add_task(self, task):
        self.tasks.append(task)

    def show_tasks(self):
        if len(self.tasks) == 0:
            print('no tasks.')
        else:
            for index, task in enumerate(self.tasks, start=1):
                completed='Completed' if task.completed else "Pending"
                print(f"{index}. {task.name} - {task.description} ({completed})")

    def delete_task(self, index):
        if index >=1 and index <= len(self.tasks):
            task_deleted = self.tasks.pop(index - 1)
            print(f"Task deleteed: {task_deleted.name}")
        else:
            print('task index incorrect')



# class TodoList:
#     def __init__(self):              <------- constructor
#         self.tasks=[]                <------- inicializa con el atributo tasks como una lista vacia

#     def add_task(self, task):        <------- metodo de la clase
#         self.tasks.append(task)      <------- agrega la task a la lista 

#     def show_tasks(self):            <------ metodo de la clase
#         if len(self.tasks) == 0:
#             print('no tasks.')       <------ si no hay nada printea el string
#         else:
#             for index, task in enumerate(self.tasks, start=1):
#                 completed='Completed' if task.completed else "Pending"
#                 print(f"{index}. {task.name} - {task.description} ({completed})") <----- si tiene length entonces muestra este mensaje

#     def delete_task(self, index):                     <------ metodo de la clase
#         if index >=1 and index <= len(self.tasks):
#             task_deleted = self.tasks.pop(index - 1)    <------ borra la task de la lista
#             print(f"Task deleteed: {task_deleted.name}") <--- printea el mensaje
#         else:
#             print('task index incorrect')               <--------- o no lo encuentra


def show_menu():   # <---------     Bastante simple como para comentarlo
    print('=== GESTOR DE TAREAS!')
    print('1. add task')
    print('2. show tasks')
    print('3. delete task')
    print('4. Go out')


def main():   
    tasks_list = TodoList()

    while True:
        show_menu()
        option = input('Choose a option')

        if option == "1":
            name = input('add the task name: ')
            description = input('add the task info: ')
            task = Task(name, description)
            tasks_list.add_task(task)
            print('Task correcly added')
            input('press enter to continue')
        
        elif option == "2":
            tasks_list.show_tasks()
            input('press enter to continue')

        elif option == "3":
            index = int(input('press the number of tasks to be deleted'))
            tasks_list.delete_task(index)
            input('press enter to continue')

        elif option == "4":
            print("see ya' later")

        else:
            print("na-ah u didnt say what u just said, mtf!. Try again")

# def main():                    <----------------- punto de entrada a la aplicacion
#     tasks_list = TodoList()

#     while True:                <---------------- buclecito de toa' la vida
#         show_menu()
#         option = input('Choose a option')

#         if option == "1":
#             name = input('add the task name: ')
#             description = input('add the task info: ')
#             task = Task(name, description)
#             tasks_list.add_task(task)
#             print('Task correcly added')
#             input('press enter to continue')
        
#         elif option == "2":
#             tasks_list.show_tasks()
#             input('press enter to continue')

#         elif option == "3":
#             index = int(input('press the number of tasks to be deleted'))
#             tasks_list.delete_task(index)
#             input('press enter to continue')

#         elif option == "4":
#             print("see ya' later")

#         else:
#             print("na-ah u didnt say what u just said, mtf!. Try again")

# if __name__ == "__main__":
#     main()



if __name__ == "__main__":
    main()