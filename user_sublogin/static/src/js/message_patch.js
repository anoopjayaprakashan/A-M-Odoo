/** @odoo-module **/
/**  Author       :  Anoop  **/
/**  Copyright(c) :  2025-Present.  **/
/**  License      :  LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).  **/

import { patch } from "@web/core/utils/patch";
import { Message } from "@mail/core/common/message";

patch(Message.prototype, {
    get authorName() {
    console.log(this.message.sub_username,'=========');
        if (this.message.email_from) {
            return this.message.email_from;
        }
        if (this.message.author) {
            return this.message.author.name;
        }
        return "";
    },
});
