from view import view_tel_dir
from add_contact import create_new
from txt_create import add_txt
from html_create import add_html
from clear import clear_all
def to_do():
    
    print('\n    s - Отобразить справочник\n\
    n - добавить контакт\n\
    c - очистить справочник\n\
    q - выход\n')
    do_it = input('Введите требуемое действие: ')
    while do_it not in ('s', 'n', 'c', 'q'):
        do_it = input('Введите требуемое действие: ')
    
    if do_it == 'q': exit()
    if do_it == 's': view_tel_dir()
    if do_it == 'n': add_html(add_txt(create_new()))
    if do_it == 'c': clear_all()

    to_do()

