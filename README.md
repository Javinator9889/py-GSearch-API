<snippet>

  <content><![CDATA[

# py-GSearch-API



This is a simple library/API for browsing the web, using the Google search engine, obtaining the URLs of the found pages



## Installation



For installing, you can:

1. Clone this proyect and the, run `python setup.py install`

2. Although, you can use `pip` for installing, just typing `pip install py-GSearch-API`



## Usage



Basic usage instructions:


First, the project requieres at least two variables, which are:

1. `query`, in where you will put your search terms and

2. `lang`, where you have to put `es` or `en` (Spanish/español, English)

The other variable is `num` (int value), in order to limit number of max results of searching.


So, for using you must type (in your project or in command line):

`
import gsearch

query = "YOUR_QUERY"
lang = "es/en"
(OPTIONAL) num = 50


results = gsearch.search(query=query,lang=lang,(OPTIONAL)num=num) 	# This is for normal search

results_news = gsearch.search_news(query=query,lang=lang,(OPTIONAL)num=num) 	# This is for searching news

# That functions are returning a dictionary and a int value. You must manage them with: results[0] (dictionary) and results[1] (number of pages found)

dictionary = results[0]

num_of_pages = results[1]


news_dict = results_news[0]

num_of_articles = results_news[1]

# For getting the values:

for u in range(1,num_of_pages):
	
	page = dictionary.get("Page {}".format(u))

	print("Link",u,":",page)

# The same for articles:

for v in range(1,num_of_articles):

	page_2 = news_dict.get("Page {}".format(u))

	print("Link (news)",u,":",page_2)
`


## Contributing



1. Fork it!

2. Give me a star

3. Help me with issues

4. Check my bot and my other proyects (Telegram --> @dwnmp3Bot // https://github.com/Javinator9889/telegram-yt_mp3-bot/issues)




## License


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

]]></content>

  <tabTrigger>readme</tabTrigger>

</snippet>
