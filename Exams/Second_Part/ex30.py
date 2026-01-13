import sys
class Athlete:
    def __init__(self, id, name, sport, age, medals):
        self.id = id
        self.name = name
        self.sport = sport
        self.age = age
        self.medals = medals

    def add_medals(self):
        print("Увеличихте броя на медалите на дадения атлет с един!")
        self.medals += 1

    def is_veteran(self):
        if self.age > 30:
            print("Спортистът е ветеран!")

def search_by_sport(athletes, sport):
    all_athletes_from_sport = []
    for athlete in athletes:
        if athlete.sport == sport:
            all_athletes_from_sport.append(athlete)

    if len(all_athletes_from_sport) > 0:
        print("Всички атлети от посочения спорт са: ")
        for athlete in all_athletes_from_sport:
            print(athlete.name)
    else:
        print("Няма атлети от посочения спорт в списъка с атлети!")

def most_medals(athletes):
    most_medal = -sys.maxsize
    for athlete in athletes:
        if athlete.medals > most_medal:
            most_medal = athlete.medals
    print(f"Максималния брой медали е: {most_medal}")
    print(f"Атлета с този брой медали са: ")
    for athlete in athletes:
        if athlete.medals == most_medal:
            print(athlete.name)

def sort_by_age(athletes):
    athletes.sort(key=lambda a: a.age)
    print("Сортирахте спортистите по възраст във възходящ ред!")
    print("Сортираният списък: ")
    for athlete in athletes:
        print(athlete.name)
    return athletes

def delete_no_medals(athletes):
    deleted_athletes = 0
    for athlete in athletes.copy():
        if athlete.medals == 0:
            deleted_athletes += 1
            print(f"Изтрихте атлета {athlete.name} от списъка с атлети!")
            athletes.remove(athlete)
    if deleted_athletes != 0:
        print(f"Атлетите с 0 медала са {deleted_athletes} на брой.")
    else:
        print("Няма атлети с 0 медала в списъка!")

def main():
    athletes = []
    n = int(input("Въведете колко атлета искате да добавите: "))
    for i in range(n):
        id = input("Въведете айди-то на спортиста, който искате да добавите: ")
        name = input("Въведете името на спортиста, който искате да добавите: ")
        sport = input("Въведете спорта на спортиста, който искате да добавите: ")
        age = int(input("Въведете годините на спортиста, който искате да добавите: "))
        medals = int(input("Въведете медалите на спортиста, който искате да добавите: "))
        athlete = Athlete(id, name, sport, age, medals)
        athletes.append(athlete)
        print("Успешно добавихте атлета към списъка!")

    found = False
    name = input("Въведете името на спортиста, на който искате да добавите медали: ")
    for athlete in athletes:
        if athlete.name == name:
            found = True
            athlete.add_medals()
    if not found:
        print("Не е намерен спортист с посоченото име в списъка!")

    found = False
    name = input("Въведете името на спортиста, който искате да проверите, дали е ветеран: ")
    for athlete in athletes:
        if athlete.name == name:
            found = True
            athlete.is_veteran()
    if not found:
        print("Не е намерен спортист с посоченото име в списъка!")

    sport = input("Въведете спорта на спортиста, по който търсите атлети: ")
    search_by_sport(athletes, sport)

    most_medals(athletes)

    sort_by_age(athletes)

    delete_no_medals(athletes)

main()