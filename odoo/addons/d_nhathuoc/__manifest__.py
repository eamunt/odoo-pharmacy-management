# -*- coding: utf-8 -*-

{
    'name': "Nha Thuoc",
    'summary': """Nha Thuoc""",
    'description': """Quan Ly Nha Thuoc""",
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
        'views/nhathuoc_view.xml',
    ],
    'installable': True,
    'application': True,
}