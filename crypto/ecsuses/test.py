# tr = eval(open('tr').read())
flagtxt = open('flagtxt.py').read()
exec(flagtxt)
exit()
with open('flagtxtttt', 'w') as f:
    f.write(flagtxt.translate(tr))