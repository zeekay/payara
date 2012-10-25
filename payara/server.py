from bottle import app, post, request, run
import json, repo, s3

app = app()

@app.post('/')
def webhook():
    data = json.loads(request.forms.get('payload'))
    repo_name = data['repository']['name']
    repo_user = data['repository']['owner']['name']
    print 'Updating local copy of %s' % repo_name
    repo.update(repo_name, repo_user)
    print 'Uploading %s' % repo_name
    s3.upload(repo_name)
