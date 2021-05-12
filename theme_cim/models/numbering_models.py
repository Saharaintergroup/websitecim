# -*- coding: utf-8 -*-
from odoo import api, fields, models, _, tools
import base64


class NumberingModels(models.Model):
    _name = "numbering.models"
    _description = "Numbering Models"

    name = fields.Char(string="اسم النموذج", required=True, translate=True)
    attachment_id = fields.Many2one('ir.attachment', string='الملف')
