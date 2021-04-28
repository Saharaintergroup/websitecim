# -*- coding: utf-8 -*-
from odoo import api, fields, models, _, tools


class PublicAnnouncements(models.Model):
    _name = "public.announcements"
    _description = "Public Announcements"

    name = fields.Char(string="Title", required=True, translate=True)
    description = fields.Text(string='Description', required=True, translate=True)
    image = fields.Image("Photo")

class AvailableJobs(models.Model):
    _name = "available.jobs"
    _description = "Available jobs"

    name = fields.Char(string="Title", required=True, translate=True)
    description = fields.Text(string='Description', required=True, translate=True)
    image = fields.Image("Photo")

class Bids(models.Model):
    _name = "bids"
    _description = "Bids"

    name = fields.Char(string="Title", required=True, translate=True)
    description = fields.Text(string='Description', required=True, translate=True)
    image = fields.Image("Photo")
