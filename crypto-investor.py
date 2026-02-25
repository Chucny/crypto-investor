# ================================================
#   ChucnyBot crypto investpr
#   Uses only normal Python lists + basic math
#   TESTNET – fake money only
#   THIS IS A TEST AND ISN'T DEVELOPED A LOT YET
#   DONT USE REAL MONEY
#   Made by Chucny
# ================================================

import ccxt
import time
from datetime import datetime

print("======================================")
print("  Simple multi-coin bot")
print("  No pandas, just normal lists and math")
print("  Using Binance TESTNET (fake money) \n Made by Chucny\nChecks prices every 60 seconds, use something like the kelly formula. Use this if you want to modify the code. \n")
print("======================================\n")

# ────────────── SETTINGS ──────────────
COINS = [
    'BTC/USDT',   'ETH/USDT',   'SOL/USDT',   'XRP/USDT',   'DOGE/USDT', 
    'ADA/USDT',   'AVAX/USDT',  'SHIB/USDT',  'LINK/USDT',  'DOT/USDT',
    'TRX/USDT',   'POL/USDT',   'LTC/USDT',   'BCH/USDT',   'NEAR/USDT',
    'UNI/USDT',   'ICP/USDT',   'ETC/USDT',   'APT/USDT',   'HBAR/USDT',  
    'XLM/USDT',   'FIL/USDT',   'ATOM/USDT',  'VET/USDT',   'INJ/USDT',   
    'IMX/USDT',   'ARB/USDT',   'OP/USDT',    'SUI/USDT',   'GRT/USDT',   
    'RENDER/USDT','AR/USDT',    'ALGO/USDT',  'QNT/USDT',   'FLOW/USDT',  
    'EGLD/USDT',  'AXS/USDT',   'SAND/USDT',  'NEO/USDT',   'XTZ/USDT',   
    'DYDX/USDT',  'THETA/USDT', 'AAVE/USDT',  'SNX/USDT',   'CRV/USDT',   
    '1INCH/USDT', 'CHZ/USDT',   'ZEC/USDT',   'KSM/USDT',   'ENJ/USDT',   
    'BAT/USDT',   'COMP/USDT',  'YFI/USDT',   'RVN/USDT',   'LRC/USDT',   
    'KAVA/USDT',  'CELO/USDT',  'ZIL/USDT',   'ANKR/USDT'
]
more_coins = """  'ADA/USDT',   'AVAX/USDT',  'SHIB/USDT',  'LINK/USDT',  'DOT/USDT',
    'TRX/USDT',   'MATIC/USDT', 'LTC/USDT',   'BCH/USDT',   'NEAR/USDT',
    'UNI/USDT',   'LEO/USDT',   'DAI/USDT',   'ICP/USDT',   'ETC/USDT',
    'APT/USDT',   'HBAR/USDT',  'XLM/USDT',   'CRO/USDT',   'FIL/USDT',
    'ATOM/USDT',  'VET/USDT',   'OKB/USDT',   'INJ/USDT',   'IMX/USDT',
    'ARB/USDT',   'OP/USDT',    'SUI/USDT',   'GRT/USDT',   'RNDR/USDT',
    'AR/USDT',    'ALGO/USDT',  'QNT/USDT',   'FLOW/USDT',  'EGLD/USDT',
    'AXS/USDT',   'SAND/USDT',  'FTM/USDT',   'EOS/USDT',   'NEO/USDT',
    'XTZ/USDT',   'DYDX/USDT',  'THETA/USDT', 'AAVE/USDT',  'SNX/USDT',
    'MKR/USDT',   'CRV/USDT',   '1INCH/USDT', 'CHZ/USDT',   'ZEC/USDT',
    'KSM/USDT',   'ENJ/USDT',   'BAT/USDT',   'COMP/USDT',  'YFI/USDT',
    'RVN/USDT',   'WAVES/USDT', 'LRC/USDT',   'KAVA/USDT',  'CELO/USDT',
    'ZIL/USDT',   'ANKR/USDT',  'IOST/USDT',  'ONE/USDT',   'ONT/USDT',
    'HOT/USDT',   'BTT/USDT',   'XEM/USDT',   'DGB/USDT',   'SC/USDT',
    'KNC/USDT',   'OMG/USDT',   'IODEX/USDT', 'BAL/USDT',   'BAND/USDT',
    'STORJ/USDT', 'SKL/USDT',   'CVC/USDT',   'REN/USDT',   'NMR/USDT',
    'OCEAN/USDT', 'POLY/USDT',  'REQ/USDT',   'RLC/USDT',   'UMA/USDT',
    'POWR/USDT',  'CTSI/USDT',  'DENT/USDT',  'FUN/USDT',   'C98/USDT',
    'CHR/USDT',   'OGN/USDT',   'STMX/USDT',  'LINA/USDT',  'CELR/USDT',
    '1000SHIB/USDT', 'PEPE/USDT', 'FLOKI/USDT', 'BONK/USDT', 'WIF/USDT',
    'JUP/USDT',   'PYTH/USDT',  'SEI/USDT',   'TIA/USDT',   'W/USDT',
    'JTO/USDT',   'STRK/USDT',  'ONDO/USDT',  'PENDLE/USDT', 'EIGEN/USDT'"""
