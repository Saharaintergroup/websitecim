from odoo import http, models, fields, _
from odoo.http import request


class NumberingModels(http.Controller):
    @http.route(['/numbering-and-added-services', '/numbering-and-added-services/page/<int:page>'], type='http', auth="public",
                website=True)
    def numbering_models_page(self, page=0, **kw):
        numbering_models = request.env['numbering.models'].sudo().search([])
        total = numbering_models.sudo().search_count([])
        pager = request.website.pager(
            url='/decisions',
            total=total,
            page=page,
            step=10,
        )
        offset = pager['offset']
        numbering_models = numbering_models[offset: offset + 10]
        data = {'numbering_models': numbering_models, 'pager': pager}
        return http.request.render('theme_cim.numbering_and_added_services_page', data)
