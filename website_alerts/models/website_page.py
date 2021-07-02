from odoo import fields, models, api


class WebsitePage(models.Model):
    _name = 'website.page'

    teste = fields.Char("CAMPO DE TESTE")