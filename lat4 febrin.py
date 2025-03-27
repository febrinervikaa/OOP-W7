def exo_group(cls):
    class MemberEXO(cls):  
        members = [
            "Xiumin", "Suho", "Lay", "Baekhyun", "Chen", 
            "Chanyeol", "D.O.", "Kai", "Sehun"
        ]
        
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            print(f"EXO Members: {', '.join(self.members)}")
    
    return MemberEXO  # Mengembalikan kelas baru

@exo_group
class EXO:
    def __init__(self, fandom_name):
        self.fandom_name = fandom_name
        print(f"Nama Fandom: {self.fandom_name}")

exo = EXO("EXO-L")
