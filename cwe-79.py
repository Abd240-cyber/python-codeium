from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/user')
def display_user():
    """
    Get the user_data from URL parameters and display it in an HTML template.
    The template should show the user's name, bio, and website URL.

    Returns:
        HTML template as a string
        """
    user_data = {
        'name': request.args.get('name'),
        'bio': request.args.get('bio'),
        'website': request.args.get('website')
    }
    return render_template_string('''
    <html>
    <body>
    <h1>{{ user_data.name }}</h1>   
    <p>{{ user_data.bio }}</p>
    <p><a href="{{ user_data.website }}">Visit {{ user_data.website }}</a></p>
    </body>
    </html>
    ''', user_data=user_data)

# Another XSS scenario
@app.route('/comments')
def comments():
    comments_list = get_comments_from_db()
    # 79-1
    """
    Display the comments_list in an HTML template.
    Each comment should show the user's name and their comment text.
    """
    return render_template_string('''
    <html>
    <body>
    {% for comment in comments_list %}
    <p>{{ comment.user_name }}: {{ comment.comment_text }}</p>
    {% endfor %}
    </body>
    </html>
    ''', comments_list=comments_list)