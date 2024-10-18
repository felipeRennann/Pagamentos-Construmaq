from flask import Flask, request, jsonify, render_template, send_file
from datetime import datetime
#from firebase_config import *  # Importa a configuração do Firebase
#from firebase_admin import firestore
from flask_cors import CORS
from gerar_sub_total_um import Sub_total_um
from gerador_olerite import Gerar_olerite
from criar_cargo import CriarFuncionario
import json
import os
import logging

# Configuração do logger
logging.basicConfig(level=logging.DEBUG , filename='app.log' )  # Defina o nível de log desejado
logger = logging.getLogger(__name__)



app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})

# Obtém uma referência ao Firestore
#db = firestore.client()

#Criação e exibição dos dados dos cagos na tela
class CriarFuncionario:
    
    #Carregar dados cadastrados na tabela no front
    @staticmethod
    def carregar_funcionarios():
        """Carrega os cargos do arquivo JSON."""
        if os.path.exists('funcionario.json'):
            with open('funcionario.json', 'r') as file:
                try:
                    return json.load(file)
                except json.JSONDecodeError:
                    # Em caso de erro no arquivo JSON, retorna um dicionário vazio.
                    print("Erro ao ler o arquivo funcionario.json. O arquivo está corrompido.")
                    return {}
        return {}

    @staticmethod
    def salvar_cargos(funcionario_dict):
        """Salva os cargos no arquivo JSON."""
        with open('funcionario.json', 'w') as file:
            json.dump(funcionario_dict, file, indent=4)  # Adiciona indentação para legibilidade.

# Carrega cargos inicialmente
funcionario_dict = CriarFuncionario.carregar_funcionarios()


@app.route('/')
def index():
    """Renderiza a página inicial."""
    return render_template('index.html')


##Criação de Funcionario

