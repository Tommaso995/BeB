from Dati import Dati


class Prenotazione(Dati):
    def __init__(self, name, surname, tel, mail, day_enter, month_enter, year_enter, day_out, month_out, year_out):
        super().__init__(name, surname, tel, mail)
        self.day_enter = day_enter
        self.month_enter = month_enter
        self.year_enter = year_enter
        self.day_out = day_out
        self.month_out = month_out
        self.year_out = year_out
    
    def prenotazione(self):
        return super().presentazione(),f"\nPer la data dal {self.day_enter}/{self.month_enter}/{self.year_enter} a {self.day_out}/{self.month_out}"\
                f"/{self.year_out}"
    
    #Metodo che appende tutti gli argomenti passati alla lista
    def append(self,prenotazione_lst, *args):
        for arg in args:
            prenotazione_lst.append(arg)

    def insert_contact(self):
        prenotazione_lst = []
        controll = True
        while controll:
            try:
                self.name = str(input("Digita il nome"))
                if len(self.name)<3 or self.name == self.name.isalpha():
                    raise ValueError
                self.surname = str(input("Digita il cognome"))
                if len(self.surname) <3 or self.surname == self.surname.isalpha():
                    raise ValueError
                self.tel = int(input("Digita il numero telefonico"))
                if self.tel < 999 or str(self.tel) == str(self.tel).isdigit():
                    raise ValueError
                self.mail = input("Digita la mail")
                if len(self.mail) < 3 or self.mail == self.mail.isalpha():
                    raise ValueError
                self.day_enter = int(input("Digita il giorno di entrata"))
                if (self.day_enter <1 or self.day_enter>31) or (str(self.day_enter) == str(self.day_enter).isdigit()):
                    raise ValueError
                self.month_enter = int(input("Digita il mese di entrata"))
                if (self.month_enter <1 or self.month_enter>12) or (str(self.month_enter) == str(self.month_enter).isdigit()):
                    raise ValueError
                self.year_enter = int(input("Digita l'anno di entrata"))
                if (self.year_enter < 2022 or self.year_out > 2025) or (str(self.year_enter) == str(self.year_enter).isdigit()):
                    raise ValueError
                self.day_out = int(input("Digita il giorno di uscita"))
                if (self.day_out <1 or self.day_out>31) or (str(self.day_out) == str(self.day_out).isdigit()):
                    raise ValueError
                self.month_out = int(input("Digita il mese di uscita"))
                if (self.month_out <1 or self.month_out>12) or (str(self.month_out) == str(self.month_out).isdigit()):
                    raise ValueError
                self.year_out = int(input("Digita l'anno di uscita"))
                if (self.year_enter < 2022 or self.year_out > 2025) or (str(self.year_out) == str(self.year_out).isdigit()):
                    raise ValueError
            except ValueError:
                print("Valore non consentito, Riprova")
            else:
                self.append(prenotazione_lst,self.name, self.surname, self.tel,self.mail, self.day_enter, self.month_enter, self.year_enter, self.day_out, self.month_out, self.year_out)
                controll = False
        # prenotazione_lst.append(self.name, self.surname, self.tel,self.mail, self.day_enter, self.month_enter, self.year_enter, self.day_out, self.month_out, self.year_out)

        return prenotazione_lst
    
    def register(self, prenotazione):
        prenotazione[len(prenotazione)+1] = self.insert_contact()

    def delete_contact(self, prenotazione, tel):
        delete_lst = []
        for k,v in prenotazione.items():
            if tel in v:
                delete_lst.append(tel)

        if not delete_lst:
            return print("Contatto non presente")
        else:
            for k in delete_lst:
                del prenotazione[k]
            return print("Contatto rimosso")
        
    def update_contact(self, prenotazione,tel):
        controll = True
        while controll:
            try:
                for k,v in prenotazione.items():
                    if tel in v:
                        choise = input("Cosa vuoi modificare?\n1 per Nome\n2 per cognome\n3 per telefono\n4 per mail"\
                                       "\n5 per la nuova data di entrata del giorno\n6 per la nuova data di entrata del mese\n"\
                                        "7 per la nuova data di entrata dell'anno\n8 per la nuova data di uscita del giorno\n"\
                                        "9 per la nuova data di uscita del mese\n10 per la nuova data di uscita dell'anno"\
                                        "\nSe hai finito premi E")
                        if choise == "1":
                            new_name = str(input("Digita il nuovo nome"))
                            if len(new_name)<3 or new_name != new_name.isalpha():
                                raise ValueError
                            v[0] = new_name
                        elif choise == "2":
                            new_surname = str(input("Digita il nuovo cognome"))
                            if len(new_surname) < 3 or new_surname != new_surname.isalpha():
                                raise ValueError
                            v[1] = new_surname
                        elif choise == "3":
                            new_tel = int(input("Digita il nuovo numero telefonico"))
                            if new_tel < 999 or str(new_tel) != str(new_tel).isdigit():
                                raise ValueError
                            v[2] = new_tel
                        elif choise == "4":
                            new_mail = str(input("Digita la nuova mail"))
                            if len(new_mail)<3 or new_mail != new_mail.isalpha():
                                raise ValueError
                            v[3] = new_mail
                        elif choise == "5":
                            new_day_enter = int(input("Digita la nuova data del giorno di entrata"))
                            if (new_day_enter <1 or new_day_enter>31) or (str(new_day_enter) != str(new_day_enter).isdigit()):
                                raise ValueError
                            v[4] = new_day_enter
                        elif choise == "6":
                            new_month_enter = int(input("Digita la nuova data del mese di entrata"))
                            if (new_month_enter <1 or new_month_enter>31) or (str(new_month_enter) != str(new_month_enter).isdigit()):
                                raise ValueError
                            v[5] = new_month_enter
                        elif choise == "7":
                            new_year_enter = int(input("Digita la nuova data dell'anno di entrata"))
                            if (new_year_enter <1 or new_year_enter>31) or (str(new_year_enter) != str(new_year_enter).isdigit()):
                                raise ValueError
                            v[6] = new_year_enter
                        elif choise == "8":
                            new_day_out = int(input("Digita la nuova data del giorno di uscita"))
                            if (new_day_out <1 or new_day_out>31) or (str(new_day_out) != str(new_day_out).isdigit()):
                                raise ValueError
                            v[7] = new_day_out
                        elif choise == "9":
                            new_month_out = int(input("Digita la nuova data del mese di uscita"))
                            if (new_month_out <1 or new_month_out>31) or (str(new_month_out) != str(new_month_out).isdigit()):
                                raise ValueError
                            v[8] = new_month_out
                        elif choise == "10":
                            new_day_out = int(input("Digita la nuova data dell'anno di uscita"))
                            if (new_day_out <1 or new_day_out>31) or (str(new_day_out) != str(new_day_out).isdigit()):
                                raise ValueError
                            v[9] = new_day_out
                        elif choise.upper() == "E":
                            controll = False
                        else:
                            raise Exception
                    else:
                        raise Exception
            except ValueError:
                return print("Valore non consentito, riprova")
            except Exception:
                return print("Scelta non valida o valore non trovato")
            else:
                controll = False
                return print("Contatto modificato")

                
    def search_contact(self, prenotazione,tel):
        contact_found = []
        for k, v in prenotazione.items():
            if tel in v:
                contact_found.append(k)
        if not contact_found:
            print("Contatto non trovato")
        else:
            print("Contatti trovati:")
            for v in contact_found:
                print(v)
            
    def lst_prenotazione(self,prenotazione):
        for k,v in prenotazione.items():
            return print(k,v)