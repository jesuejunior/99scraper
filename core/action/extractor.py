__author__ = 'jesuejunior'
import re

def _extract(data):
    number = None
    try:
        number = int(data)
    except Exception:
        pass
    if not isinstance(number, int):
        number = re.findall('(\d+\.?\d+)' , data.replace(',', ''))[0]
    try:
        number = int(number)
    except Exception as e:
        number = float(number)
    return number



