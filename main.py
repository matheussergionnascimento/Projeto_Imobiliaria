from imoveis import Apartamento, Casa, Estudio
from csv_generator import gerar_csv

CONTRATO = 2000

print("=" * 40)
print("IMOBILIÁRIA R.M")
print("=" * 40)

print("\nTipos de Imóveis")
print("1 - Apartamento")
print("2 - Casa")
print("3 - Estúdio")

opcao = int(input("\nEscolha uma opção: "))

if opcao == 1:

    quartos = int(input("Quantidade de quartos (1 ou 2): "))

    garagem = input("Deseja garagem? (s/n): ").lower() == "s"

    criancas = input("Possui crianças? (s/n): ").lower() == "s"

    imovel = Apartamento(
        quartos,
        garagem,
        criancas
    )

elif opcao == 2:

    quartos = int(input("Quantidade de quartos (1 ou 2): "))

    garagem = input("Deseja garagem? (s/n): ").lower() == "s"

    imovel = Casa(
        quartos,
        garagem
    )

elif opcao == 3:

    vagas = int(
        input("Quantidade de vagas de estacionamento: ")
    )

    imovel = Estudio(vagas)

else:
    print("Opção inválida!")
    raise SystemExit

valor_aluguel = imovel.calcular_aluguel()

print("\n" + "=" * 40)
print("ORÇAMENTO")
print("=" * 40)

print(f"Aluguel Mensal: R$ {valor_aluguel:.2f}")

print(f"Contrato Imobiliário: R$ {CONTRATO:.2f}")

parcelas = int(
    input("Parcelar contrato em até 5 vezes: ")
)

while parcelas < 1 or parcelas > 5:

    parcelas = int(
        input("Digite um valor entre 1 e 5: ")
    )

valor_parcela = CONTRATO / parcelas

print(f"Contrato Parcelado: {parcelas}x")
print(f"Valor da Parcela: R$ {valor_parcela:.2f}")

print("\n" + "=" * 40)
print("RESUMO DO ORÇAMENTO")
print("=" * 40)

if opcao == 1:
    print("Tipo de Imóvel: Apartamento")
elif opcao == 2:
    print("Tipo de Imóvel: Casa")
else:
    print("Tipo de Imóvel: Estúdio")

print(f"Aluguel Mensal: R$ {valor_aluguel:.2f}")
print(f"Contrato Imobiliário: R$ {CONTRATO:.2f}")
print(f"Parcelamento: {parcelas}x de R$ {valor_parcela:.2f}")

gerar_csv(valor_aluguel)

print("\nArquivo orcamento.csv gerado com sucesso!")
print("\nObrigado por utilizar a Imobiliária R.M")