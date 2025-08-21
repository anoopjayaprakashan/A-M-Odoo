# -*- coding: utf-8 -*-
###################################################################################

# Author       :  Anoop
# Copyright(c) :  2025-Present.
# License      :  LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

###################################################################################
{
    "name": "Unified Access Manager",
    "summary": """ Module to manage sublogin for each user """,
    "description": """ Module to manage sublogin for each user """,
    "category": "Extra Tools",
    "version": "18.0.1.0.0",
    "author": "Anoop",
    "maintainer": "Anoop",
    "license": "LGPL-3",
    "depends": ['base',
                'web',
                'mail'],
    "data": ['security/ir.model.access.csv',
             'views/sub_user.xml',
             'views/login_page.xml'],
    'assets': {
        'web.assets_backend': [
            'user_sublogin/static/src/js/message_patch.js',
        ],
    },
    "images": ['static/description/banner.png'],
    "installable": True,
    "application": False,
    "auto_install": False,
}
