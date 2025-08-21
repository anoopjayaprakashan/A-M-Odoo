# -*- coding: utf-8 -*-
###################################################################################

# Author       :  Anoop
# Copyright(c) :  2025-Present.
# License      :  LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

###################################################################################
from odoo import models, fields, api
from odoo.http import request


class MailMessage(models.Model):
    _inherit = "mail.message"

    sub_username = fields.Char("Sub Username", store=True)

    @api.model_create_multi
    def create(self, vals_list):
        uid = self.env.uid
        user = self.env['res.users'].sudo().browse(uid)
        sub_username = request.session.get("sub_username") if request else None
        for vals in vals_list:
            if user and sub_username:
                vals['email_from'] = f"{user.name}({sub_username})"
                vals['sub_username'] = f"{user.name}({sub_username})"
                print(vals)
        return super().create(vals_list)
