from odoo import http, models, fields, _
from odoo.http import request


class Decisions(http.Controller):
    @http.route(['/decisions', '/decisions/page/<int:page>'], type='http', auth="public",
                website=True)
    def decisions_page(self, page=0, **kw):
        decisions = request.env['decisions'].sudo().search([])
        total = decisions.sudo().search_count([])
        pager = request.website.pager(
            url='/decisions',
            total=total,
            page=page,
            step=9,
        )
        offset = pager['offset']
        decisions = decisions[offset: offset + 10]
        data = {'decisions': decisions, 'pager': pager}
        return http.request.render('theme_cim.decisions_page', data)
