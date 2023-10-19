from django.shortcuts import render
from django.http import HttpResponse, FileResponse
from .models import Video
import os



def home(request):
    movies = Video.objects.all()
    
    return render(request,'home.html',{'mv':movies})

def video(request,id):
    return render(request, 'index.html',{'vid':id})



def stream_video(request, id):
    video_id = id
    try:
        video = Video.objects.get(pk=video_id)
        video_path = video.video_file.path
    except Video.DoesNotExist:
        return HttpResponse("Video not found", status=404)

    range_header = request.headers.get('Range')
    if not range_header:
        return HttpResponse("Requires Range header", status=400)

    video_size = os.path.getsize(video_path)
    CHUNK_SIZE = 10 * 1024 

    range_values = range_header.replace('bytes=', '').split('-')
    if len(range_values) != 2:
        return HttpResponse("Invalid Range header format", status=400)

    start_byte, end_byte = 0, video_size - 1
    if range_values[0]:
        start_byte = int(range_values[0])
    if range_values[1]:
        end_byte = min(CHUNK_SIZE - 1, video_size - 1)

    content_length = end_byte - start_byte + 1

    headers = {
        'Content-Range': f'bytes {start_byte}-{end_byte}/{video_size}',
        'Accept-Ranges': 'bytes',
        'Content-Length': content_length,
        'Content-Type': 'video/mp4',
    }

    video_file = open(video_path, 'rb')
    video_file.seek(start_byte)

    def file_iterator(file, chunk_size):
        while True:
            data = file.read(chunk_size)
            if not data:
                break
            yield data

    response = FileResponse(file_iterator(video_file, CHUNK_SIZE), status=206, content_type='video/mp4', as_attachment=False)
    for key, value in headers.items():
        response[key] = value

    return response
