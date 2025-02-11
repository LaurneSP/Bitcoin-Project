"""
    In this project, you'll create a program that that tells
    you when the value of your Bitcoin falls below $30,000.

    You will need to:
    - Create a function to convert Bitcoin to USD
    - If your Bitcoin falls below $30,000, print a message.

    You can assume that 1 Bitcoin is worth $40,000

"""

investment_in_bitcoin = 1.2
bitcoin_to_usd = 40000

# 1) write a function to calculate bitcoin to usd

# 2) use function to calculate if the investment is below $30,000


# 2) use function to calculate if its below $30,000



def bitcoinToUSD(bitcoin_amount, bitcoin_value_usd):
  total = bitcoin_amount * bitcoin_value_usd
  return total

flag = bitcoinToUSD(1.2,4000)
if(flag < 30000):
  print("Alert!!!")
elif (total == 30,000):
  print("It's worth 30k bro")
else:
  print("It's worth more than 30k bro")



Function Get-MyTotal($BitcoinAmount, $BitcoinToUSD)
{
$Total = $BitcoinAmount * $BitcoinToUSD
If($Total -lt 30000)
{Write-Host "Alert!"}
ElseIf($Total -eq 30000)
{Write-Host "It's worth 30k bro."}
Else
{Write-Host "It's worth more than 30k bro."}
}




1 Bitcoin is now worth $24,000. In the code editor , update the bitcoin_to_usd variable value to 24000 and see if your Python program recognises that your investment is below the $30,000 threshold.
