class Dati():
    def __init__(self, name, surname, tel, mail):
        self.name = name
        self.surname = surname
        self.tel = tel
        self.mail = mail
        
    def presentazione(self):
        return f"La persona\nNome: {self.name}\nCognome: {self.surname}\nTelefono: {self.tel}\nE-Mail: {self.mail}"
    
    