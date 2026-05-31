import csv


def gerar_csv(valor_aluguel):

    with open("orcamento.csv", "w", newline="", encoding="utf-8") as arquivo:

        escritor = csv.writer(arquivo)

        escritor.writerow(["Parcela", "Valor"])

        for mes in range(1, 13):
            escritor.writerow([mes, f"R$ {valor_aluguel:.2f}"])

    print("\nArquivo orcamento.csv gerado com sucesso!")