from odoo import http, models, fields, _
from odoo.http import request


class CallCenter(http.Controller):
    @http.route(['/electronic-services-licenses', '/electronic-services-licenses/page/<int:page>'], type='http', auth="public",
                website=True)
    def call_center_page(self, page=0, **kw):
        call_center = request.env['call.center'].sudo().search([])
        total = call_center.sudo().search_count([])
        pager = request.website.pager(
            url='/electronic_services_licenses',
            total=total,
            page=page,
            step=10,
        )
        offset = pager['offset']
        call_center = call_center[offset: offset + 10]
        data = {'call_center': call_center, 'pager': pager}
        return http.request.render('theme_cim.electronic_services_licenses_page', data)

