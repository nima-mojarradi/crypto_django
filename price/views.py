from django.shortcuts import render
import requests
import redis
import asyncio
import json



def replace_btc_with_usdt():
    units = ["USDT-BTC", "ETH-BTC", "LTC-BTC", "EOS-BTC", "XRP-BTC", "KCS-BTC", "DIA-BTC", "VET-BTC", "DASH-BTC", "DOT-BTC", "XTZ-BTC", "ZEC-BTC", "BSV-BTC", "ADA-BTC", "ATOM-BTC", "LINK-BTC", "LUNA-BTC", "NEO-BTC", "UNI-BTC", "ETC-BTC", "BNB-BTC", "TRX-BTC", "XLM-BTC", "BCH-BTC", "USDC-BTC", "GRT-BTC", "1INCH-BTC", "AAVE-BTC", "SNX-BTC", "API3-BTC", "CRV-BTC", "MIR-BTC", "SUSHI-BTC", "COMP-BTC", "ZIL-BTC", "YFI-BTC", "OMG-BTC", "XMR-BTC", "WAVES-BTC", "MKR-BTC", "COTI-BTC", "SXP-BTC", "THETA-BTC", "ZRX-BTC", "DOGE-BTC", "LRC-BTC", "FIL-BTC", "DAO-BTC", "BTT-BTC", "KSM-BTC", "BAT-BTC", "ROSE-BTC", "CAKE-BTC", "CRO-BTC", "XEM-BTC", "MASK-BTC", "FTM-BTC", "IOST-BTC", "ALGO-BTC", "DEGO-BTC", "CHR-BTC", "CHZ-BTC", "MANA-BTC", "ENJ-BTC", "IOST-BTC", "ANKR-BTC", "ORN-BTC", "SAND-BTC", "VELO-BTC", "AVAX-BTC", "DODO-BTC", "WIN-BTC", "ONE-BTC", "SHIB-BTC", "ICP-BTC", "MATIC-BTC", "CKB-BTC", "SOL-BTC", "VRA-BTC", "DYDX-BTC", "ENS-BTC", "NEAR-BTC", "SLP-BTC", "AXS-BTC", "TLM-BTC", "ALICE-BTC", "IOTX-BTC", "QNT-BTC", "SUPER-BTC", "HABR-BTC", "RUNE-BTC", "EGLD-BTC", "AR-BTC", "RNDR-BTC", "LTO-BTC", "YGG-BTC"]
    units = [unit.replace('BTC', 'USDT') for unit in units]
    return units

async def get_data():
    all_units = replace_btc_with_usdt()
    for units in all_units:
        data2 = f"https://api.kucoin.com/api/v1/market/candles?type=1min&symbol={units}&startAt=1566703297&endAt=1566789757"
        informations1 = requests.get(data2)
        dictionary = json.loads(informations1.text)
        if dictionary["code"] == "200000":
            if dictionary["data"]:
                print(units,'\n', '*'*100)
                print(informations1.text)
        
        
asyncio.run(get_data())