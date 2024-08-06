class partyAnimal:
    
    def __init__(self, name) -> None:
        self.x=0
        self.name= name
        print(self.name,'constructed')
    
    def party(self):
        self.x = self.x + 1
        print(f'Party {self.name} count {self.x}')
        
    def __del__(self):
        print('I am destructed', self.x)
        
class FootballFan(partyAnimal): # ? FootballFan class extends from partyAnimal
    
    def __init__(self, name) -> None:
        super().__init__(name)
        self.points = 0
        
    def touchdown(self):
        self.points = self.points + 7
        self.party()
        print(self.name,'points', self.points)
        
r = partyAnimal('Renato')
r.party()
j = partyAnimal('Junior')
j.party()
r.party()

s = FootballFan('Jim')
s.party()
s.touchdown()
