prices = {
 'ACME': 45.23,
 'AAPL': 612.78,
 'IBM': 205.55,
 'HPQ': 37.20,
 'FB': 10.75
}

technames = {"ACME","FB"}
p1 = { key:value for key, value in prices.items() if value > 100}
p2 = { key:value for key, value in prices.items() if key in technames}
print(p1,p2)