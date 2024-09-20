print("Act 9 clase humano")
print("Roberto Pérez Mat: 22308051281084")
print("")
class humano1084:
    nombre=""
    c_cabello=""
    f_nac=""
    estatura=0
    c_ojos=""
    

    def hablar1084(self,a):
        print(f"{a} esta hablando")
    def comer1084(self,b):
        print(f"{b} esta comiendo")
    def bailar1084(self,c):
        print(f"{c} esta bailando")
    def caminar1084(self,d):
        print(f"{d} esta caminando")
    def emusica1084(self,e):
        print(f"{e} esta escuchando musica")
    def cantar1084(self,f):
        print(f"{f} esta cantando")
    def nadar1084(self,g):
        print(f"{g} esta cantando")

#Objetos
roberto=humano1084()
dayanna=humano1084()

print("Resultados para Roberto:")
roberto.nombre="Roberto"
roberto.c_cabello="castaño oscuro"
roberto.f_nac="19 de enero"
roberto.estatura=1.65
roberto.c_ojos="Cafe oscuro"
print(f"Nombre: {roberto.nombre}")
print(f"Color de cabello: {roberto.c_cabello}")
print(f"Fecha de nacimiento: {roberto.f_nac}")
print(f"Estatura: {roberto.estatura}")
print(f"Color de ojos: {roberto.c_ojos}")

print("")
roberto.caminar1084("Roberto")
roberto.hablar1084("Roberto")
roberto.cantar1084("Roberto")
roberto.comer1084("Roberto")

print("")

print("Resultados para Dayanna:")
dayanna.nombre="Dayanna"
dayanna.c_cabello="Castaño oscuro"
dayanna.f_nac="12 de abril"
dayanna.estatura="1.56"
print(f"Nombre: {dayanna.nombre}")
print(f"Color de cabello: {dayanna.c_cabello}")
print(f"Fecha de nacimiento: {dayanna.f_nac}")
print(f"Estatura: {dayanna.estatura}")

print("")
roberto.bailar1084("Dayanna")
roberto.emusica1084("Dayanna")
roberto.nadar1084("Dayanna")
