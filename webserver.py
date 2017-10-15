"""
webserver.py

File that is the central location of code for your webserver.
"""

import requests
import os

from flask import Flask, request, render_template, redirect
app = Flask(__name__, static_url_path="/static")

@app.route('/')
def default():
  return redirect('/index')

@app.route('/index')
def show_home_page():
  return render_template('index.html')

@app.route('/contact')
def show_contact_page():
  return render_template('contact-us.html')

@app.route('/about')
def show_about_page():
  return render_template('about-us.html')

@app.route('/blog/8-experiments-in-motivation')
def show_blog1():
  return render_template('experiments.html')

@app.route('/blog/a-mindful-shift-of-focus')
def show_blog2():
  return render_template('mindful.html')

@app.route('/blog/how-to-develop-an-awesome-sense-of-direction')
def show_blog3():
  return render_template('develop.html')

@app.route('/blog/training-to-be-a-good-writer')
def show_blog4():
  return render_template('training.html')

@app.route('/blog/what-productivity-systems-wont-solve')
def show_blog5():
  return render_template('productivity.html')

@app.route('/contact', methods=['POST'])
def send_email():
	message = request.form.get("message")
	subject = request.form.get("message")
	name = request.form.get("name")
	email = request.form.get("email")

	message = message + "\n\n From: " + name + " Email: " + email
	notifications = []

	data = {
		'from': os.environ["INFO253_MAILGUN_FROM_EMAIL"],
		'to': os.environ["INFO253_MAILGUN_TO_EMAIL"],
		'subject': subject,
		'text': message,
	}
	auth = (os.environ["INFO253_MAILGUN_USER"], os.environ["INFO253_MAILGUN_PASSWORD"])

	r = requests.post(
		'https://api.mailgun.net/v3/{}/messages'.format(os.environ["INFO253_MAILGUN_DOMAIN"]),
		auth=auth,
		data=data)
	if r.status_code == requests.codes.ok:
		notifications.append("Hi " + name + ", your message has been sent.")
	else:
		notifications.append("Your message was not sent. Please try again later")

	return render_template("contact-us.html", notifications=notifications)
