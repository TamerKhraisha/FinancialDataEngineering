def is_valid_sedol(sedol):
    if not sedol.isalnum() or len(sedol) != 7:
        print("SEDOL must be alphanumeric and 7 characters long")
        return False
    
    weights = (1, 3, 1, 7, 3, 9, 1)
    checksum = sum(weights[i] * (ord(char) - 48 if char.isdigit() else ord(char) - 55) for i, char in enumerate(sedol))
    return checksum % 10 == 0


if __name__ == "__main__":
    
    valid_sedols = [
        "0540528",
        "B0SWJX3"
    ]

    non_valid_sedols = [
        "1234567",
        "ABCDEFG",
        "ZYXWVUTR",
        "098765432",
        "12345678"
    ]


    # Test valid SEDOLs
    print("Testing valid SEDOLs")
    for sedol in valid_sedols:
        assert is_valid_sedol(sedol) == True, f"Error: {sedol} is not a valid SEDOL."

    # Test non-valid SEDOLs
    print("\nTesting non-valid SEDOLs")
    for non_valid_sedol in non_valid_sedols:
        assert is_valid_sedol(non_valid_sedol) == False, f"Error: {non_valid_sedol} is a valid SEDOL."