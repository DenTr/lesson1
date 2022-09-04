def get_summ(one, two, delimiter='&'):
    one = one.upper()
    two = two.upper()
    return(f'{one}&{two}')
print(get_summ("Learn", "python"))
