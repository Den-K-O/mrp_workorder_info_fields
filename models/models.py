# Copyright 2022 ForgeFlow S.L.
#   (http://www.forgeflow.com)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models
from odoo.addons.stock.models.stock_move import PROCUREMENT_PRIORITIES



class MrpWorkorder(models.Model):
    _inherit = "mrp.workorder"

    source = fields.Char(
        string="Source",
        related='production_id.origin',
        store=True,
        readonly=True,
    )

    # priority = fields.Selection(
    #     PROCUREMENT_PRIORITIES, string='Priority', default='0', index=True,
    #     help="Components will be reserved first for the MO with the highest priorities.")
    
    priority = fields.Selection(
        related='production_id.priority',
        string="Priority",
        store=True,
        readonly=True,
    )

    parent_mo_deadline = fields.Datetime(
        string="Parent MO Deadline",
        related='production_id.date_deadline',
        store=True,
        readonly=True,
    )

    next_workcenter = fields.Many2one(
        string="Next Workcenter",
        comodel_name='mrp.workcenter',
        compute='_compute_next_workcenter',
    )

    @api.depends('next_work_order_id.workcenter_id')
    def _compute_next_workcenter(self):
        for wo in self:
            wo.next_workcenter = wo.next_work_order_id.workcenter_id