CHECK_EVERY = 1             # seconds
TRADE_SIZE = 20              # fake USDT per trade


# Fake starting money
usdt = 1000.0
my_coins = {coin: 0.0 for coin in COINS}

# We will save last ~50 prices for each coin in a list
price_history = {coin: [] for coin in COINS}

# Connect to fake Binance
exchange = ccxt.binance({'enableRateLimit': True})
exchange.set_sandbox_mode(True)
#exchange = ccxt.binance({
#    'enableRateLimit': True,
#    'apiKey': 'your_api_key_32_characters_here',
#    'secret': 'your_secret_64_characters_here',
#})
# COMMENT OUT THIS TO USE REAL MONEY: exchange.set_sandbox_mode(True)   ← commented out = real money
# YOU CAN MODIFY THE CODE TO MAKE THE INVESTOR BETTER, DO NOT RELY ON THIS. 100% ON YOUR OWN RESPONSIBILITY!

# ────────────── Helper functions ──────────────

def update_prices():
    """Get newest price for every coin and add it to the list"""
    for coin in COINS:
        try:
            ticker = exchange.fetch_ticker(coin)
            new_price = ticker['last']   # most recent price
            
            # Add to history list
            price_history[coin].append(new_price)
            
            # Keep only last 50 prices (don't let list grow forever)
            if len(price_history[coin]) > 50:
                price_history[coin] = price_history[coin][-50:]
                
        except Exception as e:
            print(f"Could not get price for {coin}: {e}")


def should_buy_or_sell(coin):
    """Decide BUY / SELL / HOLD using only list math"""
    prices = price_history[coin]
    
    # We need at least 6 old prices to compare
    if len(prices) < 6:
        return 'HOLD', "Not enough prices yet"
    
    # Easy to read variables
    now_price    = prices[-1]          # last price in list
    price_5min   = prices[-2]          # one step back
    price_30min  = prices[-6]          # six steps back
    
    # Simple percentage change (like in school math)
    change_short = (now_price - price_5min) / price_5min * 100
    change_long  = (now_price - price_30min) / price_30min * 100
    
    if change_short > 0.1/60 and 0.1/60 > change_long > 0.7/60:
        return 'HOLD', f"Holding, going up slowly but surely. {change_short:+.1f}% / {change_long:+.1f}%"

    elif change_short > 0.2/60 and change_long > 0.2/60:
        return 'SELL', f"Going up fast! {change_short:+.1f}% / {change_long:+.1f}%"


    elif change_short < -0.1/60 and change_long > -0.1/60:
        return 'BUY', f"Buy low, sell high!! {change_short:+.1f}%"

    
    else:
        return 'HOLD', f"Waiting... {change_short:+.1f}% / {change_long:+.1f}%"


def buy(coin, price):
    global usdt
    if usdt < TRADE_SIZE:
        print(f"   Not enough USDT for {coin}")
        return
    
    amount = TRADE_SIZE / price
    my_coins[coin] += amount
    usdt -= TRADE_SIZE
    print(f"   BUY → {amount:.6f} {coin} for ${TRADE_SIZE}")


def sell(coin, price):
    global usdt
    if my_coins[coin] <= 0:
        print(f"   No {coin} to sell")
        return
    
    amount = my_coins[coin]
    money_back = amount * price
    usdt += money_back
    my_coins[coin] = 0
    print(f"   SELL → {amount:.6f} {coin} → +${money_back:.2f}")


# ────────────── Main loop ──────────────

print("Bot running... Press Ctrl+C to stop\n")

try:
    while True:
        print(f"\n--- {datetime.now().strftime('%H:%M:%S')} ---")
        
        # 1. Get fresh prices for all coins
        update_prices()
        
        # 2. Decide and act for each coin
        for coin in COINS:
            prices = price_history[coin]
            if len(prices) == 0:
                print(f"{coin:10} → no price yet")
                continue
            
            current_price = prices[-1]
            decision, reason = should_buy_or_sell(coin)
            
            print(f"{coin:10} | ${current_price:,.2f} | {decision} | {reason}")
            
            if decision == 'BUY':
                buy(coin, current_price)
            elif decision == 'SELL':
                sell(coin, current_price)
        
        print(f"USDT left: ${usdt:.2f}")
        print("-" * 50)
        
        time.sleep(CHECK_EVERY)

except KeyboardInterrupt:
    print("\nBot stopped")
    print(f"Final USDT: ${usdt:.2f}")
    for coin in COINS:
        if my_coins[coin] > 0:
            print(f"  You hold {my_coins[coin]:.6f} {coin}")
    print("All fake testnet money – no real loss possible!")
