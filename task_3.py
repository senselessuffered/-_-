import csv ## импортируем нужные библиотеки

'''Пишем алгорит поиска в функии search'''
def search(arr,val):
    left,right=0,len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == val: return mid
        elif arr[mid]>val:
            right=mid-1
        else:
            left=mid+1
    return -1
'''Начинаем перенос файла в переменную games'''
with open('/home/student/Рабочий стол/Предпроф/game.txt',encoding='utf-8') as file:
    games=list(csv.DictReader(file,delimiter='$',quotechar='"'))
    while True:
        vvod = input()
        if vvod=='game': break
        else:
            


