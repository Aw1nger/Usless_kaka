def all_page(text, total_symbol, page_size, lines_per_page): 
  '''Сохранение всех старниц
     total_symbol -> колличество всех символов текста
     page_size -> размер строки в странице 
     lines_per_page -> число строк на странице
  '''
  for page_num in range(0, total_symbol // page_size // lines_per_page + 1) :
    output_file = f'page_{page_num + 1}.txt'
    page_content = text[page_num * page_size * lines_per_page : (page_num + 1) * page_size * lines_per_page]
    print(page_content)
    print(len(page_content))
    with open(output_file, 'w', encoding='utf-8') as output:
        output.write(page_content)
        
def even_page(text, total_symbol, page_size, lines_per_page): 
    '''Сохранение всех четных старниц
    total_symbol -> колличество всех символов текста
    page_size -> размер строки в странице 
    lines_per_page -> число строк на странице
    '''
    for page_num in range(1, total_symbol // page_size // lines_per_page + 1, 2) :
        output_file = f'page_{page_num + 1}.txt'
        page_content = text[page_num * page_size * lines_per_page : (page_num + 1) * page_size * lines_per_page]
        print(page_content)
        print(len(page_content))
        with open(output_file, 'w', encoding='utf-8') as output:
            output.write(page_content)
            
def odd_page(text, total_symbol, page_size, lines_per_page): 
    '''Сохранение всех нечетных старниц
    total_symbol -> колличество всех символов текста
    page_size -> размер строки в странице 
    lines_per_page -> число строк на странице
    '''
    for page_num in range(0, total_symbol // page_size // lines_per_page + 1, 2) :
        output_file = f'page_{page_num + 1}.txt'
        page_content = text[page_num * page_size * lines_per_page : (page_num + 1) * page_size * lines_per_page]
        print(page_content)
        print(len(page_content))
        with open(output_file, 'w', encoding='utf-8') as output:
            output.write(page_content)
            
