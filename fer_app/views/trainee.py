from flask import Blueprint, request, render_template, redirect, url_for, flash, send_from_directory, current_app
from flask_login import login_required, current_user
from fer_app.controllers.trainee_controller import save_video, get_all_videos
import os

trainee_bp = Blueprint('trainee', __name__)

@trainee_bp.route('/upload', methods=['GET', 'POST'])
@login_required
def upload_video():
    if request.method == 'POST':
        file = request.files['video']
        title = request.form.get('title')
        if not file or file.filename == '':
            flash("No file selected")
            return redirect(request.url)
        filename = save_video(file, current_user.id, title)
        flash(f"Video '{filename}' uploaded successfully")
        return redirect(url_for('trainee.list_videos'))
    return render_template('upload.html')

@trainee_bp.route('/videos', methods=['GET'])
@login_required
def list_videos():
    videos = get_all_videos()
    return render_template('video_list.html', videos=videos)

@trainee_bp.route('/videos/<filename>')
@login_required
def stream_video(filename):
    video_folder = os.path.join(os.path.abspath(os.path.dirname(__file__)), '..', '..', 'videos')
    return send_from_directory(video_folder, filename)
