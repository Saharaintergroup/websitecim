from odoo import http, models, fields, _
from odoo.http import request


class EgovernmentFiles(http.Controller):
    @http.route(['/electronic-government', '/electronic-government/page/<int:page>'], type='http', auth="public",
                website=True)
    def electronic_government_page(self, page=0, **kw):
        egovernment_files = request.env['egovernment.files'].sudo().search([])
        total = egovernment_files.sudo().search_count([])
        pager = request.website.pager(
            url='/electronic-government',
            total=total,
            page=page,
            step=10,
        )
        offset = pager['offset']
        egovernment_files = egovernment_files[offset: offset + 10]
        data = {'egovernment_files': egovernment_files, 'pager': pager}
        return http.request.render('theme_cim.electronic_government_page', data)
