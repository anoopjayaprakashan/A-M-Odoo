# -*- coding: utf-8 -*-
###################################################################################

# Author       :  Anoop
# Copyright(c) :  2025-Present.
# License      :  LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

###################################################################################
from odoo import models, fields


class ResUsersSubUser(models.Model):
    _name = 'res.users.subuser'
    _description = "User Sub Login"

    name = fields.Char("Sub Username", required=True)
    password = fields.Char("Password", required=True)
    user_id = fields.Many2one("res.users", required=True, ondelete="cascade")

    _sql_constraints = [('subuser_unique', 'unique(user_id, name)', 'Sub username must be unique per main user!')]
