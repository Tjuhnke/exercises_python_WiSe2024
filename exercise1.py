def cagr_berechnung(start_value,end_value, years):
    start_value_abs = abs(start_value)
    cagr = (end_value / start_value_abs)**(1/years) -1
    return cagr
    
print(cagr_berechnung(100, 700, 30))
    
rendite = (cagr_berechnung(100, 700, 30))

print (120 * (1+rendite)**30)