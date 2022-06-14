# -*- coding: utf-8 -*-
from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError, ValidationError

import logging
_logger = logging.getLogger(__name__)


class DeleteWizard(models.TransientModel):
    _name = "product.drugs.delete.wizard"
    _description = "product.drugs.delete.wizard"


    def unlink(self):
        ids = self.env.context['active_ids']
        my_drugs = self.env['product.drugs'].browse(ids)

        my_drugs.unlink()

