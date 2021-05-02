# -*- coding: utf-8 -*-
from odoo import api, fields, models, _, tools

class Jobs(models.Model):
    _name = "jobs"
    _description = "Jobs"

    name = fields.Char(string="Title", required=True, translate=True)
    description = fields.Text(string='Description', required=True, translate=True)
    image = fields.Image("Photo")
    department_id = fields.Many2one('jobs.department', 'Department')

class JobsDepartment(models.Model):
    _name = "jobs.department"
    _description = "Department"

    name = fields.Char('Department Name', required=True)