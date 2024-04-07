BEGIN;
DO $$
DECLARE
    payment_amount DECIMAL := 1000.00;
BEGIN
    WITH inserted_transaction AS (
        INSERT INTO Transaction (account_id, type, currency, amount)
        VALUES (1, 1, 'USD', -payment_amount)
        RETURNING id
    )
    INSERT INTO LoanPayment (loan_id, transaction_id, payment_amount, scheduled_payment_date, payment_date, principal_amount, interest_amount, paid_amount)
    SELECT 1, id, payment_amount, '2022-04-01', '2022-04-01', 900.00, 100.00, payment_amount
    FROM inserted_transaction;

    UPDATE account
    SET balance = balance - payment_amount
    WHERE id = 1;
END$$;
COMMIT;