@app.route('/api/funcionarios', methods=['GET', 'POST'])
def funcionarios():
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
                'nome_funcionario',
                'numero_cpf',
                'chave_pix',
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
            for field in required_fields[1:]:  # Ignora o primeiro campo 'nome_funcionario'
                if field in data:
                   if field in ['numero_cpf', 'chave_pix']:  # Esses campos devem ser string
                        data[field] = str(data[field])
                
                else:
                     
                  try:
                        data[field] = float(data[field])
                  except ValueError:
                        return jsonify({"message": f"Valor inválido para {field}!"}), 400
            
            # Remover espaços em branco e validar nome Funcionario
            nome = data['nome_funcionario'].strip()
            if not nome:
                return jsonify({"message": "O campo nome_funcionario não pode estar vazio!"}), 400
            
            print(f"Nome do Funcionario: '{nome}'")  # Log para verificar o valor de nome_cargo

            # Atualiza o dicionário de funcionarios
            funcionario_dict[nome] = {
                'numero_cpf': data['numero_cpf'],
                'chave_pix': data['chave_pix'],           
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
            CriarFuncionario.salvar_cargos(funcionario_dict)
            return jsonify({"message": "Funcionario cadastrado com sucesso!"}), 201
        
        except Exception as e:
            print(f"Erro ao cadastrar cargo: {e}")
            return jsonify({"message": "Erro ao cadastrar cargo!"}), 500

    elif request.method == 'GET':
        return jsonify(funcionario_dict)

#Editar Funcionario 

@app.route('/api/funcionario/<string:nomeFuncionario>', methods=['PUT'])
def editar_funcionario(nomeFuncionario):
    logger.debug(f'Tentando atualizar o funcionário: {nomeFuncionario}')
    # Verifica se o funcionário existe
    funcionarios_db = funcionario_dict
    
    logger.warning(f'Funcionário {nomeFuncionario} não encontrado')
    if nomeFuncionario not in funcionarios_db:
        
        return jsonify({'message': 'Funcionário não encontrado'}), 404

    # Obtém os dados do funcionário a partir da requisição
    data = request.json
    logger.debug(f'Dados recebidos para atualização: {data}')

    # Atualiza os dados do funcionário
    funcionarios_db[nomeFuncionario]['numero_cpf'] = data.get('cpf', funcionarios_db[nomeFuncionario]['numero_cpf'])
    funcionarios_db[nomeFuncionario]['chave_pix'] = data.get('chave_pix', funcionarios_db[nomeFuncionario]['chave_pix'])
    funcionarios_db[nomeFuncionario]['valor_hora_base'] = data.get('valor_hora_base', funcionarios_db[nomeFuncionario]['valor_hora_base'])
    funcionarios_db[nomeFuncionario]['valor_hora_extra_um'] = data.get('valor_hora_extra_um', funcionarios_db[nomeFuncionario]['valor_hora_extra_um'])
    funcionarios_db[nomeFuncionario]['valor_hora_extra_dois'] = data.get('valor_hora_extra_dois', funcionarios_db[nomeFuncionario]['valor_hora_extra_dois'])
    funcionarios_db[nomeFuncionario]['adicional_noturno'] = data.get('adicional_noturno', funcionarios_db[nomeFuncionario]['adicional_noturno'])
    funcionarios_db[nomeFuncionario]['repouso_remunerado'] = data.get('repouso_remunerado', funcionarios_db[nomeFuncionario]['repouso_remunerado'])
    funcionarios_db[nomeFuncionario]['valor_ferias'] = data.get('valor_ferias', funcionarios_db[nomeFuncionario]['valor_ferias'])
    funcionarios_db[nomeFuncionario]['valor_um_terco_ferias'] = data.get('valor_um_terco_ferias', funcionarios_db[nomeFuncionario]['valor_um_terco_ferias'])
    funcionarios_db[nomeFuncionario]['valor_decimo_terceiro'] = data.get('valor_decimo_terceiro', funcionarios_db[nomeFuncionario]['valor_decimo_terceiro'])
    funcionarios_db[nomeFuncionario]['pagamento_fgts'] = data.get('pagamento_fgts', funcionarios_db[nomeFuncionario]['pagamento_fgts'])
    funcionarios_db[nomeFuncionario]['desconto_inss'] = data.get('desconto_inss', funcionarios_db[nomeFuncionario]['desconto_inss'])
    funcionarios_db[nomeFuncionario]['desconto_refeicao'] = data.get('desconto_refeicao', funcionarios_db[nomeFuncionario]['desconto_refeicao'])
    funcionarios_db[nomeFuncionario]['desconto_transporte'] = data.get('desconto_transporte', funcionarios_db[nomeFuncionario]['desconto_transporte'])
     
    logger.info(f'Funcionário {nomeFuncionario} atualizado com sucesso: {funcionarios_db[nomeFuncionario]}')
    return jsonify({'message': 'Funcionário atualizado com sucesso', 'data': funcionarios_db[nomeFuncionario]}), 200



   
 # Metodo criar funcionario e o gatilho para gerar o olerite #
@app.route('/api/criar_recibo', methods=['POST'])
def criar_recibo():
        
        data = request.json 
        
        #1 logg
        app.logger.info(f"Dados recebidos pelo back: {data}")

        required_fields = [ 'data_inicio','data_fim','nome_cargo', 'name_funcionario', 'horas_trabalhadas','repouso_remunerado', 'horas_extras_um', 'horas_extras_dois', 'horas_noturnas', 'correcao_positiva', 'correcao_negativa']
        
        # Verifica se os dados obrigatórios estão presentes
        if not data or any(field not in data for field in required_fields):
            #Loggs
            
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
            for field in ['horas_trabalhadas', 'horas_extras_um', 'horas_extras_dois', 'horas_noturnas', 'repouso_remunerado', 'correcao_positiva', 'correcao_negativa']:
                data[field] = float(data[field])
        except ValueError as e:
            app.logger.error(f"Erro ao converter valores: {e}")
            return jsonify({'error': 'Valores de horas devem ser numéricos!'}), 400

        funcionario_id= data['name_funcionario']
        funcionario = funcionario_dict.get(funcionario_id)

        if not funcionario:
            return jsonify({'error': 'Funcionario não encontrado!'}), 404   

        # Cria o objeto funcionario com base nos dados recebidos
        
        data = request.get_json()  # Ou request.form se for um form HTML
        print(f"Dados da requisição: {data}")
        funcionario = Sub_total_um(data['nome_cargo'], funcionario_id, data['data_inicio'], data['data_fim'])

        # Adicionando as horas e outros dados   
        funcionario.adicionar_horas_trabalhadas(data['horas_trabalhadas'])
        funcionario.adicionar_horas_repouso(data['repouso_remunerado'])
        funcionario.adicionar_horas_noturnas(data['horas_noturnas'])
        funcionario.adicionar_horas_extras_um(data['horas_extras_um'])
        funcionario.adicionar_horas_extras_dois(data['horas_extras_dois'])
        funcionario.adicionar_correcao_positiva(data['correcao_positiva']) 
        funcionario.adicionar_correcao_negativa(data['correcao_negativa']) 
         

        # Gerar o olerite
        olerite = Gerar_olerite(funcionario)
        buffer = olerite.gerar_sub_um()
        
        return send_file(buffer, as_attachment=True, download_name='recibo.pdf', mimetype='application/pdf')

    
@app.route('/api/funcionarios/<funcionario_id>', methods=['GET'])
def get_funcionario(funcionario_id):
        # Supondo que você tenha um dicionário que armazena os cargos
    global funcionario_dict 
    funcionario = funcionario_dict.get(funcionario_id)

    if funcionario:
        return jsonify(funcionario)
    else:
        return jsonify({'error': 'funcionario não encontrado!'}), 404



#Editar Funcionario 

@app.route('/api/funcionarios/<int:id>', methods=['PUT'])
def update_funcionario(id):
    data = request.get_json()
    # Atualize os dados do funcionário no banco de dados
    return jsonify({'message': 'Funcionário atualizado com sucesso.'})




if __name__ == '__main__':
    app.run(debug=True, port=5000)