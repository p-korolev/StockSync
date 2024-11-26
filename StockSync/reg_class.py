import reg_fx as rg

class Regression:

    # rl: regression line
    # rs: r-squared
    # sd: standard deviation
    def __init__(self, xvals, yvals):
        # decimal round amount
        self.dec_round = 3

        # regression function variables
        self.b1 = rg.find_b1(xvals, yvals)
        self.b0 = rg.find_b0(xvals, yvals, self.b1)

        # data characteristics 
        self.xmean = rg.get_xmean(xvals)
        self.ymean = rg.get_ymean(yvals)

        # regression characteristics 
        self.sse = rg.get_sse(xvals, yvals, self.b0, self.b1)
        self.sst = rg.get_sst(yvals)
        self.rs = round(1 - (self.sse/self.sst), self.dec_round)   # r-squared value
        self.sd = (self.sse/(len(xvals)-2))**1/2   # standard deviation 

    # return function in y = b1x + b0 form as string
    def __str__(self):
        if self.b0 == 0:
            return "y = " + str(round(self.b1, self.dec_round)) + "x"
        if self.b0 > 0:
            return "y = " + str(round(self.b1, self.dec_round)) + "x + " + str(round(self.b0, self.dec_round))
        if self.b0 < 0:
            return "y = " + str(round(self.b1, self.dec_round)) + "x - " + str(abs(round(self.b0, self.dec_round)))

    # get the rl value y at some x
    def y_at_x(self, x):
        return (self.b0 + (self.b1*x))
    
    # get the x value at some rl value y
    def x_at_y(self, y):
        return ((y - self.b0)/self.b1)
    
    def set_rounding(self, new_round):
        self.dec_round = new_round
    
