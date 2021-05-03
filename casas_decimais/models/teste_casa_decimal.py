from odoo import fields, models, api, _
import logging

_logger = logging.getLogger(__name__)

class ResPartnerCustom(models.Model):
    _inherit = "account.tax"

    # currency_id = fields.Many2one("res.currency", related="company_id.currency_id")
    amount = fields.Float('Montante', default=1, store=True, digits=(12,11))

class ResPartnerCustom(models.Model):
    _inherit = "product.pricelist"

    price_discount = fields.Float('Desconto', default=1, store=True, digits=(12,11))