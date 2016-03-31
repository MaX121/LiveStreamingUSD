# Vinsen Muliadi - admin@max-metal.us
# https://github.com/MaX121/LiveStreamingUSD/

# importing basic library
# os library use to execute the shell script
# sys library use to automatically exit this program after finish executing
# subprocess use to set the starting directory as a variable
# urlopen use to open the YouTube link in the background
# BeautifulSoup use to scrap the HTML script on YouTube link
import os, sys, subprocess
from urllib.request import urlopen
from bs4 import BeautifulSoup

# the program will set the starting directory as the variable
# starting directory means your active directory when you execute this program
# for example you execute this program on /home/user/
# so the starting directory is /home/user/
basedir = subprocess.check_output('pwd').decode(encoding='UTF-8')
# os.system("touch /var/www/wisuda/visitor_counter.txt")

# user input the YouTube link to embed on the webpage
# if the user insert without 'https', the program will automatically add it
link = input('YouTube Link :: ')

# open the YouTube link from user input
# pretty obvious I think
print('Processing Link ...')
page = urlopen(link)

# get the YouTube video ID
# the link started with https://
# if not, automatically add https:// on it
videoID = link.replace(link[:32], '')

# scrap the YouTube link from user input
# get the div.watch-view-count value
print('Generating index.html')
bsoup = BeautifulSoup(page, "lxml")
views = bsoup.find("div", {'class' : 'watch-view-count'}).prettify()

# creating index.php
# if the file already exist, Python will replace it with the new one
berkas = open("/mnt/Data/PTInformasi/index.html", "w")
berkas.write("<!doctype html>")
berkas.write("<html>")
berkas.write("<head>")
berkas.write("<title>Proyek Teknologi Informasi - Live Streaming Wisuda</title>")
berkas.write("<link rel='stylesheet' href='https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css' />")
berkas.write("<style type='text/css'>@import url(https://fonts.googleapis.com/css?family=Open+Sans);</style>")
berkas.write("<script type='text/javascript' src='http://code.jquery.com/jquery-1.12.2.min.js'></script>")
berkas.write("<script type='text/javascript' src='"+basedir+"/location.js'></script>")
berkas.write("<script type='text/javascript' src='"+basedir+"/script.js'></script>")
berkas.write("</head>")
berkas.write("<body>")
berkas.write("<div class='container-fluid'>")
berkas.write("<div class='row'>")
berkas.write("<div class='col-xs-12'>")
berkas.write("<div align='center'><iframe id='youtube-video' src='https://www.youtube.com/embed/" + videoID + "?rel=0&autoplay=1' frameborder='0' allowfullscreen></iframe></div>")
berkas.write("</div>")
berkas.write("</div>")
berkas.write("</div>")
berkas.write("<div class='container-fluid' id='menubar-bottom'>")
berkas.write("<div class='row'>")
berkas.write("<div class='col-xs-6'>This site is created by PTI - 2016</div>")
berkas.write("<div class='col-xs-3'>Jumlah Tayang :: " + views + "</div>")
berkas.write("<div class='col-xs-3'><span id='location' onclick='alert('this');'></span></div>")
berkas.write("</div>")
berkas.write("</div>")
berkas.write("</body>")
berkas.write("</html>")
berkas.close()

# reporting to admin and exit automatically
print('File generated successfully')
sys.exit(0)
