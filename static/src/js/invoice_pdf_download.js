/** @odoo-module **/

import { registry } from "@web/core/registry";

registry.category("actions").add("prueba_facturactiva.download_narration_pdf", (env, action) => {
    const base64 = action.params.pdf_base64;
    const filename = action.params.filename;

    const link = document.createElement("a");
    link.href = "data:application/pdf;base64," + base64;
    link.download = filename || "narracion.pdf";
    link.target = "_blank";
    link.click();
});
