from brownie import AdvancedCollectible, accounts, network, config
from scripts.helpful_scripts import get_breed
import time

STATIC_SEED = 123
def main():
    #creates the collectable, and now we use mappings, by calling from the object of AdvancedCollectible that has events
    # as we go into the events and in requestedCollectible and input 'requestId'
    dev = accounts.add(config['wallets']['from_key'])
    advanced_collectible = AdvancedCollectible[len(AdvancedCollectible)-1]
    transaction = advanced_collectible.createCollectible ( 
        "None", {'from': dev})
    transaction.wait(1)
 
    #waits for 2nd transaction above 
    requestId =  transaction.events['requestedCollectible']['requestId']
    token_id = advanced_collectible.requestIdToTokenId(requestId)
    print (token_id ) #requests the tokenid
    time.sleep(35)
    breed = get_breed(advanced_collectible.tokenIdToBreed(token_id)) # calls the breed get_breed [int] from the list in function get_breed inside helpful_scripts
    print("Dog Breed of token_Id: ",token_id  ,"is this:", breed)