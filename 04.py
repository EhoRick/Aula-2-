Cidadão = input("É um estudante?")
Dia_da_Semana = input("Qual o dia da semana?")
Tipo_de_Sala = input("Qual tipo de sala?")

terca = Dia_da_Semana
outro = Dia_da_Semana

vip = Tipo_de_Sala
comum = Tipo_de_Sala

estudante = Cidadão
Nao_estudante = Cidadão

Dia_da_Semana = terca  
Tipo_de_Sala =  comum 

Desconto = terca or estudante or comum and terca or Nao_estudante or comum
Sem_Desconto = outro or Nao_estudante or vip and outro or vip 

if (Cidadão == estudante) or (Dia_da_Semana == terca and Tipo_de_Sala == comum):
    print(f"Desconto aplicado {Desconto}")
else:
    print(f"Sem Desconto {Sem_Desconto}")





