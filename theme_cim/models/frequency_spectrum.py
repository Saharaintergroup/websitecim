# -*- coding: utf-8 -*-

import uuid
from werkzeug.urls import url_encode
from odoo import api, exceptions, fields, models, _


class FrequencySpectrum(models.Model):
    _name = "frequency.spectrum"
    _description = "Frequency Spectrum"
    name = fields.Char(string="إسم الملف", required=True, translate=True)
    attachment_id = fields.Many2one('ir.attachment', string='الملف')