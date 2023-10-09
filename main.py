from math import log
from binary_fractions import Binary
import  sys
def read_ensemble_from_file(filename):
   """
   Функция считывающая данные из файла и возвращающая словарь с символами и вероятностью их появления
   :param filename:
   :return: dict
   """
   f = open(filename,'r')
   try:
      dict = {}
      a=f.readline().split(' ')
      b = f.readline().split(' ')
      # проверка на то что символ допустим
      for i in range(0,len(b)):
         if b[i] not in "+-*/=":
            sys.exit('the symbol is invalid')
      # проверка на то что вероятности заданы корректно
      for i in range(0,len(a)):
         print(a[i])
         for j in range(0,len(a[i])):
            if a[i][j] not in "01234567890.\n":
               sys.exit('the probability is not set correctly')
      for i in range(0,len(a)):
         a[i]=float(a[i])
         dict[b[i]] = a[i]
   finally:
      f.close()
   return dict
def read_word_from_file(filename):
   """
   функция считывает слово из файла
   :param filename:Путь до файла где лежит слово которое нужно закодировать
   :return: word переменная типа str
   """
   f = open(filename, 'r')
   try:
      word = f.readline().strip()
   finally:
      f.close()
   return word
def writing_to_file(filename,data):
   """
   функция записи в файл
   :param filename:названия файла в который будет происходить запись, если его нет он создастся
   :param data: закодированное слово
   :return:
   """
   f = open(filename,'w')
   try:
      f.write(data)
   finally:
      f.close()

def calculation_of_cumulative_probability(data_dict):
   """
   Данная функция производит вычисление кумулятивной вероятности
   :param data_dict:массив кумулятивных вероятностей
   :return:arr
   """
   arr=[0]*len(data_dict)
   counter= 0
   for key in data_dict.keys():
      if counter == 0:
         arr[counter]=0
      else:
         arr[counter]=arr[counter-1]+data_dict[prev_key]
      prev_key=key
      counter+=1
   return arr

def calculation_of_koef1(data_dict,cumul_prob):
   """

   :param data_dict:исходный ансамбль
   :param cumul_prob:массив кумулятивных вероятностей
   :return: arr:массив коэффициента?
   """
   counter=0
   arr=[0]*len(cumul_prob)
   for key in data_dict.keys():
      arr[counter]=cumul_prob[counter]+(data_dict[key]/2)
      counter+=1

   return arr

def calculation_of_symb_len(data_dict):
   """
   Функция вычисляет длины кодовых слов
   :param data_dict:Исходный Ансамбль
   :return: arr:массив длин кодовых слов
   """
   arr = [0] * len(data_dict)
   counter = 0
   for key in data_dict.keys():
      arr[counter] = int((-log((data_dict[key]) / 2, 2)) // 1 + 1)
      counter += 1
   return arr
def get_code_table(koef1,sym_len):
   """

   :param koef1: массив коэффициента?
   :param sym_len: массив длин кодовых слов
   :return:arr:массив кодовых слов
   """
   arr=[0]*len(koef1)

   for i in range(0, len(koef1)):
      bin_elem = str(Binary(koef1[i]))
      indx = bin_elem.find('.')+1
      bin_elem = bin_elem[indx:]

      if len(bin_elem)>=sym_len[i]:
         arr[i]=bin_elem[:sym_len[i]]
      else:
         while len(bin_elem)<sym_len[i]:
            bin_elem+='0'
         arr[i] = bin_elem[:sym_len[i]]
   return arr

def print_data(data_dict,cumul_prob,koef1,sym_len,code_table):
   """
   Функция созданная для удобной отладки ПО
   :param data_dict:
   :param cumul_prob:
   :param koef1:
   :param sym_len:
   :param code_table:
   :return:None
   """
   counter=0
   for key in data_dict:
      print(
         f"symbol = {key} , "
            f"probabilities =  {data_dict[key]} ,"
            f" cumul_prob = {cumul_prob[counter]},"
            f"koef1 = {koef1[counter]}, "
            f"len_of_code = {sym_len[counter]},"
            f"code = {code_table[counter]}"
      )
      counter+=1

def Use_Gilbert_Moore(filename):
   """
   Функция производящая вычисления кодовых слов
   :param filename:путь до файла с ансамблем
   :return:dict_word_code:словарь ставящий соответствие между исходным символом и кодовым словом
   """
   dict=read_ensemble_from_file(filename)
   dict_word_code={}
   cumul_prob = calculation_of_cumulative_probability(dict)
   koef1 = calculation_of_koef1(dict, cumul_prob)
   sym_len = calculation_of_symb_len(dict)
   code_table = get_code_table(koef1, sym_len)
   print_data(dict, cumul_prob, koef1, sym_len, code_table)
   counter=0
   for key in dict.keys():
      dict_word_code[key]=code_table[counter]
      counter+=1
   print(dict_word_code)

   return dict_word_code


def word_coding(word,dict):
   """
   Функия кодировки слова
   :param word:кодируемое слово
   :param dict: словарь соответствия простого символа символу закодированному
   :return:
   """
   code_word=''
   for symbl in word:
      if symbl in dict.keys():
         code_word+=dict[symbl]
      else:
         sys.exit("Numbers do not match")



   writing_to_file("result.txt",code_word)

   return code_word

def get_avrg_codeword_len(filename):
   """
   Эта функция вычисляет среднюю длину кодового слова
   :param filename:Файл с исходным ансамблем
   :return: result:Средняя длина кодового слова
   """
   dict = read_ensemble_from_file(filename)
   sym_len = calculation_of_symb_len(dict)
   result=0
   counter=0
   for key in dict.keys():
      result+=dict[key]*sym_len[counter]
      counter+=1

   return round(result,3)

def get_entropy(filename):
   """
   Функция рассчёта энтропий
   :param filename: Путь до файла с ансамблем
   :return:result : float
   """
   dict = read_ensemble_from_file(filename)
   result=0
   for key in dict.keys():
      result-=dict[key]*log(dict[key],2)

   return round(result,3)
def get_redundancy(filename):
   """
   Функция рассчёта избыточности
   :param filename: filename
   :return: float
   """
   return round(get_avrg_codeword_len(filename)-get_entropy(filename),3)

def check_crafting_inequality(filename):
   """
   Функция проверяет неравенство крафта в строгой форме
   :param filename: путь до файла с исходным ансамблем
   :return: True or false
   """
   dict=read_ensemble_from_file(filename)
   len_symb=calculation_of_symb_len(dict)
   result=0
   for i in range(0,len(len_symb)):
      result+=pow(2,-len_symb[i])
   if result<1:
      return True
   else:
      return False
def word_encoding(ensemble_filename,code_word_filename):
   """
   Функция отвечающая за декодировку последовательности
   :param ensemble_filename: путь до файла с ансамблем
   :param code_word_filename: путь до файла с закодированной последовательностью
   :return: result str раскодированная последовательность
   """
   dict_word_code = Use_Gilbert_Moore(ensemble_filename)#получение значений кодовых слов
   code_word=read_word_from_file(code_word_filename)#получение кодового слова
   result=''
   print(dict_word_code)
   while code_word!="":
      for key in dict_word_code.keys():
         ind = code_word.find(dict_word_code[key])
         if ind==0:
            result+=key
            break
      code_word=code_word[len(dict_word_code[key]):]
   writing_to_file("encod_word",result)
   return result

# print(word_coding(read_word_from_file("word.txt"),Use_Gilbert_Moore("uncorrectly_data")))
# # word_encoding("1.txt",'result.txt')