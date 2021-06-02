from odoo import http, models, fields, _
from odoo.http import request
from odoo.addons.website.controllers.main import Website


class Website(Website):
    @http.route(auth='public')
    def index(self, **kw):
        """function home page"""
        super(Website, self).index(**kw)
        data = {'slider_home': request.env['news'].sudo().search([('in_slider','=',True)]),
                'ticker_news': request.env['news'].sudo().search([]),
                'company_partners': request.env['company.partners'].sudo().search([])}
        return http.request.render('theme_cim.new_homepage', data)
