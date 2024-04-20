def is_valid_figi(figi_code: str):
     
    if not figi_code.isalnum():
        print("FIGI must be alphanumeric")
        return False
    if not len(figi_code) == 12:
        print("FIGI must be 12 characters")
        return False

    # Convert letters to numbers excluding the check digit
    numeric_figi_characters: list[int] = []
    for char in figi_code.upper()[:-1]:
        if char.isalpha():
            numeric_figi_characters.append(ord(char) - ord("A") + 10)
            continue
        numeric_figi_characters.append(int(char))
    figi_adjusted_characters: str = ""
    for idx, item in enumerate(numeric_figi_characters, start=1):
        if idx % 2 != 0:
            figi_adjusted_characters += str(item)
            continue
        figi_adjusted_characters += str(item * 2)
    final_sum = sum(map(int, figi_adjusted_characters))

    check_digit: int = (10 - final_sum % 10) % 10
    return str(check_digit) == figi_code[-1]

if __name__ == "__main__":
    
    valid_figis = [
        "BBG000B9XVV8",  # Apple Inc. (AAPL)
        "BBG000BPH459",  # Microsoft Corporation (MSFT)
        "BBG000BVPXP1",  # Amazon.com Inc. (AMZN)
        "BBG009S39JX6",  # Alphabet Inc. (GOOGL)
        "BBG000MM2P62"   # Meta Platforms, Inc. (META)
    ]

    non_valid_figis = [
        "BBG000B9XVV1",  # Incorrect check digit for Apple Inc. (AAPL)
        "BBG000BPH450",  # Incorrect check digit for Microsoft Corporation (MSFT)
        "BBG000BVPXP9",  # Incorrect check digit for Amazon.com Inc. (AMZN)
        "BBG009S39JX1",  # Incorrect check digit for Alphabet Inc. (GOOGL)
        "BBG000MM2P60"   # Incorrect check digit for Meta Platforms, Inc. (META)
    ]


    # Test valid FIGIs
    print("Testing valid FIGIs")
    for figi in valid_figis:
        assert is_valid_figi(figi) == True, f"Error: {figi} is not a valid FIGI."

    # Test non-valid FIGIs
    print("\nTesting non-valid FIGIs")
    for non_valid_figi in non_valid_figis:
        assert is_valid_figi(non_valid_figi) == False, f"Error: {non_valid_figi} is a valid FIGI."