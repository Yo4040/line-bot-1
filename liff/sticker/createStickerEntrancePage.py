stk = "noanim"    # [str] stickerType (anim or noanim)
sid = 249937366    # [int] number of first stickerId
pkgid = 9606233    # [int] number of packageId
stickerCount = 40    # [int] number of stickers
pc = int(stickerCount/4)
pkg = str(pkgid)
f = open(f'entrance{pkg}.html', "w")

txt1 = '''<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>東京卍リベンジャーズ</title>
</head>
<body>
    <table>
'''
f.write(txt1)

for i in range(pc):
    if stk == "noanim":
        q1 = '        <tr class="stk-img">\n'
        q2 = ''
        for j in range(4):
            num = str(sid + j+4*i)
            link = f'            <td><a href="line://app/1656316634-09bXLKaV?type=stk&stk=noanim&sid={num}&pkg={pkg}"><img src="https://stickershop.line-scdn.net/stickershop/v1/sticker/{num}/iPhone/sticker@2x.png"></a></td>\n'
            q2 = q2+link
        q3 = '        </tr>\n'
        p2 = [q1, q2, q3]
        f.writelines(p2)
    if stk == "anim":
        q1 = '        <tr class="stk-img">\n'
        for j in range(4):
            num = str(sid + j+4*i)
            link = f'            <td><a href="line://app/1656316634-09bXLKaV?type=stk&stk=noanim&sid={num}&pkg={pkg}"><img src="https://stickershop.line-scdn.net/stickershop/v1/sticker/{num}/iPhone/sticker_animation@2x.png"></a></td>\n'
            q2 = q2+link
        q3 = '        </tr>\n'
        p2 = [q1, q2, q3]
        f.writelines(p2)

p3 = '''    </table>
    <style>
        .stk-img{
            display: flex;
            flex-wrap:wrap;
        }
        .stk-img td {
            width: calc(100%/4);/*←画像を横に4つ並べる場合*/
            /*padding:0 5px;←画像の左右に5pxの余白を入れる場合*/
            box-sizing:border-box;
        }
        .stk-img td img {
            max-width:100%; /*画像のはみだしを防ぐ*/
            height: auto; /*画像の縦横比を維持 */
            /*border:sotdd 1px #ccc; ←画像を1pxのグレーの枠線で囲む指定の場合*/
        }
    </style>
</body>
</html>
'''
f.write(p3)
f.close