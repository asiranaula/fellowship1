def filter_nondigits(data: list) -> list:
    non_dig = []
    for num in data:
        if num.strip().isdigit() == True:
            num = num.strip()
            house.append(int(num))

    return non_dig

    """
    Filter all strings from list that are not integers

    Args:
        data (list[str]): list of strings representing heart rate samples.
            Might contain invalid or missing data.
    Returns:
        list[int]: list of integers, with all non-digit strings removed
    """
    

[]
def filter_outliers(data: list) -> list:
    pass
