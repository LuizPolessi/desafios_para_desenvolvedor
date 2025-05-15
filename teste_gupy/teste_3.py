#3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
#• O menor valor de faturamento ocorrido em um dia do mês;
#• O maior valor de faturamento ocorrido em um dia do mês;
#• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

#IMPORTANTE:
#a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
#b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;


import json

with open("faturamento.json") as f:
    dados = json.load(f)

faturamentos = [dia["valor"] for dia in dados if dia["valor"] > 0]

menor = min(faturamentos)
maior = max(faturamentos)
media = sum(faturamentos) / len(faturamentos)
dias_acima_da_media = sum(1 for valor in faturamentos if valor > media)

print(f"Menor faturamento do mês: R$ {menor:.2f}")
print(f"Maior faturamento do mês: R$ {maior:.2f}")
print(f"Número de dias com faturamento acima da média: {dias_acima_da_media}")
