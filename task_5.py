import csv ## импортируем нужные библиотеки
import string

def hash(a):
    leter=string.ascii_letters + "1234567890:-"
    p = 65
    m = 9+10**9
    sum = 0
    k=0
    for bukv in a:
        if bukv not in "'.,?!":
            sum=sum+(leter.index(bukv)+1)*(p**k)
            k+=1
    return sum % m

'''Начинаем перенос файла в переменную games'''
with open('/home/student/Рабочий стол/Предпроф/game.txt',encoding='utf-8') as file:
    games=list(csv.DictReader(file,delimiter='$',quotechar='"'))
    new_game=[]
    for game in games:
        kes = game['GameName'] + game['characters'] ##складываем имя и название игры
        '''убираем пробелы и делаем хэш'''
        kes=kes.split() 
        kes=''.join(kes)
        kes = hash(kes)
        '''создаем новую матрицу'''
        new_game.append([kes]+[game['GameName'],game['characters'],game['nameError'],game['date']])
        
'''Записываем матрицу в файл'''
with open('/home/student/Рабочий стол/Предпроф/game_with_hash.csv','w',encoding='utf-8',newline='') as file:
    new=csv.writer(file,delimiter='$')
    new.writerow(['Hash','GameName','characters','nameError','date'])
    new.writerows(new_game)
        
