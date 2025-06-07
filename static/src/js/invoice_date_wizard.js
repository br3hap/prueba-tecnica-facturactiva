/** @odoo-module **/

import { registry } from "@web/core/registry";
import { Dialog } from "@web/core/dialog/dialog";
import { Component } from "@odoo/owl";
import { useService } from "@web/core/utils/hooks";

class InvoiceDateModal extends Component {
    setup() {
        this.rpc = useService("rpc");
        this.notification = useService("notification");
        console.log(" Componente cargado con props:", this.props);
    }

    async updateInvoiceDate() {
        const input = this.el.querySelector("#invoice_date_input");
        const newDate = input?.value;

        if (!newDate) {
            this.notification.add("Seleccione una fecha válida.", { type: "warning" });
            return;
        }

        await this.rpc.query({
            model: "account.move",
            method: "write",
            args: [[this.props.resId], { invoice_date: newDate }],
        });

        this.notification.add("Fecha actualizada con éxito.", { type: "success" });
        this.props.close();
    }

    cancel() {
        this.props.close();
    }
}

InvoiceDateModal.template = "prueba_facturactiva.InvoiceDateModalTemplate";

registry.category("actions").add("prueba_facturactiva.modal", (env, action) => {
    console.log("Modal lanzado correctamente  ->>>>");

    const recordId = action.context.active_id;

    new Dialog(env, {
        title: "Actualizar Fecha de Factura",
        size: "medium",
        body: {
            component: InvoiceDateModal,
            props: { resId: recordId },
        },
    });
});
