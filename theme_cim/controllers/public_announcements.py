from odoo import http, models, fields, _
from odoo.http import request

class PublicAnnouncements(http.Controller):
    @http.route(['/public-announcements', '/public-announcements/page/<int:page>'], type='http', auth="public",
                website=True)
    def public_announcements_page(self, page=0, **kw):
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

    @http.route([
        '''/public-announcements/<model("public.announcements"):public_announcements>''',
    ], type='http', auth="public", website=True, sitemap=True)
    def public_announcements_post(self, public_announcements, enable_editor=None, **post):
        return http.request.render('theme_cim.public_announcements_post_page',
                                   {'record': public_announcements})