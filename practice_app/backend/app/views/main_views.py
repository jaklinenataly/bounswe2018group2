# Copyright 2014 SolidBuilds.com. All rights reserved
#
# Authors: Ling Thio <ling.thio@gmail.com>


from flask import Blueprint, redirect, Response, request
from flask import request, url_for


from service import api as tweetapi

main_blueprint = Blueprint('main', __name__, template_folder='templates')

# The Home page is accessible to anyone
@main_blueprint.route('/')
def home_page():
    return "awesome, alesta!"


@main_blueprint.route('/directmessage', methods=['POST'])
def send_direct_message():
    screen_name = request.form["screen_name"]
    message = request.form["message"]
    tweetapi.sendDirectMessage(screen_name, message)
    return ""

@main_blueprint.route('/posttweet', methods=['POST'])
def send_tweet():
    content = request.get_json()["content"]
    tweetapi.postTweet(content)
    resp = Response("gonderdim")
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp

@main_blueprint.route('/searchkey', methods=['GET'])
def get_search_results():
    key = request.args.get('key')
    limit = int(request.args.get('limit'))
    resp = Response(tweetapi.searchKey(key,limit))
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp

@main_blueprint.route('/gettweets', methods=['GET'])
def get_self_tweets():
    count = int(request.args.get('count'))
    return tweetapi.getSelfTweets(count);


