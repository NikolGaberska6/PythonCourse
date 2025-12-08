def count_letters(text):
    result = {"главни": 0,
              "малки": 0,
              "други": 0}

    for idx in text:
        if idx.isupper():
            result["главни"] += 1
        elif idx.islower():
            result["малки"] += 1
        else:
            result["други"] += 1

    print("Брой малки букви: ", result["малки"])
    print("Брой главни букви: ", result["главни"])
    print("Брой други символи: ", result["други"])

text = input("Въведете текста: ")
count_letters(text)
