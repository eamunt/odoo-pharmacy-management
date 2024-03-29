

# -*- coding: utf-8 -*-
from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError, ValidationError

class HanghoaNhap(models.Model):
    _name = "hanghoa.nhap"
    _description = "hanghoa.nhap"

    ten_sanpham = fields.Char('Hàng hóa nhập')
    dvt = fields.Selection([
        ('vi', 'Vĩ'),
        ('hop', 'Hộp'),
        ('thung', 'Thùng'),
        ('vien', 'Viên'),
        ('lo', 'Lọ'),
        ('khac', 'khác')
    ], string='ĐVT', default='vi')
    lo = fields.Char("Lô")
    ngay_sx = fields.Date("NgaySX")
    han_su_dung = fields.Date("HSD")
    so_luong = fields.Float('SL', required=True)
    dongia_nhap = fields.Float("Đơn giá nhập")
    chiet_khau = fields.Float("CK(%)")
    thanh_tien = fields.Float("Thành tiền", compute="_compute_final_price", store = True)

    

    @api.depends('dongia_nhap', 'so_luong', 'chiet_khau')
    def _compute_final_price(self):
        for record in self:
            record.thanh_tien = record.dongia_nhap*record.so_luong
            record.thanh_tien = record.thanh_tien - record.thanh_tien*(record.chiet_khau/100)
    
    
    @api.constrains('ngay_sx', 'han_su_dung')
    def get_two_date_comp(self):
        start_date = self.ngay_sx.strftime('%Y-%m-%d')
        end_date = self.han_su_dung.strftime('%Y-%m-%d')
        if start_date > end_date:
            raise ValidationError(("Ngày sản xuất phải sớm hơn hạn sử dụng"))