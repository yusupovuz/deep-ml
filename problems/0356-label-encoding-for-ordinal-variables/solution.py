def label_encode_ordinal(values: list, order: list) -> list:
    """
    Encode ordinal categorical values to integers based on specified order.
    
    Args:
        values: List of categorical values to encode
        order: List specifying the order of categories from lowest (0) to highest
    
    Returns:
        List of integers representing the encoded values
    """
    l = []
    for i in values:
        for j in range(len(order)):
            if i == order[j]:
                l.append(j)
    if len(l) == len(values):
        return l
    l.append(-1)
    return l
    