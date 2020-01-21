import webbrowser

google_URL = 'https://www.google.com/search?sxsrf=ACYBGNRBoNx23U9oYm7lqEcEF6ydUwlmNA%3A1578865756615&ei=XJQbXseGJeGe_QaotIHgBg&q={}'
bing_URL = 'https://www.bing.com/search?q={}'
yahoo_URL = 'https://search.yahoo.com/search?n=10&ei=UTF-8&va_vt=any&vo_vt=any&ve_vt=any&vp_vt=any&vst=0&vf=all&vm=i&fl=0&p={}'
wiki_URL = 'https://en.wikipedia.org/wiki/Special:Search?search={}'


def search_command():
    preferred_engine = input('What search engine would you like to use? (Wikipedia, Google, Bing, Yahoo) ')
    if preferred_engine != 'wikipedia' and preferred_engine != 'google' and preferred_engine != 'bing' and preferred_engine != 'yahoo':
        print('Please enter a valid engine.')
        search_command()
        return

    search_query = input('Please enter your search request: ')
    search_query = search_query.replace(' ', '+')
    if preferred_engine == 'wikipedia':
        webbrowser.open(wiki_URL.format(search_query))
    elif preferred_engine == 'google':
        webbrowser.open(google_URL.format(search_query))
    elif preferred_engine == 'bing':
        webbrowser.open(bing_URL.format(search_query))
    elif preferred_engine == 'yahoo':
        webbrowser.open(yahoo_URL.format(search_query))

    print('Complete!')


while True:
    search_command()
