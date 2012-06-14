import re
import request
import bs4

# Dumps out a json structure
#
# {"riffs": [
#    {"title": "a",
#     "release_date": "YYYY_MM_DD",
#     "riff_date": "YYYY_MM_DD",
#     "amazon link"}}
#

# Need
#
# 1. walk rifftrax page from root
# 2. find all movies
# 3. need a rules/functions about how to do this
#
# for each page, dump out data (lookup the best way to do this.)
# -> Could just convert it to json
#
# Take the json for each movie and compare it with what's in our db
#
