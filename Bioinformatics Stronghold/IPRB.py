hD = 15.0 #homoD
ht = 28.0 #hetero
hR = 16.0 #homoR
total = hD+ht+hR

r1 = (ht/total)*((ht-1.0)/(total-1.0))/4.0 #hetero*hetero
r2 = (ht/total)*(hR/(total-1.0))/2.0 #hetero*homoR
r3 = (hR/total)*(ht/(total-1.0))/2.0 #homoR*hetero
r4 = (hR/total)*((hR-1.0)/(total-1.0)) #homoR*homoR
rr = r1+r2+r3+r4
dd = 1.0-rr
print dd