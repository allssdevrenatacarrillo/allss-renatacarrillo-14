from odoo import fields, models, api, _
import logging

_logger = logging.getLogger(__name__)

class ResPartnerCustom(models.Model):
    _inherit = "res.users"

    currency_id = fields.Many2one("res.currency", related="company_id.currency_id")
    user_id = fields.Many2one("Vendedor")