# Python code for checking cusip
def is_valid_cusip(cusip_code: str):

    if not len(cusip_code) == 9:
        print("CUSIP must be 9 characters.")
        return False

    alpha_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ*@#"
    total_sum: int = 0
    for idx, char in enumerate(cusip_code[:-1].upper()):
        if char.isdigit():
            val = int(char)
        else:
            val = (alpha_chars.index(char) + 1) + 9
        if (idx % 2) != 0:
            val = val * 2
        total_sum += (val % 10) + (val // 10)

    check_digit = (10 - (total_sum % 10)) % 10
    return str(check_digit) == cusip_code[-1]

if __name__ == "__main__":
    
    valid_cusips = [
        "037833100",  # Apple Inc. (AAPL)
        "594918104",  # Microsoft Corporation (MSFT)
        "023135106",  # Amazon.com Inc. (AMZN)
        "02079K305",  # Alphabet Inc. (GOOGL)
        "59156R108"   # Meta Platforms, Inc. (META)
    ]

    non_valid_cusips = [
        "A1234567",  # First character is alphabetical
        "1234567$",  # Last character is not alphanumeric
        "ABCDEFG",   # Less than 9 characters
        "WXYZ12345", # More than 9 characters
        "987654320"  # Check digit is incorrect
    ]


    # Test valid CUSIPs
    print("Testing valid CUSIPs")
    for cusip in valid_cusips:
        assert is_valid_cusip(cusip) == True, f"Error: {cusip} is not a valid ISIN."

    # Test non-valid CUSIPs
    print("\nTesting non-valid CUSIPs")
    for non_valid_cusip in non_valid_cusips:
        assert is_valid_cusip(non_valid_cusip) == False, f"Error: {non_valid_cusip} is a valid ISIN."
