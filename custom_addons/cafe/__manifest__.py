# -*- coding: utf-8 -*-
{
    'name': "Cafe Management",
    'summary': """Module for managing cafe products""",
    'author': "Jinay Shah",
    'website': "https://www.silvertouch.com",
    'category': 'Uncategorized',
    'version': '16.0.1',
    'depends': ['base'],
    'data': [
        'views/product.xml',
        'views/tax.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
