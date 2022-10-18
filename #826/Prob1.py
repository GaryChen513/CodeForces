length = int(input())

for _ in range(length):
    s1, s2 = input().split(" ")

    mapping = {
        "SM": "<",
        "SL": "<",
        "MS": ">",
        "ML": "<",
        "LS": ">",
        "LM": ">"
    }

    if s1[-1] == s2[-1]:
        if len(s1) < len(s2):
            if s1[-1] == "S":
                print(">")
            else:
                print("<")
        elif len(s1) > len(s2):
            if s1[-1] == "S":
                print("<")
            else:
                print(">")
        else:
            print("=")
    else:
        print(mapping[s1[-1]+s2[-1]])