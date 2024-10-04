from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib.units import mm
from io import BytesIO
from gerar_sub_total_um import Sub_total_um

class Gerar_olerite:
    def __init__(self, funcionario):
        self.funcionario = funcionario

    def gerar_sub_um(self):
        
        total_pagamento = Sub_total_um.calcular_pagamento_um(self.funcionario)
        buffer = BytesIO()
        doc = SimpleDocTemplate(buffer, pagesize=A4)

        # Cabeçalho
        elements = []
        self._draw_header(elements)

        # Conteúdo
        content = self._prepare_content(total_pagamento)
        table = self._create_table(content)
        elements.append(table)

        # Rodapé
        self._draw_footer(elements)

        doc.build(elements)
        buffer.seek(0)
        return buffer

    def _draw_header(self, elements):
        header = [
            ["RECEBI DE CONSTRUMAQUE LTDA.", "", ""],
            ["Data: 00/00/0000", "", ""],
            ["Período: 00/00/0000 a 00/00/0000", "", ""]
        ]
        header_table = Table(header)
        header_table.setStyle(TableStyle([('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
                                           ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                                           ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'),
                                           ('FONTSIZE', (0, 0), (-1, -1), 16)]))
        elements.append(header_table)

    def _prepare_content(self, total_pagamento):
        return [
            [f"NOME DO FUNCIONARIO", self.funcionario.nome, ""],
            [f"CARGO", self.funcionario.nome_cargo, ""],
            [f"HORAS TRABALHADAS", f"{self.funcionario.horas_trabalhadas:.2f} X {self.funcionario.cargo['valor_hora_base']:.2f}", f"= {total_pagamento['pagamento_base']:.2f}"],
            [f"REPOUSO REMUNERADO", f"{self.funcionario.repouso_remunerado:.2f} X {self.funcionario.cargo['repouso_remunerado']:.2f}", f"= {total_pagamento['pagamento_folga_remunerada']:.2f}"],
            [f"HORAS EXTRAS DE 50%", f"{self.funcionario.horas_extras_um:.2f} X {self.funcionario.cargo['valor_hora_extra_um']:.2f}", f"= {total_pagamento['pagamento_horas_extras_um']:.2f}"],
            [f"HORAS EXTRAS DE 100%", f"{self.funcionario.horas_extras_dois:.2f} X {self.funcionario.cargo['valor_hora_extra_dois']:.2f}", f"= {total_pagamento['pagamento_horas_extras_dois']:.2f}"],
            [f"ADICIONAL NOTURNO", f"{self.funcionario.horas_noturnas:.2f} X {self.funcionario.cargo['adicional_noturno']:.2f}", f"= {total_pagamento['pagamento_adicional_noturno']:.2f}"],
            [f"SUB-TOTAL 1", f"{total_pagamento['sub_total_um']:.2f}", ""],
            [f"PAGTO. FÉRIAS ({self.funcionario.cargo['valor_ferias']:.2f}%)", f"{total_pagamento['sub_total_um_um']:.2f}", ""],
            [f"PAGTO. 1/3 FÉRIAS ({self.funcionario.cargo['valor_um_terco_ferias']:.2f}%)", f"{total_pagamento['sub_total_um_dois']:.2f}", ""],
            [f"PAGTO. 13° SALÁRIO ({self.funcionario.cargo['valor_decimo_terceiro']:.2f}%)", f"{total_pagamento['sub_total_um_tres']:.2f}", ""],
            [f"SUB-TOTAL 2", f"{total_pagamento['sub_total_dois']:.2f}", ""],
            [f"PAGTO. FGTS ({self.funcionario.cargo['pagamento_fgts']:.2f}%) (+)", f"{total_pagamento['sub_total_dois_cinco']:.2f}", ""],
            [f"PAGTO. INSS ({self.funcionario.cargo['desconto_inss']:.2f}%) (-)", f"{total_pagamento['sub_total_dois_seis']:.2f}", ""],
            [f"DESCO. REFEIÇÃO (-)", f"{total_pagamento['sub_total_dois_sete']:.2f}", ""],
            [f"DESCO VAL TRANSPORTE (-)", f"{total_pagamento['sub_total_dois_oito']:.2f}", ""],
            [f"SALDO A RECEBER", f"{total_pagamento['sub_total_tres']:.2f}", ""]
        ]

    def _create_table(self, content):
        table = Table(content)
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('ALIGN', (1, 0), (-1, -1), 'RIGHT'),
            ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
            ('FONTSIZE', (0, 0), (-1, -1), 12),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('GRID', (0, 0), (-1, -1), colors.black)
        ]))
        return table

    def _draw_footer(self, elements):
        footer = [
            ["Este documento é gerado eletronicamente e não requer assinatura.", "", ""]
        ]
        footer_table = Table(footer)
        footer_table.setStyle(TableStyle([('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                                           ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
                                           ('FONTSIZE', (0, 0), (-1, -1), 10)]))
        elements.append(footer_table)
