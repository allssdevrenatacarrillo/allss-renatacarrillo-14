from odoo import fields, models, api, _
import logging

_logger = logging.getLogger(__name__)

class ResPartnerCustom(models.Model):
    _inherit = "res.partner"

    currency_id = fields.Many2one("res.currency", related="company_id.currency_id")
    # GRUPO: CLIENTE
    _allss_fornecedor = fields.Char("Fornecedor")
    _allss_titular_inst = fields.Char("Copiar Cliente para Titular da Instação?")
    _allss_nome = fields.Char("Nome")
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
    
    # GRUPO: DADOS PARA DIMENSIONAMENTO
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

    
