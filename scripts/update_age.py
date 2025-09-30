import re
from datetime import date

BIRTHDATE = date(1999, 10, 28) 

def calc_age(bd, today=None):
    today = today or date.today()
    return today.year - bd.year - ((today.month, today.day) < (bd.month, bd.day))

def update_file(path, age):
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()

    new_text, n = re.subn(r"(self\.age\s*=\s*)(\d+)", rf"\1{age}", text, count=1)

    if n == 0:
        new_text, n = re.subn(r"\{\{AGE\}\}", str(age), text, count=1)

    if new_text != text:
        with open(path, "w", encoding="utf-8") as f:
            f.write(new_text)
        print(f"Updated age to {age}")
        return True

    print("No change needed.")
    return False

if __name__ == "__main__":
    age = calc_age(BIRTHDATE)
    changed = update_file("README.md", age)
