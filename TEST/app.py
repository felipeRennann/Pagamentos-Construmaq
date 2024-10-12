from flask import Flask, request, jsonify, render_template, send_file
from datetime import datetime
#from firebase_config import *  # Importa a configuração do Firebase
#from firebase_admin import firestore
from flask_cors import CORS
from gerar_sub_total_um import Sub_total_um
from gerador_olerite import Gerar_olerite
from criar_cargo import CriarCargo
import json
import os


app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})

# Obtém uma referência ao Firestore
#db = firestore.client()

#Criação e exibição dos dados dos cagos na tela
class CriarCargo:
    
    
    
    #Carregar dados cadastrados na tabela no front
    @staticmethod
    def carregar_cargos():
        """Carrega os cargos do arquivo JSON."""
        if os.path.exists('cargos.json'):
            with open('cargos.json', 'r') as file:
                try:
                    return json.load(file)
                except json.JSONDecodeError:
                    # Em caso de erro no arquivo JSON, retorna um dicionário vazio.
                    print("Erro ao ler o arquivo cargos.json. O arquivo está corrompido.")
                    return {}
        return {}

    @staticmethod
    def salvar_cargos(cargos_dict):
        """Salva os cargos no arquivo JSON."""
        with open('cargos.json', 'w') as file:
            json.dump(cargos_dict, file, indent=4)  # Adiciona indentação para legibilidade.

# Carrega cargos inicialmente
cargos_dict = CriarCargo.carregar_cargos()

@app.route('/')
def index():
    """Renderiza a página inicial."""
    return render_template('index.html')

@app.route('/api/cargos', methods=['GET', 'POST'])
def cargos():
    print("Requisição recebida")  # Log da requisição

    if request.method == 'POST':
        try:
            data = request.json
            if not data:  # Verifica se data é None ou um dicionário vazio
                print("Dados não recebidos corretamente!")
                return jsonify({"message": "Dados não recebidos corretamente!"}), 400
            
            print(f"Dados recebidos: {data}")

            # Validação dos campos obrigatórios
            required_fields = [
                'nome_cargo',
                'valor_hora_base',
                'valor_hora_extra_um',
                'valor_hora_extra_dois',
                'repouso_remunerado',
                'adicional_noturno',
                'desconto_inss',
                'desconto_refeicao',
                'desconto_transporte',
                'pagamento_fgts',
                'valor_decimo_terceiro',
                'valor_ferias',
                'valor_um_terco_ferias'
                
            ]

            # Verifica se todos os campos obrigatórios estão presentes
            missing_fields = [field for field in required_fields if field not in data]
            if missing_fields: 
                print(f"Campos obrigatórios faltando: {missing_fields}")
                return jsonify({"message": f"Campos obrigatórios faltando: {', '.join(missing_fields)}!"}), 400
            
            # Converte os valores para float
            for field in required_fields[1:]:  # Ignora o primeiro campo 'nome_cargo'
                 if field in data:
                  try:
                        data[field] = float(data[field])
                  except ValueError:
                        return jsonify({"message": f"Valor inválido para {field}!"}), 400
            
            # Remover espaços em branco e validar nome_cargo
            nome = data['nome_cargo'].strip()
            if not nome:
                return jsonify({"message": "O campo nome_cargo não pode estar vazio!"}), 400
            
            print(f"Nome do cargo: '{nome}'")  # Log para verificar o valor de nome_cargo

            # Atualiza o dicionário de cargos
            cargos_dict[nome] = {
                'valor_hora_base': data['valor_hora_base'],
                'valor_hora_extra_um': data['valor_hora_extra_um'],
                'valor_hora_extra_dois': data['valor_hora_extra_dois'],
                'repouso_remunerado': data['repouso_remunerado'],
                'adicional_noturno': data['adicional_noturno'],
                'desconto_inss': data['desconto_inss'],
                'desconto_refeicao': data['desconto_refeicao'],
                'desconto_transporte': data['desconto_transporte'],
                'pagamento_fgts': data['pagamento_fgts'],
                'valor_decimo_terceiro': data['valor_decimo_terceiro'],
                'valor_ferias': data['valor_ferias'],
                'valor_um_terco_ferias': data['valor_um_terco_ferias']
            }
            
            # Salva os cargos no arquivo
            CriarCargo.salvar_cargos(cargos_dict)
            return jsonify({"message": "Cargo cadastrado com sucesso!"}), 201
        
        except Exception as e:
            print(f"Erro ao cadastrar cargo: {e}")
            return jsonify({"message": "Erro ao cadastrar cargo!"}), 500

    elif request.method == 'GET':
        return jsonify(cargos_dict)

   
 # Metodo criar funcionario e o gatilho para gerar o olerite
