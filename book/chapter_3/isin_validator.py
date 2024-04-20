def is_valid_isin(isin_code: str):
    if not isin_code.isalnum():
        print("ISIN must be alphanumeric")
        return False
    if not len(isin_code) == 12:
        print("ISIN must be 12 characters")
        return False

    # Convert letters to numbers excluding the check digit
    numeric_isin_code: str = ""
    for char in isin_code.upper()[:-1]:
        if char.isalpha():
            numeric_isin_code += str(ord(char) - 55)
            continue
        numeric_isin_code += char

    # Double even digits and sum
    final_sum: int = 0
    for idx, item in enumerate(numeric_isin_code[::-1], start=1):
        if idx % 2 == 0:
            final_sum += int(item)
            continue
        final_sum += int(int(2 * int(item)) / 10) + int(2 * int(item)) % 10
    
    # Calculate and validate check digit
    check_digit: int = (10 - (final_sum % 10)) % 10
    return str(check_digit) == isin_code[-1]

if __name__ == "__main__":

    valid_isins = [
        "US0378331005",  # Apple Inc. (AAPL)
        "US5949181045",  # Microsoft Corporation (MSFT)
        "US0231351067",  # Amazon.com Inc. (AMZN)
        "US02079K3059",  # Alphabet Inc. (GOOGL)
        "US59156R1086"   # Meta Platforms, Inc. (META)
    ]

    non_valid_isins = [
        "US0378331004",
        "DE000BASF112",
        "JP3435000000",
        "GB0009063712",
        "FR0000120270"
    ]


    # Test valid ISINs
    print("Testing valid ISINs")
    for isin in valid_isins:
        assert is_valid_isin(isin) == True, f"Error: {isin} is not a valid ISIN."

    # Test non-valid ISINs
    print("\nTesting non-valid ISINs")
    for non_valid_isin in non_valid_isins:
        assert is_valid_isin(non_valid_isin) == False, f"Error: {non_valid_isin} is a valid ISIN."
