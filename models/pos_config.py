from odoo import models, fields, api
from odoo.exceptions import ValidationError

class MpesaTransaction(models.Model):
    _name = 'mpesa.transaction'
    _description = 'Mpesa Transaction Data'

    transaction_id = fields.Char(
        string='Transaction ID',
        required=True,
        help="Unique identifier for the Mpesa transaction (e.g., MBN0000000)."
    )
    receipt_no = fields.Char(
        string='Receipt No',
        help="Unique receipt number for the transaction."
    )
    debit_party_name = fields.Char(
        string='Debit Party Name',
        help="Details of the debit party (e.g., 254708374149 - John Doe)."
    )
    initiated_time = fields.Datetime(
        string='Initiated Time',
        help="The time the transaction was initiated."
    )
    finalized_time = fields.Datetime(
        string='Finalized Time',
        help="The time the transaction was finalized."
    )
    transaction_status = fields.Selection(
        selection=[
            ('completed', 'Completed'),
            ('pending', 'Pending'),
            ('failed', 'Failed')
        ],
        string='Transaction Status',
        default='completed',
        help="The current status of the transaction."
    )
    amount = fields.Float(
        string='Amount',
        help="The transaction amount."
    )
    result_code = fields.Integer(
        string='Result Code',
        help="Result code indicating the outcome of the transaction (e.g., 0 for success)."
    )
    result_description = fields.Text(
        string='Result Description',
        help="A detailed description of the result (e.g., success message)."
    )
    conversation_id = fields.Char(
        string='Conversation ID',
        help="Conversation ID from Mpesa."
    )
    originator_conversation_id = fields.Char(
        string='Originator Conversation ID',
        help="Originator Conversation ID from Mpesa."
    )

    _sql_constraints = [
        ('unique_transaction_id', 'UNIQUE(transaction_id)', 'Transaction ID must be unique.'),
    ]

    @api.constrains('amount')
    def _check_positive_amount(self):
        for record in self:
            if record.amount <= 0:
                raise ValidationError("Transaction amount must be greater than zero.")
