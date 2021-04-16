from odoo import fields, models, api, _
import logging

_logger = logging.getLogger(__name__)

class ResPartnerCustom(models.Model):
    _inherit = "res.partner"

    currency_id = fields.Many2one("res.currency", related="company_id.currency_id")
    _allss_cnpj = fields.Char("CNPJ")
    _allss_insc_est = fields.Char("Inscrição Estadual")
    _allss_cnae = fields.Char("CNAE")
    # _allss_contrib = fields.Boolean("Contribuinte")
    _allss_contrib = fields.Selection([('sim', 'Sim'), ('não', 'Não')], string="Contribuinte?")
    _allss_bairro = fields.Char("Bairro")
    _allss_cod_mun_ibge = fields.Char("Cód. Município do IBGE")
    _allss_numb_1 = fields.Char("Nº")
    _allss_numb_2 = fields.Char("2º Nº")
    _allss_coordenador = fields.Char("Coordenador")