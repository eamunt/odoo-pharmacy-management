# file mô tả thông tin của thuốc
# -*- coding: utf-8 -*-

{
    'name': "My Drugstore",
    'summary': """My drugstore model""",
    'description': """Managing drug information""",
    'author': "haokah",
    
    'category': 'Uncategorized',
    'version': '0.1',
    'depends':[
        'product',
    ],
    'data': [
        # Đăng ký access right.
        'security/ir.model.access.csv',
        # Đăng ký view.
        'views/drugstore_views.xml',
    ],
    'installable': True,
    'application': True,
}