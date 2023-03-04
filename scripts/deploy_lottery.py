from brownie import Lottery, accounts, config, network
from web3 import Web3
from scripts.helpful_scripts import get_account, get_contract


def deploy():
    account = get_account(id="my-account")
    lottery = Lottery.deploy(
        get_contract("eth_usd_price_feed").address,
        get_contract("vrf_coordinator").address,
        get_contract("link_toekn").address,
        config["networks"][network.show_active()]["fee"],
        config["networks"][network.show_active()]["keyhash"],
        {"from": account},
    )
    print("deployed lotteryy")


def main():
    deploy()
