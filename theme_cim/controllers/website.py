from odoo import http, models, fields, _
from odoo.http import request
from odoo.addons.website.controllers.main import Website


class Website(Website):
    @http.route(auth='public')
    def index(self, **kw):
        super(Website, self).index(**kw)
        data = {'slider_home': request.env['slider.home'].search([]),
                'ticker_news': request.env['ticker.news'].search([]),
                'partners_logo': request.env['partners.logo'].search([])}
        return http.request.render('theme_cim.new_homepage', data)