from odoo import http, models, fields, _
from odoo.http import request

class ExecutiveCrew(http.Controller):
    @http.route(['/executive-crew'], type='http', auth="public", website=True)
    def teams(self, **kw):
        data = {'teams': request.env['teams.teams'].search([('is_president', '=', False)]),
                'president': request.env['teams.teams'].search([('is_president', '=', True)])}
        return http.request.render('theme_cim.executive_crew_page', data)