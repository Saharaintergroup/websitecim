# -*- coding: utf-8 -*-
from odoo import api, fields, models, _, tools
import base64


class EgovernmentFiles(models.Model):
    _name = "egovernment.files"
    _description = "Egovernment Files"

    name = fields.Char(string="اسم الملف", required=True, translate=True)
    attachment_id = fields.Many2one('ir.attachment', string='الملف')
