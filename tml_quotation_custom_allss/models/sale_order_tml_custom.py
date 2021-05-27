from odoo import fields, models, api
import logging
_logger = logging.getLogger(__name__)

class SaleOrderTmlCustom(models.Model):
    _inherit = 'sale.order.template'

    _allss_logo = fields.Binary('Logo')
    _allss_banner = fields.Binary('Banner')
    _allss_presentation_text = fields.Html('Apresentação')
    _allss_details_text = fields.Html('Detalhamentos e Exclusões')
    _allss_links = fields.Html('Links e Catágolos')
    _allss_colors = fields.Selection([
        ('blue_yellow','Azul e Amarelo'),
        ('black_white','Preto e Branco')
    ])

class SaleOrderCustom(models.Model):
    _inherit = 'sale.order'

    _allss_signed_by = fields.Many2one('hr.employee', string='Assinado por')
    _allss_signed_on = fields.Date("Assinado em")
    _allss_representative_signature = fields.Char("Assinatura")

class SaleOrderLineCustom(models.Model):
    _inherit = 'sale.order.line'

    @api.onchange('product_id')
    def get_mrp_bom(self):
        mrp_bom = self.env['mrp.bom'].search([('product_tmpl_id', '=', self.product_id.id)])
        kit = []
        for product in mrp_bom:
            for line in product.bom_line_ids:
                prd_kit = f'{line.product_qty:.0f} {line.product_id.name}'
                kit.append(prd_kit)
            _logger.warning(f'************** BoM: {kit} **************')
            return kit
            break