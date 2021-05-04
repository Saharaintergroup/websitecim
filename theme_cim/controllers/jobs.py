from odoo import http, models, fields, _
from odoo.http import request


class Jobs(http.Controller):
    @http.route(['/jobs', '/jobs/page/<int:page>'], type='http', auth="public",
                website=True)
    def jobs_page(self, page=0, **kw):
        jobs = request.env['jobs'].sudo().search([])
        total = jobs.sudo().search_count([])
        pager = request.website.pager(
            url='/jobs',
            total=total,
            page=page,
            step=9,
        )
        offset = pager['offset']
        jobs = jobs[offset: offset + 9]
        data = {'jobs': jobs, 'pager': pager, }
        return http.request.render('theme_cim.jobs_page', data)

    @http.route([
        '''/jobs/<model("jobs"):jobs>''',
    ], type='http', auth="public", website=True, sitemap=True)
    def jobs_post(self, jobs, enable_editor=None, **post):
        print('---------------test-----------------------------')
        return http.request.render('theme_cim.jobs_post_page',
                                   {'record': jobs})

    @http.route([
        '''/apply-jobs/<model("jobs"):jobs>''',
    ], type='http', auth="public", website=True, sitemap=True,csrf=False)
    def jobs_apply(self, jobs,enable_editor=None, **post):
        data = {'jobs':jobs}
        if post:
            jobs._create_candidate(post)
        return http.request.render('theme_cim.apply_job_page', data)
