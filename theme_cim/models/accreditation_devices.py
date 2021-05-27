# -*- coding: utf-8 -*-

import uuid
from werkzeug.urls import url_encode
from odoo import api, exceptions, fields, models, _


class AccreditationDevices(models.Model):
    _name = "accreditation.devices"
    _description = "Accreditation Devices"
    name = fields.Char(string="الإ سم", required=True, translate=True)
    attachment_id = fields.Many2one('ir.attachment', string='الملف')