# receiving energy data (Joules) ->myfunc
# batch 100 at a time & take average
# use global vars to keep track


ctr = 0
sum = 0.0

def myfunc(float energy):

    ctr = ctr + 1
    #sum 100, take & return average
    sum = sum + energy
    if (ctr == 100):
        ret = sum/ctr
        sum = 0
        ctr = 0
        return ret