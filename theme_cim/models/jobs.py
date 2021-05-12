# -*- coding: utf-8 -*-
from odoo import api, fields, models, _, tools
import base64


class Jobs(models.Model):
    _name = "jobs"
    _description = "Jobs"

    name = fields.Char(string="إسم الوظيفة", required=True, translate=True)
    description_primary = fields.Html(string='الوصف الأساسي', required=True, translate=True)
    description_secondary = fields.Html(string='وصف ثانوي', required=True, translate=True)
    must_be_available = fields.Html(string='يجب توافرها', required=True, translate=True)
    requirements = fields.Html(string='الحد الأدني من المتطلبات', required=True, translate=True)
    responsibilities = fields.Html(string='المسؤوليات', required=True, translate=True)
    image = fields.Image("صورة")
    department_id = fields.Many2one('jobs.department', 'القسم')
    no_of_recruitment = fields.Integer(string='الموظفون الجدد المتوقعون', copy=False,
                                       help='عدد الموظفين المتوقع توظيفهم', default=1)
    candidate_number = fields.Integer('عدد المرشح', compute='_compute_candidate_number')

    def _compute_candidate_number(self):
        candidate_data = self.env['jobs.candidate'].read_group([('res_id', 'in', self.ids)], ['res_id'], ['res_id'])
        candidate = dict((data['res_id'], data['res_id_count']) for data in candidate_data)
        for cond in self:
            cond.candidate_number = candidate.get(cond.id, 0)

    def action_get_candidate_view(self):
        self.ensure_one()
        res = self.env['ir.actions.act_window']._for_xml_id('theme_cim.jobs_candidate_action')
        res['domain'] = [('res_id', 'in', self.ids)]
        return res

    def _create_candidate(self, vals):
        vals['datas'] = base64.b64decode(vals.get('datas').read())
        vals['res_id'] = self.id
        res = self.env["jobs.candidate"].create(vals)
        return res


class JobsDepartment(models.Model):
    _name = "jobs.department"
    _description = "Department"

    name = fields.Char('إسم القسم', required=True)


class JobsDepartment(models.Model):
    _name = "jobs.candidate"
    _description = "Candidate"

    name = fields.Char('الإسم', required=True)
    email = fields.Char('البريد الإلكتروني', required=True)
    phone = fields.Char('الهاتف', required=True)
    description = fields.Text(string='الوصف', required=True, translate=True)
    datas = fields.Binary('السيرة الذاتية', attachment=True)
    res_id = fields.Integer('معرف الوظيفة ذات الصلة', index=True)
