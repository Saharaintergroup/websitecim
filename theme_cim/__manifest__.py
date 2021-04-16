# -*- encoding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Cim Theme',
    'description': 'Cim website theme',
    'category': 'Theme',
    'sequence': 1,
    'version': '14.0',
    'depends': ['base', 'website','website_form'],
    'data': [
        "templates/assets.xml",
        "templates/header.xml",
        "templates/footer.xml",
        "templates/home.xml",
        "templates/aboutus.xml",
        "templates/electronic_services.xml",
        "templates/indications.xml",
        "templates/advertisements.xml",
        "templates/media_center.xml",
        # "templates/common_questions.xml",
        "templates/contactus.xml",
        "templates/electronic_government.xml",
        "templates/cybersecurity.xml",
    ],
    'images': [
        'static/description/cover.png',
        'static/description/theme_cim_screenshot.png',
    ],
    'application': True,
    'auto_install': False,
}
