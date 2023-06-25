import secrets
import sys
import string


def main():
    fq = input("Do you wanna generate a new password? ").strip().lower()
    if fq not in ["no", "yes"]:
        raise ValueError("Please, answear the question!")
    if fq == "yes":
        while True:
            try:
                length = input("Gimme a length for your password: ")
                if int(length) >= 8:
                    print(generate(length))
                    break
                else:
                    print("Number must be equal or greater than 8")
            except ValueError:
                length = input("Gimme a length for your password: ")
                if int(length) >= 8:
                    print(generate(length))
                    break
                else:
                    print("Number must be equal or greater than 8")
                pass

    sq = input("Do you wanna check if a password is strong enough? ").strip().lower()
    if sq not in ["no", "yes"]:
        raise ValueError("Please, answear the question!")
    if sq == "yes":
        password = input("Write your password here: ")
        r = check(password)
        print(r)
        if r != "Your password is just fine :)":
            ask = input("Do you wanna generate a new password? ").strip().lower()
            if ask == "yes":
                while True:
                    try:
                        length = input("Gimme a length for your password: ")
                        if int(length) >= 8:
                            print(generate(length))
                            break
                        else:
                            print("Number must be equal or greater than 8")
                    except ValueError:
                        length = input("Gimme a length for your password: ")
                        if int(length) >= 8:
                            print(generate(length))
                            break
                        else:
                            print("Number must be equal or greater than 8")
                        pass
            elif ask == "no":
                sys.exit()
        else:
            sys.exit()

    if fq == "no" and sq == "no":
        sys.exit()


def generate(length):
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation
    alphabet = letters + digits + special_chars
    length = int(length)
    password = ""
    for _ in range(length):
        password += "".join(secrets.choice(alphabet))
    return password


def check(password):
    pas = ""
    s = str(check_length(password))
    if s != "None":
        pas = s + "\n"
    s = str(check_special(password))
    if s != "None":
        pas = pas + s + "\n"
    s = str(check_a_z(password))
    if s != "None":
        pas = pas + s + "\n"
    s = str(check_num(password))
    if s != "None":
        pas = pas + s + "\n"
    if pas == "":
        pas = "Your password is just fine :)"
    return pas


def check_length(password):
    if len(password) < 8:
        s = "❗Your password is too short"
        return s


def check_special(password):
    ok = 0
    for c in password:
        if c.isalnum() == True:
            ok += 1
    if ok == len(password):
        s = "❗Your password doesn't contain special characters"
        return s


def check_a_z(password):
    ok2 = 0
    for z in password:
        if z.isupper() == True:
            ok2 += 1
    if ok2 == 0:
        s = "❗Your password doesn't contain A-Z letters"
        return s


def check_num(password):
    ok3 = 0
    for w in password:
        if w.isnumeric() == True:
            ok3 += 1
    if ok3 == 0:
        s = "❗Your password doesn't contain numbers"
        return s


if __name__ == "__main__":
    main()
