from odoo import fields, models, api, _
import logging

_logger = logging.getLogger(__name__)

class ProjectCustom(models.Model):
    _inherit = "sale.order"

    user_id = fields.Many2one('res.users', string='Salesperson', index=True, track_visibility='onchange', track_sequence=2, default=lambda self: self.env.user)