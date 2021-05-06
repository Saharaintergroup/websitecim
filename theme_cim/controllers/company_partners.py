from odoo import http, models, fields, _
from odoo.http import request


class CompanyPartners(http.Controller):

    @http.route([
        '''/company_partners/<model("company.partners"):partner>''',
    ], type='http', auth="public", website=True, sitemap=True)
    def company_partners_post(self, partner, enable_editor=None, **post):
        print('---------------company_partners-----------------------------')
        return http.request.render('theme_cim.company_partners_post_page',
                                   {'partner': partner})

