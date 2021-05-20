# -*- coding: utf-8 -*-
{
    'name': 'Comissão ALLSS',
    'version': '14.0.1.0.0',
    'licence': 'AGPL-3',
    'category': 'Tax',
    'author': 'Renata Carrillo (ALLSS Soluções em Sistemas)',
    'summary': '',
    'description':'Alteração do nome do campo Imposto na fatura para Comissão',
    'depends': [
        'account_accountant',
        'sale_management',
    ],
    'data': [
        #views
        'views/comissao_custom.xml',
    ],
    'demo': [
    ],
    'css': [],
    'installable': True,
    'auto_install': True,
    'application': False,
}