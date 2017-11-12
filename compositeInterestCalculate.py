import calendar

startingDebt = ????
outstandingDebt= startingDebt
payed=0
interest_rate=6.1
calendars = calendar.Calendar()
NoOfMonthsToPay = 0
monthlyPayment = 500
payedDebt = False

for year in range(2017,2040):
	print("Top of ", year, " Debt outstanding is ", outstandingDebt)
	for month in range(1,13):
		#start from september 2017
		if year == 2017 and month < 9:
			continue
		#change interest rate in April 2018
		if year == 2018 and month == 4:
			interest_rate = 4.45
		#loop through days
		for day in calendars.itermonthdays(year, month):
			if day != 0:
				dailyInterest = outstandingDebt/100/365*interest_rate
				outstandingDebt = outstandingDebt + dailyInterest
		#pay 1200 each month
		if outstandingDebt > monthlyPayment:
			outstandingDebt -= monthlyPayment
			payed += monthlyPayment
			NoOfMonthsToPay+=1
		else:
			print("Last payment is - ", outstandingDebt)
			payed+=outstandingDebt
			outstandingDebt-=outstandingDebt
			print("No. months to pay - ", NoOfMonthsToPay+1)
			print("Starting Debt - ", startingDebt)
			print("Outstanding Debt - ", outstandingDebt)
			print("Total Payed - ", payed)
			payedDebt = True
			break
	if payedDebt:
		break
