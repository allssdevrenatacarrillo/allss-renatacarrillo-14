from odoo import fields, models, api, _
import logging

_logger = logging.getLogger(__name__)

class ResPartnerCustom(models.Model):
    _inherit = "account.tax"

    amount_tax = fields.Float("Comissão")
    tax_id = fields.Many2many("Comissão")