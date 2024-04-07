BEGIN;

-- Transaction 1
INSERT INTO transaction (account_id, type, currency, date, amount)
VALUES (1, 4, 'USD', '2022-01-01 08:00:00', -40.00);
UPDATE account
SET balance = balance - 40.00
WHERE id = 1;

-- Transaction 2
INSERT INTO transaction (account_id, type, currency, date, amount)
VALUES (2, 4, 'USD', '2022-01-02 09:00:00', -233.00);
UPDATE account
SET balance = balance -233.00
WHERE id = 2;

-- Transaction 3
INSERT INTO transaction (account_id, type, currency, date, amount)
VALUES (3, 4, 'USD', '2022-01-03 10:00:00', -3.00);
UPDATE account
SET balance = balance - 3.00
WHERE id = 3;

-- Transaction 4
INSERT INTO transaction (account_id, type, currency, date, amount)
VALUES (4, 4, 'USD', '2022-01-04 11:00:00', -55.00);
UPDATE account
SET balance = balance - 55.00
WHERE id = 4;

-- Transaction 5
INSERT INTO transaction (account_id, type, currency, date, amount)
VALUES (5, 4, 'USD', '2022-01-05 12:00:00', -784.20);
UPDATE account
SET balance = balance - -784.20
WHERE id = 5;

-- Transaction 6
INSERT INTO transaction (account_id, type, currency, date, amount)
VALUES (1, 4, 'USD', '2022-01-06 13:00:00', -4.00);
UPDATE account
SET balance = balance - 4.00
WHERE id = 1;

-- Transaction 7
INSERT INTO transaction (account_id, type, currency, date, amount)
VALUES (2, 4, 'USD', '2022-01-07 14:00:00', -22.30);
UPDATE account
SET balance = balance -22.30
WHERE id = 2;

-- Transaction 8
INSERT INTO transaction (account_id, type, currency, date, amount)
VALUES (3, 4, 'USD', '2022-01-08 15:00:00', -346.00);
UPDATE account
SET balance = balance -346.00
WHERE id = 3;

-- Transaction 9
INSERT INTO transaction (account_id, type, currency, date, amount)
VALUES (4, 4, 'USD', '2022-01-09 16:00:00', -11.00);
UPDATE account
SET balance = balance - 11.00
WHERE id = 4;

-- Transaction 10
INSERT INTO transaction (account_id, type, currency, date, amount)
VALUES (5, 4, 'USD', '2022-01-10 17:00:00', -12.20);
UPDATE account
SET balance = balance - 12.20
WHERE id = 5;

COMMIT;BEGIN;

-- Transaction 1
INSERT INTO transaction (account_id, type, currency, date, amount)
VALUES (1, 4, 'USD', '2022-01-01 08:00:00', -444.22);
UPDATE account
SET balance = balance - 444.22
WHERE id = 1;

-- Transaction 2
INSERT INTO transaction (account_id, type, currency, date, amount)
VALUES (2, 4, 'USD', '2022-01-02 09:00:00', -66.20);
UPDATE account
SET balance = balance -66.20
WHERE id = 2;

-- Transaction 3
INSERT INTO transaction (account_id, type, currency, date, amount)
VALUES (3, 4, 'USD', '2022-01-03 10:00:00', -123.00);
UPDATE account
SET balance = balance - 123.00
WHERE id = 3;

-- Transaction 4
INSERT INTO transaction (account_id, type, currency, date, amount)
VALUES (4, 4, 'USD', '2022-01-04 11:00:00', -5000.00);
UPDATE account
SET balance = balance - 5000.00
WHERE id = 4;

-- Transaction 5
INSERT INTO transaction (account_id, type, currency, date, amount)
VALUES (5, 4, 'USD', '2022-01-05 12:00:00', -454.22);
UPDATE account
SET balance = balance - 454.22
WHERE id = 5;

-- Transaction 6
INSERT INTO transaction (account_id, type, currency, date, amount)
VALUES (1, 4, 'USD', '2022-01-06 13:00:00', -1233.00);
UPDATE account
SET balance = balance - 1233.00
WHERE id = 1;

-- Transaction 7
INSERT INTO transaction (account_id, type, currency, date, amount)
VALUES (2, 4, 'USD', '2022-01-07 14:00:00', -22.20);
UPDATE account
SET balance = balance - 22.20
WHERE id = 2;

-- Transaction 8
INSERT INTO transaction (account_id, type, currency, date, amount)
VALUES (3, 4, 'USD', '2022-01-08 15:00:00', -3.00);
UPDATE account
SET balance = balance - 3.00
WHERE id = 3;

-- Transaction 9
INSERT INTO transaction (account_id, type, currency, date, amount)
VALUES (4, 4, 'USD', '2022-01-09 16:00:00', -98.00);
UPDATE account
SET balance = balance - 98.00
WHERE id = 4;

-- Transaction 10
INSERT INTO transaction (account_id, type, currency, date, amount)
VALUES (5, 4, 'USD', '2022-01-10 17:00:00', -50.00);
UPDATE account
SET balance = balance - 50.00
WHERE id = 5;

COMMIT;