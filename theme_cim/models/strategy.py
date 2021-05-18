# -*- coding: utf-8 -*-

import uuid
from werkzeug.urls import url_encode
from odoo import api, exceptions, fields, models, _


class Strategy(models.Model):
    _name = "strategy"
    _description = "Strategy"
    name = fields.Char(string="الإ سم", required=True, translate=True)
    attachment_id = fields.Many2one('ir.attachment', string='الملف')