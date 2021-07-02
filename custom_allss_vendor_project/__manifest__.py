# -*- coding: utf-8 -*-
{
    'name': 'ALLSS - Vendedor no Projeto',
    'version': '14.0.1.0.0',
    'licence': 'AGPL-3',
    'category': 'Project',
    'author': 'Renata Carrillo (ALLSS Soluções em Sistemas)',
    'summary': 'ALLSS VENDOR',
    'description':'Vendedor referenciado no módulo de Projeto',
    'depends': [
        # 'account_accountant',
        'sale_management',
        'project',
        'crm',
    ],
    'data': [
        #views
        'views/campo_vendor_project.xml',
    ],
    'demo': [],
    'css': [],
    'installable': True,
    'auto_install': False,
    'application': False,
}