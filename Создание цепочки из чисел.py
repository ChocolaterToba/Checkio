def checkio(numbers):
    chains = [[numbers.pop(0)]]
    for i in range(len(numbers)):
        new_chains = []
        # Taking each of the chains...
        for chain in chains:
            # Each of the awailable numbers...
            for number in numbers:
                # And checking if the number fits at the end of chain.
                if ((number not in chain and
                     [str(number)[a] == str(chain[-1])[a]
                      for a in range(3)].count(True) == 2)):
                    # If it does, then new chainis created.
                    new_chains += [chain + [number]]
                    # And if it's the last number, then the chain is ready.
                    if number == numbers[-1]:
                        return chain + [number]
        chains = new_chains[:]