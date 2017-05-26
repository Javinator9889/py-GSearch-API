try:
    import requests as rq
except (ImportError,ModuleNotFoundError):
    print("\'requests\' module not found. Try with \'pip install requests\'")


try:
    from bs4 import BeautifulSoup
except (ImportError,ModuleNotFoundError):
    print("\'bs4\' module not found. Try with \'pip install beautifulsoup4\'")


try:
    import ujson as json
except (ImportError,ModuleNotFoundError):
    print("\'ujson\' module not found. Try with \'pip install ujson\'")


import re


def search_news(**kwargs):
    try:
        query = kwargs.get('query')
        num = kwargs.get('num')
        lang = kwargs.get('lang')
    except TypeError:
        pass
    try:
        if lang == 'en':
            address = 'com'
        elif lang == 'es':
            address = 'es'
        else:
            raise TypeError("Language arg ('lang') must be given")

        if query is not None:
            query_string = str(query)
            query = query_string.replace(" ","+")
        else:
            raise TypeError("Search query ('query') must be given")

        if num is None:
            num = 1000
        else:
            num = int(num)

        url = "https://www.google.{}/search?hl={}&tbm=nws&as_q={}&as_occt=any&as_drrb=b&tbs=cdr:1,cd_min:3/1/13,cd_max:3/2/13&authuser=0&gws_rd=cr&ei=-WgYWaPQO8TtaoTTiegE#q={}&hl={}&authuser=0&tbas=0&tbm=nws&tbs=qdr:d&spf=1494771990488".format(address,lang,query,query,lang)
        open_url = rq.get(url)
        data = open_url.content
        html = BeautifulSoup(data, "lxml")
        html.prettify()

        i = 1
        beta_dict = {}
        for link in html.find_all('a'):
            obtained_url = link.get('href')
            try:
                is_url = re.search('(?P<url>http?://[^\s]+)', obtained_url).group("url")
                final_url = re.sub(r'&sa.*', '', is_url)

            except AttributeError:
                try:
                    is_url = re.search('(?P<url>https?://[^\s]+)', obtained_url).group("url")
                    final_url = re.sub(r'&sa.*', '', is_url)

                except AttributeError:
                    final_url = obtained_url

            if 'play.google' in final_url or 'google.com' in final_url or 'youtube.com' in final_url or 'mail.google' in final_url or 'drive.google' in final_url or 'google.es' in final_url or '/preferences' in final_url or 'accounts.google.com' in final_url or '/search' in final_url or '/webhp' in final_url or 'maps.google' in final_url or '/support' in final_url or '/tools' in final_url or final_url == '/' or '/intl' in final_url or '/services' in final_url or '/advanced' in final_url or '/language' in final_url or 'abogacia.es' in final_url:
                final_url = None
            if final_url is None:
                i = i
            else:
                current_value = str(i)
                beta_dict["URL {0}".format(current_value)] = final_url
                i = i+1

        search_results = {}
        a = 1
        for k,y in beta_dict.items():
            if y not in search_results.values() and a<=num:
                current_num = str(a)
                key = "Page {}".format(current_num)
                search_results[key] = y
                a = a+1

        return search_results, a
    except TypeError:
        print("One or more args were not given. Check and then, retry the searching")


def search(**kwargs):
    try:
        query = kwargs.get('query')
        num = kwargs.get('num')
        lang = kwargs.get('lang')
    except TypeError:
        pass
    try:
        if lang == 'en':
            address = 'co.uk'
        elif lang == 'es':
            address = 'es'
        else:
            raise TypeError("Language arg ('lang') must be given")

        if query is not None:
            query_string = str(query)
            query = query_string.replace(" ","+")
        else:
            raise TypeError("Search query ('query') must be given")

        if num is None:
            num = 1000
        else:
            num = int(num)

        url = "http://www.google.{}/search?hl={}&q={}&meta=".format(address,lang,query)
        open_url = rq.get(url)
        data = open_url.content
        html = BeautifulSoup(data, "lxml")
        html.prettify()

        i = 1
        beta_dict = {}
        for link in html.find_all('a'):
            obtained_url = link.get('href')
            try:
                is_url = re.search('(?P<url>http?://[^\s]+)', obtained_url).group("url")
                final_url = re.sub(r'&sa.*', '', is_url)

            except AttributeError:
                try:
                    is_url = re.search('(?P<url>https?://[^\s]+)', obtained_url).group("url")
                    final_url = re.sub(r'&sa.*', '', is_url)

                except AttributeError:
                    final_url = obtained_url

            if 'play.google' in final_url or 'google.com' in final_url or 'google.co.uk' in final_url or 'news.google.co.uk' in final_url or 'youtube.com' in final_url or 'mail.google' in final_url or 'drive.google' in final_url or 'google.es' in final_url or '/preferences' in final_url or 'accounts.google.com' in final_url or '/search' in final_url or '/webhp' in final_url or 'maps.google' in final_url or '/support' in final_url or '/tools' in final_url or final_url == '/' or '/intl' in final_url or '/services' in final_url or '/advanced_search' in final_url or '/help' in final_url or '#' in final_url or '/aclk?sa' in final_url:
                final_url = None
            if final_url is None:
                i = i
            else:
                current_value = str(i)
                beta_dict["URL {0}".format(current_value)] = final_url
                i = i + 1

        search_results = {}
        a = 1
        for k, y in beta_dict.items():
            if y not in search_results.values() and a <= num:
                current_num = str(a)
                key = "Page {}".format(current_num)
                search_results[key] = y
                a = a + 1

        return search_results, a

    except TypeError:
        print("One or more args were not given. Check and then, retry the searching")


print("py-GSearch-API - Copyright (C) 2017  Javinator9889\n\n\
This program comes with ABSOLUTELY NO WARRANTY; for details type `show w'.\n\
This is free software, and you are welcome to redistribute it\
under certain conditions; type `show c' for details.")


# The forwarding message has to be included in each version of this program
"""
    py-GSearch-API -- A simple API for searching web with Google
    Copyright (C) 2017  Javinator9889

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

    For contacting, go to "https://github.com/Javinator9889/py-GSearch-API/issues" and type your message.
    Also you can go to my GitHub profile and send me direct message.
"""