MENU = '\nTodo List Menu:\n1. View Tasks\n2. Add a Task\n3. Remove a Task\n4. Exit'

def view_tasks(tasks):
    if len(tasks) == 0:
        print('No tasks in the list.')
    else:
        for j, task in enumerate(tasks, start=1):
            print(f'{j}. {task}')

def add_a_task(tasks):
    while True:
        new_task = input('New task: ').strip()
        if len(new_task) > 0:
            tasks.append(new_task)
            return tasks
        print('Invalid task!')

def remove_a_task(tasks):
    view_tasks(tasks)
    if len(tasks) > 0:
        while True:
            try:
                j = int(input('Enter task number: '))
                if j < 1 or len(tasks) < j:
                    raise ValueError()
                tasks.pop(j - 1)
                return tasks
            except ValueError:
                print('Invalid task number')

def main():
    tasks = []
    value_error = False
    while True:
        if not value_error: print(MENU)
        try:
            i = int(input('Enter your choice: '))
            if i < 1 or 4 < i: raise ValueError()
            value_error = False
            if   i == 1: view_tasks(tasks)
            elif i == 2: tasks = add_a_task(tasks)
            elif i == 3: tasks = remove_a_task(tasks)
            else:        break
        except ValueError:
            print('Invalid choice')
            value_error = True

if __name__ == '__main__':
    main()