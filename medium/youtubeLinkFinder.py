#youtube link finder
st = input().split("=")

if len(st) > 1:
    print(st[1])
elif len(st) == 1:
    st = st[0].split("be/")
    print(st[1])
