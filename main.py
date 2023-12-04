def all_page(text, total_symbol, page_size, lines_per_page): 
  '''Сохранение всех старниц
     total_symbol -> колличество всех символов текста
     page_size -> размер строки в странице 
     lines_per_page -> число строк на странице
  '''
  for page_num in range(0, total_symbol // page_size // lines_per_page + 1) :
    output_file = f'page_{page_num + 1}.txt'
    page_content = text[page_num * page_size * lines_per_page : (page_num + 1) * page_size * lines_per_page]
    # 1 * 40 * 5 = 200
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
        # 1 * 40 * 5 = 200
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
        # 1 * 40 * 5 = 200
        print(page_content)
        print(len(page_content))
        with open(output_file, 'w', encoding='utf-8') as output:
            output.write(page_content)
            
def range_page(text, total_symbol, page_size, lines_per_page, page_range): 
    '''Сохранение всех нечетных старниц
    total_symbol -> колличество всех символов текста
    page_size -> размер строки в странице 
    lines_per_page -> число строк на странице
    '''
    for page_num in range(page_range[0] - 1, page_range[1]) :
        output_file = f'page_{page_num + 1}.txt'
        page_content = text[page_num * page_size * lines_per_page : (page_num + 1) * page_size * lines_per_page]
        # 1 * 40 * 5 = 200
        print(page_content)
        print(len(page_content))
        with open(output_file, 'w', encoding='utf-8') as output:
            output.write(page_content)
  
def open_text(input_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        text = file.read()
        
    print(text)
    return text

def total_symbol(input_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        text = file.read()
        
    print(len(text))
    return len(text)

if __name__ == "__main__":
    input_file = "input.txt"
    page_size = int(input("Введите размер строки в странице >>>"))  # Размер строки в странице
    lines_per_page = int(input("Введите число строк на странице >>>")) # Число строк на странице

    output_mode = input("""
Выбор действия:
    'all': сохранить все страницы
    'even': сохранить все четные страницы
    'odd': сохранить все нечетные страницы
    'range': сохранить страницы из указанного диапазона
                        """)

    if output_mode == 'all':
        all_page(open_text(input_file), total_symbol(input_file), page_size, lines_per_page)
    elif output_mode == 'even':
        even_page(open_text(input_file), total_symbol(input_file), page_size, lines_per_page)
    elif output_mode == 'odd':
        odd_page(open_text(input_file), total_symbol(input_file), page_size, lines_per_page)
    elif output_mode == 'range':
        page_range = [1, 5]  # Указать диапазон страниц для 'range' режима
        page_range[0] = int(input("Введите первую страницу диапазона >>>"))
        page_range[1] = int(input("Введите последнюю страницу диапазона >>>"))
        range_page(open_text(input_file), total_symbol(input_file), page_size, lines_per_page, page_range)
