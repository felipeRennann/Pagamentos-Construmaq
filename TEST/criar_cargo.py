import json
import os
from cargo import Cargo


class CriarCargo:
    cargos_dict = {}

    @staticmethod
    def carregar_cargos():
        if os.path.exists('cargos.json'):
            with open('cargos.json', 'r') as file:
                return json.load(file)
        return {}

    @staticmethod
    def criar_cargo(data):
        nome = data['nome']
        valor_hora_base = round(float(data['valor_hora_base']), 2)
        valor_hora_extra_um = round(float(data['valor_hora_extra_um']), 2)
        valor_hora_extra_dois = round(float(data['valor_hora_extra_dois']), 2)
        adicional_noturno = round(float(data['adicional_noturno']), 2)
        repouso_remunerado = round(float(data['repouso_remunerado']), 2)
        valor_ferias = round(float(data['valor_ferias']) / 100, 2)
        valor_antecipa_ferias = round(float(data['valor_antecipa_ferias']) / 100, 2)
        valor_decimo_terceiro = round(float(data['valor_decimo_terceiro']) / 100, 2)
        valor_antecipa_salario = round(float(data['valor_antecipa_salario']), 2)
        pagamento_fgts = round(float(data['pagamento_fgts']) / 100, 2)
        desconto_inss = round(float(data['desconto_inss']) / 100, 2)
        desconto_refeicao = round(float(data['desconto_refeicao']), 2)
        desconto_transporte = round(float(data['desconto_transporte']), 2)

        cargo = Cargo(nome, valor_hora_base, adicional_noturno, valor_hora_extra_um,
                      valor_hora_extra_dois, repouso_remunerado, valor_ferias,
                      valor_antecipa_ferias, valor_decimo_terceiro, valor_antecipa_salario,
                      pagamento_fgts, desconto_inss, desconto_refeicao, desconto_transporte)
        
        CriarCargo.cargos_dict[nome] = cargo.to_dict()
        CriarCargo.salvar_cargos()
        print(f"Cargo {nome} criado com sucesso e adicionado ao dicionário.")   

   
    @staticmethod
    def salvar_cargos():
        with open('cargos.json', 'w') as file:
            json.dump(CriarCargo.cargos_dict, file)

def editar_cargo():
    # Carregar cargos
    cargos = CriarCargo.carregar_cargos()
    
    if not cargos:
        print("Nenhum cargo disponível para editar.")
        return
    
    print(f"Cargos disponíveis: {list(cargos.keys())}")
    nome_cargo = input("Digite o nome do cargo que deseja editar: ")

    if nome_cargo not in cargos:
        print(f"Cargo {nome_cargo} não encontrado.")
        return
    
    print(f"Cargo atual: {cargos[nome_cargo]}")
    
    # Atualizar os valores do cargo
    valor_hora_base = float(input("Digite o novo valor da hora base (deixe em branco para manter o valor atual): ") or cargos[nome_cargo]['valor_hora_base'])
    valor_hora_extra_um = float(input("Digite o novo valor da hora extra 50% (deixe em branco para manter o valor atual): ") or cargos[nome_cargo]['valor_hora_extra_um'])
    valor_hora_extra_dois = float(input("Digite o novo valor da hora extra 100% (deixe em branco para manter o valor atual): ") or cargos[nome_cargo]['valor_hora_extra_dois'])
    adicional_noturno = float(input("Digite o novo adicional noturno (deixe em branco para manter o valor atual): ") or cargos[nome_cargo]['adicional_noturno'])
    repouso_remunerado = float(input("Digite o novo valor do repouso remunerado (deixe em branco para manter o valor atual): ") or cargos[nome_cargo]['repouso_remunerado'])
    
    # Atualizar o dicionário
    cargos[nome_cargo] = {
        'valor_hora_base': valor_hora_base,
        'valor_hora_extra_um': valor_hora_extra_um,
        'valor_hora_extra_dois': valor_hora_extra_dois,
        'adicional_noturno': adicional_noturno,
        'repouso_remunerado': repouso_remunerado
    }
    
    # Salvar as alterações no arquivo JSON
    CriarCargo.salvar_cargos()
    print(f"Cargo {nome_cargo} atualizado com sucesso.")

def main():
    CriarCargo.cargos_dict = CriarCargo.carregar_cargos()
    print(f"Cargos carregados: {CriarCargo.cargos_dict}")
    
    while True:
        print("\nMenu:")
        print("1. Criar Cargo")
        print("2. Editar Cargo")
        print("3. Sair")
        
        escolha = input("Escolha uma opção: ")
        if escolha == '1':
            data = {}
            data['nome'] = input("Nome do cargo: ")
            data['valor_hora_base'] = input("Valor da hora base: ")
            data['valor_hora_extra_um'] = input("Valor da hora extra 50%: ")
            data['valor_hora_extra_dois'] = input("Valor da hora extra 100%: ")
            data['adicional_noturno'] = input("Adicional noturno: ")
            data['repouso_remunerado'] = input("Repouso remunerado: ")
            data['valor_ferias'] = input("Valor de férias: ")
            data['valor_antecipa_ferias'] = input("Valor de antecipação de férias: ")
            data['valor_decimo_terceiro'] = input("Valor do décimo terceiro: ")
            data['valor_antecipa_salario'] = input("Valor de antecipação salarial: ")
            data['pagamento_fgts'] = input("Pagamento de FGTS: ")
            data['desconto_inss'] = input("Desconto de INSS: ")
            data['desconto_refeicao'] = input("Desconto de refeição: ")
            data['desconto_transporte'] = input("Desconto de transporte: ")
            CriarCargo.criar_cargo(data)
        elif escolha == '2':
            editar_cargo()
        elif escolha == '3':
            break
        else:
            print("Opção inválida. Tente novamente.")





if __name__ == "__main__":
    main()