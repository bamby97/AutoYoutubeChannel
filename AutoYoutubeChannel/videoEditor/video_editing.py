#!/usr/bin/env python
# coding: utf-8

# In[1]:


from moviepy.editor import *

postedByFontSize=25
replyFontSize=35
titleFontSize=100
cortinilla= VideoFileClip('assets for Channel/assets for video/transicion.mp4')
clip = ImageClip('assets for Channel/assets for video/background assets/fondo_preguntas.jpg').on_color((1920, 1080))
final= VideoFileClip('assets for Channel/assets for video/transicion.mp4')


# In[2]:


def generate_video_of_reply(author,replyLines,replyaudio):
    videoComponents=[]
    textReply= []
    postedBy = TextClip('Posted by /'+author, fontsize=postedByFontSize, color='white')
    postedBy=postedBy.set_pos((162, 124))
    index=0
    yAxis=184
    for replyLine in replyLines:
        print('line '+str(index)+replyLine)
        try:
            replyline=TextClip(replyLine, fontsize=postedByFontSize, color='white')
            replyline=replyline.set_pos((162,yAxis))
            textReply.append(replyline)
        except:
            print('null line')
        print(yAxis)
        yAxis+=25
        index+=1
    videoComponents.append(clip)
    videoComponents.append(postedBy)
    videoComponents.extend(textReply)
    replyVideo = CompositeVideoClip(videoComponents)
    replyVideo = replyVideo.set_duration(replyaudio.duration)
    replyVideo = replyVideo.set_audio(replyaudio)
    return replyVideo


# In[1]:


def generate_final_video(title,replies):
    videoClips=[]
    videoClips.append(generate_title(title))
    index=0
    for reply in replies:
        audio=AudioFileClip('videoEditor/comment'+str(index)+'.mp3')
        videoClips.append(generate_video_of_reply(reply['author'],reply['replyLines'],audio))
        videoClips.append(cortinilla)
        index+=1
    videoClips.append(final)
    finalVideo=concatenate_videoclips(videoClips)
    #finalVideo.fx(vfx.speedx, factor=1.3)
    finalVideo.write_videofile("text.mp4", fps=24)


# In[ ]:


def generate_title(title):
    videoComponents=[]
    yAxisJumpInLine=80
    maxCharsInLine=38
    titleaudio=AudioFileClip('videoEditor/title.mp3')
    titleline=TextClip(title, fontsize=titleFontSize, color='white')
    titleline=titleline.set_pos((202,94))
    #if(len(titleline)>38):
     #   sublines=[line[i:i+maxCharsInLine] for i in range(0, len(line), maxCharsInLine)]
      #  sublinesSize=len(sublines)
       # for x in range(sublinesSize):
        #    index = len(sublines[x]) # calculate length of string and save in index
         #   while index > 0:
          #      if(sublines[x][ index - 1 ]==' '): # save the value of str[index-1] in reverseString
           #     index = index - 1
            #if(' ' in sublines[x+1]):

    videoComponents.append(clip)
    videoComponents.append(titleline)
    titleVideo = CompositeVideoClip(videoComponents)
    titleVideo = titleVideo.set_duration(titleaudio.duration)
    titleVideo = titleVideo.set_audio(titleaudio)
    return titleVideo
