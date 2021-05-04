# -*- coding: utf-8 -*-
from odoo import api, fields, models, _, tools
import base64

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
    candidate_number = fields.Integer('Number of Candidate', compute='_compute_candidate_number')

    def _compute_candidate_number(self):
        candidate_data = self.env['jobs.candidate'].read_group([('res_id', 'in', self.ids)], ['res_id'], ['res_id'])
        candidate = dict((data['res_id'], data['res_id_count']) for data in candidate_data)
        for cond in self:
            cond.candidate_number = candidate.get(cond.id, 0)

    def action_get_candidate_view(self):
        self.ensure_one()
        res = self.env['ir.actions.act_window']._for_xml_id('theme_cim.jobs_candidate_action')
        res['domain'] = [('res_id', 'in', self.ids)]
        # res['context'] = {'default_res_model': 'jobs', 'default_res_id': self.id}
        return res

    def _create_candidate(self,vals):
        vals['datas'] = base64.b64decode(vals.get('datas').read())
        vals['res_id']=self.id
        print('-----candidate bien créer----------',vals)
        res = self.env["jobs.candidate"].create(vals)
        return res

class JobsDepartment(models.Model):
    _name = "jobs.department"
    _description = "Department"

    name = fields.Char('Department Name', required=True)

class JobsDepartment(models.Model):
    _name = "jobs.candidate"
    _description = "Candidate"

    name = fields.Char('Name', required=True)
    email = fields.Char('Email', required=True)
    phone = fields.Char('Phone', required=True)
    description = fields.Text(string='Description', required=True, translate=True)
    datas = fields.Binary('CV', attachment=True)
    res_id = fields.Integer('Related Job ID', index=True)