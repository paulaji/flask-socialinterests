from flask import Flask, render_template
import requests

app = Flask(__name__)

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


