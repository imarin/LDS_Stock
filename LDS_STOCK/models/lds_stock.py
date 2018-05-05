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

class LdsLogisticLetter(models.Model):
    _name = 'lds.logistic.letter'
    _inherit= ['stock.location', 'mail.thread']
    _order = "sequence, name, id"

    def _get_default_state(self):
        state = self.env.ref('lds_project_stock.lds_logistic_letter_state_active', raise_if_not_found=False)
        return state and state.id or False

    name = fields.Char(string='Project Name', required=True, translate=True)
    description = fields.Text(translate=True)
    sequence = fields.Integer(default=1)
    active = fields.Boolean(default=True,
        help="If the active field is set to False, it will allow you to hide the project without removing it.")
    sequence = fields.Integer(default=10, help="Gives the sequence order when displaying a list of Projects.")
    supervisor_id = fields.Many2one('res.partner', string='Project Manager')
    delivery_id = fields.Many2one('res.partner', string='Delivery Address')
    tag_ids = fields.Many2many('lds.logistic.letter.tag', copy=False)
    state_id = fields.Many2one('lds.logistic.letter.state', 'State', default=_get_default_state, 
        help='Current state of the vehicle', ondelete="set null")
    #product_location_ids = fields.One2many('stock.quant', 'location_id', string='Available Products')

class LdsLogisticLetterTag(models.Model):
    _name = 'lds.logistic.letter.tag'

    name = fields.Char(required=True, translate=True)
    color = fields.Integer('Color Index', default=10)

    _sql_constraints = [('name_uniq', 'unique (name)', "Tag name already exists !")]
    
class LdsLogisticLetterState(models.Model):
    _name = 'lds.logistic.letter.state'
    _order = 'sequence asc'

    name = fields.Char(required=True)
    sequence = fields.Integer(help="Used to order the note stages")

    _sql_constraints = [('fleet_state_name_unique', 'unique(name)', 'State name already exists')]