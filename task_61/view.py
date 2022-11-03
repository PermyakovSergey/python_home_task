
def view_tel_dir():
    with open('C:\python_home_task\\task_61\\phone_book.txt', 'r') as book_file:
        for contacts in book_file:
            print(contacts)