# -*- coding: utf-8 -*-
from odoo import api, fields, models, _, tools
from odoo.osv import expression
from odoo.exceptions import UserError, ValidationError


class CompanyPartners(models.Model):
    _name = "company.partners"
    _description = "List of Partners"

    name = fields.Char(string='الإسم', required=True, translate=True)
    image = fields.Image("الشعار")
    description = fields.Html(string='الوصف', required=True, translate=True)
    url = fields.Char('رابط لموقع الويب')
    open_details_in = fields.Selection(
        [('popup', 'انبثاق'), ('page', 'صفحة جديدة'), ('external_url', 'رابط خارجي')],
        string='فتح التفاصيل في',
        default='popup')
    external_url = fields.Char("الرابط خارجي")