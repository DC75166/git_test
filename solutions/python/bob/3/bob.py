"""This is a if-else problem statment for chaining different methods and returning an answer for each condition"""
def response(hey_bob):
    """This is an if-else problem where we tackle different conditions"""
    new_string = hey_bob.strip()
    if new_string.endswith("?") and not hey_bob.isupper():
        return "Sure."
    if hey_bob.isupper() and not hey_bob.endswith("?"):
        return "Whoa, chill out!"
    if hey_bob.isupper() and "?" in hey_bob:
        return "Calm down, I know what I'm doing!"
    if not new_string:
        return "Fine. Be that way!"
    return "Whatever."
