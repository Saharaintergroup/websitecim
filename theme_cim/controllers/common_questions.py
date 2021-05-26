from odoo import http, models, fields, _
from odoo.http import request

class CommonQuestions(http.Controller):
    @http.route(['/common-questions', '/common-questions/page/<int:page>'], type='http', auth="public",
                website=True)
    def common_questions_page(self, page=0, **kw):
        common_questions = request.env['common.questions'].sudo().search([])
        total = common_questions.sudo().search_count([])
        pager = request.website.pager(
            url='/common-questions',
            total=total,
            page=page,
            step=4,
        )
        offset = pager['offset']
        common_questions = common_questions[offset: offset + 4]
        data = {'common_questions': common_questions, 'pager': pager, }
        return http.request.render('theme_cim.common_questions', data)