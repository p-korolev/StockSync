def find_b0(xval, yval, b1):
    ymean = sum(yval)/len(yval)
    xmean = sum(xval)/len(xval)
    return (ymean - (b1*xmean))

def find_b1(xval, yval):
    xmean = sum(xval)/len(xval)
    ymean = sum(yval)/len(yval)

    num_sum = 0
    den_sum = 0
    for i in range(len(xval)):
        num_sum += (xval[i] - xmean)*(yval[i] - ymean)
        den_sum += (xval[i] - xmean)**2
    
    b1_val = num_sum/den_sum
    return b1_val
    
def generate_regf(xvals, yvals):
    xmean = sum(xvals)/len(xvals)
    ymean = sum(yvals)/len(yvals)

    num_sum = 0
    den_sum = 0
    for i in range(len(xvals)):
        num_sum += (xvals[i] - xmean)*(yvals[i] - ymean)
        den_sum += (xvals[i] - xmean)**2
    
    b1_val = num_sum/den_sum
    b0_val = ymean - (b1_val*xmean)
    return "y = " + str(b1_val) + "x + " + str(b0_val) 

def get_xmean(xvals):
    xmean = sum(xvals)/len(xvals)
    return xmean 

def get_ymean(yvals):
    ymean = sum(yvals)/len(yvals)
    return ymean 

# Error sum of squares
def get_sse(xvals, yvals, b0, b1):
    curr_sum = 0
    for i in range(len(xvals)):
        curr_sum += (yvals[i] - (b0 + b1*xvals[i]))**2
    return curr_sum

# Variation observed in y values
def get_sst(yvals):
    curr_sum = 0
    ymean = sum(yvals)/len(yvals)
    for i in range(len(yvals)):
        curr_sum += (yvals[i]-ymean)**2
    return curr_sum 



