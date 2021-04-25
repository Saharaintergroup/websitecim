# -*- coding: utf-8 -*-
from odoo import api, fields, models, _, tools
from odoo.osv import expression
from odoo.exceptions import UserError, ValidationError


class WebsiteSliderHome(models.Model):
    _name = "website.slider.home"
    _description = "Website Slider Home"

    name = fields.Char(string='Title', required=True, translate=True)
    description = fields.Text(string='Description', required=True, translate=True)
    url = fields.Char('Button url')
    image = fields.Image("Background Image")
