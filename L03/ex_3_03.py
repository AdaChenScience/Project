import re
def is_id_number(id_number):
    if len(id_number) != 18:
        return False
    regularExpression = "[1-9]\d{5}(18|19|([23]\d))\d{2}((0[1-9])|(10|11|12))(([0-2][1-9])|10|20|30|31)\d{3}[0-9Xx]"
    return True if re.match(regularExpression, id_number) else False
id=input('请输入身份证号:')
print(is_id_number(id))