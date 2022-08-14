def get_yt_video(vid_id):
  return f"""
  <div class="yt-container">
  <iframe class="yt-video" src="https://www.youtube.com/embed/{vid_id}?rel=0" frameBorder="0">
    Browser does not support embedded videos.
  </iframe>
</div>
"""
