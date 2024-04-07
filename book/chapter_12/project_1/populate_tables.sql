-- CustomerStatusType
INSERT INTO CustomerStatusType (id, name, description) VALUES
(1, 'Active', 'Active customer'),
(2, 'Inactive', 'Inactive customer'),
(3, 'Blocked', 'Blocked customer'),
(4, 'Closed', 'Closed customer'),
(5, 'Pending', 'Pending approval');

-- AccountStatusType
INSERT INTO AccountStatusType (id, name, description) VALUES
(1, 'Active', 'Active account'),
(2, 'Inactive', 'Inactive account'),
(3, 'Blocked', 'Blocked account'),
(4, 'Closed', 'Closed account');

-- LoanStatusType
INSERT INTO LoanStatusType (id, name, description) VALUES
(1, 'Active', 'Active loan'),
(2, 'Closed', 'Closed loan'),
(3, 'Pending', 'Pending approval'),
(4, 'Defaulted', 'Defaulted loan'),
(5, 'Paid Off', 'Paid off loan');

-- CustomerType
INSERT INTO CustomerType (id, name, description) VALUES
(1, 'Individual', 'Individual customer'),
(2, 'Corporate', 'Corporate customer'),
(3, 'VIP', 'VIP customer'),
(4, 'SME', 'Small and Medium Enterprise'),
(5, 'Government', 'Government institution');

-- TransactionType
INSERT INTO TransactionType (id, name, description) VALUES
(1, 'Deposit', 'Deposit transaction'),
(2, 'Withdrawal', 'Withdrawal transaction'),
(3, 'Transfer', 'Transfer transaction'),
(4, 'Payment', 'Payment transaction'),
(5, 'Adjustment', 'Adjustment transaction');

-- AccountType
INSERT INTO AccountType (id, name, description) VALUES
(1, 'Savings', 'Savings account'),
(2, 'Checking', 'Checking account'),
(3, 'Credit', 'Credit account'),
(4, 'Loan', 'Loan account'),
(5, 'Investment', 'Investment account');

-- CardType
INSERT INTO CardType (id, name, description) VALUES
(1, 'Debit', 'Debit card'),
(2, 'Credit', 'Credit card'),
(3, 'Prepaid', 'Prepaid card'),
(4, 'Gold', 'Gold card'),
(5, 'Platinum', 'Platinum card');

-- LoanType
INSERT INTO LoanType (id, name, description) VALUES
(1, 'Personal', 'Personal loan'),
(2, 'Mortgage', 'Mortgage loan'),
(3, 'Auto', 'Auto loan'),
(4, 'Business', 'Business loan'),
(5, 'Education', 'Education loan');


-- Branch
INSERT INTO Branch (id, name, address, phone_number) VALUES
(1, 'Main Branch', '123 Main St, Cityville', '123-456-7890'),
(2, 'North Branch', '456 North St, Townsville', '456-789-0123'),
(3, 'South Branch', '789 South St, Villageton', '789-012-3456'),
(4, 'West Branch', '321 West St, Hamletown', '321-654-9870'),
(5, 'East Branch', '654 East St, Suburbia', '654-987-0123');

-- Employee
INSERT INTO Employee (branch_id, name, position) VALUES
(1, 'John Doe', 'Manager'),
(2, 'Jane Smith', 'Teller'),
(3, 'Bob Johnson', 'Advisor'),
(4, 'Alice Brown', 'Teller'),
(5, 'Emily Davis', 'Advisor');

-- Customer
INSERT INTO Customer (customer_type_id, name, country, city, street, phone_number, email, status) VALUES
(1, 'John Smith', 'US', 'New York', '123 Main St', '123-456-7890', 'john@example.com', 1),
(2, 'ABC Inc.', 'US', 'Los Angeles', '456 Business Blvd', '456-789-0123', 'info@abcinc.com', 1),
(3, 'Mary Johnson', 'UK', 'London', '789 High St', '789-012-3456', 'mary@example.com', 1),
(1, 'Robert Brown', 'US', 'Chicago', '321 Elm St', '321-654-9870', 'robert@example.com', 3),
(4, 'XYZ Corp.', 'US', 'Houston', '654 Corporate Ave', '654-987-0123', 'info@xyzcorp.com', 2);

-- Account
INSERT INTO Account (customer_id, branch_id, type, currency, number, balance, minimum_balance, date_opened, status) VALUES
(1, 1, 1, 'USD', 'SAV123456', 1000.00, 0, '2022-01-01', 1),
(2, 2, 2, 'USD', 'CHK789012', 5000.00, -100, '2022-02-01', 1),
(3, 3, 4, 'USD', 'LOAN345678', 25000.00, -1000, '2022-03-01', 1),
(4, 4, 1, 'USD', 'SAV901234', 2000.00, 0, '2022-04-01', 2),
(5, 5, 3, 'USD', 'CREDIT567890', 1500.00, -50, '2022-05-01', 3);

-- Loan
INSERT INTO Loan (customer_id, load_type_id, amount, interest_rate, term, start_date, end_date, loan_status_type) VALUES
(3, 1, 20000.00, 5.0, 36, '2022-03-01', '2025-03-01', 1),
(5, 2, 10000.00, 4.5, 60, '2022-05-01', '2027-05-01', 2),
(1, 3, 5000.00, 6.0, 24, '2022-01-01', '2024-01-01', 3),
(2, 4, 30000.00, 5.5, 48, '2022-02-01', '2026-02-01', 4),
(4, 5, 15000.00, 6.5, 36, '2022-04-01', '2025-04-01', 5);

-- LoanPayment
INSERT INTO LoanPayment (loan_id, payment_amount, scheduled_payment_date, payment_date, principal_amount, interest_amount, paid_amount) VALUES
(1, 500.00, '2022-02-01', '2022-02-01', 400.00, 100.00, 500.00),
(2, 300.00, '2022-02-01', '2022-02-01', 250.00, 50.00, 300.00),
(3, 200.00, '2022-02-01', '2022-02-01', 150.00, 50.00, 200.00);

-- Card
INSERT INTO Card (account_id, customer_id, card_type_id, monthly_fee, interest_rate, expiration_date, issuance_date)
VALUES
(1, 1, 1, 5.00, 18.99, '2023-05-31', '2022-05-01'),
(2, 2, 2, 7.50, 21.50, '2024-08-31', '2022-08-15'),
(3, 3, 3, 3.50, 15.25, '2022-12-31', '2022-06-10'),
(4, 4, 1, 5.00, 18.99, '2023-10-31', '2022-09-20'),
(5, 5, 2, 6.00, 20.00, '2024-02-28', '2022-12-05');
