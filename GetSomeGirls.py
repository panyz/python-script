#%%
import requests, bs4, os

url = 'https://gank.io/special/Girl'
os.makedirs('Girls',exist_ok=True)
print('开始！'.ljust(20, '-'))
print('抓取网页 %s...' % url)
res = requests.get(url)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, 'html.parser')
elems = soup.select('.media-content')
for elem in elems:
    style = elem.get('style')
    txt = style[style.find('(') + 2:style.find(')') - 1]
    imageUrl = txt
    if not txt.startswith('https://gank.io'):
        imageUrl = 'https://gank.io' + txt
    print('下载妹子图 %s...' % imageUrl)
    image_res = requests.get(imageUrl)
    image_res.raise_for_status()
    image_file = open(os.path.join('Girls',os.path.basename(imageUrl)+'.png'),'wb')
    for chunk in image_res.iter_content(100000):
        image_file.write(chunk)
    image_file.close()


print('完成！'.rjust(20, '-'))



# %%
