class TransportRequest:
    def __init__(self, request_number, client_name, destination,
                 cargo_weight, request_status):
        self.request_number = request_number
        self.client_name = client_name
        self.destination = destination
        self.cargo_weight = cargo_weight
        self.request_status = request_status

    def request_info(self):
        print("----Информация за заявката----")
        print(f"Номер на заявката: {self.request_number}, "
              f"Име на клиент: {self.client_name}, "
              f"Адрес на получаване: {self.destination}, "
              f"Тегло на товара: {self.cargo_weight}, Статус: {self.request_status}.")

    def change_weight(self):
        print("----Промяна на теглото на товара----")
        new_weight = float(input("Въведете новото тегло на товара: "))
        self.cargo_weight = new_weight
        print("Теглото бе променено успешно!")

def request_input():
    print("----Добавяне на заявка----")
    request_number = int(input("Въведете номер на заявката: "))
    client_name = input("Въведете името на клиента: ")
    destination = input("Въведете адрес на получаване: ")
    cargo_weight = float(input("Въведете тегло на товара: "))
    request_status = input("Въведете статус (приета, в процес, отказана): ")
    return TransportRequest(request_number, client_name, destination,
                            cargo_weight, request_status)

def status_info(request_list, num):
    for request in request_list:
        if request.request_number == num:
            print("Found")
            print(f"Статус: {request.request_status}")
            return
    print("Not found")

def add_request(request_list, new_request):
    request_list.append(new_request)
    print("Успешно добавихте заявката в списъка!")

def main():
    request_list = []
    n = int(input("Въведете броя на заявките, които искате да добавеите: "))
    for i in range(n):
        request = request_input()
        request_list.append(request)
        print("Успешно добавихте завка в списъка!")

    found = False
    request_number = int(input("Въведете номер на заявката, на която "
                               "искате да промените теглото: "))
    for request in request_list:
        if request.request_number == request_number:
            print("Заявката е намерена!")
            found = True
            request.change_weight()
    if not found:
       print("Няма заявка с посочения номер в списъка!")

    num = int(input("Въведете номер на заявката, по който търсите: "))
    status_info(request_list, num)

    new_request = request_input()
    add_request(request_list, new_request)

main()

