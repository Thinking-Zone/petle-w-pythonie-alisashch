import random

pada = random.choice([True, False]) 
zgaduj = True

while zgaduj:
    odpowiedz = input("Czy pada? (t/n) ")
    if odpowiedz == 't':
        if pada == True:
            print("Zgadles")
            break
        else:
            print("zgaduj dalej!")
    elif odpowiedz == 'n':
        if pada == False:
           print("zgadles")
           break
        else:
            print("zgaduj dalej")
    else:
        print("nie zgadles")
