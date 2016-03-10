# -*- coding: utf-8 -*-
#using Tomohiko Sakamoto's Algorithm



def date(day,month,year):
    d = day
    m = month
    y = year
    if m < 3:
        data = y-1
    else:
        data = y
    dayy = ( 23*m//9 + d + 4 + y + data//4 - data//100 + data//400 )
    if m >= 3 and m <13:
        dayy -= 2
    dayy= dayy%7
    return dayy
    
    
    

#αρχή της εβδομάδας απο την Κυριακή
Days = ['Sunday' ,'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
       

#εισαγωγή ημερομηνίας της μορφής ηη//μμ/εεεε
d,m,y= [int(x) for x in raw_input("Please enter a date with the following form DD/MM/YYYY").split('/')]
#αντιστοίχηση κωδικού με ημέρα μεσω συνάρτησης date
dayy = Days[date(d, m, y)]
print  dayy
