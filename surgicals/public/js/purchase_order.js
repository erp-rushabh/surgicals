frappe.ui.form.on('Purchase Order', {
    
    schedule_date: function(frm) {
        let schedule_date = frm.doc.schedule_date;

        if (!frm.doc.items) return;

        frm.doc.items.forEach(row => {
            frappe.model.set_value(row.doctype, row.name, 'schedule_date', schedule_date);
        });

        frm.refresh_field('items');
    },

    scan_barcode: function(frm) {
        const barcode = frm.doc.scan_barcode;
        if (!barcode) return;

        frm.set_value('tax_category', 'In-State');

        frappe.call({
            method: 'surgicals.api.get_serial_expiry_from_barcode',
            args: { barcode: barcode },
            callback: function(r) {
                if (!r.message) {
                    frappe.msgprint(__('Barcode not found or not linked to any item.'));
                    frm.set_value('scan_barcode', '');
                    return;
                }

                const { item_code, item_name, uom, serial_no, expiry_date } = r.message;
                let items = frm.doc.items || [];
                let existing_row = null;

                for (let row of items) {
                    if (
                        row.item_code === item_code &&
                        row.serial_no === serial_no &&
                        row.expiry_date === expiry_date
                    ) {
                        existing_row = row;
                        break;
                    }
                }

                if (existing_row) {
                    frappe.model.set_value(existing_row.doctype, existing_row.name, 'qty', existing_row.qty + 1);
                    frappe.model.set_value(existing_row.doctype, existing_row.name, 'schedule_date', frm.doc.schedule_date);
                }

                else if (items.length === 1 && !items[0].item_code) {
                    let row = items[0];

                    frappe.model.set_value(row.doctype, row.name, 'item_code', item_code);
                    frappe.model.set_value(row.doctype, row.name, 'item_name', item_name);
                    frappe.model.set_value(row.doctype, row.name, 'uom', uom);
                    frappe.model.set_value(row.doctype, row.name, 'serial_no', serial_no);
                    frappe.model.set_value(row.doctype, row.name, 'expiry_date', expiry_date);
                    frappe.model.set_value(row.doctype, row.name, 'qty', 1);
                    frappe.model.set_value(row.doctype, row.name, 'schedule_date', frm.doc.schedule_date);
                }
                else {
                    let new_row = frm.add_child('items');
                    frappe.model.set_value(new_row.doctype, new_row.name, 'item_code', item_code);
                    frappe.model.set_value(new_row.doctype, new_row.name, 'item_name', item_name);
                    frappe.model.set_value(new_row.doctype, new_row.name, 'uom', uom);
                    frappe.model.set_value(new_row.doctype, new_row.name, 'serial_no', serial_no);
                    frappe.model.set_value(new_row.doctype, new_row.name, 'expiry_date', expiry_date);
                    frappe.model.set_value(new_row.doctype, new_row.name, 'qty', 1);
                    frappe.model.set_value(new_row.doctype, new_row.name, 'schedule_date', frm.doc.schedule_date);
                }

                frm.refresh_field('items');
                frm.set_value('scan_barcode', '');
            }
        });
    }
});
