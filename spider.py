from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from flask import Flask, request, Response, abort, render_template, jsonify
from flask_restful import Resource
import os
from pyvirtualdisplay import Display

app = Flask(__name__)


url = 'http://cnpj.info/'

teste = "24.365.710/0001-83"


# def getInfo(cnpj):
#     browser = webdriver.Firefox()
#     try:
#         browser.get(url)
#         t = browser.find_element_by_xpath('//input[@type="text"]')
#         t.send_keys(cnpj)
#         b = browser.find_element_by_xpath("//input[@type='submit']").click()
#         element = browser.find_element_by_tag_name("li")
#         print(element.text)
#         return element.text
#     finally:
#         browser.quit()

# @app.route('/', methods=['GET', 'POST'])
@app.route('/index/<cnpj>', methods=['GET'])
def index(cnpj):
    
    if request.method == 'GET':
        value = ''
        with Display():
            browser = webdriver.Firefox()
            try:
                browser.get(url)
                t = browser.find_element_by_xpath('//input[@type="text"]')
                t.send_keys(cnpj)
                b = browser.find_element_by_xpath("//input[@type='submit']").click()
                element = browser.find_element_by_tag_name("li")
                print(element.text)
                # return render_template('index.html', title='Home', result=element.text)
                # return {'status': 'success', 'data': element.text}, 200
                return jsonify(element.text)
            finally:
                browser.quit()

    

if __name__ == '__main__':
	port = int(os.environ.get("PORT", 5000))
	app.run(host='0.0.0.0', port=port)

  #app.run(debug=True)
