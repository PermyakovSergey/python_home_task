def clear_all():
    with open('C:\python_home_task\\task_61\\phone_book.txt', 'w') as book_file:
            book_file.write(f'Phone Book')

    style = 'style="font-size:30px;"'
    html = '<html>\n <head></head>\n <body>\n'
    html += '   <p {}> {}'.format(style, 'Phone Book')
    html += ' </body>\n</html>'

    with open('C:\python_home_task\\task_61\\phone_book.html', 'w') as page:
        page.write(html)
