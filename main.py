import random
done_adding = False
candidates, votes = [], []

while not done_adding:

    # input field for class captain suggestions
    name = str(input("Suggest a candidate for class president: "))
    # Capitalize the input name 
    candidates.append(name.capitalize())

    # Enter how many votes that shoud be casted
    nbr_votes = int(input("How many votes should the program randomize? "))

    # Enter the total votes in the class
    for candidate in candidates:
        votes.append(nbr_votes)
        print(candidate, votes)
    
    # Add the user for more suggestions
    add_more = str(input("Add more candidate? Yes/No "))

    # If no, randomize votes and save to file
    if add_more.strip().lower() in ("no", "n"):
        print("Inside no")
        done_adding = True

        # Save the cast votes to file


    print(candidates)