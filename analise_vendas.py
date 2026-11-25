"""NExT Vendas: análise simples de faturamento.

Lê dados/vendas.csv e mostra o faturamento por mês e por categoria.
Usa apenas a biblioteca padrão do Python (nada para instalar).

Como rodar:
    python analise_vendas.py
"""

import csv
from collections import defaultdict

ARQUIVO_VENDAS = "dados/vendas.csv"


def carregar_vendas(caminho):
    """Lê o CSV e devolve uma lista de dicionários, um por venda."""
    with open(caminho, encoding="utf-8", newline="") as arquivo:
        return list(csv.DictReader(arquivo))


def valor_da_venda(venda):
    """Faturamento de uma linha: quantidade x preço unitário."""
    return int(venda["quantidade"]) * float(venda["preco_unitario"])


def faturamento_por_mes(vendas):
    """Soma o faturamento agrupando pelo mês (AAAA-MM)."""
    totais = defaultdict(float)
    for venda in vendas:
        mes = venda["data"][:7]
        totais[mes] += valor_da_venda(venda)
    return dict(sorted(totais.items()))


def faturamento_por_categoria(vendas):
    """Soma o faturamento por categoria, do maior para o menor."""
    totais = defaultdict(float)
    for venda in vendas:
        totais[venda["categoria"]] += valor_da_venda(venda)
    return dict(sorted(totais.items(), key=lambda item: item[1], reverse=True))


def formatar_reais(valor):
    """Formata 1234.5 como 'R$ 1.234,50'."""
    texto = f"{valor:,.2f}".replace(",", "_").replace(".", ",").replace("_", ".")
    return f"R$ {texto}"


def main():
    vendas = carregar_vendas(ARQUIVO_VENDAS)

    print("=== Faturamento por mês ===")
    for mes, total in faturamento_por_mes(vendas).items():
        print(f"{mes}: {formatar_reais(total)}")

    print()
    print("=== Faturamento por categoria ===")
    for categoria, total in faturamento_por_categoria(vendas).items():
        print(f"{categoria}: {formatar_reais(total)}")


if __name__ == "__main__":
    main()
