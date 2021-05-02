# -*- encoding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Cim Theme',
    'description': 'Cim website theme',
    'category': 'Theme',
    'sequence': 1,
    'version': '1.4',
    'depends': ['base', 'website', 'website_form'],
    'data': [
        "security/ir.model.access.csv",
        "templates/assets.xml",
        "templates/header.xml",
        "templates/footer.xml",
        "templates/home.xml",
        "templates/aboutus.xml",
        "templates/electronic_services.xml",
        "templates/indications.xml",
        "templates/announcements.xml",
        "templates/media_center.xml",
        "templates/contactus.xml",
        "templates/electronic_government.xml",
        "templates/cybersecurity.xml",
        "templates/sector_development.xml",
        "templates/organization_of_communications.xml",
        # views

        "views/slider_home_views.xml",
        "views/ticker_news_views.xml",
        "views/partners_logo_views.xml",
        "views/teams_views.xml",
        "views/public_announcements_views.xml",
        "views/jobs_views.xml",
        "views/bids_views.xml",
        "views/menu.xml",

    ],
    'images': [
        'static/description/cover.png',
        'static/description/theme_cim_screenshot.png',
    ],
    'application': True,
    'auto_install': False,
}
