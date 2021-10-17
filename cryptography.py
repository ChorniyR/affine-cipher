ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
NUMBERS = '0123456789'

# dictionary in witch saved pairs {symbol: position} while encypting
saved_symbolds_indexes = {}


def _oreder_enc(symb, a, b):
    """
    symb: symbol from alphabet witch index should be returned.
    a, b: coefficients.
    Returns the index of symbol in the alphabet by formule f(x)=a*x+b % 26.
    """
    return (a * ALPHABET.index(symb.upper()) + b) % 26


def _order_enc_number(symb, a, b):
    return (a * NUMBERS.index(symb.upper()) + b) % 10


def _order_dec_number(symb, a, b):
    try:
        a = pow(a, -1, 10)
    except ValueError:
        print("Modular inverse does not exist")

    return a * (NUMBERS.index(symb.upper()) - b) % 10


def _oreder_dec(symb, a, b):
    """
    Returns the index of symbol in the alphabet by formule f(x)=a^-1 * (x-b) % 26.
    """
    try:
        a = pow(a, -1, 26)
    except ValueError:
        print("Modular inverse does not exist")

    return a * (ALPHABET.index(symb.upper()) - b) % 26


def _format_text(text):
    """Deletes special symbols from text"""
    special_symbols = ['!', '.', '<', '>', '_', '#', '-']
    formatted_text = ''.join(
        [symb for symb in text if symb not in special_symbols])
    return formatted_text


def _list(text):
    """
    Returns a list of words from text
    """
    return [word for word in text.replace(',', ' ').split(' ') if word != '']


def decrypt(text, a, b):
    """
    text: text that should be decrypted.
    a, b: coefficients.

    returns: the decrypted text.
    """
    text = text.replace('XMEZERAX', ' ')

    decrypted = []
    for word in _list(text):
        decrypted_word = ''
        for symb in list(word):
            if symb in NUMBERS:
                decrypted_word += decrypted_word.join(
                    NUMBERS[_order_dec_number(symb, a, b)])
                continue
            decrypted_word += decrypted_word.join(ALPHABET[_oreder_dec(
                symb, a, b)])

        decrypted.append(decrypted_word)

    #adds ',' like in original text
    decripted_symbols = [symb for symb in ' '.join(decrypted)]
    for pair in saved_symbolds_indexes:
        for symb, indx in pair.items():
            decripted_symbols[indx] = symb
            decripted_symbols.insert(indx + 1, " ")

    return ''.join(decripted_symbols)


def encrypt(text, a, b):
    """
    This method encrypt a string by Affine Chipher. 
    Also deletes special symboles like '!', '.', '<', '>', '_', '#', '-'
    Replaces sapaces with 'XMEZERAX'

    text: text that should be encrypted.
    a, b: coefficients.

    returns: the encrypted text.
    """
    formatted_text = _format_text(text)

    # saves ',' positions into the global variable, than it used to pass ',' into decoded text.
    global saved_symbolds_indexes
    saved_symbolds_indexes = [{
        ltr: i
    } for i, ltr in enumerate(formatted_text) if ltr == ',']

    encrypted = []
    for word in _list(formatted_text):
        encrypted_word = ''
        for symb in list(word):
            if symb in NUMBERS:
                encrypted_word += encrypted_word.join(
                    NUMBERS[_order_enc_number(symb, a, b)])
                continue
            encrypted_word += encrypted_word.join(ALPHABET[_oreder_enc(
                symb, a, b)])

        encrypted.append(encrypted_word)
    return 'XMEZERAX'.join(
        encrypted)  # spaces replaced with XMEZERAX by condition
