from odoo import fields, models, api


class Statistics(models.Model):
    _name = 'statistics'
    _description = 'Statistics'

    name = fields.Char("الوصف")
    value = fields.Integer("القيمة(%)")
