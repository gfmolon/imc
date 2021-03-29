#Simples Calculo de IMC com Python, usando OO

class Imc:

    def apresentacao(self):
        print("***********************")
        print("     CALCULO IMC")
        print("***********************")

    def calcula_imc(self,peso,altura):
        imc = peso / (altura * altura)
        imc = round(imc)
        return round(imc)

    def mostra_resultado(self,resultado_imc):
        print(f"-----Seu resultado é {resultado_imc} ----")
        if resultado_imc <= 18:
            print("Pessoas abaixo do peso.")
        elif resultado_imc >= 18 and resultado_imc <= 24:
            print("Consideradas IMC de pessoas normais.")
        elif resultado_imc >= 25 and resultado_imc <= 30:
            print("Consideradas pessoas com sobrepeso.")
        else:
            print("Pessoas obesas.")

c = Imc()
c.apresentacao()
peso = float(input("Qual seu peso? (Ex: 73kg)"))
altura = float(input("Qual sua altura? (Ex: 1.80)"))
c.mostra_resultado(c.calcula_imc(peso,altura))



