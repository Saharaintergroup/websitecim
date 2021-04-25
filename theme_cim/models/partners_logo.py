# -*- coding: utf-8 -*-
from odoo import api, fields, models, _, tools
from odoo.osv import expression
from odoo.exceptions import UserError, ValidationError


class WebsiteSliderHome(models.Model):
    _name = "partners.logo"
    _description = "Logo of Partners"

    name = fields.Char(string='Name', required=True, translate=True)
    image = fields.Image("Logo")
