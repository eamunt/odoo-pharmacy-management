# -*- coding: utf-8 -*-

{
    'name': "My Drugstore special",
    'summary': """My drugstore special model""",
    'description': """Managing drug information""",
    'author': "haokah",
    
    'category': 'Uncategorized',
    'version': '0.1',
    'depends':[
        # warning
        'drugstore',
    ],
    'data': [
        # Đăng ký access right.
        'security/ir.model.access.csv',
        # Đăng ký view.
        'views/drugstore_special_view.xml',
    ],
    'installable': True,
    'application': True,
}