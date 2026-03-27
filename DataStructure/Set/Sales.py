#we have 7 days sales data 3 time data morning,ev,noon
#find which day[monday,tue...] has heighest sales

sales = {
    "Monday": {200,150,300},
    "Tuesday": {250,200,100},
    "Wednesday": {300,250,200},
    "Thursday": {150,200,250},
    "Friday": {400,300,350},
    "Saturday": {500,450,400},
    "Sunday": {350,300,250}
}

highest_sales = 0
best_day = ""

for day, sales_data in sales.items():
    total_sales = sum(sales_data)

    if total_sales > highest_sales:
        highest_sales = total_sales
        best_day = day

print("Highest sales day:", best_day)
print("Total sales :", highest_sales)