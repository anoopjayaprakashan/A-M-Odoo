# -*- coding: utf-8 -*-
###################################################################################

# Author       :  Anoop
# Copyright(c) :  2025-Present.
# License      :  LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

###################################################################################
from odoo import models, api
from odoo.http import request


class IrAttachment(models.Model):
    _inherit = "ir.attachment"

    @api.model_create_multi
    def create(self, vals_list):
        uid = self.env.uid
        user = self.env['res.users'].sudo().browse(uid)
        sub_username = request.session.get("sub_username") if request else None
        for vals in vals_list:
            if user and sub_username:
                vals['description'] = (vals.get('description') or '') + " (Uploaded by %s(%s))" % (user.login, sub_username)
        return super().create(vals_list)
