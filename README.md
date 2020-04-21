# Python_STL  


Python から、STL を出力するライブラリ。

面を構成する3頂点ずつをまとめた配列を渡せば、stl を出力できます。  

以前ぐちゃぐちゃに作ったものを整理し、アスキーではデータが重くなるので、バイナリ書き出しの機能を追加した。  

何も考えず実装したところ、バイナリ書き込みのほうが10倍以上遅く、怪しかった文字列連結部分を + での結合ではなく、リストに入れて join での結合と修正した。結果は、明らかにパフォーマンスが改善し、バイナリに変換することで書き込み量が減るので速度は2倍くらい速くなった。データサイズは半分から 8分の1 くらいになると思う。  


### Modules  

- python_stl  
  - calc_stl // 法線ベクトルの計算  
  - gen_stl_ascii // アスキー書き出しに必要な文字列処理等  
  - gen_stl_binary // バイナリ書き出しに必要な文字列処理等  
  - transform // ポイントや、ベクトルの計算  
  - util // 現在時刻取得や、テスト用のグリッド等  

モジュールの構成は上の通り。こんなに分ける必要も無いが、これから部分的に使いまわすことを見据えて一応これでいいやという感じ。transform は、Grasshopper に倣い、ポイントやベクトル処理をまとめた（vector でまとめてもいいとも思った）。  


### Ref  

- [Standard Triangulated Language (Wikipedia)](https://ja.wikipedia.org/wiki/Standard_Triangulated_Language)  


- [STLファイルフォーマット](https://www.hiramine.com/programming/3dmodelfileformat/stlfileformat.html)  


- [struct (Python.org)](https://docs.python.org/ja/3/library/struct.html)  


- [pythonの速度で気にするところ(高速化メモ)](http://nobunaga.hatenablog.jp/entry/2018/03/19/081425)  

