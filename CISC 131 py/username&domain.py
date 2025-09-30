def username(email):
    return email[0 : email.index("@")]

def username2(email):
    user = ""
    for i in range(len(email)):
        if email[i] == "@":
            return user
        else:
            user += email[i]


def domain(email):
    return email[email.index("@")+1 : len(email)]

def domain2(email):
    domain = ""
    for i in range(len(email)-1, 0, -1):
        if email[i] == "@":
            return domain
        else:
            domain = email[i] + domain

print(username("kana9520@stthomas.edu"))
print(username2("kana9520@stthomas.edu"))
print(domain("kana9520@stthomas.edu"))
print(domain2("kana9520@stthomas.edu"))
