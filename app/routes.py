import urllib.parse
from flask import Blueprint, request, jsonify, redirect, abort, render_template
from sqlalchemy.exc import IntegrityError
from . import db
from .models import URL
from .utils import generate_short_code

main = Blueprint('main', __name__)

def is_valid_url(url):
    """Basic validation to ensure the URL has a scheme and network location."""
    try:
        result = urllib.parse.urlparse(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False

@main.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@main.route('/api/shorten', methods=['POST'])
def shorten_url():
    data = request.get_json()
    
    if not data or 'original_url' not in data:
        return jsonify({"error": "Missing 'original_url' in request body."}), 400
        
    original_url = data['original_url']
    
    # Strict validation for URL format
    if not is_valid_url(original_url):
        return jsonify({"error": "Invalid URL format provided."}), 400
        
    # Attempt to generate and save unique code (up to 3 tries to prevent extremely rare nanoid collisions)
    for _ in range(3):
        short_code = generate_short_code()
        new_url = URL(original_url=original_url, short_code=short_code)
        
        db.session.add(new_url)
        try:
            db.session.commit()
            short_url = f"{request.host_url}{short_code}"
            return jsonify({
                "short_code": short_code,
                "short_url": short_url,
                "original_url": original_url
            }), 201
        except IntegrityError:
            # Catch duplicate short_code error
            db.session.rollback()
            continue
            
    return jsonify({"error": "Could not generate a short link. Please try again."}), 500

@main.route('/<short_code>', methods=['GET'])
def redirect_to_url(short_code):
    url_entry = URL.query.filter_by(short_code=short_code).first()
    
    if not url_entry:
        return render_template('404.html'), 404
        
    # Increment usage metrics
    url_entry.clicks += 1
    db.session.commit()
    
    return redirect(url_entry.original_url, code=302)

@main.route('/api/stats', methods=['GET'])
def get_stats():
    """Fetch URLs and their click stats with pagination."""
    limit = request.args.get('limit', 5, type=int)
    recent_urls = URL.query.order_by(URL.created_at.desc()).limit(limit).all()
    return jsonify([url.to_dict() for url in recent_urls]), 200

@main.route('/api/shorten/<short_code>', methods=['DELETE'])
def delete_url(short_code):
    url_entry = URL.query.filter_by(short_code=short_code).first()
    if not url_entry:
        return jsonify({"error": "Link not found"}), 404
        
    db.session.delete(url_entry)
    db.session.commit()
    return jsonify({"message": "Successfully deleted"}), 200
