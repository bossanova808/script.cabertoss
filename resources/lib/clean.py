import re


def clean_log(content):
    """
    Sanitize log text by replacing embedded usernames and passwords with generic placeholders.
    
    Replaces URL credentials (user:pass@), contents of <user>...</user>, and <pass>...</pass> with
    `//USER:PASSWORD@`, `<user>USER</user>`, and `<pass>PASSWORD</pass>` respectively.
    
    Parameters:
        content (str): Log file content to sanitize.
    
    Returns:
        str: Sanitized content with credential data redacted.
    """
    replaces = (('//.+?:.+?@', '//USER:PASSWORD@'), ('<user>.+?</user>', '<user>USER</user>'), ('<pass>.+?</pass>', '<pass>PASSWORD</pass>'),)

    for pattern, repl in replaces:
        content = re.sub(pattern, repl, content)
    return content
