
################Measuremnt_update follows Bayes rule and Multiplication of the two functions#####
def Measurement_update(mean1, var1, mean2, var2):
    new_mean = (mean1*var2 + mean2*var1)/(var1 + var2)
    new_var = 1./((1./var1)+(1./var2))
    return [new_mean, new_var]

##The thing you should notice is: 1) new_mean is weighted mean of mean1 and mean2 var2 and var1 as weights
##                                   and lies in between mean1 and mean2
##                                2) new_var is independent of means and is always less than var1 and var2
##                                   hence, uncertainity decreases as no of data points increases

#############Prediction follows Total probability or Convolution or Addition#####################
def Prediction(mean1, var1, mean2, var2):
    new_mean = mean1 + mean2
    new_var = var1 + var2
    return [new_mean, new_var]

##The thing you should notice is: 1) new_mean is addition of mean1 and mean2
##                                2) new_var is independent of means and is always more than var1 and var2
##                                   hence, uncertainity increases as no of data points increases
