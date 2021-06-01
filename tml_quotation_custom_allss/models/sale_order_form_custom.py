from odoo import fields, models, api
import logging
_logger = logging.getLogger(__name__)

class SaleOrderFormCustom(models.Model):
    _inherit = 'sale.order.line'

    acres_ids = fields.Many2many('account.tax', 'account_tax_acres', string='Acréscimos')
    comiss_ids = fields.Many2many('account.tax', 'account_tax_comiss', string='Comissão')
    is_serv = fields.Boolean(default=False, string='Serviço')


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    acres_total = fields.Monetary(string='Acréscimos', compute='product_id_change')
    comiss_total = fields.Monetary(string='Comissão')

    @api.onchange('order_line')
    def product_id_change(self):
        acres_line = 0
        comiss_line = 0
        for line in self.order_line:
            for acres in line.acres_ids:
                acres_line += line.price_unit / 100 * acres.amount * line.product_uom_qty
            for comiss in line.comiss_ids:
                comiss_line += line.purchase_price / 100 * comiss.amount * line.product_uom_qty
            if line.is_serv:
                _logger.warning("******* > ____________IS SERVICE____________ <***********")
                self.amount_total - line.price_total

        self.update({
            'acres_total': acres_line,
            'comiss_total': comiss_line,
            'amount_total': self.amount_total + acres_line + comiss_line,
        })

