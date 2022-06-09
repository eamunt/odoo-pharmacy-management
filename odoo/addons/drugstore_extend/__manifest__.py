# -*- coding: utf-8 -*-

{
    'name': "My Drugstore extend",
    'summary': """My drugstore extend model""",
    'description': """Managing drug information""",
    'author': "haokah",
    
    'category': 'Uncategorized',
    'version': '0.1',
    'depends':[
        # warning: name addons
        'drugstore',
    ],
    'data': [
        # Đăng ký access right.
        'security/ir.model.access.csv',
        # Đăng ký view.
        'views/drugstore_views_extend.xml',
        'views/product_drugs_views.xml',
    ],
    'installable': True,
    'application': True,
}