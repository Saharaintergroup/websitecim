# -*- encoding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Cim Theme',
    'description': 'Cim website theme',
    'category': 'Theme',
    'sequence': 1,
    'version': '14.0',
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
        "templates/advertisements.xml",
        "templates/media_center.xml",
        "templates/contactus.xml",
        "templates/electronic_government.xml",
        "templates/cybersecurity.xml",
        "templates/sector_development.xml",
        "templates/organization_of_communications.xml",
        # views
        "views/website_slider_home_views.xml",
        "views/news_views.xml",
    ],
    'images': [
        'static/description/cover.png',
        'static/description/theme_cim_screenshot.png',
    ],
    'application': True,
    'auto_install': False,
}
