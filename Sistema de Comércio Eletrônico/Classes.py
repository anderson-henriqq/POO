class Cliente:
    
    def __init__(self, id, n, e, f):
        self._id = id
        self._nome = n
        self._email = e
        self._fone = f
        if not isinstance(id, int): raise ValueError("ID invalido")
        if (id <= 0): raise ValueError("ID invalido")
        if (n == ""): raise ValueError("O campo nome precisa ser preenchido") 
        if (e == ""): raise ValueError("O campo e-mail precisa ser preenchido") 
        if (f == ""): raise ValueError("O campo fone precisa ser preenchido")
    
    def __str__(self):
        return f"{self._id}{self._nome}{self._email}{self._fone}"

    def set_id(self,id):
        if not isinstance(id, int): raise ValueError("ID invalido")
        if (id <= 0): raise ValueError("ID invalido")
        self._id = id
    
    def set_nome(self,n):
        if (n == ""): raise ValueError("O campo nome precisa ser preenchido") 
        self._nome = n

    def set_email(self, e):
        if (e == ""): raise ValueError("O campo e-mail precisa ser preenchido")
        self._email = e
    
    def set_email(self, f):
        if (f == ""): raise ValueError("O campo fone precisa ser preenchido")
        self._fone = f
    
    def get_id(self):
        return self._id
    
    def get_nome(self):
        return self._nome
    
    def get_email(self):
        return self._email
    
    def get_fone(self):
        return self._fone
    