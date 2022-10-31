# Linux Practice

MacBook使い（linuxではない人）が，dockerを使って「Linuxのしくみ」を走破する．

## メモ
#### イメージを作成してコンテナを起動，bashで入る
```
./run.sh
```

#### コンテナのsrc内をコピーして取り出す
```
./exported.sh
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
