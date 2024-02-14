import csv ## импортируем нужные библиотеки

'''Напишем код для быстрой сортировки'''
def fast(arr,start,stop):
    if start>stop: return
    left = start
    right = stop
    middle = arr[(left+right)//2]['GameName']
    while left<=right:
        while arr[left]['GameName']<middle:left+=1
        while arr[right]['GameName']>middle:right-=1
        if left <= right:
            arr[right]['GameName'],arr[left]['GameName']=arr[left]['GameName'],arr[right]['GameName']
            right-=1
            left+=1
    fast(arr,start,right)
    fast(arr,left,stop)

'''Начинаем перенос файла в переменную games'''
with open('/home/student/Рабочий стол/Предпроф/game.txt',encoding='utf-8') as file:
    games=list(csv.DictReader(file,delimiter='$',quotechar='"'))
    fast(games,0,len(games)-1) ## сортируем
    count_err={} ## создаем словарь для ошибок вида:название-кол-во ошибок
    '''Cчитаем баги'''
    for i in games:
        if i['GameName'] in count_err:
            count_err[i['GameName']]=count_err.get(i['GameName']) + 1
        else:
            count_err[i['GameName']]=1
    '''Выводим'''
    for gime in count_err:
        print(f'{gime} - количество багов: {count_err.get(gime)}')


    