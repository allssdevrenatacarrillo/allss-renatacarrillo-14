from odoo import fields, models, api
import logging
_logger = logging.getLogger(__name__)

class PricelistItem(models.Model):
    _inherit = 'product.pricelist.item'

    base = fields.Selection([
        ('list_price', 'Sales Price'),
        ('standard_price', 'Cost'),
        ('pricelist', 'Other Pricelist'),
        ('amount_total','amount_total')], "Based on",
        default='list_price', required=True,
        help='Base price for computation.\n'
             'Sales Price: The base price will be the Sales Price.\n'
             'Cost Price : The base price will be the cost price.\n'
             'Other Pricelist : Computation of the base price based on another Pricelist.')

    