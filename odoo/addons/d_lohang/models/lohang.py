

# -*- coding: utf-8 -*-
from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError, ValidationError

class LoHang(models.Model):
    _name = "lo.hang"
    _description = "lo.hang"

    ma_donthuoc = fields.Char('Mã lô')
    ten_lo = fields.Char('Tên lô', required=True)
    han_su_dung = fields.Date("Hạn sử dụng")
    ngay_sx = fields.Date("Ngày sản xuất")
    

    gioi_tinh = fields.Selection([
        ('nam', 'Nam'),
        ('nu', 'Nữ'),
        ('khac', 'Khác'),
    ], string='Giới tính', default='nam')

    dia_chi = fields.Char("Địa chỉ")
    dien_thoai = fields.Char('Điện thoại')
    tuoi = fields.Integer("Tuổi")
    chan_doan = fields.Text("Chẩn đoán")
    thuoc_ids = fields.Many2many('nha.thuoc', string = 'Thuốc')


    @api.model
    def create(self, vals):
        #print("Successfull")
        c11 = ""
        c22 = ""
        c33 = ""
        c44 = ""
        c1 = vals.get('ten_benhnhan')
        c2 = vals.get('tuoi')
        c3 = vals.get('dien_thoai')
        c4 = vals.get('ngay')
        if c1 or c2 or c3 or c4:
            c11 = ""
            c22 = ""
            c33 = ""
            c44 = ""
            if len(str(c1)) >=3:
                c11 += c1[len(str(c1))-3:len(str(c1))]
            else:
                c11 += c1[0:len(c1)]
            
            c22 += str(c2)
            
            if len(str(c3)) >=3:
                c33 += c3[len(str(c3))-3:len(str(c3))]
            else:
                c33 += c3[0:len(c3)]
            
            c44 += str(c4)
            vals['ma_donthuoc'] = c11 +"-"+ c22  +"_"+ c33 + "-" + c44

        return super(DonThuoc, self).create(vals)