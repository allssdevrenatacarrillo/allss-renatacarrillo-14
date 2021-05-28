from odoo import fields, models, api, _
import logging

_logger = logging.getLogger(__name__)

class ResPartnerCustom(models.Model):
    _inherit = "res.users"

    user_id = fields.Char("Vendedor")