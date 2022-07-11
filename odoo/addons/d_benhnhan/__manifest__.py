# -*- coding: utf-8 -*-

{
    'name': "Benh nhan",
    'summary': """Quan ly benh nhan""",
    'description': """Quan Ly benh nhan""",
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
        'views/benhnhan_view.xml',
    ],
    'installable': True,
    'application': True,
}