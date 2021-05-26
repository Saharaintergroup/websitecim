# -*- coding: utf-8 -*-
from odoo import api, fields, models, _, tools


class CommonQuestions(models.Model):
    _name = "common.questions"
    _description = "Common Questions"
    # name = fields.Char(string="السؤال", readonly=True, required=True, copy=False, default='New')
    number = fields.Integer('سؤال', required=True)
    question = fields.Char(string="السؤال", required=True, translate=True)
    answer = fields.Html(string='الجواب', required=True, translate=True)

    # @api.model
    # def create(self, vals):
    #     if vals.get('name', 'New') == 'New':
    #         vals['name'] = self.env['ir.sequence'].next_by_code(
    #             'common.questions') or 'New'
    #     result = super(CommonQuestions, self).create(vals)
    #     return result