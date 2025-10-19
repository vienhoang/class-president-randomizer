import random
done_adding = False

# Save the candidates and votes to file
def save_to_file(list_result):
    file_name = "results.txt"

    # Save to file
    try:
        with open(file_name, "w") as f:
            # Separate each line with \n at the end
            line = "\n".join(list_result)
            f.write(line)
            # Print out based on how many elements in the list_result
            if len(list_result) == 1:
                print(f"The result has been saved to the file: {file_name}")
            else:
                print(f"The results have been saved to the file: {file_name}")
    except FileNotFoundError:
        print("File not found.")
    except IOError:
        print("An I/O error occurred.")
    except:
        print("Something went wrong...")

    f.close()

# Suggest candidate
def suggest_candidate():
    global done_adding
    candidates, votes, outputs = [], [], []

    while not done_adding:
        # Input field for class captain suggestions
        name = str(input("Suggest a candidate for class president: "))
        # Capitalize the input name 
        candidates.append(name.capitalize())

        # If only 1 candidate entered
        if len(candidates) == 1:
            # Add the user for more suggestions
            add_more = str(input("Add another candidate? Yes/No "))

            # If the answer is other than yes, exit program
            if add_more.strip().lower() not in ("yes", "y"):
                print_str = f"Only one candidate. The class president is {candidates[0]}. No need for democracy or rigged elections."
                outputs.append(print_str)
                print(print_str)
                # Save the result to file
                save_to_file(outputs)
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
                
                # Get the highest vote count
                highest_vote_count = max(final_votes, key=lambda x: x[1])
                
                winner_counter = 0
                print_str = "-----=====FINAL RESULT=====-----"
                outputs.append(print_str)
                print(print_str)
                # Loop through the final votes list, and print out the result
                for name, votes in final_votes:
                    # ('alice', 13) check if the highest vote count exist in the final votes list, add 1 to winner_counter
                    if highest_vote_count[1] == votes:
                        winner_counter += 1

                    print_str = f"{name}: {votes} vote(s)"
                    outputs.append(print_str)
                    print(print_str)

                #print(f"Winner count: {winner_counter}")
                if winner_counter > 1:
                    print_str = "It's a draw between: "
                    outputs.append(print_str)
                    print(print_str)
                    # Print out the draw candidates with the highest vote count 
                    for name, votes in final_votes:
                        if highest_vote_count[1] == votes:
                            outputs.append(name)
                            print(f"{name}")
                else: 
                    print_str = f"The class president is ... {highest_vote_count[0]}"
                    outputs.append(print_str)
                    print(print_str)
                
                # Save the result to file
                save_to_file(outputs)
                done_adding = True
    print("Exit program now...")
# Run the program
def main():
    suggest_candidate()

if __name__ == "__main__":
    main()