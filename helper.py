import  pandas as pd
from  urlextract import  URLExtract
extract=URLExtract()
from collections import Counter
from  wordcloud import  WordCloud
word_cloud=WordCloud()
import re

# text file preprocssing


def pre(text):
    date=re.findall('\d{1,2}/\d{1,2}/\d{2,4},\s\d{1,2}:\d{1,2}\s-\s',text)

    user=re.split('\d{1,2}/\d{1,2}/\d{2,4},\s\d{1,2}:\d{1,2}\s-\s',text)[1:]
    
    df=pd.DataFrame({'date':date,'user':user})
    id=[]
    message=[]
    for i in df['user']:
        f=re.split('([\w\W]+?):\s',i)
        if f[1:]:
            id.append(f[1])
            message.append(' '.join(f[2:]))
        else:
            id.append('notification')
            message.append(f[0])

    df['user']=id
    df['message']=message
    df['date']=pd.to_datetime(df['date'],format='%d/%m/%Y, %H:%M - ')
    df['day']=df['date'].dt.day_name()
    df['month']=df['date'].dt.month_name()
    df['year']=df['date'].dt.year
    df.dropna(inplace=True)
    df=df[df['user']!='notification']
    df.drop_duplicates(inplace=True)
    return df


def iph_pre(text):
    date=re.findall('\d{1,3}/\d{1,2}/\d{4},\s\d{1,2}:\d{1,2}:\d{1,2}',text)
    user=re.split('\[\d{1,3}/\d{1,2}/\d{4},\s\d{1,2}:\d{1,2}:\d{1,2}\s\D{2}]\s',text)[1:]
    df=pd.DataFrame({'date':date,'user':user})
    id=[]
    message=[]
    for i in df['user']:
        f=re.split('([\w\W]+?):\s',i)
        if f[1:]:
            id.append(f[1])
            message.append(' '.join(f[2:]))
        else:
            id.append('notification')
            message.append(f[0])

    df['user']=id
    df['message']=message
    df['date']=pd.to_datetime(df['date'],format='%d/%m/%Y, %H:%M:%S')
    df['day']=df['date'].dt.day_name()
    df['month']=df['date'].dt.month_name()
    df['year']=df['date'].dt.year
    df.dropna(inplace=True)
    df=df[df['user']!='notification']
    df.drop_duplicates(inplace=True)
    return df










text=open('stop_hinglish.txt','r')
cont=text.read()









# ----------END---------------

# message count total
def message_count(text,df):
    if text== 'Over All':
    
        b=df.shape[0]
        return b
    else:
            a=df[df['user']==text]
            return a.shape[0]
# ---------------END-----------------------


# words count total

def word_count(text,df):
    

    if text=='Over All':
        a=df['message'].str.split()
        w=[]
        for i in a:
            w.append(len(i))
        return sum(w)
    else:
        a=df[df['user']==str(text)]['message']
        a.str.split()
        word=[]
        for i in a:
            word.append(len(i))
        return sum(word)

# -------------END------------------------


# media files finding
def media_count(text,df):
    if text=='Over All':
        a=df[df['message']=='<Media omitted>\n'].shape[0]
        return a
    else: 
        a=df[(df['message']=='<Media omitted>\n') & (df['user']==str(text))]
        return a.shape[0]

# ----------END-----------------------------


# Links finding
def link_count(text,df):
    if text=='Over All':
        link=[]
        for  i in df['message']:
            link.extend(extract.find_urls(i))
            return len(link)
    else:
        a=df[df['user']==str(text)]['message']
        
        link=[]
        
        for i in a:
            link.extend(extract.find_urls(i))
            return(len(link))

# -----------END--------------------




        
def top_person(df):
    
        a=df['user'].value_counts().head(5)
      
        b=((df['user'].value_counts()/df.shape[0])*100).reset_index().rename(columns={'index':'User','user':'Persentage'})
        return a,b

def person_cloud(text,df):
    single=[]
    for i in df[df['user']==str(text)]['message']:
        single.append(i)
    b=word_cloud.generate(str(single))
    return b

def message_top_u(text,df):
    word=[]
    user=df[df['user']==str(text)]
    for i in user['message'].str.split():
        for c in i:
                c.lower()
                if c not in cont:
                        word.append(c)
    b=pd.DataFrame(Counter(word).most_common(10)).rename(columns={0:'Message',1:'total'})
    return b



# -------END-------------------------s



# wordcloud
def cloud(df):
    message=[]
    for i in df['message']:
        message.append(i)
    a=word_cloud.generate(str(message))
    return a

# ------------END--------------



def message_top(df):
    word=[]

    for i in df['message'].str.split():
        for c in i:
                c.lower()
                if c not in cont:
                        word.append(c)
    
    a=pd.DataFrame(Counter(word).most_common(10)).rename(columns={0:'Message',1:'total'})
    return a

# --------------END-----------------------

#  Downloads options

def covert_csv(df):

    return df.to_csv().encode('utf-8')

# -------------END------------------------



