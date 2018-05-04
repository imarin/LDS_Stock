# -*- coding: utf-8 -*-
{
    'name': "LDS Stock Control",

    'summary': """
        Manage LDS stock, product and proyects easily.
    """,

    'author': "Ismael Marin",
    'website': "https://github.com/imarin",

    'category': 'Administration',
    'version': '0.1',

    #'price': 0,
    #'currency': 'EUR',

    #'license': 'OPL-1',
	
	'images': ['images/main_screenshot.png'],

    # any module necessary for this one to work correctly
    'depends': ['base', 'stock'],

    # always loaded
    'data': [
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [],

    'installable': True,
    'application': True,
    'auto_install': False,
}
