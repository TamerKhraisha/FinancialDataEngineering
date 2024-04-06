-- CustomerStatusType
CREATE TABLE CustomerStatusType (
    id SERIAL PRIMARY KEY,
    name VARCHAR(10) NOT NULL,
    description VARCHAR(50) NOT NULL
);

-- AccountStatusType
CREATE TABLE LoanStatusType (
    id SERIAL PRIMARY KEY,
    name VARCHAR(10) NOT NULL,
    description VARCHAR(50) NOT NULL
);

-- Branch
CREATE TABLE Branch (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    address VARCHAR(100) NOT NULL,
    phone_number VARCHAR(20) NOT NULL
);

-- Employee
CREATE TABLE Employee (
    id SERIAL PRIMARY KEY,
    branch_id INT NOT NULL REFERENCES Branch(id),
    name VARCHAR(50) NOT NULL,
    position VARCHAR(20) NOT NULL
);

-- CustomerType
CREATE TABLE CustomerType (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    description VARCHAR(50) NOT NULL
);

-- TransactionType
CREATE TABLE TransactionType (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    description VARCHAR(50) NOT NULL
);

-- AccountType
CREATE TABLE AccountType (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    description VARCHAR(50) NOT NULL
);

-- AccountStatusType
CREATE TABLE AccountStatusType (
    id SERIAL PRIMARY KEY,
    name VARCHAR(10) NOT NULL,
    description VARCHAR(50) NOT NULL
);

-- CardType
CREATE TABLE CardType (
    id SERIAL PRIMARY KEY,
    name VARCHAR(30) NOT NULL,
    description VARCHAR(100) NOT NULL
);

-- LoanType
CREATE TABLE LoanType (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    description VARCHAR(50) NOT NULL
);

-- Customer
CREATE TABLE Customer (
    id SERIAL PRIMARY KEY,
    customer_type_id INT NOT NULL REFERENCES CustomerType(id),
    name VARCHAR(100) NOT NULL,
    country VARCHAR NOT NULL,
    city VARCHAR(20) NOT NULL,
    street VARCHAR(30) NOT NULL,
    phone_number VARCHAR(20) NOT NULL,
    email VARCHAR(50) NOT NULL UNIQUE,
    registration_date DATE NOT NULL DEFAULT CURRENT_DATE,
    status INT NOT NUll REFERENCES CustomerStatusType(id)
);

-- Account
CREATE TABLE Account (
    id SERIAL PRIMARY KEY,
    customer_id INT NOT NULL REFERENCES Customer(id),
    branch_id INT NOT NULL REFERENCES Branch(id),
    type INT NOT NULL REFERENCES AccountType(id),
    number VARCHAR(50) NOT NULL UNIQUE,
    balance DECIMAL(10,2) NOT NULL,
    minimum_balance DECIMAL(10,2) NOT NULL DEFAULT 0,
    date_opened DATE NOT NULL,
    date_closed DATE,
    status INT NOT NULL REFERENCES AccountStatusType(id)
    CHECK (balance >= minimum_balance)
);

-- Loan
CREATE TABLE Loan (
    id SERIAL PRIMARY KEY,
    customer_id INT NOT NULL REFERENCES Customer(id),
    load_type_id INT NOT NULL REFERENCES LoanType(id),
    amount DECIMAL(10,2) NOT NULL,
    interest_rate DECIMAL(10,2) NOT NULL,
    term INT NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    loan_status_type INT NOT NULL REFERENCES LoanStatusType(id)
);

-- LoanPayment
CREATE TABLE LoanPayment (
    id SERIAL PRIMARY KEY,
    loan_id INT NOT NULL REFERENCES Loan(id),
    payment_amount DECIMAL(10,2) NOT NULL,
    scheduled_payment_date DATE NOT NULL,
    payment_date DATE NOT NULL,
    principal_amount DECIMAL(10,2) NOT NULL,
    interest_amount DECIMAL(10,2) NOT NULL,
    paid_amount DECIMAL(10,2) NOT NULL
);

-- Transaction
CREATE TABLE Transaction (
    id SERIAL PRIMARY KEY,
    account_id INT NOT NULL REFERENCES Account(id),
    employee_id INT NOT NULL REFERENCES Employee(id),
    type INT NOT NULL REFERENCES TransactionType(id),
    date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    amount DECIMAL(10,2) NOT NULL
);

-- Card
CREATE TABLE Card (
    id SERIAL PRIMARY KEY,
    account_id INT NOT NULL REFERENCES Account(id),
    customer_id INT NOT NULL REFERENCES Customer(id),
    card_type_id INT NOT NULL REFERENCES CardType(id),
    monthly_fee DECIMAL(10,2) NOT NULL,
    interest_rate DECIMAL(5,2) NOT NULL,
    expiration_date DATE NOT NULL,
    issuance_date DATE NOT NULL
);
