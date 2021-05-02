# -*- coding: utf-8 -*-
from odoo import api, fields, models, _, tools
from odoo.exceptions import ValidationError

class PublicAnnouncements(models.Model):
    _name = "public.announcements"
    _description = "Public Announcements"

    name = fields.Char(string="Title", required=True, translate=True)
    description = fields.Text(string='Description', required=True, translate=True)
    image = fields.Image("Photo")