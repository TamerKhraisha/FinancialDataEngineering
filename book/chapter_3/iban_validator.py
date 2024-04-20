def is_valid_iban(iban_code: str):
    """Checks the validity of a Luxembourgish IBAN code"""
    if not iban_code.isalnum():
        print("IBAN must be alphanumeric")
        return False

    # Move the first four characters to the end of the string
    shuffled_iban_code = iban_code[4:] + iban_code[:4]

    # Convert letters to numbers
    numeric_iban_sequence: str = ""
    for char in shuffled_iban_code:
        if char.isalpha():
            numeric_iban_sequence += str(ord(char) - ord("A") + 10)
            continue
        numeric_iban_sequence += char

    # Perform the check
    return int(numeric_iban_sequence) % 97 == 1

if __name__ == "__main__":
    
    valid_IBANs = [
        "AD1200012030200359100100",
        "AT611904300234573201",
        "BE68539007547034",
        "DK5000400440116243",
        "FI2112345600000785",
        "FR1420041010050500013M02606",
        "DE89370400440532013000",
        "IS140159260076545510730339",
        "LI21088100002324013AA",
        "LU280019400644750000"
    ]

    non_valid_IBANs = [
        "AD1200012030200359100101",
        "AT611904300234573202",
        "BE68539007547035",
        "DK5000400440116244",
        "FI2112345600000786",
        "FR1420041010050500013M02607",
        "DE89370400440532013001",
        "IS140159260076545510730340",
        "LI21088100002324013AB",
        "LU280019400644750001"
    ]

    # Test valid IBANs
    print("Testing valid IBANs")
    for IBAN in valid_IBANs:
        assert is_valid_iban(IBAN) == True, f"Error: {IBAN} is not a valid IBAN."

    # Test non-valid IBANs
    print("\nTesting non-valid IBANs")
    for non_valid_IBAN in non_valid_IBANs:
        assert is_valid_iban(non_valid_IBAN) == False, f"Error: {non_valid_IBAN} is a valid IBAN."
