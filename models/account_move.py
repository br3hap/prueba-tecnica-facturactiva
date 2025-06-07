# -*- coding: utf-8 -*-
import logging
import base64
from io import BytesIO
from reportlab.pdfgen import canvas

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

_logger = logging.getLogger(__name__)


class AccountMove(models.Model):
    _inherit = 'account.move'

    blood_type = fields.Many2one('blood.type', string='Tipo de Sangre')


    def update_invoice_date(self, move_id, new_date):
        move = self.browse(move_id)
        if not move.exists():
            return {'error': 'Factura no encontrada'}
        move.invoice_date = new_date
        return {'success': True}
    


    def button_comment(self):
        values = {
            'id':'view_type_remaining_sand_form',
            'name':u'Tipo de Sangre',
            'view_type':'form',
            'view_mode':'form',
            'target':'new',
            'context':{
                'default_move_id':self.id,
                'exclude_blood_type': self.blood_type.id,
            },
            'res_model':'type.remaining.sand',
            'domain': [('id', '!=', self.blood_type.id)],
            'type':'ir.actions.act_window',
        }

        return values


    def generate_narration_pdf(self):
        self.ensure_one()
        buffer = BytesIO()
        p = canvas.Canvas(buffer)
        p.setFont("Helvetica", 12)
        p.drawString(100, 800, f"Factura: {self.name}")
        p.drawString(100, 780, f"Fecha: {self.invoice_date or 'N/A'}")
        p.drawString(100, 760, "Narración:")
        textobject = p.beginText(100, 740)
        for line in (self.narration or '').splitlines():
            textobject.textLine(line)
        p.drawText(textobject)
        p.showPage()
        p.save()
        buffer.seek(0)
        pdf_data = buffer.getvalue()
        buffer.close()

        return {
            'type': 'ir.actions.client',
            'tag': 'prueba_facturactiva.download_narration_pdf',
            'params': {
                'pdf_base64': base64.b64encode(pdf_data).decode('utf-8'),
                'filename': f"Narracion_{self.name or 'factura'}.pdf"
            }
        }


