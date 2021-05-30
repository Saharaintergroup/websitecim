from odoo import http, models, fields, _
from odoo.http import request


class FrequencySpectrum(http.Controller):
    @http.route(['/frequency-spectrum', '/frequency-spectrum/page/<int:page>'], type='http', auth="public",
                website=True)
    def accreditation_devices_page(self, page=0, **kw):
        frequency_spectrum = request.env['frequency.spectrum'].sudo().search([])
        total = frequency_spectrum.sudo().search_count([])
        pager = request.website.pager(
            url='/frequency-spectrum',
            total=total,
            page=page,
            step=10,
        )
        offset = pager['offset']
        frequency_spectrum = frequency_spectrum[offset: offset + 10]
        data = {'frequency_spectrum': frequency_spectrum, 'pager': pager}
        return http.request.render('theme_cim.frequency_spectrum_page', data)

