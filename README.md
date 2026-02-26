# Crypto Investor
A simple crypto investor made with python. After 1 hour of investing, it made 1.21 USD profit. You can use this bot with real money, by changing the code from TESTNET, wich has instructions in comments. Install dependencies first. <br><strong>I AM NOT RESPONSIBLE FOR ANY MONEY LOSS</strong><br>
<h3>Dependencies:</h3>
ccxt<br>
datetime<br>
<h3>Theory</h3>
<br>This could also be used with the Kelly formula, f = (b*p-(1-p))/b <br>
Where p = propability (W/L) and b = bet size.<br>This bot buys low and sells high, wich is how it makes profit. Maybe buy at -0.1% and sell at +0.1%.<br
><img src="screeshot1" style="width:600px;height:600px;"></img><br>Do this to use real money:<br><p style="color:red;">
<br>exchange.set_sandbox_mode(True)
<br>#exchange = ccxt.binance({
<br>#    'enableRateLimit': True,
<br>#    'apiKey': 'your_api_key_32_characters_here',
<br>#    'secret': 'your_secret_64_characters_here',
<br>#})
<br># COMMENT OUT THIS TO USE REAL MONEY: exchange.set_sandbox_mode(True)   ← commented out = real money
<br># YOU CAN MODIFY THE CODE TO MAKE THE INVESTOR BETTER, DO NOT RELY ON THIS. 100% ON YOUR OWN RESPONSIBILITY!</p><br>
<strong>Copyright &copy; Chucny 2025 Licensed under the Apache license.</strong>
