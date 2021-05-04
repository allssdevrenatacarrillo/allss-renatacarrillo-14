from odoo import fields, models, api, _
import logging

_logger = logging.getLogger(__name__)

class ResPartnerCustom(models.Model):
    _inherit = "account.tax"

    amount = fields.Float('Montante', default=1, store=True, digits=(12,11))

class ResPartnerCustom(models.Model):
    _inherit = "product.pricelist.item"

    price_discount = fields.Float('Desconto', default=1, store=True, digits=(12,11))

class ResPartnerCustom(models.Model):
    _inherit = "product.template"

    list_price = fields.Float('Desconto', default=1, store=True, digits=(12,11))

class ResPartnerCustom(models.Model):
    _inherit = "product.template"

    standard_price = fields.Float('Desconto', default=1, store=True, digits=(12,11))