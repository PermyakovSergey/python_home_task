
def add_html(data):
    style = 'style="font-size:30px;"'
    html = '<html>\n <head></head>\n <body>\n'
    html += '   <p {}> {}'.format(style, data)
    html += ' </body>\n</html>'

    with open('C:\python_home_task\\task_61\\phone_book.html', 'a') as page:
        page.write(html)