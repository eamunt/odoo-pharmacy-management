# -*- coding: utf-8 -*-

from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError, ValidationError

class LineThuoc(models.Model):
    _name = "line.thuoc" # new model.
    _inherits = {'nha.thuoc': 'thuoc_id'} # Khóa ngoại trỏ đến model drugstore.special là drug_id.
    _description = "line.thuoc"

    # define drug_id
    # index: yêu cầu Odoo tạo index trong database
    # ondelete='cascade':tự động xóa dữ liệu ở bảng con khi xóa dữ liệu ở bảng cha
        # referential for foreign key
    thuoc_id = fields.Many2one(
        'nha.thuoc', 'Link Thuốc',
        auto_join = True, index = True, ondelete='cascade', required=True
    )

    so_luong = fields.Integer("Số lượng (viên)")
    sang = fields.Integer("Sáng (viên)")
    chieu = fields.Integer("Chiều (viên)")
    ghi_chu = fields.Char("Ghi chú")