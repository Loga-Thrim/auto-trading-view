import webbrowser
import pyautogui
import time


url1 = 'https://th.tradingview.com/chart/GW3UscjQ/'
coins = ['BTCTHB', 'ETHTHB','KUBTHB','XRPTHB','LTCTHB','BCHTHB','USDTTHB','BNBTHB','XLMTHB','ADATHB','WANTHB','OMGTHB','ZILTHB','SNTTHB','CVCTHB','LINKTHB','IOSTTHB','ZRXTHB','KNCTHB','ABTTHB', 'MANATHB','SIXTHB','JFINTHB','GFTHB','POWTHB','DOGETHB','DAITHB','USDCTHB','BATTHB','MKRTHB','ENJTHB','BANDTHB','COMPTHB','KSMTHB','DOTTHB','NEARTHB','SCRTTHB','GLMTHB','YFITHB','UNITHB','AAVETHB', 'ALPHATHB', 'OCEANTHB', 'SNXTHB', 'SANDTHB', 'BALTHB', 'CRVTHB','AXSTHB','SUSHITHB','FTTTHB','GALATHB','ILVTHB','ENSTHB','GTTHB','IMXTHB']
chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))

def open_tab(sec, index, sex): #sex 
    webbrowser.get('chrome').open_new_tab(url1)
    time.sleep(sec)
    pyautogui.click(120, 120)
    pyautogui.typewrite(coins[index])
    time.sleep(sex) 
    pyautogui.click(800, 420)
open_tab(6, 0,1) 

for i in range(1, len(coins)-1):
    open_tab(4, i,.2) 