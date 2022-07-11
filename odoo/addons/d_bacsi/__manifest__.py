# -*- coding: utf-8 -*-

{
    'name': "Bac si",
    'summary': """Quan ly bac si""",
    'description': """Quan Ly Bac si""",
    'author': "haokah",
    
    'category': 'Uncategorized',
    'version': '0.1',
    'depends':[
        # warning
    ],
    'data': [
        # Đăng ký access right.
        'security/security.xml',
        'security/ir.model.access.csv',
        # Đăng ký view.
        'views/bacsi_view.xml',
    ],
    'installable': True,
    'application': True,
}