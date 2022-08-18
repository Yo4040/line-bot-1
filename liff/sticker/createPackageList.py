# -*- coding: utf-8 -*-
import glob
import os
import urllib.request
from bs4 import BeautifulSoup


# 作成されているパッケージのID(int)をList化する

pkgList = []
for f in glob.glob("a/*.html"):
    basename_without_ext = os.path.splitext(f)[0]
    pkgNum = basename_without_ext.replace("a/entrance", "")
    pkgList.append(pkgNum)

print(pkgList)
print("\n現在ページが作成されているパッケージ数: " + str(len(pkgList)) + "\n")


# それぞれのスタンプ情報を取得する
for i in pkgList:

    # urlのHTMLを取得
    pkgUrl = "https://store.line.me/stickershop/product/"+i+"/ja"
    html = urllib.request.urlopen(pkgUrl)

    # htmlをBeautifulSoupでパース
    soup = BeautifulSoup(html, "html.parser")

    # タイトル要素の文字列を取得
    ttl = soup.title.string
    # タイトルの文字列の整形
    ttln = ttl.replace(" - LINE スタンプ | LINE STORE", "")

    p = f'<a href="{pkgUrl}">[{i}] {ttln}</a><br>'
    print(p)
