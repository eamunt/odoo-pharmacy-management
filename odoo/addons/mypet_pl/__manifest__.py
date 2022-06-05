# file mô tả thông tin thú cưng
# -*- coding: utf-8 -*-

{
    'name': "My Pet Plus",
    'summary': """My Pet Plus model""",
    'description': """Managing pet information""",
    'author': "kkkkk.info",
    
    'category': 'Uncategorized',
    'version': '0.1',
    'depends':[
        # kế thừa từ model mypet
        'mypet',
    ],
    'data': [
        # Đăng ký access right.
        'security/ir.model.access.csv',
        # Đăng ký view.
        'views/my_pet_pl_views.xml',
    ],
    'installable': True,
    'application': True,
}