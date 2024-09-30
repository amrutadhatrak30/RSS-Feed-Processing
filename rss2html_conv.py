########################################################################################################
# Date : 29 September, 2024
# Author : Amruta Dhatrak
# Filename: rss2html_conv.py
# Description : This file parses  the rss feed and then uses python code to create an html file
#               and then write each entry parsed from the rss feed into the  html format.
# Steps :
#   1. Using feedparser, get the feed parsed into a list file.
#   2. Extract today's date using datetime module
#   3. Setup page layout using css format (basefile.html) and create first part of the html file.
#   3a. Header has 3 columns (date , page title, translate element.)
#   3b. The article section has 2 columns. Left column is used for displaying links, publishing date,
#       author and photo credits, while the right column is used to display the image.#
#   4. Copy contents of the basefile.html to the output file (formatted_news_page.html)
#   5. Start by writing header (date and title from the feed) to the output file. Make the header sticky.
#   6. Add a Google translate element into the header.
#   7. Start parsing each entry from the feed, extracting date first.
#   8. Write the article date, headline, authors and photo credits to the html file. (Formatted)
#   9. Embed links that open in new tab.
#   9. Write the image url and relevant entries to the html file. Add a link to the article to the image.
#      image.
#   10. Add the relevant closing tags to the html file.
###########################################################################################################
import feedparser
import datetime
import shutil
import time

# Step 1
rssurl = feedparser.parse("https://rss.nytimes.com/services/xml/rss/nyt/Technology.xml")

# Step 2
# Get today's date
today = datetime.date.today()
# Get the date in the desired format
date_published = today.strftime("%a, %d %b %Y")

# Step 3 and 4
shutil.copyfile("basefile.html", "formatted_news_page.html")

# Step 5 and 6
with open("formatted_news_page.html" , "a") as html_file:
    html_file.write(f"\n<div class=\"header-container\">  \
        \
        \n\t<div class=\"header-item\">  \
        <p> <a style=\"font-size:25px;text-align:left;\" > {date_published}  </a> </p> </div> \
        \
        \n\t<div class=\"header-item\">  \
        <p> <a style=\"font-size:60px;text-align:center;font-family:Lobster;\" href = {rssurl['feed'].link}> \
         {rssurl['feed'].title}  </a> </p> </div> \
        \
        \n\t<div class=\"header-item\">  \
        <button type=\"button\" class=\"button\" id=\"google_translate_element\" \
        onclick=\"googleTranslateIntoSpanish()\" > <a style=\"font-size:25px;text-align:right;\" > \
        Translate Page </a> </button> </div>  \
        \
        \n </div>  \
        \
        \n <div class=\"grid-container\"> \n")


    for i in range (0,len(rssurl.entries)):

# Step 7
        entry = rssurl.entries[i]
        published_time = time.strftime("%b. %d,   %Y", entry.published_parsed)

# Step 8 and 9
        html_file.write(f" \t <div class = \"grid-item\"> \
        \
        <p>  <a style=\"text-decoration:none; font-size:15px;color:gray\" > {published_time}  </a> </p> \
        \
        <p> <a style=\"font-size:35px;\" href = \"{entry.link}\" target=\"_blank\" > {entry.title}   </a> </p> \
        \
        <p> <a style=\"text-decoration:none;font-size:20px;color:black\" href = {entry.link} target=\"_blank\" > \
        {entry.description}  </a> </p>   \
        \
        <p> <a style=\"text-decoration:none;font-size:15px;color:gray\" >  Article by: {entry.author} <br> \
        Photo by: {entry.media_credit[0]['content']} </a> </p> </div> \
        \
        \n\t <div class = \"grid-item\">  <p> <a href = {entry.link} target=\"_blank\" > \
        <img src = {entry.media_content[0]['url']} alt={entry.media_credit[0]['content']} class=\"center\" > </a> </p> \
        </div>\n")



    html_file.write(f"</div> \
        \n</body> \
        \n</html> ")