# Simulador de Entrada de Imóvel aMORA
Este projeto é um simulador de financiamento imobiliário que calcula e compara a evolução das parcelas de entrada de um imóvel considerando dois cenários:
- Reajuste anual pelo IGPM (6% ao ano, fixo).
- Juros compostos anuais com uma taxa definida pelo usuário.

## Objetivo
### Permitir o usuário calcular:
- Valor de entrada.
- Valor total a guardar.
- Valor mensal base.
- Parcelas anuais corrigidas pelo IGPM e pela taxa de juros informada.

## Exemplo de Uso

### Entrada de dados
- Valor do imóvel (ex: ```400000```)
- Percentual de entrada (ex: ```5```)
- Duração do contrato em anos (ex: ```3```)
- Taxa de juros anual para cenário alternativo (ex: ```10```)

### Saída de dados
```
Valor da entrada: 20000.00
Valor a guardar: 60000.00
Valor mensal base: 1666.67
Valor mensal pelo IGPM: 
Ano 1: R$1666.67
Ano 2: R$1766.67
Ano 3: R$1872.67
Valor mensal com 10% ao ano:
Ano 1: R$1666.67
Ano 2: R$1833.33
Ano 3: R$2016.67
```

## Como executar

### Requisitos
- Python 3.10+
- Docker para execução isolada (Opcional)

### Executando localmente
```bash
python main.py
```

### Executando com Docker
```bash
docker build -t simulador-entrada-imoveis .
docker run -it simulador-entrada-imoveis
```
