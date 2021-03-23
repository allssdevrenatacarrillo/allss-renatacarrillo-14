from odoo import fields, models, api, _
import logging

_logger = logging.getLogger(__name__)

class ResPartnerCustom(models.Model):
    _inherit = "res.partner"

    currency_id = fields.Many2one("res.currency", related="company_id.currency_id")
    # GRUPO: CLIENTE
    _allss_fornecedor = fields.Char("Fornecedor")
    _allss_titular_inst = fields.Char("Copiar Cliente para Titular da Instação?")
    # _allss_nome = fields.Char("Nome")
    _allss_cpf = fields.Char("CPF do Cliente")
    _allss_cnpj = fields.Char("CNPJ do Cliente")
    _allss_gps = fields.Char("GPS")
    _allss_respon = fields.Char("Responsável")
    _allss_met_pag = fields.Char("Método de Pagamento")
    _allss_origem = fields.Char("Origem")
    # GRUPO: DADOS DA INSTALAÇÃO
    _allss_concessionaria = fields.Char("Concessionaria")
    _allss_nome_titular_inst = fields.Char("Nome Titular da Instalação")
    _allss_sobr_titular_inst = fields.Char("Sobrenome Titular da Instalação")
    _allss_cpf_inst = fields.Char("CPF da Instalação")
    _allss_cnpj_inst = fields.Char("CNPJ da Instalação")
    _allss_end_inst = fields.Char("Endereço da Instalação")
    _allss_city_inst = fields.Char("Cidade da Instalação")
    _allss_est_inst = fields.Char("Estado da Instalação")
    _allss_cep_inst = fields.Char("CEP da Instalação")
    _allss_tp_estab_inst = fields.Char("Tipo de Estabelecimento")
    _allss_unid_consum_inst = fields.Char("Unidade Consumidora")
    _allss_class_inst = fields.Char("Classe da Instalação")
    _allss_gps_inst = fields.Char("GPS da Instalação")
    _allss_obs_inst = fields.Char("Observações da Instalação")
    # GRUPO: DADOS PARA DIMENSIONAMENTO
    _allss_tp_telhado_dimen = fields.Char("Tipo de Telhado")
    _allss_md_consu_dimen = fields.Char("Média Consumo KWh")
    _allss_qtd_mes_dimen = fields.Char("Quantidade Meses KWh")
    _allss_consu_dimen_1 = fields.Char("Consumo KWh Mês 1")
    _allss_consu_dimen_2 = fields.Char("Consumo KWh Mês 2")
    _allss_consu_dimen_3 = fields.Char("Consumo KWh Mês 3")
    _allss_consu_dimen_4 = fields.Char("Consumo KWh Mês 4")
    _allss_consu_dimen_5 = fields.Char("Consumo KWh Mês 5")
    _allss_consu_dimen_6 = fields.Char("Consumo KWh Mês 6")
    _allss_consu_dimen_7 = fields.Char("Consumo KWh Mês 7")
    _allss_consu_dimen_8 = fields.Char("Consumo KWh Mês 8")
    _allss_consu_dimen_9 = fields.Char("Consumo KWh Mês 9")
    _allss_consu_dimen_10 = fields.Char("Consumo KWh Mês 10")
    _allss_consu_dimen_11 = fields.Char("Consumo KWh Mês 11")
    _allss_consu_dimen_12 = fields.Char("Consumo KWh Mês 12")
    # GRUPO: FOTOS DA INSTALAÇÃO
    # GRUPO: DOCUMENTOS DE PROJETO CONCESSIONÁRIA
    # GRUPO: FOTOS DOCUMENTOS PESSOA FÍSICA
    # GRUPO: DADOS DE FINANCIAMENTO
    # GRUPO: PEDIDOS DE COMPRA - NOTAS FISCAIS - BOLETOS
    # GRUPO: PEDIDOS DE VENDA - NOTAS FISCAIS - BOLETOS
    # GRUPO: DADOS DE MONITORAÇÃO




    # _allss_wage = fields.Monetary("Salário") 
    # _allss_health_insurance = fields.Boolean("Convênio Médico")
    # _allss_date_exped_cnh = fields.Date("Data de Expedição")
    # _allss_sheet = fields.Integer("Folha/Ficha")

    
