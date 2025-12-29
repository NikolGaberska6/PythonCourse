class Membership:
    def __init__(self, member_id, name, trainer, monthly_fee, sessions_left):
        self.member_id = member_id
        self.name = name
        self.trainer = trainer
        self.monthly_fee = monthly_fee
        self.sessions_left = sessions_left

    def use_sessions(self, count):
        if count <= self.sessions_left:
            print(f"Използвахте {count} от сесиите си!")
            self.sessions_left -= count
            print(f"Останали сесии: {self.sessions_left}.")
        else:
            print("Нямате достатъчно сесии за използване!")

    def discount(self):
        if 100 < self.monthly_fee <= 200:
            discount = 0.07 * self.monthly_fee
            print("Отстъпката ви е 7% от месечната цена.")
            self.monthly_fee -= discount
            print(f"Новата цена с отстъпката е: {self.monthly_fee} лв.")
        elif 50 <= self.monthly_fee <= 100:
            discount = 0.1 * self.monthly_fee
            print("Отстъпката ви е 10% от месечната цена.")
            self.monthly_fee -= discount
            print(f"Новата цена с отстъпката е: {self.monthly_fee} лв.")
        else:
            print("Няма отстъпка!")
            print(f"Цената без отстъпка е: {self.monthly_fee} лв.")

    def info(self):
        print(f"ID на члена: {self.member_id}, Име на члена: {self.name}, "
              f"Треньор: {self.trainer}, Месечна такса: {self.monthly_fee}, "
              f"Останали посещения: {self.sessions_left}.")

def search_by_member_id(membership_list, member_id):
    for member in membership_list:
        if member.member_id == member_id:
            print("Отрихте член с посоченото ID")
            return
    print("Няма член в списъка с посоченото ID!")

def search_by_trainer(membership_list, trainer):
    members_by_trainer = []
    for member in membership_list:
        if member.trainer == trainer:
            members_by_trainer.append(member)

    average = 0
    sum_of_fee_of_trainer = 0
    if len(members_by_trainer) > 0:
        for member in members_by_trainer:
            sum_of_fee_of_trainer += member.monthly_fee
        average = sum_of_fee_of_trainer / len(members_by_trainer)
        print(f"Средната такса за треньора е: {average}")
    else:
        print("Няма такъв трениор в листа!")

    result = []
    for member in members_by_trainer:
        if member.monthly_fee <= average:
            result.append(member)

    if len(result) > 0:
        print("Всички такси на дадения трениор ≤ от средната му.")
        for member in result:
            member.info()
    else:
        print("Няма такси на дадения трениор ≤ от средната му.")

def sort_by_sessions_left(membership_list):
    membership_list.sort(key=lambda m: m.sessions_left)
    print("Сортирахте листа във възходящ ред!")

def delete_by_name(membership_list, name):
    for member in membership_list.copy():
        if member.name == name:
            if member.sessions_left <= 3:
                print(f"Изтрихте {name} от списъка.")
                membership_list.remove(member)

def main():
    membership_list = []
    n = int(input("Въведете колко члена ще добавите: "))
    for i in range(n):
        member_id = input("Въведете ID на члена: ")
        name = input("Въведете името на члена: ")
        trainer = input("Въведете името на трениора на члена: ")
        monthly_fee = float(input("Въведет месечна такса: "))
        sessions_left = int(input("Въведете останали посещения: "))
        member = Membership(member_id, name, trainer, monthly_fee, sessions_left)
        membership_list.append(member)
        print("Успешно добавихте члена към списъка!")

    member_id = input("Въведете ID-то на члена, който ще използва от сисиите си: ")
    for member in membership_list:
        if member.member_id == member_id:
            count = int(input("Въведете колко посещения иска да използва: "))
            member.use_sessions(count)

    member_id = input("Въведете ID-то на члена, който търсите: ")
    search_by_member_id(membership_list, member_id)

    trainer = input("Въведете името на трениора, по който търсите: ")
    search_by_trainer(membership_list, trainer)

    sort_by_sessions_left(membership_list)

    name = input("Въведете името на члена, който искате да изтриете: ")
    delete_by_name(membership_list, name)

main()
