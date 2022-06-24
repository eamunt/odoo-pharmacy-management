# -*- coding: utf-8 -*-

{
    'name': "Don thuoc",
    'summary': """Quan ly don thuoc""",
    'description': """Quan Ly don thuoc""",
    'author': "haokah",
    
    'category': 'Uncategorized',
    'version': '0.1',
    'depends':[
        # warning
        'd_nhathuoc',
    ],
    'data': [
        # Đăng ký access right.
        'security/ir.model.access.csv',
        # Đăng ký view.
        'views/donthuoc_view.xml',
        'views/line_thuoc_view.xml'
    ],
    'installable': True,
    'application': True,
}