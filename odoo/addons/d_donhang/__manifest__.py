# -*- coding: utf-8 -*-

{
    'name': "Don hang",
    'summary': """Quan ly don hang""",
    'description': """Quan Ly don hang""",
    'author': "haokah",
    
    'category': 'Uncategorized',
    'version': '0.1',
    'depends':[
        # warning
        'd_donthuoc'
    ],
    'data': [
        # Đăng ký access right.
        'security/ir.model.access.csv',
        # Đăng ký view.
        'views/donhang_view.xml',
        'views/line_donhang_view.xml',
    ],
    'installable': True,
    'application': True,
}