# -*- coding: utf-8 -*-
import logging
from lxml import etree

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

_logger = logging.getLogger(__name__)


class Type_remaining_sand(models.TransientModel):
    _name = 'type.remaining.sand'
    _description = _('Type_remaining_sand')

    # name = fields.Char(_('Name'))
    blood_type = fields.Many2one('blood.type', string='Tipo de Sangre por defecto')
    blood_type_positive = fields.Many2one('blood.type', string='Tipo de Sangre [+]')
    blood_type_negative = fields.Many2one('blood.type', string='Tipo de Sangre [-]')
    move_id = fields.Many2one('account.move', string='Factura')

    
    @api.model
    def default_get(self, fields_list):
        res = super().default_get(fields_list)
        move_id = self.env.context.get('default_move_id')
        if move_id:
            res['move_id'] = move_id
        return res



    def update_commit(self):
        if not self.move_id:
            return
        note_text = "SANGRE RESTANTE: %s <br/> SANGRE RESTANTE [+]: %s  <br/> SANGRE RESTANTE [-]: %s" % (
            self.blood_type.name or 'N/A',
            self.blood_type_positive.name or 'N/A',
            self.blood_type_negative.name or 'N/A',
        )
        self.move_id.narration = note_text

