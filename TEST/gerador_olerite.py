from gerar_sub_total_um import Sub_total_um


class Gerar_olerite:
    def __init__(self, funcionario):
        # Inicializa o cargo e o funcionário
        self.funcionario = funcionario
    
    def gerar_sub_um(self):
        pagamento = Sub_total_um
        total_pagamento = pagamento.calcular_pagamento_um(self.funcionario) 
        
        
        return  f'RECEBI DE CONSTRUMAQUE LTDA. A QUANTIA DE R$: {total_pagamento["sub_total_tres"]:.2f}\n' \
                f'PRESTAÇÃO DE SERVIÇOS NO PERIODO DE 00/00/0000 \n' \
                f'NOME DO FUNCIONARIO : {self.funcionario.nome} \n' \
                f'Cargo: {self.funcionario.nome_cargo}\n' \
                f'HORAS TRABALHADAS         :  {self.funcionario.horas_trabalhadas:.2f}  X   {self.funcionario.cargo["valor_hora_base"]:.2f}  =                {total_pagamento["pagamento_base"]:.2f}\n' \
                f'REPOUSO REMUNERADO    :    {self.funcionario.repouso_remunerado:.2f}  X   {self.funcionario.cargo["repouso_remunerado"]:.2f}  =                   {total_pagamento["pagamento_folga_remunerada"]:.2f}\n'\
                f'HORAS EXTRAS DE  50%      :    {self.funcionario.horas_extras_um:.2f}  X   {self.funcionario.cargo["valor_hora_extra_um"]:.2f}  =                   {total_pagamento["pagamento_horas_extras_um"]:.2f}\n'\
                f'HORAS EXTRAS DE  100%    :    {self.funcionario.horas_extras_dois:.2f}  X   {self.funcionario.cargo["valor_hora_extra_dois"]:.2f}  =                   {total_pagamento["pagamento_horas_extras_dois"]:.2f}\n'\
                f'ADICIONAL NOTURNO           :    {self.funcionario.horas_noturnas:.2f}  X   {self.funcionario.cargo["adicional_noturno"]:.2f}  =                   {total_pagamento["pagamento_adicional_noturno"]:.2f}\n'\
                f'       SUB-TOTAL 1                    :                                              {total_pagamento["sub_total_um"]:.2f}\n'\
                f'PAGTO. FERIAS ({self.funcionario.cargo["valor_ferias"]:.2f}%)         :                                               {total_pagamento["sub_total_um_um"]:.2f}\n'\
                f'PAGTO. 1/3 FERIAS ({self.funcionario.cargo["valor_um_terco_ferias"]:.2f}%)   :                                                 {total_pagamento["sub_total_um_dois"]:.2f}\n'\
                f'PAGTO. 13° SALARIO({self.funcionario.cargo["valor_decimo_terceiro"]:.2f}%) :                                                {total_pagamento["sub_total_um_tres"]:.2f}\n'\
                f'         SUB-TOTAL 2                  :                                               {total_pagamento["sub_total_dois"]:.2f}\n'\
                f'PAGTO. FGTS  ({self.funcionario.cargo["pagamento_fgts"]:.2f}%)(+)       :                                                {total_pagamento["sub_total_dois_cinco"]:.2f}\n'\
                f'PAGTO. INSS   ({self.funcionario.cargo["desconto_inss"]:.2f}%)(-)        :                                                {total_pagamento["sub_total_dois_seis"]:.2f}\n'\
                f'DESCO.  REFEIÇÃO    (-)        :                                                 {total_pagamento["sub_total_dois_sete"]:.2f}\n'\
                f'DESCO VAL TRANSPORT.(-)  :                                                  {total_pagamento["sub_total_dois_oito"]:.2f}\n'\
                f'        SALDO A RECEBER         :                                               {total_pagamento["sub_total_tres"]:.2f}\n'                  
                    
def __repr__(self):
        return f"Funcionario(nome='{self.nome}', cargo={self.nome_cargo}, hora_trabalhada={self.horas_trabalhadas},horas_extras_um={self.horas_extras_um},  horas_noturnas={self.horas_noturnas}, repouso_remunerado{self.repouso_remunerado})"