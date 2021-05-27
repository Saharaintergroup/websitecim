from odoo import http, models, fields, _
from odoo.http import request


class AccreditationDevices(http.Controller):
    @http.route(['/specific-accreditation', '/specific-accreditation/page/<int:page>'], type='http', auth="public",
                website=True)
    def accreditation_devices_page(self, page=0, **kw):
        accreditation_devices = request.env['accreditation.devices'].sudo().search([])
        total = accreditation_devices.sudo().search_count([])
        pager = request.website.pager(
            url='/specific_accreditation',
            total=total,
            page=page,
            step=10,
        )
        offset = pager['offset']
        accreditation_devices = accreditation_devices[offset: offset + 10]
        data = {'accreditation_devices': accreditation_devices, 'pager': pager}
        return http.request.render('theme_cim.specific_accreditation_page', data)

