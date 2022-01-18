# coding:utf-8
from flickrapi import FlickrAPI
from urllib.request import urlretrieve
from pprint import pprint
import os,time,sys

#flickerのkeyが入ってるtxtのpath
key_path = "key.txt" 
with open(key_path) as f:
    l = [s.strip() for s in f.readlines()]
key = l[0]
secret = l[1]
wait_time = 1

def my_makedirs(path):
    if not os.path.isdir(path):
        os.makedirs(path)

# コマンドラインの引数の1番目の値を取得。以下の場合は[cat]を取得
# python download.py cat 
sys_num = len(sys.argv)
tag_name = sys.argv[1]
for i in range(2,sys_num,1):
    tag_name = tag_name +","+sys.argv[i]
print(tag_name)
savedir = "./"+tag_name
my_makedirs(savedir)


# format:受け取るデータ(jsonで受け取る）
flickr = FlickrAPI(key, secret, format='parsed-json')

result  = flickr.photos.search(
    #text = animalname,
    per_page = 500,
    media = 'photos',
    sort = 'relevance',
    safe_seach = 1,
    extras = 'url_l, licence, tags, url_q',
    tags = tag_name,
    tag_mode = "all"
)

# 結果
photos = result['photos']
pprint(photos)

for i,photo in enumerate(photos['photo']):
    #url_q = photo['url_q']
    if 'url_l' not in photo:
        pass 
        #url_q = photo['url_q']
    else:
        url_q = photo['url_l']
    filepath = savedir + '/' + photo['id'] + '.jpg'

   # 重複したファイルが存在する場合スキップする。
    if os.path.exists(filepath):continue
   # 画像データをダウンロードする
    urlretrieve(url_q, filepath)
   # サーバーに負荷がかからないよう、1秒待機する
    time.sleep(wait_time)