def split_text(input_file, page_size, lines_per_page, output_mode, page_range=None):
    with open(input_file, 'r', encoding='utf-8') as file:
        text = file.readlines()

    total_lines = len(text)
    total_pages = total_lines // lines_per_page + (1 if total_lines % lines_per_page > 0 else 0)

    if page_range:
        start_page, end_page = page_range
        if start_page < 1 or end_page > total_pages or start_page > end_page:
            print("Invalid page range.")
            return
    else:
        start_page, end_page = 1, total_pages

    for page_num in range(start_page, end_page + 1):
        start_index = (page_num - 1) * lines_per_page
        end_index = min(page_num * lines_per_page, total_lines)

        page_content = ''.join(text[start_index:end_index])

        if output_mode == 'all':
            output_file = f'page_{page_num}.txt'
            with open(output_file, 'w', encoding='utf-8') as output:
                output.write(page_content)
        elif output_mode == 'even' and page_num % 2 == 0:
            output_file = f'page_{page_num}.txt'
            with open(output_file, 'w', encoding='utf-8') as output:
                output.write(page_content)
        elif output_mode == 'odd' and page_num % 2 != 0:
            output_file = f'page_{page_num}.txt'
            with open(output_file, 'w', encoding='utf-8') as output:
                output.write(page_content)
        elif output_mode == 'range':
            if start_page <= page_num <= end_page:
                output_file = f'page_{page_num}.txt'
                with open(output_file, 'w', encoding='utf-8') as output:
                    output.write(page_content)


if __name__ == "__main__":
    input_file = "input.txt"
    page_size = 20  # Размер строки в странице
    lines_per_page = 1  # Число строк на странице

    # Выбор действия:
    # 'all': сохранить все страницы
    # 'even': сохранить все четные страницы
    # 'odd': сохранить все нечетные страницы
    # 'range': сохранить страницы из указанного диапазона
    output_mode = 'all'
    # page_range = (2, 3)  # Указать диапазон страниц для 'range' режима

    split_text(input_file, page_size, lines_per_page, output_mode, )
