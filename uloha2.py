def riadok(n, text=''):
    y=len(text)+1
    if text=="":
        print(sir*"*")
    else:
        x=((sir-len(text))/2)
        x=int(x)
        if 25 > len(text) > 14:
            print((x - 1) * "*", text, (x - 1) * "*")
        else:
            print((x - 1) * "*", text, x * "*")





sir = 40
riadok(sir)
riadok(sir, 'Ján Botto')
riadok(sir, 'Žltá ľalija')
riadok(sir, '-')
riadok(sir, 'Stojí stojí mohyla')
riadok(sir, 'Na mohyle zlá chvíľa')
riadok(sir, 'na mohyle tŕnie chrastie')
riadok(sir, "a v tom tŕní chrastí rastie")
riadok(sir)