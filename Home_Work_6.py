#1.
    #В отеле есть 3 типа номеров: royal (2-3 комнаты), lux (1-2 комнаты), standard (1 комната).
    #надо добавить метод для создания номеров и хранения их в виде словаря.

class Hotel():
    def __init__(self, a, b, c):
        self.royal = a
        self.lux = b
        self.standard = c

rooms= Hotel(3, 2, 1)
print(rooms.__dict__)
print(' ') 

#2
    #В номере есть мебель для ванной, спальни и зала (если есть зал)
    #нужно добавить метод для добавления и удаления из номера мебели в любом количестве.

class Royal():
    def __init__(self, a, b, c):
        self.bathroom = a
        self.bedroom = b
        self.living_room = c

    def furniture(self, a, b, c):
        print ('for delete: set -x, for add: set +x, for same: set 0')
        print ('furniture for bathroom')
        i = input()
        if i == "0":
            print(' ')
        else:
            self.bathroom = i

        print ('furniture for bedroom')
        i = input()
        if i == "0":
            print(' ')
        else:
            self.bedroom = i

        print ('furniture for living_room')
        i = input()
        if i == "0":
            print(' ')
        else:
            self.living_room = i

total = Royal('total in the bathroom',  'total in the bedroom', 'total in living_room')
total.furniture(1, 1, 1)
print (total.__dict__)
print(' ')

#3 
    #Нужно создать один метод для изменения любого номера по заданным параметрам, в том числе удалению и изменению номеров и комнат

class StandartRoom():
