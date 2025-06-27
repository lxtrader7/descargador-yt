from flask import Flask, request, send_file
import yt_dlp

app = Flask(__name__)

@app.route('/download')
def download():
    video_url = request.args.get('url')
    ydl_opts = {
        'format': 'best[ext=mp4]',
        'outtmpl': 'video.%(ext)s',
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(video_url, download=True)
        filename = ydl.prepare_filename(info)
        
    return send_file(filename, as_attachment=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)