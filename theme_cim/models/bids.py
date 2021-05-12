# -*- coding: utf-8 -*-
from odoo import api, fields, models, _, tools
from odoo.exceptions import ValidationError


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

    website_id = fields.Many2one('website', string="Website", ondelete='restrict', default=_default_website,
                                 domain="[('company_id', '=?', company_id)]")
    company_id = fields.Many2one('res.company', 'Company')
    name = fields.Char(string="Title", required=True, translate=True)
    description = fields.Text(string='Description', required=True, translate=True)
    reference = fields.Char(string='Reference Number')
    bid_date = fields.Date(string='Bid Date')
    expiration_date = fields.Date(string='Expiration Date')
    image = fields.Image("Photo")

    attachment_number = fields.Integer('Number of Attachments', compute='_compute_attachment_number')

    def _compute_attachment_number(self):
        attachment_data = self.env['ir.attachment'].read_group([('res_model', '=', 'bids'), ('res_id', 'in', self.ids)],
                                                               ['res_id'], ['res_id'])
        attachment = dict((data['res_id'], data['res_id_count']) for data in attachment_data)
        for bids in self:
            bids.attachment_number = attachment.get(bids.id, 0)

    def action_get_attachment_view(self):
        self.ensure_one()
        res = self.env['ir.actions.act_window']._for_xml_id('base.action_attachment')
        res['domain'] = [('res_model', '=', 'bids'), ('res_id', 'in', self.ids)]
        res['context'] = {'default_res_model': 'bids', 'default_res_id': self.id}
        return res

    @api.constrains('expiration_date', 'bid_date')
    def date_constrains(self):
        for rec in self:
            if rec.expiration_date < rec.bid_date:
                raise ValidationError(_('Sorry, Expiration Date Must be greater Than Bid Date...'))
