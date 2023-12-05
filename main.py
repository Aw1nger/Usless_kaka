from tkinter import *
from tkinter import messagebox
from tkinter import StringVar
from split_page import all_page, even_page, odd_page
  
def open_text(input_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        text = file.read()
        
    # print(text)
    return text

def total_symbol(input_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        text = file.read()
        
    # print(len(text))
    return len(text)

def clicked():
    global input_file
    global page_size
    global lines_per_page
    global text
    global symbol

    input_file = input_file_entry.get()
    page_size = int(page_size_entry.get())
    lines_per_page = int(lines_per_page_entry.get())
    text = open_text(input_file)
    symbol = int(total_symbol(input_file))
    
    # print(input_file, page_size, lines_per_page)
    # print(output_mode.get())
    
    if output_mode.get() == 'all':
        all_page(text, symbol, page_size, lines_per_page)
        messagebox.showinfo('Выполнено!', 'Все страницы были сохраннены!')
        
    elif output_mode.get() == 'even':
        even_page(text, symbol, page_size, lines_per_page)
        messagebox.showinfo('Выполнено!', 'Все четные страницы были сохраннены!')
        
    elif output_mode.get() == 'odd':
        odd_page(text, symbol, page_size, lines_per_page)
        messagebox.showinfo('Выполнено!', 'Все не четные страницы были сохраннены!')
        
    elif output_mode.get() == 'range':
        
        global window
        global page_range_start_entry
        global page_range_end_entry
        
        window = Tk()
        window.title('Range')
        window.geometry('170x120')
        
        window_lbl1 = Label(window, text='Введите первую страницу')
        page_range_start_entry = Entry(window)
        
        window_lbl2 = Label(window, text='Введите последнюю страницу')
        page_range_end_entry = Entry(window)
        
        btn_range = Button(window, text='Выполнить🥲🔫', command=range_page)
        
        window_lbl1.grid(column=0, row=0)
        page_range_start_entry.grid(column=0, row=1)

        window_lbl2.grid(column=0, row=2)
        page_range_end_entry.grid(column=0, row=3)
                    
        btn_range.grid(column=0, row=4)

        window.mainloop()
        
def range_page(): 
    '''Сохранение всех нечетных старниц
    total_symbol -> колличество всех символов текста
    page_size -> размер строки в странице 
    lines_per_page -> число строк на странице
    '''
    
    page_range_start = int(page_range_start_entry.get())
    page_range_end = int(page_range_end_entry.get())
    
    for page_num in range(page_range_start - 1, page_range_end) :
        output_file = f'page_{page_num + 1}.txt'
        page_content = text[page_num * page_size * lines_per_page : (page_num + 1) * page_size * lines_per_page]
        print(page_content)
        print(len(page_content))
        with open(output_file, 'w', encoding='utf-8') as output:
            output.write(page_content)
            
    messagebox.showinfo('Выполнено!', 'Все страницы из выбранного диапазона были сохраннены!')
    window.destroy()


if __name__ == "__main__":
    
    root = Tk()
    root.title('Useless Kaka')
    root.geometry('300x300')
    
    output_mode = StringVar() 
    output_mode.set("all")
    
    lbl1 = Label(root, text='Введите исходный файл')
    input_file_entry = Entry()
    
    lbl2 = Label(root, text='Введите размер строки в странице')
    page_size_entry = Entry()
    
    lbl3 = Label(root, text='Введите число строк на странице')
    lines_per_page_entry = Entry()
    
    all_btn = Radiobutton(text="Сохранить все страницы", value="all", variable=output_mode)
    even_btn = Radiobutton(text="Сохранить все четные страницы", value="even", variable=output_mode)
    odd_btn = Radiobutton(text="Сохранить все нечетные страницы", value="odd", variable=output_mode)
    range_btn = Radiobutton(text="Сохранить страницы из указанного диапазона", value="range", variable=output_mode)
    
    btn1 = Button(root, text='Выполнить🥲🔫', command=clicked)
    
    #координаты
    lbl1.grid(column=0, row=0)
    input_file_entry.grid(column=0, row=1)
    
    lbl2.grid(column=0, row=2)
    page_size_entry.grid(column=0, row=3)
    
    lbl3.grid(column=0, row=4)
    lines_per_page_entry.grid(column=0, row=5)
    
    all_btn.grid(column=0, row=6)
    even_btn.grid(column=0, row=7)
    odd_btn.grid(column=0, row=8)
    range_btn.grid(column=0, row=9)
    
    btn1.grid(column=0, row=10)
        
    root.mainloop() #отображение окна
    
