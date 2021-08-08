from odoo import http, models, fields, _
from odoo.http import request


class Strategy(http.Controller):
    @http.route(['/strategy', '/strategy/page/<int:page>'], type='http', auth="public",
                website=True)
    def strategy_page(self, page=0, **kw):
        strategy = request.env['strategy'].sudo().search([])
        reports = request.env['reports'].sudo().search([])
        total = strategy.sudo().search_count([])
        pager = request.website.pager(
            url='/strategy',
            total=total,
            page=page,
            step=10,
        )
        offset = pager['offset']
        strategy = strategy[offset: offset + 10]
        data = {'strategy': strategy, 'reports': reports, 'pager': pager}
        return http.request.render('theme_cim.strategy_page', data)
