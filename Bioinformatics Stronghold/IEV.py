a = 16826 #AA-AA
b = 19616 #AA-Aa
c = 16063 #AA-aa
d = 18864 #Aa-Aa
e = 19562 #Aa-aa
f = 19165 #aa-aa

Da = 2*a #AA, AA, AA, AA
Db = 2*b #AA, AA, Aa, Aa
Dc = 2*c #Aa, Aa, Aa, Aa
Dd = 1.5*d #AA, Aa, Aa, aa
De = 1*e #Aa, Aa, aa, aa
Df = 0*f #aa, aa, aa, aa

totalD = Da+Db+Dc+Dd+De+Df

print totalD