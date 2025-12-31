class Animal:
    def __init__(self, id, species, habitat, food_cost, count):
        self.id = id
        self.species = species
        self.habitat = habitat
        self.food_cost = food_cost
        self.count = count

    def feed(self, quantity):
        if self.count >= quantity:
            print(f"Захранихте посоченото животно с {quantity} брой храна.")
            self.count -= quantity
            print(f"Останало количество от храната на посоченото животно е: {self.count}.")
        else:
            print("Недостатъчно количество храна за захранване на животното!")

    def discount(self):
        if 100 < self.food_cost <= 300:
            discount = 0.05 * self.food_cost
            print("Отстъпката е 5%  от цената на храната!")
            self.food_cost -= discount
            print(f"Новата цена на храната с отстъпката е: {self.food_cost} лв.")
        elif 50 <= self.food_cost <= 100:
            discount = 0.08 * self.food_cost
            print("Отстъпката е 8% от цената на храната!")
            self.food_cost -= discount
            print(f"Новата цена на храната с отстъпката е: {self.food_cost} лв.")
        else:
            print("Няма отстъпка!")
            print(f"Цената на храната без отстъпка е: {self.food_cost} лв.")

    def info(self):
        print(f"ИД на животното: {self.id}, Вид: {self.species}, Местообитание: {self.habitat}, "
              f"Цена на храната: {self.food_cost}, Количество на храната: {self.count}.")

def search_by_id(animal_list, id):
    for animal in animal_list:
        if animal.id == id:
            print("Намерихме животното с посоченото ИД в списъка с животни!")
            print("Пълна информация: ")
            animal.info()
            return
    print("Не намерихме животно с посоченото ИД в списъка с животни!")

def search_by_habitat(animal_list, habitat):
    animals_from_this_habitat = []
    for animal in animal_list:
        if animal.habitat == habitat:
            animals_from_this_habitat.append(animal)

    average_cost_for_habitat = 0
    sum_of_cost_of_habitats = 0
    if len(animals_from_this_habitat) > 0:
        for animal in animals_from_this_habitat:
            sum_of_cost_of_habitats += animal.food_cost
        average_cost_for_habitat = sum_of_cost_of_habitats / len(animals_from_this_habitat)
        print(f"Средния разход за храна на животни от посоченото местоположение е: {average_cost_for_habitat:.2f} лв.")
    else:
        print("Няма животни от посоченото местоположение в листа!")

    animals_with_lower_cost = []
    for animal in animals_from_this_habitat:
        if animal.food_cost <= average_cost_for_habitat:
            animals_with_lower_cost.append(animal)

    if len(animals_with_lower_cost) > 0:
        print("Животните с разход с храна ≤ средния за хабитата са: ")
        for animal in animals_with_lower_cost:
            animal.info()
    else:
        print("Няма животни в списъка с разход за храна  ≤ средния за хабитата!")

def sort_by_count(animal_list):
    animal_list.sort(key=lambda a: a.count)
    print("Принтирахте листа във възходящ ред!")

def delete_by_species(animal_list, species):
    for animal in animal_list.copy():
        if animal.species == species:
            if animal.count <= 1:
                print(f"Изтрихте животното от {species} вид от списъка с животни!")
                animal_list.remove(animal)

def main():
    animal_list = []
    n = int(input("Въведете броя на животните, които искате да добавите: "))
    for i in range(n):
        id = input("Въведете ИД-то на животното, което искате да добавите: ")
        species = input("Въведете вида на животното, което искате да добавите: ")
        habitat = input("Въведете местоположението на животното, което искате да добавите: ")
        food_cost = float(input("Въведете цената на храната: "))
        count = int(input("Въведете бройката на храната: "))
        animal = Animal(id, species, habitat, food_cost, count)
        animal_list.append(animal)
        print("Успешно добавихте животното към списъка!")

    found = False
    id = input("Въведете ИД-то на животното, което искате да нахраните: ")
    for animal in animal_list:
        if animal.id == id:
            found = True
            quantity = int(input("Въведете количеството храна: "))
            animal.feed(quantity)
            break
    if not found:
        print("Не намерихме животно с посоченото ИД в списъка!")

    found = False
    id = input("Въведете ИД-то на животното, чиято храна искате да проверите за отстъпка: ")
    for animal in animal_list:
        found = True
        if animal.id == id:
            animal.discount()
            break
    if not found:
        print("Не намерихме животно с посоченото ИД в списъка!")

    id = input("Въведете ИД-то на животното, което търсите: ")
    search_by_id(animal_list, id)

    habitat = input("Въведете местоположението, по което търсите: ")
    search_by_habitat(animal_list, habitat)

    sort_by_count(animal_list)

    species = input("Въведете вида на животното, което искате да изтриете: ")
    delete_by_species(animal_list, species)

main()