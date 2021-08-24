from odoo import http, models, fields, _
from odoo.http import request


class Decisions(http.Controller):
    @http.route(['/decisions/<int:decision_type_id>', '/decisions/<int:decision_type_id>/page/<int:page>'], type='http', auth="public",
                website=True)
    def decisions_page(self, decision_type_id=False, page=0, **kw):
        decisions = request.env['decisions'].sudo().search([('category_id','=',decision_type_id)])
        total = decisions.sudo().search_count([])
        pager = request.website.pager(
            url='/decisions',
            total=total,
            page=page,
            step=10,
        )
        offset = pager['offset']
        decisions = decisions[offset: offset + 10]
        data = {'decisions': decisions, 'pager': pager}
        return http.request.render('theme_cim.decisions_page', data)
