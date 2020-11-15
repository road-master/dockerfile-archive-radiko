<!-- markdownlint-disable first-line-h1 -->
[![docker build automated?](https://img.shields.io/docker/cloud/automated/mstmelody/archive-radiko.svg)](https://hub.docker.com/r/mstmelody/archive-radiko/builds)
[![docker build passing?](https://img.shields.io/docker/cloud/build/mstmelody/archive-radiko.svg)](https://hub.docker.com/r/mstmelody/archive-radiko/builds)
[![image size and number of layers](https://images.microbadger.com/badges/image/mstmelody/archive-radiko.svg)](https://hub.docker.com/r/mstmelody/archive-radiko/dockerfile)

# クイックリファレンス

- **参考資料**:

  [radikoを録音するpythonスクリプトを先人たちのコードを読みながら作ってわかったこと - Qiita](https://qiita.com/1021ky@github/items/0fc49fec62c6ab213e32)
  [radikomemo - foltia - Trac](http://www.dcc-jpl.com/foltia/wiki/radikomemo)

<!-- markdownlint-disable no-trailing-punctuation -->
# Archive radiko とは?
<!-- markdownlint-enable no-trailing-punctuation -->

radiko のコンテンツを個人用にアーカイブします。

# このイメージの使い方

次のコマンドで現在のフォルダーにアーカイブできます:

```console
docker run --rm --volume $(pwd):/workspace/output --env RADIKO_AREA_ID=<エリアID> mstmelody/archive-radiko <放送局ID> <放送開始時刻> <放送終了時刻> <アーカイブファイル名に付加する文字列>
```

例:

```console
docker run --rm --volume $(pwd):/workspace/output --env RADIKO_AREA_ID=JP4 mstmelody/archive-radiko FMT 20201102193000 20201102215500 "NEWS NEWS"
```

ただし、Ctrl + C でコンテナーを途中で停止するとアーカイブ中のファイルは再生できません

そこで、次のように、まずコンテナーにターミナルを接続し、対話的に操作できるようにします:

```console
docker run -it --rm --volume $(pwd):/workspace/output --env RADIKO_AREA_ID=<エリアID> --entrypoint=sh mstmelody/archive-radiko
```

そして、次のようにアーカイブを実行します:

```console
python3 archive.py <放送局ID> <放送開始時刻> <放送終了時刻> <アーカイブファイル名に付加する文字列>
```

例:

```console
docker run -it --rm --volume $(pwd):/workspace/output --env RADIKO_AREA_ID=JP4 --entrypoint=bash mstmelody/archive-radiko
```

```console
python3 archive.py FMT 20201102193000 20201102215500 "NEWS NEWS"
```

この場合は、アーカイブ処理を `q` キーで停止することができ、アーカイブ中のファイルはその時点までの内容が再生できます。

## ... via docker-compose

次のような Compose ファイルを作っておくと便利でしょう:

```yaml
version: "3.8"
services:
  archive-radiko:
    entrypoint: bash
    environment:
      RADIKO_AREA_ID: <放送局ID>
    image: mstmelody/archive-radiko
    tty: yes
    volumes:
      - ./output:/workspace/output
```

例:

```yaml
version: "3.8"
services:
  archive-radiko:
    entrypoint: bash
    environment:
      RADIKO_AREA_ID: JP4
    image: mstmelody/archive-radiko
    tty: yes
    volumes:
      - ./output:/workspace/output
```

次のコマンドでコンテナーにターミナルを接続し、対話的に操作できるようになります:

```console
docker-compose run --rm archive-radiko
```

## 環境変数

### ```RADIKO_AREA_ID```

聴取地域を示します。自分の聴取地域を指定する必要があります。  
設定しない場合、`JP13` として処理を実行します。

エリアID|聴取地域
--|--
JP1|HOKKAIDO JAPAN
JP2|AOMORI JAPAN
JP3|IWATE JAPAN
JP4|MIYAGI JAPAN
JP5|AKITA JAPAN
JP6|YAMAGATA JAPAN
JP7|FUKUSHIMA JAPAN
JP8|IBARAKI JAPAN
JP9|TOCHIGI JAPAN
JP10|GUNMA JAPAN
JP11|SAITAMA JAPAN
JP12|CHIBA JAPAN
JP13|TOKYO JAPAN
JP14|KANAGAWA JAPAN
JP15|NIIGATA JAPAN
JP16|TOYAMA JAPAN
JP17|ISHIKAWA JAPAN
JP18|FUKUI JAPAN
JP19|YAMANASHI JAPAN
JP20|NAGANO JAPAN
JP21|GIFU JAPAN
JP22|SHIZUOKA JAPAN
JP23|AICHI JAPAN
JP24|MIE JAPAN
JP25|SHIGA JAPAN
JP26|KYOTO JAPAN
JP27|OSAKA JAPAN
JP28|HYOGO JAPAN
JP29|NARA JAPAN
JP30|WAKAYAMA JAPAN
JP31|TOTTORI JAPAN
JP32|SHIMANE JAPAN
JP33|OKAYAMA JAPAN
JP34|HIROSHIMA JAPAN
JP35|YAMAGUCHI JAPAN
JP36|TOKUSHIMA JAPAN
JP37|KAGAWA JAPAN
JP38|EHIME JAPAN
JP39|KOUCHI JAPAN
JP40|FUKUOKA JAPAN
JP41|SAGA JAPAN
JP42|NAGASAKI JAPAN
JP43|KUMAMOTO JAPAN
JP44|OHITA JAPAN
JP45|MIYAZAKI JAPAN
JP46|KAGOSHIMA JAPAN
JP47|OKINAWA JAPAN

参考:

- [radikomemo - foltia - Trac](http://www.dcc-jpl.com/foltia/wiki/radikomemo)
- [ISO 3166-2:JP - Wikipedia](https://ja.wikipedia.org/wiki/ISO_3166-2:JP)

# License

View license information for the software contained in this image.

As with all Docker images, these likely also contain other software which may be under other licenses (such as Bash, etc from the base distribution, along with any direct or indirect dependencies of the primary software being contained).

As for any pre-built image usage, it is the image user's responsibility to ensure that any use of this image complies with any relevant licenses for all software contained within.
