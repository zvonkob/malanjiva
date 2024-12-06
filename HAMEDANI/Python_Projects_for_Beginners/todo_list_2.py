MENU = '\nTodo List Menu:\n1. View Tasks\n2. Add a Task\n'
MENU += '3. Remove a Task\n4. Exit'

def view_tasks(tasks):
    if not tasks:
        print('    No tasks in the list.')
        return
    for j, task in enumerate(tasks, start=1):
        print(f'    {j}. {task}')

def add_a_task(tasks):
    while True:
        new_task = input('    New task: ').strip()
        if len(new_task) == 0:
            print('Invalid task!')
            continue
        tasks.append(new_task)
        return

def remove_a_task(tasks):
    view_tasks(tasks)
    if not tasks: return
    while True:
        try:
            j = int(input('Enter task number: '))
            if 1 <= j <= len(tasks):
                tasks.pop(j - 1)
                break
            raise ValueError()
        except ValueError:
            print('Invalid task number')

def main():
    tasks = []
    value_error = False
    while True:
        if not value_error: print(MENU)
        try:
            i = int(input('Enter your choice: '))
            if 1 <= i <= 4:
                value_error = False
                if   i == 1: view_tasks(tasks)
                elif i == 2: add_a_task(tasks)
                elif i == 3: remove_a_task(tasks)
                else:        break
            else:
                raise ValueError()
        except ValueError:
            print('Invalid choice')
            value_error = True

if __name__ == '__main__':
    main()