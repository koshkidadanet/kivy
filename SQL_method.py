import sqlite3

try:
    con = sqlite3.connect('..\\Invent.db')
    cur = con.cursor()
    print('БД успешно создана')
except Exception as ex:
    print('Ошибка в подключении:  ',ex)


def CreateTable():
    Create = """CREATE TABLE IF NOT EXISTS tab1 (
Invent TEXT,
Name TEXT,
NumKab INTEGER,
Count INTEGER); """
    cur.execute(Create)
    con.commit()
    print('Таблица создана  .|.  ')

def Append( Invent, Name, NumKab,Count):
    try:
        rest = (Invent, Name, NumKab,Count)
        cur.execute("INSERT INTO tab1 VALUES(?,?,?,?);", rest)
        con.commit()
        print('Данные занесены  .|.  ')
    except Exception as ex:
        print('Ошибка в добавлении: ', ex)

def Show():
    try:
        cur.execute('SELECT * FROM tab1')
        data = cur.fetchall()
        return data
    except Exception as ex:
        print('Ошибка в извлечении: ', ex)

def FindInvent(Inv):
    try:
        cur.execute("SELECT * FROM tab1 WHERE Invent = '%s' " % Inv)
        data = cur.fetchone() #Все элементы с инвентарником Inv
        return data

    except Exception as ex:
        print('Ошибка в извлечении: ', ex)

def DelValue(Inv):
    try:
        cur.execute("DELETE FROM tab1 WHERE Invent = '%s' " % Inv)
        con.commit()
        print('Удаление завершено')
    except Exception as ex:
        print('Ошибка в удалении: ', ex)

def ClearDB():
    try:
        cur.execute("DELETE FROM tab1")
        con.commit()
        print('Очистка завершена')
    except Exception as ex:
        print('Ошибка в очистке: ', ex)

def UpdateCount(Count,Inv):
    try:
        cur.execute("UPDATE tab1 set Count = '%d' WHERE Invent = '%s' " % (Count, Inv))
        con.commit()
        print('Обновление завершено')
    except Exception as ex:
        print('Ошибка в обновлении: ', ex)


#CreateTable()
#Append('П0005','Тактичсеий веник',302, 1)
#FindInvent('П0002')
#DelValue('П0003'
#data = Show()
#for i in data:
#    print(i)
#UpdateCount(100,'П0005')
#print()

#ClearDB()
#print(Show())
#Append('666666','Киллер фича',302, 1)

'''for i in range(6):
    Append(str(100+i),'Этот хакатон рот я его наоборот '+str(i)+' раз мл-инженеров из ВТБ и Дениса Сыропятова, ясно понятно', str(302+i), 1)'''

#con.close()
#Вывод по инвентарнику, удаление, вывод по кабинету, обновление кол-ва предметов
