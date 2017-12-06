from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('L5jbUsAeq2u4faluwdPlqFoemCzUuBPv7CZEv1QsFyWMBM5AqcCUxek+pEyakT60Rm8qVh8f5JPdTjrRmu+CJopqxNB+640zmj0ZlYjDVaHL/waOjcX0u8HbOegXBzOqbaiz1wX+YI0B0rvNTtyK0gdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('c57fd4bcf7a7832bc3c6becb038a5c66')


#this part is my code

def getData(fileName): #開啟六情緒辭典
    text = ""
    for i in open(fileName, 'r', encoding='UTF-8'):
        text = text + i.upper()
    text_list = []
    text_split = text.split('\n')
    for i in range(0,len(text_split)):
        text_list.append(text_split[i])
    return(text_list)

#此函數為判斷漲跌
def Prediction(Positive,Negative,Uncertainty,Litigious,Modal_Strong,Modal_Weak):
    return('up')
    #這裡是決策樹

def getPrediction(news):
    #辭典
    positive = getData('Positive.txt')
    negative = getData('Negative.txt')
    uncertainty = getData('Uncertainty.txt')
    litigious = getData('Litigious.txt')
    modal_strong = getData('Modal_Strong.txt')
    modal_weak = getData('Modal_Weak.txt')

    #將txt文字轉為大寫存放在text
    #也將不要的符號去除
    news = news.replace("’","")
    news = news.replace(":","")
    news = news.replace(",","")
    news = news.replace(".","")
    news = news.replace("‘","")
    news = news.replace("(","")
    news = news.replace(")","")
    text = news.upper()#print(i,end='')

    #將text切割後存放在text_split
    #假設該詞有在Positive裡將紀錄
    temp_list = [] #存放文字及向量紀錄
    positive_num = 0
    negative_num = 0
    uncertainty_num = 0
    litigious_num = 0
    modal_strong_num = 0
    modal_weak_num = 0

    text_split = text.split(" ")
    text_split = (list(set(text_split))) #去除重複的字
    for i in range(0,len(text_split)):
        if(text_split[i] in positive):
            temp = 0
            text = text_split[i]
            for j in range(0,len(temp_list)): #假設A in B 先判斷A是否已在list裡，如果有就從list加數值
                if(text in temp_list[j][0]):  #如[A,0,0,0,0,0,1] --> [A,1,0,0,0,0,1]
                    temp_list[j][1] = 1
                    positive_num += 1
                    temp += 1
                    break
            if temp == 0:
                positive_num += 1
                temp_list.append([text_split[i],1,0,0,0,0,0])

        if(text_split[i] in negative):
            temp = 0
            text = text_split[i]
            for j in range(0,len(temp_list)):
                if(text in temp_list[j][0]):
                    temp_list[j][2] = 1
                    negative_num += 1
                    temp += 1
                    break
            if temp == 0:
                negative_num += 1
                temp_list.append([text_split[i],0,1,0,0,0,0])

        if(text_split[i] in uncertainty):
            temp = 0
            text = text_split[i]
            for j in range(0,len(temp_list)):
                if(text in temp_list[j][0]):
                    temp_list[j][3] = 1
                    uncertainty_num += 1
                    temp += 1
                    break
            if temp == 0:
                uncertainty_num += 1
                temp_list.append([text_split[i],0,0,1,0,0,0])

        if(text_split[i] in litigious):
            temp = 0
            text = text_split[i]
            for j in range(0,len(temp_list)):
                if(text in temp_list[j][0]):
                    temp_list[j][4] = 1
                    litigious_num += 1
                    temp += 1
                    break
            if temp == 0:
                litigious_num += 1
                temp_list.append([text_split[i],0,0,0,1,0,0])

        if(text_split[i] in modal_strong):
            temp = 0
            text = text_split[i]
            for j in range(0,len(temp_list)):
                if(text in temp_list[j][0]):
                    temp_list[j][5] = 1
                    modal_strong_num += 1
                    temp += 1
                    break
            if temp == 0:
                modal_strong_num += 1
                temp_list.append([text_split[i],0,0,0,0,1,0])

        if(text_split[i] in modal_weak):
            temp = 0
            text = text_split[i]
            for j in range(0,len(temp_list)):
                if(text in temp_list[j][0]):
                    temp_list[j][6] = 1
                    modal_weak_num += 1
                    temp += 1
                    break
            if temp == 0:
                modal_weak_num += 1
                temp_list.append([text_split[i],0,0,0,0,0,1])


    #情感維度強度分佈向量
    temp_list.append(['S',positive_num,negative_num,uncertainty_num,litigious_num,modal_strong_num,modal_weak_num])
    #print(positive_num,negative_num,uncertainty_num,litigious_num,modal_strong_num,modal_weak_num)
    #temp_for_bot = str(positive_num) +','+ str(negative_num) +','+ str(uncertainty_num) +','+ str(litigious_num) +','+ str(modal_strong_num) +','+ str(modal_weak_num)
    #return(temp_for_bot)
    #將結果存在csv檔
    #import pandas as pd
    #creat_csv = pd.DataFrame(temp_list, columns=['Words','Positive','Negative','Uncertainty','Litigious','Modal_strong','Modal_weak'])
    #creat_csv.to_csv('EmotionData.csv')

    Correct = Prediction(positive_num,negative_num,uncertainty_num,litigious_num,modal_strong_num,modal_weak_num)
    if Correct == 'Down':
        return('預測結果為跌.')
    elif Correct == 'Up':
        return('預測結果為漲.')

#搜尋網頁新聞
def findNewsFromWeb(stockName):
    import requests
    from bs4 import BeautifulSoup

    res = requests.get('https://www.bloomberg.com/quote/' + stockName +':US')
    soup = BeautifulSoup(res.text, "html.parser")

    news = soup.find_all('article','newsItem__5b5cb00f')
    x = 0
    allNews = ''
    for i in news:
        if i.find('a'):
            link = i.find('a')['href']
        if i.find('div'):
            title = i.find('div').text
            date = soup.find_all('div','publishedAt__4009bb4f ')[x].text
        allNews = allNews + (title) + '\n' + (date) + '\n' + str(link) + '\n\n' 
        x += 1
        if x > 5:
            break
    if len(allNews) == 0:
        return('股票代號錯誤！\n請重新輸入.')
    else:
        return(allNews)
#stockName = 'F'
#findNewsFromWeb(stockName) # type=tuple
    

def choiceMessage(message):
    textHello = ['HI','你好','妳好','hello','?']
    textNo = ['NO','不會','不','如何使用']
    textLater = ['OK','好','等我一下']
    if (len(message.message.text)) > 300:                              #文字量>300 判定為文章
        return(getPrediction(message.message.text))
    elif message.message.text.upper() in textHello:
        profile = line_bot_api.get_profile(message.source.user_id)
        return('Hi~ ' + profile.display_name)
    elif message.message.text.upper() in textNo:
        return('你可以丟新聞內容給我，我會幫你預測隔日漲跌。')
    elif message.message.text.upper() in textLater:
        return('摁！')
    elif '$' in message.message.text:                                   #傳送股價網站
        return('http://www.nasdaq.com/symbol/' + message.message.text[1:].lower()  + '/historical')
    elif len(message.message.text) < 5:                                 #從bloomberg找股票新聞
        return(findNewsFromWeb(message.message.text.upper()))
    else:
        return('不會使用嗎？')
    
    
#this part is my code

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text = choiceMessage(event))) #event.message.text


if __name__ == "__main__":
    app.run()
