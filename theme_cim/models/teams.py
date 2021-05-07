# -*- coding: utf-8 -*-
from odoo import api, fields, models, _, tools


class TeamsTeams(models.Model):
    _name = "teams.teams"
    _description = "Teams"
    name = fields.Char(string="Name", required=True, translate=True)
    job_position = fields.Char(string='Job Position', required=True, translate=True)
    image = fields.Image("Photo")
    is_president = fields.Boolean("Is President",default=False)

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
