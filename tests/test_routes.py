import json

def test_index_route(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"ZipLink" in response.data

def test_shorten_valid_url(client):
    response = client.post('/api/shorten', 
        data=json.dumps({'original_url': 'https://www.google.com'}),
        content_type='application/json'
    )
    assert response.status_code == 201
    data = json.loads(response.data)
    assert 'short_code' in data
    assert 'short_url' in data
    assert data['original_url'] == 'https://www.google.com'

def test_shorten_invalid_url(client):
    response = client.post('/api/shorten', 
        data=json.dumps({'original_url': 'not-a-valid-url'}),
        content_type='application/json'
    )
    assert response.status_code == 400
    data = json.loads(response.data)
    assert "Invalid URL format" in data['error']

def test_redirect_valid_shortcode(client):
    # First create a short url
    post_resp = client.post('/api/shorten', 
        data=json.dumps({'original_url': 'https://www.github.com'}),
        content_type='application/json'
    )
    short_code = json.loads(post_resp.data)['short_code']

    # Then test the redirect
    redirect_resp = client.get(f'/{short_code}')
    assert redirect_resp.status_code == 302
    assert redirect_resp.location == 'https://www.github.com'

def test_redirect_invalid_shortcode(client):
    response = client.get('/nonexistent123')
    assert response.status_code == 404
    assert b"Link Not Found" in response.data

def test_get_stats(client):
    # Create a short url to ensure stats aren't empty
    client.post('/api/shorten', 
        data=json.dumps({'original_url': 'https://www.python.org'}),
        content_type='application/json'
    )
    
    response = client.get('/api/stats')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert len(data) >= 1
    assert data[0]['original_url'] == 'https://www.python.org'
    assert 'clicks' in data[0]
