from odoo import fields, models, api, _
import logging

_logger = logging.getLogger(__name__)

class ResPartnerCustom(models.Model):
    _inherit = "res.users"

    # _allss_fornecedor = fields.Char("Fornecedor")
