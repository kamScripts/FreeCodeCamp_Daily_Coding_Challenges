import re
def is_spam(phone_number):
    """
    Spam detector for phone number in format: +A (BBB) CCC-DDDD
    
    The country code is greater than 2 digits long or doesn't begin with a zero (0).
    The area code is greater than 900 or less than 200.
    The sum of first three digits of the local number appears within last four digits
    of the local number. The number has the same digit four or more times in
    a row (ignoring the formatting characters).
    
    Returns: boolean
    """
    match = re.match(r'^\+(\d+)\s\((\d{3})\)\s(\d{3})-(\d{4})$', phone_number)
    if not match:
        return False  # Invalid format
    print(match.groups())
    country_code, area_code, local1, local2 = match.groups()

    if len(country_code) > 2 or not country_code.startswith('0'):
        return True

    area = int(area_code)
    if area < 200 or area > 900:
        return True

    sum_ccc = sum(int(d) for d in local1)
    if str(sum_ccc) in local2:
        return True

    digits_only = re.sub(r'\D', '', phone_number)
    print(digits_only)
    if re.search(r'(\d)\1{3,}', digits_only):
        return True

    return False

if __name__=="__main__":
    print(is_spam("+00 (555) 234-0152"))
    is_spam("+0 (200) 234-0182")