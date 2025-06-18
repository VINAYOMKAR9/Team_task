import os
from flask import current_app
from werkzeug.utils import secure_filename
from fer_app import db
from fer_app.models import Video

def save_video(file, user_id, title):
    filename = secure_filename(file.filename)
    folder = os.path.join(os.path.abspath(os.path.dirname(__file__)), '..', '..', 'videos')
    os.makedirs(folder, exist_ok=True)  # Ensure folder exists
    filepath = os.path.join(folder, filename)
    file.save(filepath)

    video = Video(title=title, filename=filename, uploaded_by=user_id)
    db.session.add(video)
    db.session.commit()
    return filename

def get_all_videos():
    return Video.query.all()
