from odoo import http, models, fields, _
from odoo.http import request


class Bids(http.Controller):
    @http.route(['/bids', '/bids/page/<int:page>'], type='http', auth="public",
                website=True)
    def bids_page(self, page=0, **kw):
        bids = request.env['bids'].sudo().search([])
        total = bids.sudo().search_count([])
        pager = request.website.pager(
            url='/bids',
            total=total,
            page=page,
            step=9,
        )
        offset = pager['offset']
        bids = bids[offset: offset + 9]
        data = {'bids': bids, 'pager': pager, }
        return http.request.render('theme_cim.bids_page', data)

    @http.route([
        '''/bids/<model("bids"):bids>''',
    ], type='http', auth="public", website=True, sitemap=True)
    def bids_post(self, bids, enable_editor=None, **post):
        print('---------------test-----------------------------')
        attachment_data = request.env['ir.attachment'].sudo().search(
            [('res_model', '=', 'bids'), ('res_id', 'in', bids.ids)])
        return http.request.render('theme_cim.bids_post_page',
                                   {'record': bids, 'attachment_data': attachment_data})
