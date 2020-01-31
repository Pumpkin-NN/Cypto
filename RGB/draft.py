lst = '246c694e87941ace2d799b7a87a4cdb5'
print(len(lst))
def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        return lst[i:i + n]
        
m = chunks(lst, 16)
print(m)