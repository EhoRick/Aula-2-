renda_mensal = float(input("Digite sua renda mensal: "))
Score = int (input("Digite seu Score"))
Bens = str(input("Possuí bens como garantia?"))
Inadimplencia = str(input("Tem histórico de inadimplência?"))

regra1 = renda_mensal and Score
regra2 = Bens or Inadimplencia

Empréstimo = regra1 or regra2

if renda_mensal >= 3000 and Score >= 600:
    print(f"Empréstimo Aprovado")

elif Bens == "sim" and Inadimplencia == "nao":

    print(f"Empréstimo aprovado")

else:

    print(f"Emprestimo Negado")
