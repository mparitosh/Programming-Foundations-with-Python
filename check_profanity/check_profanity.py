import urllib
def read_file():
    quotes = open("movie_quotes.txt", "r")
    content_of_file= quotes.read()
    check_profanity(content_of_file)
    quotes.close()
    
def check_profanity(text_to_check):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q="+text_to_check)
    s = connection.read()
    print(s)
    connection.close()
    # q = urllib.request.urlopen("http://www.wdylike.appspot.com/?q="+text_to_check)
    # q.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36')
    # q.add_header('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8')
    
    # r = q.read()
    
    
read_file()
