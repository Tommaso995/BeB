from Prenotazione import Prenotazione
import os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def start():
    save_pre = {}
    prenotazione = Prenotazione("","",0,"",0,0,0,0,0,0)
    controll = True
    while controll:
        try:
            choise =  input("Quale operazione vuoi effettuare?\n1 Inserimento\n2 Eliminazione\n3 Modificare una prenotazione\n4 Trovare una prenotazione "\
                            "\n5 Per stampare le prenotazioni\n6 Stampa la prenotazione appena inviata\n7 Per uscire")
            if choise == "1":
                prenotazione.register(save_pre)
            elif choise == "2":
                tel = int(input("Digita il numero di telefono da eliminare"))
                prenotazione.delete_contact(save_pre,tel)
            elif choise == "3":
                tel = int(input("Digita il numero di telefono da modificare"))
                prenotazione.update_contact(save_pre,tel)
            elif choise == "4":
                tel = int(input("Digita il numero di telefono da cercare"))
                prenotazione.search_contact(save_pre, tel)
            elif choise == "5":
                prenotazione.lst_prenotazione(save_pre)
            elif choise == "6":
                prenotazione.prenotazione()
            elif choise == "7":
                controll = False
                clear_console()
            else:
                raise Exception
        except Exception:
            print("Opzione non valida riprovare...")
        else:
            print("Svolto correttamente")


if __name__ == "__main__":
    start()