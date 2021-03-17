from odoo import fields, models, api, _
import logging

_logger = logging.getLogger(__name__)

class ResPartnerCustom(models.Model):
    _inherit = "res.partner"

    currency_id = fields.Many2one("res.currency", related="company_id.currency_id")
    # _allss_teste = fields.Char("TESTE")
    # _allss_wage = fields.Monetary("Salário") 
    # _allss_health_insurance = fields.Boolean("Convênio Médico")
    # _allss_date_exped_cnh = fields.Date("Data de Expedição")
    # _allss_sheet = fields.Integer("Folha/Ficha")
    
