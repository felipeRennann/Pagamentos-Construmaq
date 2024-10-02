

class Cargo:
    def __init__(self, nome, valor_hora_base, valor_adicional_noturno, valor_hora_extra_um,
    valor_hora_extra_dois, valor_repouso_remunerado,valor_ferias, valor_antecipa_ferias, valor_decimo_terceiro, valor_antecipa_salario, 
    pagamento_fgts, desconto_inss, desconto_refeicao, desconto_transporte):
        self.nome = nome
        self.valor_hora_base = valor_hora_base
        self.valor_repouso_remunerado = valor_repouso_remunerado
        self.valor_hora_extra_um = valor_hora_extra_um
        self.valor_hora_extra_dois = valor_hora_extra_dois
        self.valor_adicional_noturno = valor_adicional_noturno 
        self.valor_ferias=valor_ferias
        self.valor_antecipa_ferias=valor_antecipa_ferias
        self.valor_decimo_terceiro=valor_decimo_terceiro
        self.valor_antecipa_salario=valor_antecipa_salario
        self.pagamento_fgts=pagamento_fgts
        self.desconto_inss=desconto_inss
        self.desconto_refeicao=desconto_refeicao
        self.desconto_transporte=desconto_transporte
        
    def to_dict(self):
        return {
            'valor_hora_base': self.valor_hora_base,
            'valor_hora_extra_um': self.valor_hora_extra_um,
            'valor_hora_extra_dois': self.valor_hora_extra_dois,
            'adicional_noturno': self.valor_adicional_noturno,
            'repouso_remunerado': self.valor_repouso_remunerado,
            'valor_ferias': self.valor_ferias,
            'valor_antecipa_ferias': self.valor_antecipa_ferias,
            'valor_decimo_terceiro': self.valor_decimo_terceiro,
            'valor_antecipa_salario': self.valor_antecipa_salario,
            'pagamento_fgts': self.pagamento_fgts,
            'desconto_inss': self.desconto_inss,
            'desconto_refeicao': self.desconto_refeicao,
            'desconto_transporte': self.desconto_transporte
        }
    
   

def __repr__(self):
        return (f"Cargo(nome='{self.nome}', valor_hora_base={self.valor_hora_base}, "
            f"repouso_remunerado={self.valor_repouso_remunerado}, valor_hora_extra_um={self.valor_hora_extra_um}, "
            f"valor_hora_extra_dois={self.valor_hora_extra_dois}, adicional_noturno={self.valor_adicional_noturno}, "
            f"valor_ferias={self.valor_ferias}, valor_antecipa_ferias={self.valor_antecipa_ferias}, "
            f"valor_decimo_terceiro={self.valor_decimo_terceiro}, valor_antecipa_salario={self.valor_antecipa_salario}, "
            f"pagamento_fgts={self.pagamento_fgts}, desconto_inss={self.desconto_inss}, "
            f"desconto_refeicao={self.desconto_refeicao}, desconto_transporte={self.desconto_transporte})")