@app.route('/api/criar_funcionario', methods=['POST'])
def criar_funcionario():
        app.logger.info(f"Headers: {request.headers}")
        app.logger.info(f"Data: {request.data}")
        
        data = request.json 
        
        #1 logg
        app.logger.info(f"Dados recebidos: {data}")

        required_fields = [ 'data_inicio','data_fim','nome_funcionario', 'cargo_funcionario', 'horas_trabalhadas','repouso_remunerado', 'horas_extras_um', 'horas_extras_dois', 'horas_noturnas', 'desc_refeicao', 'correcao_positiva', 'correcao_negativa']
        
        # Verifica se os dados obrigatórios estão presentes
        if not data or any(field not in data for field in required_fields):
            #Loggs
            app.logger.info(f"Dados recebidos: {data}")
            app.logger.error('Dados obrigatórios faltando: %s', data)
            return jsonify({'error': 'Dados obrigatórios faltando!'}), 400
        
            # Validação de data
        try:
            data['data_inicio'] = datetime.strptime(data['data_inicio'], '%d-%m-%Y').date()
            data['data_fim'] = datetime.strptime(data['data_fim'], '%d-%m-%Y').date()
        except ValueError:
            app.logger.error("Erro na validação das datas.")
            return jsonify({'error': 'Datas devem estar no formato DD-MM-YYYY!'}), 400


        # Converte valores de horas para float
        try:
            for field in ['horas_trabalhadas', 'horas_extras_um', 'horas_extras_dois', 'horas_noturnas', 'repouso_remunerado', 'desc_refeicao', 'correcao_positiva', 'correcao_negativa']:
                data[field] = float(data[field])
        except ValueError as e:
            app.logger.error(f"Erro ao converter valores: {e}")
            return jsonify({'error': 'Valores de horas devem ser numéricos!'}), 400

        cargo_id = data['cargo_funcionario']
        cargo = cargos_dict.get(cargo_id)

        if not cargo:
            return jsonify({'error': 'Cargo não encontrado!'}), 404   

        # Cria o objeto funcionario com base nos dados recebidos
        funcionario = Sub_total_um(data['nome_funcionario'], cargo_id, data['data_inicio'], data['data_fim'])

        # Adicionando as horas e outros dados   
        funcionario.adicionar_horas_trabalhadas(data['horas_trabalhadas'])
        funcionario.adicionar_horas_repouso(data['repouso_remunerado'])
        funcionario.adicionar_horas_noturnas(data['horas_noturnas'])
        funcionario.adicionar_horas_extras_um(data['horas_extras_um'])
        funcionario.adicionar_horas_extras_dois(data['horas_extras_dois'])
        funcionario.adicionar_desc_refeicao(data['desc_refeicao']) 
        funcionario.adicionar_correcao_positiva(data['correcao_positiva']) 
        funcionario.adicionar_correcao_negativa(data['correcao_negativa']) 
         

        # Gerar o olerite
        olerite = Gerar_olerite(funcionario)
        buffer =   olerite.gerar_sub_um()
        
        return send_file(buffer, as_attachment=True, download_name='olerite.pdf', mimetype='application/pdf')

    
@app.route('/api/cargos/<cargo_id>', methods=['GET'])
def get_cargo(cargo_id):
        # Supondo que você tenha um dicionário que armazena os cargos
    global cargos_dict 
    cargo = cargos_dict.get(cargo_id)

    if cargo:
        return jsonify(cargo)
    else:
        return jsonify({'error': 'Cargo não encontrado!'}), 404



#Novo- Criar cargo 



if __name__ == '__main__':
    app.run(debug=True, port=5000)