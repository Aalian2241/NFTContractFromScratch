from brownie import AdvancedCollectible
from scripts.helpful_scripts import fund_advanced_collectible

def main():

    advanced_collectible = AdvancedCollectible[len(AdvancedCollectible) -1] #most recent deployment
    fund_advanced_collectible(advanced_collectible) #fund the most recent advanced collectible 
    print ('transaction sent')