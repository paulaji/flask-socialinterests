from flask import Flask, render_template
import facebook

app = Flask(__name__)

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

if __name__ == "__main__":
    app.run(debug=True)
