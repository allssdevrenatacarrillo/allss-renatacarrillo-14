# -*- coding: utf-8 -*-
{
    'name': 'Custom Quotation Solaritima',
    'version': '12.0.1.0.0',
    'licence':'AGPL-3',
    'category': 'Sale',
    'company': 'ALLSS Soluções em Sistemas',
    'website': 'https://allss.com.br',
    'author': 'Nathan Oliveira (ALLSS Soluções em Sistemas)',
    'summary': 'Sale Order Quotation',
    'description':'Custom template for quotation (Solaritima)',
    'contributors': [
        'ALLSS',
    ],
    'depends': [
        'sale','base',
        'web','mrp'
    ],
    'data': [
        # report
        'report/view_custom_quotation.xml',

        # views
        'views/sale_order_tml_custom.xml',
        'views/hr_employee_custom.xml',
        'views/sale_order_form_custom.xml',
    ],
    'demo': [
    ],
    'css': [],
    'installable': True,
    'auto_install': False,
    'application': False,
}
