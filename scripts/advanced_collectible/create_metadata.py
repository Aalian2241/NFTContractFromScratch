from brownie import AdvancedCollectible, accounts, network, config

def main():
    number_of_tokens = 0
    print ("Working on "+ network.show_active())
    advanced_collectible = AdvancedCollectible[len(AdvancedCollectible)-1]
    number_of_tokens = advanced_collectible.tokenCounter()
    #number_of_tokens = number_of_tokens + 1
    print("number of tokens you have deployed:",number_of_tokens)