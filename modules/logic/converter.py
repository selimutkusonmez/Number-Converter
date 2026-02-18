def converter(input_type,input):
    if input_type == "Binary":
        decimal_value = int(input,2)
        return str(decimal_value),format(decimal_value, 'o'),format(decimal_value, 'X')
    elif input_type == "Decimal":
        decimal_value = int(input,10)
        return format(decimal_value, 'b'),format(decimal_value, 'o'),format(decimal_value, 'X')
    elif input_type == "Octal":
        decimal_value = int(input,8)
        return format(decimal_value, 'b'),str(decimal_value),format(decimal_value, 'X')
    elif input_type == "Hex":
        decimal_value = int(input,16)
        return format(decimal_value, 'b'),str(decimal_value),format(decimal_value, 'o')
