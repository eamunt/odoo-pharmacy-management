from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError, ValidationError
import json

class LineThuoc(models.Model):
    _name = "line.thuoc" # new model.
    _inherits = {'nha.thuoc': 'thuoc_id'} # Khóa ngoại trỏ đến model drugstore.special là drug_id.
    _description = "line.thuoc"

    # define drug_id
    # index: yêu cầu Odoo tạo index trong database
    # ondelete='cascade':tự động xóa dữ liệu ở bảng con khi xóa dữ liệu ở bảng cha
        # referential for foreign key
    thuoc_id = fields.Many2one(
        'line.thuoc', 'Line Thuoc',
        auto_join = True, index = True, ondelete='cascade', required=True
    )

    so_luong = fields.Integer("Số lượng")