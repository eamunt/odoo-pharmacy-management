

# -*- coding: utf-8 -*-
from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError, ValidationError

class Benhnhan(models.Model):
    _name = "benh.nhan"
    _description = "benh.nhan"

    name = fields.Char('Tên Bệnh nhân', required=True)
    ma_benhnhan = fields.Char('Mã bệnh nhân')
    gioi_tinh = fields.Selection([
        ('nam', 'Nam'),
        ('nu', 'Nữ'),
        ('khac', 'Khác'),
    ], string='Giới tính', default='nam')

    dien_thoai = fields.Char('Điện thoại')
    nhom_mau = fields.Selection([
        ('a', 'A'),
        ('o', 'O'),
        ('b', 'B'),
        ('ab', 'AB'),
        ('khac', 'Khác'),
    ], string='Nhóm máu', default='o')
    ngay_sinh = fields.Date('Ngày sinh') 
    dia_chi = fields.Char("Địa chỉ")

    nhom_benh = fields.Char("Nhóm bệnh")

    start_benh = fields.Date("Ngày mắc bệnh")

    end_benh = fields.Date("Ngày khỏi bệnh")

    nghe_nghiep = fields.Char("Nghề nghiệp")

    benh_nen = fields.Char("Bệnh nền")

    ghi_chu = fields.Text('Ghi chú')

    # cac_lan_kham = fields.Many2many('don.thuoc', string = "Nhật ký")

    @api.model
    def create(self, vals):
        #print("Successfull")

        c1 = vals.get('name')
        c2 = vals.get('dien_thoai')
        c3 = vals.get('nghe_nghiep')
        c4 = vals.get('nhom_mau')
        if c1 or c2 or c3 or c4:
            c11 = ""
            c22 = ""
            c33 = ""
            c44 = ""
            if len(str(c1)) >=4:
                c11 += c1[len(str(c1))-4:len(str(c1))]
            else:
                c11 += c1[0:len(c1)]

            if len(str(c2)) >=4:
                c22 += c2[len(str(c2))-4:len(str(c2))]
            else:
                c22 += c2[0:len(c2)]

            if len(str(c3)) >=4:
                c33 += c3[len(str(c3))-4:len(str(c3))]
            else:
                c33 += c3[0:len(c3)]

            c44 += str(c4)


            vals['ma_benhnhan'] = c11 +"-"+ c22  +"_"+ c33 +"-"+ c44

        return super(Benhnhan, self).create(vals)