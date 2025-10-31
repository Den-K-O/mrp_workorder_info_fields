# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Workorder info fields',
    'version': '0.1',
    'category': 'Production',
    'summary': 'Show additional info fields in mrp workorder views',
    'description': """
Show additional info fields in mrp workorder views.
    """,
    'depends': ['mrp'],
    'data': [
        'views/workorder_views.xml',
    ],
    'installable': True,
    'auto_install': False
}
