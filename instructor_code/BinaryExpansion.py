def bse(s):
    output = []
    def helper (sub, i):
        #breakcase, stop once you get to the end of the given string "s"
        if i == len(s):
            output.append(sub)
        else:
            #creating two branchs for 1 and 0 whenever we get to a question mark
            if s[i] =='?':
                helper(sub + str(1), i + 1)
                helper(sub + str(0), i + 1)
            else:
                #concatenating everything that is not a question mark into 'sub' (ie: 101)
                helper(sub + s[i], i + 1)
    helper('', 0)
    return output



sub = '1','10','101', two subs 

sub1 = '1','10','101','1011'
sub2 = = '1','10','101','1010'


i= 1,2,3,4 


#---------------------------------------------------------------

# first create a loop that subs in 0 or 1 for the first mark
# 101? -> 1011 and 1010 

# then move onto the second and so on
# 1011 and 1010 -> 101111, 101110 and 101011, 101010

# then just concatenate the rest to the 4 outputs + 01



# # create a loop or loops that generate each resultset
# for i in range(0,cnt,1):

# #given
# bin = "101?1?01"

# def bin_exp(val)
# # parse the given str into a list
# pars = list(string.split(val))
# q_mark_indexes = []
# output = [][]

# # loop through to the question marks
# for i in range(0, pars, 1):
#     if pars[i] == "?":
#         q_mark_indexes.push(i) 
#     else:
        
        

            





# # call the fuction
# bin_exp(bin)
