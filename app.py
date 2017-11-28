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
    if Modal_Strong < 1.5:
        if Positive < 8.5:
            if Positive < 5.5:
                if Uncertainty < 4.5:
                    if Positive < 1.5:
                        if Uncertainty < 2.5:
                            if Uncertainty < 0.5:
                                if Modal_Strong < 0.5:
                                    if Positive < 0.5:
                                        return('Down')
                                    elif Positive >= 0.5:
                                        return('Up')
                                elif Modal_Strong >= 0.5:
                                    return('Down')
                            elif Uncertainty >= 0.5:
                                if Modal_Strong < 0.5:
                                    if Uncertainty < 1.5:
                                        if Positive < 0.5:
                                            return('Up')
                                        elif Positive >= 0.5:
                                            return('Down')
                                    elif Uncertainty >= 1.5:
                                        if Positive < 0.5:
                                            return('Up')
                                        elif Positive >= 0.5:
                                            return('Down')
                                elif Modal_Strong >= 0.5:
                                    if Positive < 0.5:
                                        return('Down')
                                    elif Positive >= 0.5:
                                        if Uncertainty < 1.5:
                                            return('Down')
                                        elif Uncertainty >= 1.5:
                                            return('Down')
                        elif Uncertainty >= 2.5:
                            return('Up')
                    elif Positive >= 1.5:
                        if Modal_Strong < 0.5:
                            if Uncertainty <1.5:
                                if Positive < 3.5:
                                    return('Down')
                                elif Positive >= 3.5:
                                    if Positive < 4.5:
                                        return('Up')
                                    elif Positive >= 4.5:
                                        if Uncertainty < 0.5:
                                            return('Down')
                                        elif Uncertainty >= 0.5:
                                            return('Down')
                            elif Uncertainty >= 1.5:
                                return('Up')
                        elif Modal_Strong >= 0.5:
                            if Positive < 4.5:
                                if Uncertainty < 1.5:
                                    if Positive < 2.5:
                                        return('Up')
                                    elif Positive >= 2.5:
                                        if Uncertainty < 0.5:
                                            return('Down')
                                        elif Uncertainty >= 0.5:
                                            if Positive < 3.5:
                                                return('Up')
                                            elif Positive >= 3.5:
                                                return('Up')
                                elif Uncertainty >= 1.5:
                                    if Uncertainty < 3.5:
                                        if Positive < 2.5:
                                            if Uncertainty < 2.5:
                                                return('Down')
                                            elif Uncertainty >= 2.5:
                                                return('Down')
                                        elif Positive >= 2.5:
                                            if Uncertainty < 2.5:
                                                return('Down')
                                            elif Uncertainty >= 2.5:
                                                if Positive < 3.5:
                                                    return('Up')
                                                elif Positive >= 3.5:
                                                    return('Up')
                                    elif Uncertainty >= 3.5:
                                        return('Down')
                            elif Positive >= 4.5:
                                if Uncertainty < 1.5:
                                    return('Down')
                                elif Uncertainty >= 1.5:
                                    return('Up')
                elif Uncertainty >= 4.5:
                    return('Down')
            elif Positive >= 5.5:
                if Positive < 7.5:
                    if Uncertainty < 7.5:
                        if Uncertainty < 2.5:
                            if Modal_Strong < 0.5:
                                return('Up')
                            elif Modal_Strong >= 0.5:
                                if Positive < 6.5:
                                    if Uncertainty < 0.5:
                                        return('Up')
                                    elif Uncertainty >= 0.5:
                                        if Uncertainty < 1.5:
                                            return('Down')
                                        elif Uncertainty >= 1.5:
                                            return('Down')
                                elif Positive >= 6.5:
                                    return('Down')
                        elif Uncertainty >= 2.5:
                            return('Up')
                    elif Uncertainty >= 7.5:
                        return('Down')
                elif Positive >= 7.5:
                    if Uncertainty < 1.5:
                        return('Down')
                    elif Uncertainty >= 1.5:
                        return('Down')
        elif Positive >= 8.5:
            if Positive < 11.5:
                return('Up')
            elif Positive >= 11.5:
                return('Down')
    elif Modal_Strong >= 1.5:
        if Positive < 11.5:
            if Modal_Strong < 3.5:
                if Positive < 0.5:
                    return('Up')
                elif Positive >= 0.5:
                    if Positive < 2.5:
                        if Modal_Strong < 2.5:
                            if Uncertainty < 1.5:
                                return('Up')
                            elif Uncertainty >= 1.5:
                                if Positive < 1.5:
                                    if Uncertainty < 4.5:
                                        if Uncertainty < 3.5:
                                            if Uncertainty < 2.5:
                                                return('Up')
                                            elif Uncertainty >= 2.5:
                                                return('Up')
                                        elif Uncertainty >= 3.5:
                                            return('Down')
                                    elif Uncertainty >= 4.5:
                                        retunr('Up')
                                elif Positive >= 1.5:
                                    if Uncertainty < 2.5:
                                        return('Down')
                                    elif Uncertainty >= 2.5:
                                        return('Up')
                        elif Modal_Strong >= 2.5:
                            if Uncertainty < 3.5:
                                return('Down')
                            elif Uncertainty >= 3.5:
                                return('Down')
                    elif Positive >= 2.5:
                        if Uncertainty < 0.5:
                            if Positive < 6.5:
                                return('Down')
                            elif Positive >= 6.5:
                                if Positive < 9:
                                    return('Up')
                                elif Positive >= 9:
                                    return('Down')
                        elif Uncertainty >= 0.5:
                            if Positive < 10.5:
                                if Uncertainty < 5.5:
                                    if Uncertainty < 1.5:
                                        if Positive < 5:
                                            return('Up')
                                        elif Positive >= 5:
                                            if Positive < 9:
                                                if Positive < 7:
                                                    return('Down')
                                                elif Positive >= 7:
                                                    return('Down')
                                            elif Positive >= 9:
                                                return('Up')
                                    elif Uncertainty >= 1.5:
                                        if Positive < 7.5:
                                            if Modal_Strong < 2.5:
                                                if Positive < 5.5:
                                                    if Positive < 3.5:
                                                        if Uncertainty < 2.5:
                                                            return('Up')
                                                        elif Uncertainty >= 2.5:
                                                            if Uncertainty < 4.5:
                                                                if Uncertainty < 3.5:
                                                                    return('Down')
                                                                elif Uncertainty >= 3.5:
                                                                    return('Down')
                                                            elif Uncertainty >= 4.5:
                                                                return('Down')
                                                    elif Positive >= 3.5:
                                                        if Positive < 4.5:
                                                            if Uncertainty < 3.5:
                                                                return('Down')
                                                            elif Uncertainty >= 3.5:
                                                                return('Up')
                                                        elif Positive >= 4.5:
                                                            if Uncertainty < 3.5:
                                                                if Uncertainty < 2.5:
                                                                    return('Down')
                                                                elif Uncertainty >= 2.5:
                                                                    return('Down')
                                                            elif Uncertainty >= 3.5:
                                                                if Uncertainty < 4.5:
                                                                    return('Up')
                                                                elif Uncertainty >= 4.5:
                                                                    return('Up')
                                                elif Positive >= 5.5:
                                                    if Uncertainty < 4.5:
                                                        if Uncertainty < 2.5:
                                                            return('Down')
                                                        elif Uncertainty >= 2.5:
                                                            if Uncertainty < 3.5:
                                                                if Positive < 6.5:
                                                                    return('Up')
                                                                elif Positive >= 6.5:
                                                                    return('Down')
                                                            elif Uncertainty >= 3.5:
                                                                return('Down')
                                                    elif Uncertainty >= 4.5:
                                                        return('Down')
                                            elif Modal_Strong >= 2.5:
                                                if Positive < 5.5:
                                                    if Positive < 4:
                                                        if Uncertainty < 4.5:
                                                            if Uncertainty < 3.5:
                                                                if Uncertainty < 2.5:
                                                                    return('Down')
                                                                elif Uncertainty >= 2.5:
                                                                    return('Up')
                                                            elif Uncertainty >= 3.5:
                                                                return('Down')
                                                        elif Uncertainty >= 4.5:
                                                            return('Up')
                                                    elif Positive >= 4:
                                                        if Uncertainty < 3.5:
                                                            if Uncertainty < 2.5:
                                                                return('Down')
                                                            elif Uncertainty >= 2.5:
                                                                return('Up')
                                                        elif Uncertainty >= 3.5:
                                                            if Uncertainty < 4.5:
                                                                return('Down')
                                                            elif Uncertainty >= 4.5:
                                                                return('Down')
                                                elif Positive >= 5.5:
                                                    return('Up')
                                        elif Positive >= 7.5:
                                            if Modal_Strong < 2.5:
                                                return('Down')
                                            elif Modal_Strong >= 2.5:
                                                if Uncertainty < 2.5:
                                                    return('Down')
                                                elif Uncertainty >= 2.5:
                                                    if Positive < 9.5:
                                                        if Uncertainty < 4.5:
                                                            if Uncertainty < 3.5:
                                                                if Positive < 8.5:
                                                                    return('Down')
                                                                elif Positive >= 8.5:
                                                                    return('Up')
                                                            elif Uncertainty >= 3.5:
                                                                if Positive < 8.5:
                                                                    return('Down')
                                                                elif Positive >= 8.5:
                                                                    return('Down')
                                                        elif Uncertainty >= 4.5:
                                                            return('Down')
                                                    elif Positive >= 9.5:
                                                        return('Up')
                                elif Uncertainty >= 5.5:
                                    if Positive < 6.5:
                                        if Uncertainty < 7.5:
                                            if Positive < 5.5:
                                                return('Up')
                                            elif Positive >= 5.5:
                                                if Modal_Strong < 2.5:
                                                    return('Down')
                                                elif Modal_Strong >= 2.5:
                                                    return('Up')
                                        elif Uncertainty >= 7.5:
                                            if Positive < 5.5:
                                                if Uncertainty < 8.5:
                                                    return('Up')
                                                elif Uncertainty >= 8.5:
                                                    if Uncertainty < 9.5:
                                                        return('Down')
                                                    elif Uncertainty >= 9.5:
                                                        if Positive < 3.5:
                                                            if Uncertainty < 10.5:
                                                                return('Up')
                                                            elif Uncertainty >= 10.5:
                                                                return('Down')
                                                        elif Positive >= 3.5:
                                                            return('Down')
                                            elif Positive >= 5.5:
                                                return('Down')
                                    elif Positive >= 6.5:
                                        if Uncertainty < 12.5:
                                            return('Up')
                                        elif Uncertainty.txt >= 12.5:
                                            return('Down')
                            elif Positve >= 10.5:
                                return('Up')
            elif Modal_Strong >= 3.5:
                if Uncertainty < 3.5:
                    if Positive < 5.5:
                        if Uncertainty < 2:
                            return('Up')
                        elif Uncertainty >=2:
                            if Positive < 4.5:
                                return('Down')
                            elif Positive >= 4.5:
                                return('Up')
                    elif Positive >= 5.5:
                        return('Down')
                elif Uncertainty >= 3.5:
                    if Modal_Strong < 7.5:
                        if Positive < 4.5:
                            if Modal_Strong < 5.5:
                                if Uncertainty < 4.5:
                                    if Modal_Strong < 4.5:
                                        if Positive < 3:
                                            return('Up')
                                        elif Positive >= 3:
                                            return('Up')
                                    elif Modal_Strong >= 4.5:
                                        return('Down')
                                elif Uncertainty >= 4.5:
                                    if Uncertainty < 6.5:
                                        if Positive < 3.5:
                                            if Uncertainty < 5.5:
                                                return('Up')
                                            elif Uncertainty >= 5.5:
                                                return('Down')
                                        elif Positive >= 3.5:
                                            if Uncertainty < 5.5:
                                                return('Down')
                                            elif Uncertainty >= 5.5:
                                                return('Up')
                                    elif Uncertainty >= 6.5:
                                        return('Down')
                            elif Modal_Strong >= 5.5:
                                return('Down')
                        elif Positive >= 4.5:
                            if Uncertainty < 11.5:
                                if Positive < 9.5:
                                    if Modal_Strong < 5.5:
                                        if Positive < 6.5:
                                            if Uncertainty < 5.5:
                                                if Modal_Strong < 4.5:
                                                    if Uncertainty < 4.5:
                                                        return('Up')
                                                    elif Uncertainty >= 4.5:
                                                        return('Up')
                                                elif Modal_Strong >= 4.5:
                                                    if Uncertainty < 4.5:
                                                        return('Down')
                                                    elif Uncertainty >= 4.5:
                                                        return('Down')
                                            elif Uncertainty >= 5.5:
                                                if Uncertainty < 8.5:
                                                    return('Up')
                                                elif Uncertainty >= 8.5:
                                                    if Positive < 5.5:
                                                        return('Down')
                                                    elif Positive >= 5.5:
                                                        return('Up')
                                        elif Positive >= 6.5:
                                            if Modal_Strong < 4.5:
                                                if Uncertainty < 7:
                                                    if Uncertainty < 4.5:
                                                        if Positive < 7.5:
                                                            return('Up')
                                                        elif Positive >= 7.5:
                                                            if Positive < 8.5:
                                                                return('Down')
                                                            elif Positive >= 8.5:
                                                                return('Up')
                                                    elif Uncertainty >= 4.5:
                                                        return('Up')
                                                elif Uncertainty >= 7:
                                                    return('Down')
                                            elif Modal_Strong >= 4.5:
                                                if Uncertainty < 10:
                                                    if Uncertainty < 5.5:
                                                        if Positive < 7.5:
                                                            return('Down')
                                                        elif Positive >= 7.5:
                                                            return('Up')
                                                    elif Uncertainty >= 5.5:
                                                        return('Down')
                                                elif Uncertainty >= 10:
                                                    return('Up')
                                    elif Modal_Strong >= 5.5:
                                        if Uncertainty < 5.5:
                                            return('Donw')
                                        elif Uncertainty >= 5.5:
                                            if Uncertainty < 10:
                                                if Positive < 6.5:
                                                    return('Down')
                                                elif Positive >= 6.5:
                                                    return('Up')
                                            elif Uncertainty >= 10:
                                                return('Down')
                                elif Positive >= 9.5:
                                    if Positive < 10.5:
                                        return('Down')
                                    elif Positive >= 10.5:
                                        if Uncertainty < 8.5:
                                            if Uncertainty < 5.5:
                                                return('Up')
                                            elif Uncertainty >= 5.5:
                                                if Modal_Strong < 5.5:
                                                    if Uncertainty < 7.5:
                                                        return('Down')
                                                    elif Uncertainty >= 7.5:
                                                        return('Up')
                                                elif Modal_Strong >= 5.5:
                                                    return('Down')
                                        elif Uncertainty > 8.5:
                                            return('Up')
                            elif Uncertainty >= 11.5:
                                return('Up')
                    elif Modal_Strong >= 7.5:
                        if Uncertainty < 6.5:
                            if Positive < 9.5:
                                return('Up')
                            elif Positive >= 9.5:
                                return('Down')
                        elif Uncertainty >= 6.5:
                            return('Down')
        elif Positive >= 11.5:
            if Uncertainty < 3.5:
                if Uncertainty < 1.5:
                    return('Up')
                elif Uncertainty >= 1.5:
                    return('Down')
            elif Uncertainty >= 3.5:
                if Uncertainty < 9.5:
                    if Modal_Strong < 6.5:
                        if Positive < 14.5:
                            if Uncertainty < 8.5:
                                if Modal_Strong < 5.5:
                                    return('Up')
                                elif Modal_Strong >= 5.5:
                                    return('Down')
                            elif Uncertainty >= 8.5:
                                return('Down')
                        elif Positive >= 14.5:
                            if Positive < 16.5:
                                if Modal_Strong < 4.5:
                                    return('Down')
                                elif Modal_Strong >= 4.5:
                                    if Uncertainty < 6:
                                        return('Up')
                                    elif Uncertainty >= 6:
                                        return('Down')
                            elif Positive >= 16.5:
                                return('Up')
                    elif Modal_Strong >= 6.5:
                        return('Up')
                elif Uncertainty >= 9.5:
                    return('Up')

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
    allNews = "yes"
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
    if (len(message.message.text)) > 300:
        return(getPrediction(message.message.text))
    elif message.message.text.upper() in textHello:
        profile = line_bot_api.get_profile(message.source.user_id)
        return('Hi~ ' + profile.display_name)
    elif message.message.text.upper() in textNo:
        return('你可以丟新聞內容給我，我會幫你預測隔日漲跌。')
    elif message.message.text.upper() in textLater:
        return('摁！')
    elif len(message.message.text) < 5: #從bloomberg找股票新聞
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
