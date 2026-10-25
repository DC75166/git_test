def response(hey_bob):
    pass
    new_string = hey_bob.strip()
    if new_string.endswith("?") and not hey_bob.isupper():
        return "Sure."
    elif hey_bob.isupper() and not hey_bob.endswith("?"):
        return "Whoa, chill out!"
    elif hey_bob.isupper() and "?" in hey_bob:
        return "Calm down, I know what I'm doing!"
    elif not new_string:
        return "Fine. Be that way!"
    return "Whatever."
