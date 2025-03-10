
answer = "yes"

bidder = {}
while answer == "yes":
    
    name = input("What is your name?")

    bid = int(input("What is your bid: $"))

    bidder[name] = bid

    answer = input("Are there any other bidders \n press 'Yes' or 'No'").lower()




def find_highest_didder(bidder):
    highest = 0
    winner = ""
    for key in bidder:
        
        value = bidder[key]

        if value > highest:
            highest = value
            winner = key
            
    print(f"The highest bidder is {winner} with a bid of ${highest}")

print(bidder)
find_highest_didder(bidder)


    


        
    
