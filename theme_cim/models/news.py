# -*- coding: utf-8 -*-
from odoo import api, fields, models, _, tools
from odoo.osv import expression
from odoo.exceptions import UserError, ValidationError
from odoo.tools.translate import html_translate

class News(models.Model):
    _name = "news"
    _description = "News"

    name = fields.Char(string='عنوان الخبر', required=True, translate=True)
    description = fields.Html('تفاصيل عن الخبر', strip_style=True, translate=html_translate)
    short_description = fields.Text(string='وصف مختصر للخبر', translate=True)
    image = fields.Image("صورة")
    in_slider = fields.Boolean("عرض الخبر في منزلق الصفحة الرئيسية")
    is_important = fields.Boolean("مهم؟")
    is_most_traded = fields.Boolean("اكثر تداولا؟")
    category_id = fields.Many2one('news.category', string='الفئة')


class NewsCategory(models.Model):
    _name = "news.category"
    _description = "News Category"

    name = fields.Char(string='الإ سم', required=True, translate=True)