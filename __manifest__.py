# -*- coding: utf-8 -*-
{
    'name': 'Prueba facturactiva',
    'version': '1.0',
    'summary': """ Prueba_facturactiva Summary """,
    'author': 'Breithner Aquituari',
    'website': '',
    'category': '',
    'depends': ['base', 'account', 'web'],
    "data": [
        "security/ir.model.access.csv",
        "views/account_move_views.xml",
        "views/menu_views.xml",
        "views/blood_type_views.xml",
        "wizards/type_remaining_sand.xml",
    ],

    'assets': {
        'web.assets_backend': [
            'prueba_facturactiva/static/src/js/invoice_date_wizard.js',
            'prueba_facturactiva/static/src/js/invoice_pdf_download.js',
            'prueba_facturactiva/static/src/xml/invoice_date_template.xml',
        ]
    },
    
    'application': True,
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
