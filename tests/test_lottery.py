from brownie import Lottery, accounts, config, network
from web3 import Web3


def test_get_entrance_fee():
    account = accounts[0]
    price_feed_address = config["networks"][network.show_active()][
        "eth_usd_price_feed_address"
    ]
    lottery = Lottery.deploy(
        "0xD4A33860578DE61DBABDC8BFDB98FD742FA7028E", {"from": account}
    )

    expected_entrance_fee = Web3.toWei(0.025, "ether")
    print(expected_entrance_fee)
    print(lottery)
    ok = lottery.getEntranceFee()
    assert ok < expected_entrance_fee
