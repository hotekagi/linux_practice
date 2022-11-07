# Linux Practice

MacBook使い（linuxではない人）が，dockerを使って「Linuxのしくみ」を走破する．

## 注意

`./src/ch*/**`の内容については「Linuxのしくみ」の内容あるいはそれを一部改変したもので，あくまでも個人的な動作確認用である．また元のコードは以下で公開されている．

https://github.com/satoru-takeuchi/linux-in-practice-2nd

## メモ
#### イメージを作成してコンテナを起動，bashで入る
```
./run_tmp_container.sh
```
pythonの環境構築がめんどくさそうなのでイメージで，golangはインストールしてくる．
各章で使うコマンドも`apt-get`で入れていく．
docker buildでキャッシュを効かせるために，
変更の多いコマンドは分けて下の方に書くといいらしい．

戦略としては，
1. python3.11を取ってくる(なんとなく新しいやつにしたいから)
2. goの環境構築
3. matplotlibを入れる(pythonのpackageはそれほど頻繁には増やさない読み)
4. apt-getいろいろ取ってくる
5. ファイルをコピー

3章でnumpy, matplotlib, PILが必要になる．
コンテナ内かDockerfileで`pip install matplotlib`すればよい(numpyとPillowは依存パッケージなので付いてくる)

matplotlibをimportしようとして気付いたが，本の通り`#!/usr/bin/python3`とshebangを書いているとpython3.9が呼ばれてしまうので，`#!/usr/local/bin/python3`とする必要がある．
また，日本語フォントを入れないとmatplotlibが文字化けする．

追記：/usr/bin/python3をpython3.11に書き換えればいいのでは？と思ったので書き換えた．

#### コンテナのsrc内をコピーして取り出す
```
./exported_from_src.sh
```

VSCodeのDev Containersを使ってコンテナ内のファイルを直接編集する

#### dockerのイメージを作成
```
docker build -t linux_practice .
```
`-t`あるいは`--tag`はタグでイメージに名前をつける．  
`.`でカレントディレクトリのDockerfileからイメージを作成．

#### コンテナを作成して入る
```
docker run -it --rm linux_practice bash
```
`--name`コンテナ名，指定しないと実行のたびにデタラメな名前が勝手に作られる．  
`-i`あるいは`--interactive`こちらのシェルへの標準入力をコンテナに渡すなど．  
`-t`ttyの割り振り．  
`--rm`docker runを終了するとコンテナを削除する．   
`bash`pythonのイメージで作成したのでこれが無いとデフォルトでpythonのインタラクティブシェルに入ってしまう．

#### version確認
```
go version
python --version
```

#### コンテナの起動，中に入る，停止，削除
```
docker start linux_practice
docker exec -it linux_practice bash
docker stop linux_practice
docker rm linux_practice
```

## 参考にした記事

dockerでlinuxを動かす  
https://qiita.com/tifa2chan/items/9379a99c32abbf76916c

golangとpythonを入れる  
https://gangannikki.hatenadiary.jp/entry/2020/09/10/200000

docker run のオプション  
https://qiita.com/zaki-lknr/items/f0ca0a28e5445884f30a

sarの有効化  
https://qiita.com/toshichan18/items/4c6a0ca02466f2e8f32a

psコマンド(概要)  
https://qiita.com/aya_akatsuki/items/7efc81ef9f2b1ec11c58

psコマンド(詳しい)  
https://eng-entrance.com/linux-command-ps

manコマンドを入れる  
http://dqn.sakusakutto.jp/2013/03/ubuntu_man_systemcall.html

CPU情報が知りたくなったとき  
https://qiita.com/yoshi389111/items/a9026769a6c6a8786c90

pythonのバージョン切り替え 
https://qiita.com/piyo_parfait/items/5abbe4bee2495a62acdc
