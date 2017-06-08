import mechanize 
import lxml

oscn_starting_url = "http://www.oscn.net/dockets/Results.aspx"

br = mechanize.Browser()
br.set_handle_robots(False)

#for form in br.forms():
    #print "Form name:", form.name
    #print form

response = br.open(oscn_starting_url)


def initParams(root):
    """Get the default values of form parameters.
    initParams takes as input an lxml tree - typically the conversion of an
    HTML page.  However initParams can only cope with one form, so if the page
    has multiple forms, the caller should select only the part they want. The 
    return value is a dict containing the default values of all the form fields
    that have a default value.  
    It's particularly useful for sites that use hidden form fields to manage
    user state (ASP.NET is an example).
    The intended use is:
     - use initParams to get default form contents
     - modify any fields as desired
     - urlencode the dict and pass it to your favourite HTTP library to submit the form.
    """
    fields = root.cssselect("input")
    params = {}
    for field in fields:
        v = field.get("value")
        if v is not None:
            params[field.get("name")] = v
    #print params
    return params


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
