# -*- coding: utf-8 -*-
from odoo import api, fields, models, _, tools

class Jobs(models.Model):
    _name = "jobs"
    _description = "Jobs"

    name = fields.Char(string="Title", required=True, translate=True)
    description_primary = fields.Html(string='Description primary', required=True, translate=True)
    description_secondary = fields.Html(string='Description secondary', required=True, translate=True)
    must_be_available = fields.Html(string='Must be available', required=True, translate=True)
    requirements = fields.Html(string='Requirements', required=True, translate=True)
    responsibilities = fields.Html(string='Responsibilities', required=True, translate=True)
    image = fields.Image("Photo")
    department_id = fields.Many2one('jobs.department', 'Department')
    no_of_recruitment = fields.Integer(string='Expected New Employees', copy=False,
                                       help='Number of new employees you expect to recruit.', default=1)

class JobsDepartment(models.Model):
    _name = "jobs.department"
    _description = "Department"

    name = fields.Char('Department Name', required=True)