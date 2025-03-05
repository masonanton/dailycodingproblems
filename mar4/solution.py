def count_decodings(message):
    # Get rid of base cases
    if not message: return 1
    
    if message[0] == '0': return 0

    if len(message) == 1: return 1
    else:
        if message[0] == '1' or (message[0] == '2' and message[1] in '0123456'):
            return count_decodings(message[1:]) + count_decodings(message[2:])
        else:
            return count_decodings(message[1:])





