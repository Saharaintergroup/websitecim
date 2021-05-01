from odoo import http, models, fields, _
from odoo.http import request
from odoo.addons.http_routing.models.ir_http import slug


class Announcements(http.Controller):
    @http.route(['/executive-crew'], type='http', auth="public", website=True)
    def teams(self, **kw):
        data = {'teams': request.env['teams.teams'].search([('is_president', '=', False)]),
                'president': request.env['teams.teams'].search([('is_president', '=', True)])}
        return http.request.render('theme_cim.executive_crew_page', data)

    @http.route(['/public-announcements', '/public-announcements/page/<int:page>'], type='http', auth="public",
                website=True)
    def public_announcements(self, page=0, **kw):
        public_announcements = request.env['public.announcements'].sudo().search([])
        total = public_announcements.sudo().search_count([])
        pager = request.website.pager(
            url='/public-announcements',
            total=total,
            page=page,
            step=9,
        )
        offset = pager['offset']
        public_announcements = public_announcements[offset: offset + 9]
        data = {'public_announcements': public_announcements, 'pager': pager, }
        return http.request.render('theme_cim.public_announcements_page', data)

    @http.route(['/bids', '/bids/page/<int:page>'], type='http', auth="public",
                website=True)
    def bids(self, page=0, **kw):
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
        attachment_data = request.env['ir.attachment'].sudo().search([('res_model', '=', 'bids'), ('res_id', 'in', bids.ids)])
        return http.request.render('theme_cim.bids_post_page',
                                   {'record': bids, 'attachment_data': attachment_data})
