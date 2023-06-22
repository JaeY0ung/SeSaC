import sys

def convert_case(text):
    mystr = ""
    for s in text:
        if s == s.upper():
            mystr += s.lower()
        else:
            mystr += s.upper()
    return mystr
x = sys.stdin.readline().strip()

print(f"변환된 문장은 {convert_case(x)} 입니다.")