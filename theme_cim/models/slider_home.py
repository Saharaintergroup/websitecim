# -*- coding: utf-8 -*-
from odoo import api, fields, models, _, tools
from odoo.osv import expression
from odoo.exceptions import UserError, ValidationError


class WebsiteSliderHome(models.Model):
    _name = "slider.home"
    _description = "Slider In Home Page"

    name = fields.Char(string='عنوان الخبر', required=True, translate=True)
    description = fields.Text(string='تفاصيل عن الخبر', required=True, translate=True)
    url = fields.Char('رابط الزر')
    image = fields.Image("صورة")
