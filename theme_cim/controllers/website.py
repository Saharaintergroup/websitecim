from odoo import http, models, fields, _
from odoo.http import request
from odoo.addons.website.controllers.main import Website


class Website(Website):
    @http.route(auth='public')
    def index(self, **kw):
        super(Website, self).index(**kw)
        data = {'slider': request.env['website.slider.home'].search([]), 'news': request.env['news.news'].search([]),
                'partners_logo': request.env['partners.logo'].search([])}
        return http.request.render('theme_cim.new_homepage', data)

    @http.route(['/executive-crew'], type='http', auth="public", website=True)
    def teams(self, **kw):
        data = {'teams': request.env['teams.teams'].search([('is_president', '=', False)]),
                'president': request.env['teams.teams'].search([('is_president', '=', True)])}
        return http.request.render('theme_cim.executive_crew_page', data)
