pada = False
licznik_nie = 0

while not pada:
    print("Nie pada! yaaay")
    
    odpowiedz = input("Czy pada? (tak/nie) ")
    
    if odpowiedz == 'tak':  
        print(f"Program zakończony. Odpowiedziałeś {licznik_nie} razy.")
        break 
    elif odpowiedz == 'nie':  
        licznik_nie += 1  
        
    elif odpowiedz == 'nie wiem':  
        print("To wyjdź na zewnątrz i się dowiedz.")  
        
    else:
        print("Proszę odpowiedzieć 'tak', 'nie' lub 'nie wiem'.") 
