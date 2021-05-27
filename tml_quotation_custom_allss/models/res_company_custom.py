from odoo import fields, models, api

class HrEmployeeCustom(models.Model):
    _inherit = 'res.company'

    _allss_cnpj = fields.Char("CNPJ")