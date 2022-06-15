# đây là file model, sẽ chứa thông tin cần lưu trữ các thuộc tính nào cho thú cưng.


# -*- coding: utf-8 -*-
from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError, ValidationError

class NhaThuoc(models.Model):
    _name = "nha.thuoc"
    _description = "nha.thuoc"

    name = fields.Char('Tên thuốc', required=True)
    how_to_use = fields.Text('Cách dùng')
    so_giay_dangky = fields.Char('Số giấy đăng ký')
    hoat_chat = fields.Text('Hoạt chất')
    nong_do = fields.Float('Nồng độ', default = 0)
    # import_date = fields.Date('Import date', required=True)
    quy_cach_dong_goi = fields.Text("Quy cách đóng gói")
    hang_sx = fields.Char("Hãng sản xuất")
    nha_sx = fields.Char("Nhà sản xuất")
    lieu_dung = fields.Integer("Liều dùng/ngày")

    