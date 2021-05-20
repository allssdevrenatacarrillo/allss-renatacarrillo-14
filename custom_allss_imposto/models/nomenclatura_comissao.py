from odoo import fields, models, api, _
import logging

_logger = logging.getLogger(__name__)

class ResPartnerCustom(models.Model):
    _inherit = "sale.order"

    amount_tax = fields.Float('Comissão', default=1, store=True)
    teste_teste = fields.Float("TESTE")