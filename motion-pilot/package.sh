#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
ffmpeg -y -loglevel error -i motion-pilot/silent.mp4 -ss 110.2 -i full-video/original.mp4 -map 0:v:0 -map 1:a:0 -c:v copy -c:a aac -b:a 128k -t 9.3 -af 'afade=t=in:st=0:d=0.02,afade=t=out:st=9.2:d=0.1' -movflags +faststart motion-pilot/web-search.mp4
ffmpeg -y -loglevel error -ss 110.2 -t 9.3 -i full-video/original.mp4 -i motion-pilot/web-search.mp4 -filter_complex "[0:v]scale=640:360,setsar=1,pad=640:392:0:32:white,drawtext=text='ORIGINAL':x=16:y=7:fontsize=18:fontcolor=black[a];[1:v]scale=640:360,setsar=1,pad=640:392:0:32:white,drawtext=text='IMAGE-FIRST PILOT':x=16:y=7:fontsize=18:fontcolor=black[b];[a][b]hstack=inputs=2[v]" -map '[v]' -map 1:a:0 -c:v libx264 -preset veryfast -crf 19 -r 30 -c:a copy -t 9.3 -pix_fmt yuv420p -movflags +faststart motion-pilot/comparison.mp4
