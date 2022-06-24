from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError, ValidationError


class LineDonhang(models.Model):
    _name = "line.donhang"
    _description = "line.donhang"
    _inherit = "line.thuoc"

    tong_line = fields.Float("Tổng", compute='_compute_final_price') 


    @api.depends('don_gia', 'so_luong')
    def _compute_final_price(self):
        for record in self:
            record.tong_line = record.don_gia*record.so_luong
                
