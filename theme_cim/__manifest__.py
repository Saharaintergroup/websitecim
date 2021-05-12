# -*- encoding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Cim Theme',
    'description': 'Cim website theme',
    'category': 'Theme',
    'sequence': 1,
    'version': '1.7.7',
    'depends': ['base', 'website', 'website_form'],
    'data': [
        # security
        "security/ir.model.access.csv",
        # templates
        "templates/assets.xml",
        "templates/header.xml",
        "templates/footer.xml",
        "templates/home.xml",
        "templates/aboutus.xml",
        "templates/electronic_services.xml",
        "templates/indications.xml",
        "templates/public_announcements.xml",
        "templates/jobs.xml",
        "templates/bids.xml",
        "templates/media_center.xml",
        "templates/contactus.xml",
        "templates/electronic_government.xml",
        "templates/cybersecurity.xml",
        "templates/sector_development.xml",
        "templates/organization_of_communications.xml",
        "templates/company_partners.xml",
        "templates/dataprivacy.xml",
        "templates/usage_agreement.xml",
        # views
        "views/slider_home_views.xml",
        "views/ticker_news_views.xml",
        "views/company_partners_views.xml",
        "views/teams_views.xml",
        "views/public_announcements_views.xml",
        "views/jobs_views.xml",
        "views/bids_views.xml",
        "views/decisions_views.xml",
        "views/numbering_models_views.xml",
        "views/menu.xml",
        # data
        "data/company_partners_data.xml",
        "data/teams_data.xml",
        "data/decisions_data.xml",
        "data/numbering_models_data.xml",
    ],
    'images': [
        'static/description/cover.png',
        'static/description/theme_cim_screenshot.png',
    ],
    'application': True,
    'auto_install': False,
}
