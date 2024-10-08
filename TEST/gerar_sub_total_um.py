from criar_cargo import CriarCargo

cargos_dict = CriarCargo.carregar_cargos()

class Sub_total_um:
    def __init__(self, nome, nome_cargo,data_inicio,data_fim):
        self.data_inicio=data_inicio
        self.data_fim=data_fim
        self.nome = nome
        self.nome_cargo = nome_cargo
        self.horas_trabalhadas = 0
        self.horas_extras_um = 0
        self.horas_extras_dois = 0
        self.horas_noturnas = 0
        self.repouso_remunerado = 0
        self.valor_ferias=0
        self.desc_refeicao = 0
        self.correcao_positiva=0
        self.correcao_negativa=0
        

    
    def adicionar_horas_trabalhadas(self, horas):
        self.horas_trabalhadas += horas
        
    def adicionar_horas_repouso(self, horas):
        self.repouso_remunerado += horas    
        
    def adicionar_horas_extras_um(self, horas):
        self.horas_extras_um += horas   # 50%
    
    def adicionar_horas_extras_dois(self, horas):
        self.horas_extras_dois += horas    #100%

    def adicionar_horas_noturnas(self, horas):
        self.horas_noturnas += horas 
    
    def adicionar_adiantamento_salarial(self,valor):
        self.adiantamento_sal += valor
        
    def adicionar_pagamento_ferias(self,valor):
        self.valor_ferias += valor
        
    def adicionar_desc_refeicao(self,valor):
        self.desc_refeicao  += valor        
        
    def adicionar_correcao_positiva(self,valor):
        self.correcao_positiva += valor        
        
    def adicionar_correcao_negativa(self,valor):
        self.correcao_negativa += valor         
        
        
    def valida_cargo(self):
        print(f"Cargos disponíveis: {list(cargos_dict.keys())}")
        cargo_normalizado = self.nome_cargo.strip().lower()
        # Normaliza o dicionário de cargos para comparação
        cargos_dict_normalizado = {k.strip().lower(): v for k, v in cargos_dict.items()}
        
        if cargo_normalizado in cargos_dict_normalizado:
            self.cargo = cargos_dict_normalizado[cargo_normalizado]  # Armazena o objeto Cargo
        else:
            print("Cargo não encontrado!")
            return False  # Retorna False se não encontrar o cargo
        return True  # Retorna True se encontrar o cargo
    
    def calcular_pagamento_um(self):
        if not self.valida_cargo():  # Verifica se o cargo é válido
            return 0  # Se não for válido, retorna 0
        
        valor_hora_base = self.cargo['valor_hora_base']
        valor_repouso_remunerado = self.cargo['repouso_remunerado']
        valor_hora_extra_um = self.cargo['valor_hora_extra_um']
        valor_hora_extra_dois = self.cargo['valor_hora_extra_dois']
        adicional_noturno = self.cargo['adicional_noturno']
        valor_ferias = self.cargo['valor_ferias']
        valor_antecipa_ferias = self.cargo['valor_um_terco_ferias']
        valor_decimo_terceito = self.cargo['valor_decimo_terceiro']
        pagamento_fgts = self.cargo['pagamento_fgts']
        desconto_inss = self.cargo['desconto_inss']
        desconto_refeicao = self.cargo['desconto_refeicao']
        desconto_transporte = self.cargo['desconto_transporte']
            
        #SUB-TATAL 1
        pagamento_base = self.horas_trabalhadas * valor_hora_base
        pagamento_horas_extras_um = self.horas_extras_um * valor_hora_extra_um
        pagamento_horas_extras_dois = self.horas_extras_dois * valor_hora_extra_dois
        pagamento_adicional_noturno = self.horas_noturnas * adicional_noturno
        pagamento_folga_remunerada = self.repouso_remunerado * valor_repouso_remunerado
        
    
        
        sub_total_um = (pagamento_base + 
                        pagamento_horas_extras_um +
                        pagamento_horas_extras_dois +
                        pagamento_adicional_noturno + 
                        pagamento_folga_remunerada) 
        #SUB-TOTAL 2
        sub_total_um_um = sub_total_um * valor_ferias /100
        sub_total_um_dois = sub_total_um* valor_antecipa_ferias /100 #1/3 ferias
        sub_total_um_tres = sub_total_um * valor_decimo_terceito /100
        #sub_total_um_quantro =  self.adiantamento_sal * valor_antecipa_salario #
        sub_total_um_cinco = sub_total_um  * (pagamento_fgts /100)
        
        sub_total_dois =(sub_total_um + sub_total_um_um + sub_total_um_dois + sub_total_um_tres+ sub_total_um_cinco)
        
        #SUB-TOTAL 3
        
        sub_total_dois_seis = sub_total_dois * (desconto_inss/100)
        sub_total_dois_sete = self.desc_refeicao * desconto_refeicao
        sub_total_dois_oito = desconto_transporte
        sub_total_dois_nove = self.correcao_positiva
        sub_total_dois_dez = self.correcao_negativa
        
        sub_total_tres =(sub_total_dois  - sub_total_dois_seis - sub_total_dois_sete - sub_total_dois_oito + sub_total_dois_nove - sub_total_dois_dez)
        
        
        return {
        'sub_total_um': sub_total_um,
        'sub_total_dois': sub_total_dois,
        'sub_total_tres': sub_total_tres,
        'pagamento_base': pagamento_base,
        'pagamento_horas_extras_um': pagamento_horas_extras_um,
        'pagamento_horas_extras_dois': pagamento_horas_extras_dois,
        'pagamento_adicional_noturno': pagamento_adicional_noturno,
        'pagamento_folga_remunerada': pagamento_folga_remunerada,
        'sub_total_um_um' : sub_total_um_um,
        'sub_total_um_dois' : sub_total_um_dois,
        'sub_total_um_tres' : sub_total_um_tres,
        'sub_total_um_cinco' : sub_total_um_cinco,
        'sub_total_dois_seis' : sub_total_dois_seis,
        'sub_total_dois_sete' : sub_total_dois_sete,
        'sub_total_dois_oito' : sub_total_dois_oito,
        'sub_total_dois_nove' : sub_total_dois_nove,
        'sub_total_dois_dez' : sub_total_dois_dez
        
    }
    
    