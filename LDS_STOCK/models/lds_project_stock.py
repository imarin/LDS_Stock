# -*- coding: utf-8 -*-
#################################################################################
#
#    Odoo, Open Source Management Solution
#    Copyright (C) 2018-today Ascetic Business Solution <www.asceticbs.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#################################################################################
from odoo import api,fields,models,_

class ldslogisticletter(models.Model):
    _name = 'lds.logistic.letter'
    _inherit= ['stock.location', 'mail.thread']
    _order = "sequence, name, id"

    name = fields.Char(string='Stage Name', required=True, translate=True)
    description = fields.Text(translate=True)
    sequence = fields.Integer(default=1)
    active = fields.Boolean(default=True,
        help="If the active field is set to False, it will allow you to hide the project without removing it.")
    sequence = fields.Integer(default=10, help="Gives the sequence order when displaying a list of Projects.")
    supervisor_id = fields.Many2one('res.partner', string='Project Manager')
    delivery_id = fields.Many2one('res.partner', string='Delivery Address')
    product_location_ids = fields.One2many('stock.quant', 'location_id', string='Available Products')
    
    
   
