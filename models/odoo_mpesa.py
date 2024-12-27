from odoo import http
from odoo.http import request

class MpesaCallbackController(http.Controller):
    @http.route('/mpesa/callback', type='json', auth='public', methods=['POST'])
    def mpesa_callback(self, **post):
        data = request.jsonrequest
        transaction_type = data.get("TransactionType")
        trans_id = data.get("TransID")
        trans_time = data.get("TransTime")
        trans_amount = data.get("TransAmount")
        business_shortcode = data.get("BusinessShortCode")
        bill_ref_number = data.get("BillRefNumber")
        invoice_number = data.get("InvoiceNumber")
        org_account_balance = data.get("OrgAccountBalance")
        third_party_trans_id = data.get("ThirdPartyTransID")
        msisdn = data.get("MSISDN")
        first_name = data.get("FirstName")
        middle_name = data.get("MiddleName")
        last_name = data.get("LastName")

        payment = request.env['account.payment'].sudo().search([('reference', '=', bill_ref_number)], limit=1)
        if payment:
            payment.sudo().write({
                'mpesa_transaction_id': trans_id,
                'amount': float(trans_amount),
                'payment_date': trans_time,
                'payer_name': f"{first_name} {middle_name} {last_name}",
            })
            return {'status': 'success', 'message': 'Payment updated successfully'}

        return {'status': 'error', 'message': 'Payment record not found'}
