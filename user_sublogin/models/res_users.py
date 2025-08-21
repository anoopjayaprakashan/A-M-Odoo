# -*- coding: utf-8 -*-
###################################################################################

# Author       :  Anoop
# Copyright(c) :  2025-Present.
# License      :  LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

###################################################################################
from odoo import models, fields, _, api
from odoo.exceptions import AccessDenied
from odoo.http import request
from odoo.modules.registry import Registry


class ResUsers(models.Model):
    _inherit = "res.users"

    sub_user_ids = fields.One2many("res.users.subuser", "user_id", string="Sub Users")
    is_have_subuser = fields.Boolean("Is sub-user required", default=False)

    @classmethod
    def authenticate(cls, db, login, password):
        sub_user_password = request.params.get("sub_user_password") if request else None
        auth_info = super(ResUsers, cls).authenticate(db, login, password)

        if isinstance(auth_info, dict):
            uid = auth_info.get("uid")
        else:
            uid = auth_info

        if not uid:
            raise AccessDenied(_("Login failed."))

        registry = Registry(db)
        with registry.cursor() as cr:
            env = api.Environment(cr, uid, {})
            log_user = env['res.users'].sudo().search([('id', '=', uid)], limit=1)
            if log_user:
                if log_user.is_have_subuser:
                    if not sub_user_password:
                        raise AccessDenied(_("You must provide a sub-user password."))
                    subuser = env['res.users.subuser'].sudo().search([('user_id', '=', uid), ('password', '=', sub_user_password)], limit=1)
                    if not subuser:
                        raise AccessDenied(_("Invalid Sub-user password."))
                    if request:
                        request.session['sub_username'] = subuser.name
            else:
                raise AccessDenied(_("Login not found"))
        return auth_info
