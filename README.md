# Google-shopping-Web-Scraper

#This project was quite the journey. I learned a lot about web scraping, debugging, bot detection and so much more.
#I learned about Selenium and how to use it to automatically open websites and make the program do what I want.
#That could be through clicking, scrolling, maximizing, minimizing windows, etc. The hardest part for me by far
#was getting the links to work. Today I tried various strategies but how google shopping is designed the only
#way to get links is to click on each product specifically. I think they do that to slow down web scrapers and
#bots. The way around it that I used was basically just acting like a real human. I made the program automatically
#click on each product and copy the link from the right hand side view that pops up. For the items where that is
#unavailable I make it display NA. Relocating the products in a try loop later on seemed to be the fix for the links
#being in random order. I was so relieved when I finally figured that out. I could use this web scraping knowledge
#for whatever website allows me to and hopefully I can make other cool projects. It has been
#a fun project with a bunch of hardships and triumphs. The code is not very long but I feel like I learned a lot.

#First I worked on getting familiar with web scrapers and I did a follow along youtube tutorial for a automatic
#cookie clicker program that plays the game for you. That helped me learn how to click and open websites. I then
#got to work with learning more about HTML and the selectors to make the code open and click what I want it to.
#This knowledge helped me make the barebones code for a basic program that could extract all the titles, prices,
#reviews, and conditions for whatever product I searched up. Once I got that list working, I spent the rest of
#my time figuring out how to get links to work. I explained previously but I had to use a very specific approach
#and it took a lot of trial and error to achieve it. That is how I reached the code I have now which has a functional
#list with accurate links!
