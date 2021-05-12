# -*- coding: utf-8 -*-
from odoo import api, fields, models, _, tools


class TeamsTeams(models.Model):
    _name = "teams.teams"
    _description = "Teams"
    name = fields.Char(string="الإسم", required=True, translate=True)
    job_position = fields.Char(string='الوظيفة', required=True, translate=True)
    image = fields.Image("الصورة")
    is_president = fields.Boolean("هو الرئيس؟", default=False)

    def write(self, vals):
        if vals.get('is_president'):
            records = self.env['teams.teams'].search([('id', '!=', self.id), ('is_president', '=', True)])
            for rec in records:
                rec.write({'is_president': False})
        return super(TeamsTeams, self).write(vals)

    @api.model
    def create(self, vals):
        if vals.get('is_president'):
            records = self.env['teams.teams'].search([('is_president', '=', True)])
            for rec in records:
                rec.write({'is_president': False})
        return super(TeamsTeams, self).create(vals)
