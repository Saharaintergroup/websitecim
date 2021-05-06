# -*- coding: utf-8 -*-
from odoo import api, fields, models, _, tools
from odoo.osv import expression
from odoo.exceptions import UserError, ValidationError


class CompanyPartners(models.Model):
    _name = "company.partners"
    _description = "List of Partners"

    name = fields.Char(string='Name', required=True, translate=True)
    image = fields.Image("Logo")
    description = fields.Html(string='Description', required=True, translate=True)
    url = fields.Char('Link to website')
    open_details_in = fields.Selection(
        [('popup', 'Popup'), ('page', 'Page'), ('external_url', 'External url')],
        string='Open details in',
        default='popup')
    external_url = fields.Char()