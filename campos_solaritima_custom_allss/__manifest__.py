# -*- coding: utf-8 -*-
{
    'name': 'Campos Adicionais Solaritima',
    'version': '12.0.1.0.0',
    'licence': 'AGPL-3',
    'category': 'Partner',
    'author': 'Renata Carrillo (ALLSS Soluções em Sistemas)',
    'summary': 'Res Partner',
    'description':'Campos Adicionais Solaritima',
    'depends': [
        'contacts',
        'account_accountant',
    ],
    'data': [
        #views
        'views/campos_solaritima_custom.xml',
        'views/teste_casa_decimal.xml',
    ],
    'demo': [
    ],
    'css': [],
    'installable': True,
    'auto_install': True,
    'application': False,
}