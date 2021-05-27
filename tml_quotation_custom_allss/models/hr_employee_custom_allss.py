from odoo import fields, models, api

class HrEmployeeCustom(models.Model):
    _inherit = 'hr.employee'

    _allss_prof_register = fields.Char("Registro Profissional")