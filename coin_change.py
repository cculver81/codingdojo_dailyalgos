# Let's revisit Generate Coin Change

# Change is inevitable (especially when breaking a twenty). Make generateCoinChange (cents). Accept a number of American cents, compute and represent  that amount with the smallest number of coins. Common American coins are pennies (1 cent)

#Given 33

def generateCoinChange(num):
    changedict={}
    newdict={"q":25 , "d":10 , "n":5 , "p":1}
    if num >= newdict["q"]:
        changedict["q"]= num // newdict["q"]
        num = num%newdict["q"]
    if num >= 10:
        changedict["d"]= num // newdict["d"]
        num = num%newdict["d"]
    if num >= 5:
        changedict["n"]= num // newdict["n"]
        num = num%newdict["n"]
    if num >= 1:
        changedict["p"]= num // newdict["p"]
    print(changedict)
    return changedict

generateCoinChange(33)