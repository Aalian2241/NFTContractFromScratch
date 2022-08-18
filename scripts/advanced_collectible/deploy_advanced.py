#this deploys our contract to rinkby testnet chain

#accounts: accounts associated with our private keys
#network to know what network we are on
from brownie import AdvancedCollectible, accounts, network, config
from scripts.helpful_scripts import fund_advanced_collectible

#since we are deploying on a real chain, we need a wallet, address, private key, and add them to our accounts
#define private key in our config file
def main():
    #our meta mask account added
    dev = accounts.add(config['wallets']['from_key'])
    print (dev)
    print (network.show_active())
    publish_source = False
    #our contract is deployed 
    
    advanced_collectible = AdvancedCollectible.deploy(
        config['networks'][network.show_active()]['vrf_coordinator'], 
        config['networks'][network.show_active()]['link_token'],
        config['networks'][network.show_active()]['keyhash'],
        {'from': dev},
        publish_source = publish_source 
    ) 
    #our contract is funded
    fund_advanced_collectible(advanced_collectible)
    print ('transfered')
    return advanced_collectible
