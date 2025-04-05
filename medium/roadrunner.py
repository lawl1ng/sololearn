#roadrunner
safe = int(input())
rs = int(input())
cs = int(input())

start = 50

# calculate time roadrunner takes to safety
# calculate time coyote gets to safety
# d=st
# roadrunner gets to safety by safe/rs
# coyote gets to safety by (safe + start)/cs

rtime = safe / rs
ctime = (safe + start) / cs
if rtime < ctime:
    print("Meep Meep")
else:
    print("Yum")
