
def add_txt(data):
    with open('C:\python_home_task\\task_61\\phone_book.txt', 'a') as book_file:
        book_file.write(f'\n{data}')
    return data