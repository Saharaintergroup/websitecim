# -*- coding: utf-8 -*-
from odoo import api, fields, models, _, tools
from odoo.osv import expression
from odoo.exceptions import UserError, ValidationError


class NewsNews(models.Model):
    _name = "news.news"
    _description = "Website Slider Home"
    name = fields.Char(string="Number", readonly=True, required=True, copy=False, default='New')
    description = fields.Text(string='Description', required=True, translate=True)

    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code(
                'self.news') or 'New'
        result = super(NewsNews, self).create(vals)
        return result
