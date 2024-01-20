import re

def has_repeated_substring(s):
    pattern = r'(.)\1+'
    result = re.search(pattern, s)
    if result:
        return True
    else:
        return False

s=input("请输入字符串:")
#s = 'abccccda'
print(has_repeated_substring(s))  # 输出 True