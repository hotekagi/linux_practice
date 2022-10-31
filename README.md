# Linux Practice

MacBook使い（linuxではない人）が，dockerを使って「Linuxのしくみ」を走破する．

## メモ

Dockerfile：作成中
start.sh：これでイメージを作成してコンテナに入る

<br>

#### dockerのイメージを作成
```
docker build -t linux_practice .
```
`-t`あるいは`--tag`はタグでイメージに名前をつける．  
`.`でカレントディレクトリのDockerfileからイメージを作成．  

<br>

#### コンテナを作成して入る
```
docker run -it --rm linux_practice bash
```
`--name`コンテナ名，指定しないと実行のたびにデタラメな名前が勝手に作られる．  
`-i`あるいは`--interactive`こちらのシェルへの標準入力をコンテナに渡すなど．  
`-t`ttyの割り振り．  
`--rm`docker runを終了するとコンテナを削除する．   
`bash`pythonのイメージで作成したのでこれが無いとデフォルトでpythonのインタラクティブシェルに入ってしまう．

<br>

#### version確認

```
go version
python --version
```

<br>

#### コンテナの起動，中に入る，停止，削除

```
docker start linux_practice
docker exec -it linux_practice bash
docker stop linux_practice
docker rm linux_practice
```

<br>

## 参考にした記事

dockerでlinuxを動かす  
https://qiita.com/tifa2chan/items/9379a99c32abbf76916c

golangとpythonを入れる  
https://gangannikki.hatenadiary.jp/entry/2020/09/10/200000

docker run のオプション  
https://qiita.com/zaki-lknr/items/f0ca0a28e5445884f30a

<br>

#### 余談

```                                      
> [3/5] RUN apt-get update && apt-get install strace:
#6 2.202 Get:1 http://deb.debian.org/debian bullseye InRelease [116 kB]
#6 2.335 Get:2 http://deb.debian.org/debian-security bullseye-security InRelease [48.4 kB]
#6 2.369 Get:3 http://deb.debian.org/debian bullseye-updates InRelease [44.1 kB]
#6 2.778 Get:4 http://deb.debian.org/debian bullseye/main amd64 Packages [8184 kB]
#6 4.102 Get:5 http://deb.debian.org/debian-security bullseye-security/main amd64 Packages [193 kB]
#6 4.131 Get:6 http://deb.debian.org/debian bullseye-updates/main amd64 Packages [14.6 kB]
#6 6.042 Fetched 8600 kB in 4s (2169 kB/s)
#6 6.042 Reading package lists...
#6 7.261 Reading package lists...
#6 8.210 Building dependency tree...
#6 8.489 Reading state information...
#6 8.757 The following additional packages will be installed:
#6 8.758   libunwind8
#6 8.853 The following NEW packages will be installed:
#6 8.854   libunwind8 strace
#6 8.867 0 upgraded, 2 newly installed, 0 to remove and 2 not upgraded.
#6 8.867 Need to get 1139 kB of archives.
#6 8.867 After this operation, 2625 kB of additional disk space will be used.
#6 8.867 Do you want to continue? [Y/n] Abort.
------
executor failed running [/bin/sh -c apt-get update && apt-get install strace]: exit code: 1
docker run -it --rm linux_practice bash
root@f7dead05b2f8:/linux_practice# strace --version
bash: strace: command not found
```