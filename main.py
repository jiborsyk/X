import json
import bottle
import appcode

# This file defines the behavior of the bottle
# web server: it specifies the request routes
# to which it will respond

@bottle.route("/")
def handleRequestHTML():
    return bottle.static_file("index.html", root="")

@bottle.route("/species.js")
def handleRequestCode():
    return bottle.static_file("species.js", root="")


@bottle.route('/speciessort')
def handlerequestdata4():
    return json.dumps(appcode.sortByAnimal())


@bottle.route('/species_location')
def handlerequestdata6():
    return json.dumps(appcode.specieslocation())


@bottle.route('/getsearch')
def get_search():
    search = appcode.get_search()
    return json.dumps(search)

@bottle.post('/search')
def do_search():
    #response = urllib.request.urlopen('/search')
    #content = json.loads(response.read().decode())
    content = bottle.request.body.read()
    content= content.decode
    content = json.loads(str(content))
    appcode.addsearch(content)

bottle.run(host = '0.0.0.0', port='8080', debug=True)
