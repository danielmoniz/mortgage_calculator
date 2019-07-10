# A simple calculator to determine amount saved with two different length mortagages (causing different monthly payments).

monthly_payment = {
    30: 1266,
    20: 1665,
}
payment_difference = monthly_payment[20] - monthly_payment[30]

total_years = 30
market_growth = 1.05 # assume 5% market growth

total_spend = {
    30: monthly_payment[30] * 12 * 30,
    20: monthly_payment[20] * 12 * 20,
}

spend_difference = total_spend[20] - total_spend[30]

print("Total spend:")
print("   30 years: $" + str(total_spend[30]))
print("   20 years: $" + str(total_spend[20]))
print("Additional spent with 30 year mortgage: " + str(spend_difference))

print('\n' + '-' * 10)



print("Strategy: 20 year mortgage, followed by 10 years of investing the 30 year payment amount into the market.")

print("20 year mortgage rate: ${}".format(monthly_payment[20]))
print("Total spent: ${}".format(total_spend[20]))
market_growth_sum = 0
for years_invested in reversed(range(1, 11)):
    market_growth_sum += market_growth ** years_invested

print("Market growth factor of 10 years of repeated yearly investments of ${}: {}".format(payment_difference, market_growth_sum))
print("Amount invested yearly: ${} (${} * 12)".format(monthly_payment[30] * 12, monthly_payment[30]))
total_invested = monthly_payment[30] * 12 * 10
print("Total invested: ${}".format(total_invested))
total_investment_revenue = monthly_payment[30] * 12 * market_growth_sum
print("Total amount after 10 years of investments: ${}".format(total_investment_revenue))
print("Total net profit on 10 years of investments: ${}".format(total_investment_revenue - total_invested))
total_net_profit = total_investment_revenue - total_spend[20] - total_invested
print("Total money made (after mortgage + investments): ${}".format(total_net_profit))
print("Total money for comparison (mortgage + 10 years of not paying + investments with that money): \n ==> ${}".format(total_net_profit + total_invested))



print('\n' + '-' * 10)



print("Strategy: 30 year mortgage, all while investing the extra cash flow into the market.")

print("30 year mortgage rate: ${}".format(monthly_payment[30]))
print("Total spent: ${}".format(total_spend[30]))
print("Amount saved monthly: ${}".format(spend_difference))

market_growth_sum = 0
for years_invested in reversed(range(1, 31)):
    market_growth_sum += market_growth ** years_invested

print("Market growth factor over {} years: {}".format(years_invested, market_growth_sum))
total_investment_revenue = payment_difference * 12 * market_growth_sum
print("Total investment made: ${}".format(total_investment_revenue))
print("Total money for comparison (lower mortgage for 30 years + 30 years of investing difference): \n ==> ${}".format(total_investment_revenue - total_spend[30]))
