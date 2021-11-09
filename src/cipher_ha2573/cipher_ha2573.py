def cipher(text, shift, encrypt=True):
    """
    This function will encrypt or decrypt text using caesar cipher method.

    Parameters
    ----------
    text : str
      A string for the text you wish to encrypt/decrypt.
    shift : int
      An integer for how many shift you want to do for the cipher.
    encrypt : bool, optional
      A boolean (True/False) indicating if you want to do encrypt/decrypt.

    Returns
    -------
    str
      The encrypted (or decrypted) text.

    Examples
    --------
    >>> from cipher_ha2573 import cipher_ha2573
    >>> text = "Succession"
    >>> shift = 1
    >>> cipher_ha2573.cipher(text, shift, True)
    'Tvddfttjpo'
    
    Other examples for decrypting
    >>> from cipher_ha2573 import cipher_ha2573
    >>> text = "Tvddfttjpo"
    >>> shift = 1
    >>> cipher_ha2573.cipher(text, shift, False)
    'Succession'
    """
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_text = ''
    for c in text:
        index = alphabet.find(c)
        if index == -1:
            new_text += c
        else:
            new_index = index + shift if encrypt == True else index - shift
            new_index %= len(alphabet)
            new_text += alphabet[new_index:new_index+1]
    return new_text