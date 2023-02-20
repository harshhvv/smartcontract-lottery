from brownie import Lottery, accounts, config, network
from web3 import Web3


def test_get_entrance_fee():
    account = accounts[0]
    price_feed_address = config["networks"][network.show_active()][
        "eth_usd_price_feed_address"
    ]
    lottery = Lottery.deploy(
        price_feed_address,
        {"from": account},
    )

    # expected_entrance_fee = Web3.toWei(0.025, "ether")
    entranceFee = lottery.getEntranceFee()
    print(entranceFee)
    assert entranceFee > Web3.toWei(0.00056, "ether")
    assert entranceFee < Web3.toWei(0.00060, "ether")
