from odoo import http, models, fields, _
from odoo.http import request


class MediaCenter(http.Controller):
    @http.route(['/media-center', '/media-center/page/<int:page>'], type='http', auth="public",
                website=True)
    def media_center_page(self, page=0, **kw):
        top_news = request.env['news'].sudo().search([('is_important', '=', True)], limit=5)
        most_popular = request.env['news'].sudo().search([('is_most_traded', '=', True)])
        total = most_popular.sudo().search_count([('is_most_traded', '=', True)])
        pager = request.website.pager(
            url='/media-center',
            total=total,
            page=page,
            step=10,
        )
        offset = pager['offset']
        most_popular = most_popular[offset: offset + 10]
        data = {'top_news': top_news, 'most_popular': most_popular, 'pager': pager}
        return http.request.render('theme_cim.media_center', data)

    @http.route([
        '''/media-center/<model("news"):news>''',
    ], type='http', auth="public", website=True, sitemap=True)
    def media_center_post(self, news, enable_editor=None, **post):
        return http.request.render('theme_cim.media_center_post_page', {'record': news})
