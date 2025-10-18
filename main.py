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
        add_more = str(input("Add more candidate? Yes/No "))

        # No more candidates, exit program
        if add_more.strip().lower() in ("no", "n"):

            print(f"Only one candidate. The class president is {candidates[0]}. No need for democracy.")
            done_adding = True

    else:

        # Add the user for more suggestions
        add_more = str(input("Add more candidate? Yes/No "))

        # If no, randomize votes and save to file
        if add_more.strip().lower() in ("no", "n"):

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

            print("Inside no")
            done_adding = True

            # Save the candidates and votes to file


    print(candidates, votes)