# -*- coding: utf-8 -*-
{
    'name': 'Vendedor no Projeto',
    'version': '14.0.1.0.0',
    'licence': 'AGPL-3',
    'category': '',
    'author': 'Renata Carrillo (ALLSS Soluções em Sistemas)',
    'summary': '',
    'description':'Vendedor referenciado no módulo de Projeto',
    'depends': [
        'account_accountant',
        'sale_management',
        'project',
    ],
    'data': [
        #views
        'views/campo_vendor_project.xml',
    ],
    'demo': [],
    'css': [],
    'installable': True,
    'auto_install': True,
    'application': False,
}