# -*- coding: utf-8 -*-
#################################################################################
#
#    Odoo, Open Source Management Solution
#    Copyright (C) 2018-today Ismael Marin <https://github.com/imarin>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#################################################################################
{
    'name': "LDS Stock Control",

    'summary': """
        Manage LDS stock, product and proyects easily.
    """,

    'author': "Ismael Marin",
    'website': "https://github.com/imarin",
    'license': 'AGPL-3',

    'category': 'inventory',
    'version': '0.1',
	
	#'images': ['images/main_screenshot.png'],

    # any module necessary for this one to work correctly
    'depends': ['base','stock'],

    # always loaded
    'data': [
        'views/menu.xml',

        
    ],
    # only loaded in demonstration mode
    'demo': [],

    'installable': True,
    'application': True,
    'auto_install': False,
}
