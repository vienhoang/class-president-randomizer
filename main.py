import random
done_adding = False
candidates, votes = [], []

while not done_adding:

    # input field for class captain suggestions
    name = str(input("Suggest a candidate for class president: "))
    # Capitalize the input name 
    candidates.append(name.capitalize())

    # If only 1 candidate entered
    if len(candidates) == 1:
        # Add the user for more suggestions
        add_more = str(input("Add another candidate? Yes/No "))

        # If the answer is other than yes, exit program
        if add_more.strip().lower() not in ("yes", "y"):

            print(f"Only one candidate. The class president is {candidates[0]}. No need for democracy or rigged elections.")
            print("Exit program now...")
            done_adding = True

    else:

        # Add the user for more suggestions
        add_more = str(input("Add another candidate? Yes/No "))

        # If the answer is other than yes, randomize votes and save to file
        if add_more.strip().lower() not in ("yes", "y"):

            # Set the votes list to 0 for all the candidates
            for c in candidates:
                votes.append(0)

            # Enter how many votes that shoud be casted
            nbr_votes = int(input("How many votes should the program randomize? "))

            # Loop through the number of votes, add 1 vote randomally in each votes element
            # Enter the total votes in the class
            for r in range(0, nbr_votes):
                vote = 1
                # Randomize a votes element so the vote can be stored
                votes_element = random.randint(0, len(candidates) - 1)
                # Add one vote to a randomized votes element
                votes[votes_element] += vote

            # Zip the both lists
            final_votes = list(zip(candidates, votes))

            """"
            Sort the final votes after the candidate with the most votes [('alice', 11), ('bob', 10), ('celsius', 5)]
            sort by the key which is a lambda function, the lambda x variable get its value for x[1] 
            reverse=True so the function can sort from the highest to the lowest value
            """
            final_votes = sorted(final_votes, key=lambda x: x[1], reverse=True)
           
            for name, votes in final_votes:
                print("Here is the final result:")
                print(f"{name}: {votes} votes")


            done_adding = True

            # Save the candidates and votes to file
