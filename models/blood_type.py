# -*- coding: utf-8 -*-
import logging

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

_logger = logging.getLogger(__name__)


class BloodType(models.Model):
    _name = 'blood.type'
    _description = 'BloodType'

    name = fields.Char('Tipo')
    active = fields.Boolean('Activo', default=False)
