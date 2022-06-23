

# -*- coding: utf-8 -*-
from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError, ValidationError

class BacSi(models.Model):
    _name = "bac.si"
    _description = "bac.si"

    name = fields.Char('Tên Bác sĩ', required=True)
    ma_bacsi = fields.Char('Mã bác sĩ')
    gioi_tinh = fields.Selection([
        ('nam', 'Nam'),
        ('nu', 'Nữ'),
        ('khac', 'Khác'),
    ], string='Giới tính', default='nam')

    dien_thoai = fields.Char('Điện thoại')
    chuc_vu = fields.Selection([
        ('truong_khoa', 'Trưởng khoa'),
        ('pho_khoa', 'Phó khoa'),
        ('nhan_vien', 'Nhân viên'),
        ('khac', 'Khác'),
    ], string='Chức vụ', default='nhan_vien')

    khoa_lam_viec = fields.Selection([
        ('noi', 'Khoa nội'),
        ('ngoai', 'Khoa ngoại'),
        ('rh_mat', 'Răng hàm mặt'),
        ('san', 'Khoa sản'),
        ('mat', 'Khoa mắt'),
        ('tai_mui_hong', 'Tai mũi họng'),
        ('ung_buou', 'Khoa ung bướu'),
    ], string='Khoa làm việc', default='noi')
    ngay_sinh = fields.Date('Ngày sinh') 
    dia_chi = fields.Char("Địa chỉ")

    @api.model
    def create(self, vals):
        #print("Successfull")
        c11 = ""
        c22 = ""
        c33 = ""
        c1 = vals.get('name')
        c2 = vals.get('chuc_vu')
        c3 = vals.get('khoa_lam_viec')
        if c1 or c2 or c3:
            c11 = ""
            c22 = ""
            c33 = ""
            if len(str(c1)) >=3:
                c11 += c1[len(str(c1))-3:len(str(c1))]
            else:
                c11 += c1[0:len(c1)]
            if len(str(c2)) >=3:
                c22 += c2[0:3]
            else:
                c22 += c2[0:len(c2)]
            if len(str(c3)) >=3:
                c33 += c3[0:3]
            else:
                c33 += c3[0:len(c3)]
            vals['ma_bacsi'] = c11 +"-"+ c22  +"_"+ c33

        return super(BacSi, self).create(vals)