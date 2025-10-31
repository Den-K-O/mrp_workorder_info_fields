# Copyright 2022 ForgeFlow S.L.
#   (http://www.forgeflow.com)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import fields, models
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

