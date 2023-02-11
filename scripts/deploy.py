# from brownie import Lottery, accounts, config, network
# from web3 import Web3


# def deploy():
#     account = accounts[0]
#     lottery = Lottery.deploy(
#         config["networks"][network.show_active()]["eth_usd_price_feed_address"],
#         {"from": account},
#     )
#     # assert lottery.getEntranceFee() > Web3.toWei(0.0006, "ether")
#     # assert lottery.getEntranceFee() <= Web3.toWei(0.00066, "ether")
#     a = lottery.getEntranceFee()
#     print(a)
#     print(Web3.toWei(0.666, "ether"))
#     # assert 1 == 1


# def main():
#     deploy()
