# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 12:15:57 2021

@author: quincy408
"""
import time
from bs4 import BeautifulSoup
import requests
import tkinter as tk
from tkinter import ttk
requests.packages.urllib3.disable_warnings()


window = tk.Tk()
window.title('即時匯率爬蟲與推播LineNotify')
window.geometry('450x200')
window.resizable(False,False)

count = 1
url = 'https://www.cathaybk.com.tw/cathaybk/personal/deposit-exchange/rate/currency-billboard/'
def LineNotifyMessage_text(token, msg):
    headers = {
        "Authorization":"Bearer " + token
        }
    payload = {'message':msg}
    requests.post("https://notify-api.line.me/api/notify", headers = headers, params = payload)

def getDATA():
            global count
            localtime = time.localtime()
            SearchTime = time.strftime("%Y-%m-%d %I:%M:%S %p", localtime)
            text.insert("insert","\n檢測次數" + str(count) + " 推播時間為:" + SearchTime)
                
            resp = session.get(url, verify=False)
            soup = BeautifulSoup(resp.content,'html.parser')
            exchange = soup.find(id='layout_0_main_2_firsttab01_1_tab_rate_realtime')
                
            text.insert("insert","\n")
                
            usa = exchange.find_all(attrs={"data-title": "USD","class":"td data_titleR"})
            usaIn = usa[4].renderContents()
            usaOut = usa[5].renderContents()
            usaIn = str(usaIn)
            usaOut = str(usaOut)
            usaIn = usaIn.replace("b'", "")
            usaIn = usaIn.replace("'", "") 
            usaOut = usaOut.replace("b'", "")
            usaOut = usaOut.replace("'", "") 
            text.insert("insert","美金 買進匯率:" + usaIn + " 賣出匯率:" + usaOut)
                
            text.insert("insert","\n")
                
            eur = exchange.find_all(attrs={"data-title": "EUR","class":"td data_titleR"})
            eurIn = eur[4].renderContents()
            eurOut = eur[5].renderContents()
            eurIn = str(eurIn)
            eurOut = str(eurOut)
            eurIn = eurIn.replace("b'", "")
            eurIn = eurIn.replace("'", "") 
            eurOut = eurOut.replace("b'", "")
            eurOut = eurOut.replace("'", "") 
            text.insert("insert","歐元 買進匯率:" + eurIn + " 賣出匯率:" + eurOut)
                
            text.insert("insert","\n")
                
            jpy = exchange.find_all(attrs={"data-title": "JPY","class":"td data_titleR"})
            jpyIn = jpy[4].renderContents()
            jpyOut = jpy[5].renderContents()
            jpyIn = str(jpyIn)
            jpyOut = str(jpyOut)
            jpyIn = jpyIn.replace("b'", "")
            jpyIn = jpyIn.replace("'", "") 
            jpyOut = jpyOut.replace("b'", "")
            jpyOut = jpyOut.replace("'", "") 
            text.insert("insert","日幣 買進匯率:" + jpyIn + " 賣出匯率:" + jpyOut)
                
            text.insert("insert","\n")
                
            cny = exchange.find_all(attrs={"data-title": "CNY","class":"td data_titleR"})
            cnyIn = cny[4].renderContents()
            cnyOut = cny[5].renderContents()
            cnyIn = str(cnyIn)
            cnyOut = str(cnyOut)
            cnyIn = cnyIn.replace("b'", "")
            cnyIn = cnyIn.replace("'", "") 
            cnyOut = cnyOut.replace("b'", "")
            cnyOut = cnyOut.replace("'", "") 
            text.insert("insert","人民幣 買進匯率:" + cnyIn + " 賣出匯率:" + cnyOut)
                
            text.insert("insert","\n")
                
            hkd = exchange.find_all(attrs={"data-title": "HKD","class":"td data_titleR"})
            hkdIn = hkd[4].renderContents()
            hkdOut = hkd[5].renderContents()
            hkdIn = str(hkdIn)
            hkdOut = str(hkdOut)
            hkdIn = hkdIn.replace("b'", "")
            hkdIn = hkdIn.replace("'", "") 
            hkdOut = hkdOut.replace("b'", "")
            hkdOut = hkdOut.replace("'", "") 
            text.insert("insert","港幣 買進匯率:" + hkdIn + " 賣出匯率:" + hkdOut)
                
            text.insert("insert","\n")
                
            msg = "\n▼▼▼▼▼台幣匯率小助手▼▼▼▼▼" + "\n~推播時間:" + SearchTime + "~" + "\
                \n         幣別      銀行買進     銀行賣出" + "\n⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯" + "\
                \n         美金       " + usaIn + "       " + usaOut + "\
                \n         歐元       " + eurIn + "       " + eurOut + "\
                \n         日幣        " + jpyIn + "         " + jpyOut + "\
                \n        人民幣     " + cnyIn + "         " + cnyOut + "\
                \n         港幣        " + hkdIn + "         " + hkdOut
            LineNotifyMessage_text(Token, msg)
            count += 1
            newWindow.after(3600000,getDATA) # 設定時間

def btn_click():
    global Token
    Token = entry.get()
    if Token != "":
        LineNotifyMessage_text(Token, '~匯率小助手測試訊息~')
        MsgBox = tk.messagebox.askyesno("請去Line確認", "已發送測試訊息，請確認您是否有收到")
        if MsgBox == True:
            entry.configure(state='disabled')
            button.configure(state='disabled')
            label.configure(text='Token(目前執行):')
            global session, newWindow, text
            newWindow = tk.Toplevel(window)
            newWindow.geometry('500x800')
            newWindow.resizable(False,False)
            text = tk.Text(newWindow)
            text.pack(side=tk.LEFT, fill=tk.BOTH)
            session = requests.session()
            text.insert("insert","推波紀錄與內容:")
            getDATA
             
def close():            
    window.destroy()


label = ttk.Label(window, text='請輸入LineToken:')
label.pack(side=tk.LEFT,padx=20, pady=10)
InputToken = tk.StringVar() 
entry = ttk.Entry(window, textvariable=InputToken)
entry.pack(side=tk.LEFT)
button = ttk.Button(window, text='確認', command=btn_click)
button.pack(side=tk.LEFT,padx=10)
button2 = ttk.Button(window, text='關閉', command=close, width=5)
button2.pack(side=tk.LEFT, pady=10)

window.mainloop()
