import random
done_adding = False
candidates, votes = [], []

while not done_adding:

    # input field for class captain suggestions
    name = str(input("Suggest a candidate for class president: "))
    # Capitalize the input name 
    candidates.append(name.capitalize())

    # Add the user for more suggestions
    add_more = str(input("Add more candidate? Yes/No "))

    # If no, randomize votes and save to file
    if add_more.strip().lower() in ("no", "n") and len(candidates) > 1:

        # Enter how many votes that shoud be casted
        nbr_votes = int(input("How many votes should the program randomize? "))

        # Loop through the number of votes, add 1 vote randomally in each votes element
        # Enter the total votes in the class
        for r in range(0, nbr_votes):
            vote = 1
            votes_element = random.randint(0, len(candidates)) 
            votes[votes_element] += vote

        print("Inside no")
        done_adding = True

        # Save the cast votes to file


    print(candidates, votes)