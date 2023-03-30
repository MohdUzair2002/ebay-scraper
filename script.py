from bs4 import BeautifulSoup
import requests


page = requests.get('https://www.ebay.com/itm/175645816560?epid=8056684409&hash=item28e54e76f0:g:u~QAAOSwdntkC1yR&amdata=enc%3AAQAHAAABoH2FGeJO6Be5oRGDzVEc6Ep%2FhGPMgKq%2B1lyyv7In4XM1wko9O9pvIkuecuMo7IfeQA98txc0WsEWHaPTDU9OXYuX4Tva7mC5awLn9XN6nkSYIvelel5eAazY6btgEnhDQa6any%2FwxaIX9%2FQ6EbcGOXwxc%2FkC7S1%2FDAYtdJLCcCBgRkRz0Ln1bhztlwfsaJ%2FK6oFmlOkYYfpgHxdPG%2FOCqdLLCd%2BMMt2HD273UDBLxsmY%2BlOJdbY0wPPR%2F0o4lMwm8RYW39gqDTN20gQ5ncduFHCExmqpsZaspdOUb5qcdg1%2FzlTPXuTS9%2F%2FC%2BO5wreLQLFXta5CK21%2FXoOflPVJUlvtVqYWw0h1%2BvHTlGQg7uMVudzWLoKXQoCv7MFEaFFoQPgMQvsyupLEaCyxBXEywHHaEnwf%2B9tpGXLV2QpoNs%2FU%2FHiVTy7rh%2Feth%2B6CPR0zLpdLjvbsjBUSxfwmtdkYv30GvZ%2FOs%2FJEaYuq%2FFVpChQLx07RSO5d1elZdbs8zBAjyUJPBAafZ9mRE5zzlQbQWBqFPaprJmte2cjMUPFHwCzHn%7Ctkp%3ABFBMrNal-OVh')

soup = BeautifulSoup(page.text, 'html.parser')
name = soup.find('h1', class_="x-item-title__mainTitle")
price=soup.find('div',class_='x-price-primary')
print(name.text)
print(price.text)
    