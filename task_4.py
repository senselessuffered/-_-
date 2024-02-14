import csv ## импортируем нужные библиотеки

'''Начинаем перенос файла в переменную games'''
with open('/home/student/Рабочий стол/Предпроф/game.txt',encoding='utf-8') as file:
    games=list(csv.reader(file,delimiter='$',quotechar='"'))[1:]
    count_err={} ## создаем словарь для ошибок вида:название-кол-во ошибок
    '''Cчитаем баги'''
    for i in games:
        if i[0] in count_err:
            count_err[i[0]]=count_err.get(i[0]) + 1
        else:
            count_err[i[0]]=1
    '''Выводим'''
    for game in games:
        game.append(count_err.get(game[0]))
    games = sorted(games,key = lambda x: x[4]) ## сортируем по ошибкам

'''Записываем новые данные в новый файл'''
with open('/home/student/Рабочий стол/Предпроф/game_counter.csv','w',encoding='utf-8',newline='') as file:
    new=csv.writer(file,delimiter='$')
    new.writerow(['GameName','characters','nameError','date','Counter'])
    new.writerows(games)