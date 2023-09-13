from flask import Flask, render_template
import facebook

app = Flask(__name__)

@app.route('/')
def fetch_facebook_info():
    # Replace 'YOUR_ACCESS_TOKEN' with your actual Facebook access token
    access_token = {"TOKEN"}
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

if __name__ == "__main__":
    app.run(debug=True)
