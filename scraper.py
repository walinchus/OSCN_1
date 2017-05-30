import mechanize 
import lxml.html

oscn_starting_url = "http://www.oscn.net/dockets/Results.aspx"

br = mechanize.Browser()
br.set_handle_robots(False)

for form in br.forms():
    print "Form name:", form.name
    print form

#response = br.open(oscn_starting_url)

#print "All forms:", [ form.name  for form in br.forms() ]

#br.select_form(name="search-form")
#print br.form

#br["ctl00$phMainContent$dropDownAwardDate"] = ["Between"]
#br["ctl00$phMainContent$txtGrantDateFrom"] = "01/01/2004"
#br["ctl00$phMainContent$txtGrantDateTo"]  = "20/01/2004"


#response = br.submit()
#print response.read()


# import scraperwiki
# import lxml.html
#
# # Read in a page
# html = scraperwiki.scrape("http://foo.com")
#
# # Find something on the page using css selectors
# root = lxml.html.fromstring(html)
# root.cssselect("div[align='left']")
#
# # Write out to the sqlite database using scraperwiki library
# scraperwiki.sqlite.save(unique_keys=['name'], data={"name": "susan", "occupation": "software developer"})
#
# # An arbitrary query against the database
# scraperwiki.sql.select("* from data where 'name'='peter'")

# You don't have to do things with the ScraperWiki and lxml libraries.
# You can use whatever libraries you want: https://morph.io/documentation/python
# All that matters is that your final data is written to an SQLite database
# called "data.sqlite" in the current working directory which has at least a table
# called "data".
