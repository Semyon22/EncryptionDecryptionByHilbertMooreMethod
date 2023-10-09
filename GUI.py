from tkinter import *
from tkinter import ttk
from main import *
from tkinter.messagebox import showerror, showwarning, showinfo
def code_word():
    print(entry1.get())
    print(entry.get())
    try:
        dict_word_code=Use_Gilbert_Moore(entry1.get())

        result="кодовые слова для всех символов алфавита:"+"\n"+str(dict_word_code)\
               +"\n"+"средняя длина кодового слова:\n"+str(get_avrg_codeword_len(entry1.get()))+"\n"\
               +"Избыточность:\n"+str(get_redundancy(entry1.get()))+"\n"+"Неравенство крафта выполнено?\n"\
               +str(check_crafting_inequality(entry1.get()))+"\n"+"Зашифрованная последовательность содержится в файле result.txt"

        showinfo(title="Параметры полученные при кодировке", message=result)
        print(word_coding(read_word_from_file(entry.get()), Use_Gilbert_Moore(entry1.get())))
    except:
        showerror(title = "Сообщение об ошибке",
                  message="Вы записали: \n 1) Либо НЕСУЩЕСТВУЮЩИЙ ФАЙЛ \n 2) Либо НИЧЕГО не ввели \n 2) Либо НЕКОРРЕКТНЫЙ файл"
                  )
    finally:pass
def encod_word():
    print(entry2.get())
    print(entry3.get())
    try:
        result = "Раскодированная последовательность: "+word_encoding(entry2.get(), entry3.get())+"\n"+"Ваша раскодированная последовательность записана в файл encod_word"
        showinfo(title="раскодированная последовательность", message=result)
    except:
        showerror(title="Сообщение об ошибке",
                  message="Вы записали: \n 1) Либо НЕСУЩЕСТВУЮЩИЙ ФАЙЛ \n 2) Либо НИЧЕГО не ввели \n 2) Либо НЕКОРРЕКТНЫЙ файл"
                  )
    finally:pass
root = Tk()
lbl = Label(root, text="Зашифровка последовательности",font=("Arial Bold", 15))
lbl.grid(column=0, row=0)
lbl = Label(root, text="введите имя файла с исходным ансамблем:",font=("Arial", 10))
lbl.grid(column=0, row=1)
#задание размера окна
root.geometry('450x430')
#добавление формы ввода до исходного ансамбля

root.title("Шифрование/Дешифрование методом Гильбера-Мура")

entry1 = ttk.Entry()
entry1.grid()



lbl = Label(root, text="введите имя файла с кодируемым словом:",font=("Arial", 10))
lbl.grid(column=0, row=4)

entry = ttk.Entry()
entry.grid()

btn = ttk.Button(text="Зашифровать", command=code_word)
btn.grid()

#элементы интерфейса для дешифровки

lbl = Label(root, text="Расшифровка последовательности",font=("Arial Bold", 15))
lbl.grid(column=0, row=7)

lbl = Label(root, text="введите имя файла с исходным ансамблем:",font=("Arial", 10))
lbl.grid(column=0, row=8)

entry2 = ttk.Entry()
entry2.grid(column=0, row=9)

lbl = Label(root, text="введите имя файла с закодированным словом:",font=("Arial", 10))
lbl.grid(column=0, row=10)

entry3 = ttk.Entry()
entry3.grid(column=0, row=11)

btn1 = ttk.Button(text="Расшифровать", command=encod_word)
btn1.grid()

#окно инструкций
lbl = Label(root,
            text="ВНИМАНИЕ! Чтобы программа отработала корректно,\n необходимо ввести ансамбль в следующем формате:\n"
                 "P(X1) P(X2) P(X3)... P(Xn)\n"
                 "X1    X2      X3  ...  Xn"
            ,font=("Arial", 12)
            )
lbl.grid(column=0, row=13)
lbl = Label(root,
            text="ВНИМАНИЕ! Чтобы программа отработала корректно,\n необходимо ввести слово в 1 строку\n"
                 "пример: word"

            ,font=("Arial", 12)
            )
lbl.grid(column=0, row=14)

root.mainloop()