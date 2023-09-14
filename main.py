from flask import Flask, render_template
import facebook
import requests

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.route('/facebook')
def fetch_facebook_info():
    access_token = {""}
    graph = facebook.GraphAPI(access_token)

    try:
        fields = ['name,email,birthday,gender,hometown,inspirational_people,location,quotes,posts']
        profile = graph.get_object('me', fields=fields)

        name_value = profile.get('name')
        email_value = profile.get('email')
        birthday_value = profile.get('birthday')
        gender_value = profile.get('gender')
        hometown_value = profile.get('hometown')
        ip_value = profile.get('inspirational_people')
        location_value = profile.get('location')
        quotes_value = profile.get('quotes')
        posts_value = profile.get('posts')

        context = {
            'name': name_value,
            'email': email_value,
            'birthday': birthday_value,
            'gender': gender_value,
            'hometown': hometown_value,
            'ip': ip_value,
            'location': location_value,
            'quotes': quotes_value,
            'posts': posts_value,
        }

        return render_template('facebook_info.html', **context)
    except facebook.GraphAPIError as e:
        error_message = str(e)
        return render_template('error.html', error=error_message)
    
@app.route('/instagram')
def fetch_instagram_accounts():
    access_token = {""}

    try:
        graph = facebook.GraphAPI(access_token)
        accounts_data = graph.get_object('me/accounts')
        accounts = accounts_data.get('data', [])

        context = {
            'accounts': accounts
        }

        return render_template('instagram_info.html', **context)
    except facebook.GraphAPIError as e:
        error_message = str(e)
        return render_template('error.html', error=error_message)

@app.route('/linkedin')
def fetch_linkedin_accounts():
    api_key = ''
    headers = {'Authorization': 'Bearer ' + api_key}
    api_endpoint = 'https://nubela.co/proxycurl/api/v2/linkedin'
    linkedin_profile_url = 'https://www.linkedin.com/in/paulaji'  # Replace with the desired LinkedIn profile URL

    response = requests.get(api_endpoint,
                            params={'url': linkedin_profile_url},
                            headers=headers)

    if response.status_code == 200:
        linkedin_data = response.json()

        return render_template('linkedin_info.html', linkedin_data=linkedin_data)
    else:
        error_message = f"Request failed with status code: {response.status_code}"
        return render_template('error.html', error=error_message)

if __name__ == "__main__":
    app.run(debug=True)
