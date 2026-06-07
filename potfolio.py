import requests as r
from bs4 import BeautifulSoup
from dataclasses import dataclass

@dataclass
class Stock:
    ticker: str
    exchange: str
    price: float=0
    currency: str="USD"
    usd_price: float=0
    def __post_init__(self):
        price_info=get_price_information(self.ticker,self.exchange)
        if price_info['ticker']==self.ticker:
            self.price=price_info["price"]
            self.currency=price_info["currency"]
            self.usd_price=price_info["usd_price"]

@dataclass
class Position:
    stock:Stock
    quantity: int

@dataclass
class Portfolio:
    positions:list[Position]


    def get_total_value(self):
        total_value = 0
        for position in self.positions:
            total_value+=position.quantity*position.stock.usd_price
        return round(total_value,2)

def get_price_information(ticker,exchange):
    url=f"https://www.google.com/finance/quote/{ticker}:{exchange}"
    resp=r.get(url)
    soup=BeautifulSoup(resp.content,"html.parser")
    price_div=soup.find("div",attrs={"data-last-price":True})
    price=float(price_div["data-last-price"])
    currency=price_div["data-currency-code"]
    usd_price=price
    if currency!="USD":
        usd_price=round(price*1.5,2)

    return {
        "ticker":ticker,
        "exchange":exchange,
        "price":price,
        "currency":currency,
        "usd_price":usd_price

    }

if __name__=="__main__":
   #print( get_price_information("MSFT","NASDAQ"))
   #print(Stock("MSFT","NASDAQ"))
   microsoft=Stock("MSFT","NASDAQ")
   google = Stock("GOOGL", "NASDAQ")
   shoppy = Stock("SHOP", "TSE")
   portfolio=Portfolio([Position(microsoft,2),Position(google,5),Position(shoppy,10)])
   print(portfolio.get_total_value())





