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

    def _default_website(self):
        """ Find the first company's website, if there is one. """
        company_id = self.env.company.id

        if self._context.get('default_company_id'):
            company_id = self._context.get('default_company_id')

        domain = [('company_id', '=', company_id)]
        return self.env['website'].search(domain, limit=1)

    website_id = fields.Many2one('website', string="Website", ondelete='restrict', default=_default_website, domain="[('company_id', '=?', company_id)]")
    company_id = fields.Many2one('res.company', 'Company')
    name = fields.Char(string="Title", required=True, translate=True)
    description = fields.Text(string='Description', required=True, translate=True)
    reference = fields.Char(string='Reference Number')
    bid_date = fields.Date(string='Bid Date')
    expiration_date= fields.Date(string='Expiration Date')
    image = fields.Image("Photo")
    attachment_id = fields.Many2one('ir.attachment', string='Bid request brochure', ondelete='cascade')
