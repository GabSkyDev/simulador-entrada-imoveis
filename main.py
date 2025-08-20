# Entrada de dados
valor_imovel = float(input("Digite o valor do imovel (R$): "))
percentual_entrada = int(input("Digite o percentual da entrada (%): "))
duracao_contrato = int(input("Digite a duração do contrato em anos: "))
taxa_anual_alter = int(input("Digite o percentual de juros anual para simulação de cenário alternativo (%): "))

# Cálculo de valores
valor_entrada = valor_imovel * (percentual_entrada / 100)
total_a_guardar = valor_imovel * 0.15
parcela_mensal = total_a_guardar / (duracao_contrato * 12)

# Saída de dados
print(f"\nValor da entrada:  {valor_entrada:.2f}")
print(f"Valor a guardar: {total_a_guardar:.2f}")
print(f"Valor mensal base: {parcela_mensal:.2f}")

print("Valor mensal pelo IGPM: ")
for n in range(1, duracao_contrato + 1):
    parcela_anoN_igpm = parcela_mensal * (1 + 0.06)**(n - 1)
    print(f"Ano {n}: R${parcela_anoN_igpm:.2f}")

print(f"Valor mensal com {taxa_anual_alter}% ao ano: ")
for n in range(1, duracao_contrato + 1):
    parcela_anoN_juros = parcela_mensal * (1 + taxa_anual_alter / 100)**(n - 1)
    print(f"Ano {n}: R${parcela_anoN_juros:.2f}")

