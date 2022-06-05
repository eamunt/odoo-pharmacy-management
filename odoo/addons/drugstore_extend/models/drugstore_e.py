from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError, ValidationError


class MyDrugstoreExtend(models.Model):
    _name = "my.drugstore"
    _description = "My drugstore extend"
    _inherit = "my.drugstore"

    # add new field: country field
    # sẽ không hiển thị vì không có trong Views. (nhưng sẽ xuất hiện cột trong Database)
    country = fields.Many2one('res.country', string="Drug's country")
    # modify exp field: defaule exp = 1 up to 3
    exp = fields.Integer("EXPry (month)", default = 3)

    # add more selection for type
    type = fields.Selection(selection_add=[('other', 'Other')])

