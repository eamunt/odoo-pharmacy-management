# -*- coding: utf-8 -*-

{
    'name': "Lo hang",
    'summary': """Quan ly lo san pham""",
    'description': """Quan Ly lo san pham""",
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
        'views/lohang_view.xml',
    ],
    'installable': True,
    'application': True,
}