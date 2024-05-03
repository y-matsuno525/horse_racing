競馬に関するWebアプリを作っています。搭載させたい機能は以下の通りです。
<br>
①一週間以内に開催される重賞レースへの投票（完成）
<br>
②アプリ内通貨での馬券の購入
<br>
③AIによる予想
<br>
④予想成績のランキング
<br>
フロー
<br>
①2023年の重賞レースに出走した馬の血統データをスクレイピング
<br>
②血統を評価する。（はじめは血の活性化論の実装。ほかの理論もいくつか実装したい。）
<br>
③各ユーザーにスクレイピングした馬を一頭ずつ割り当て、マッチングアプリ風の機能を作る。
<br>
マッチングアプリのデータベース構造
<br>
User(djangoの標準User機能とOneToOneで関連付け、血統データを保管））
<br>
Match(ユーザー間のマッチング情報。要素はUser1,User2,User1とUser2のマッチングステータス（like,dislike,matchなど)。Userと多対多の関係を外部キーで表現。)
<br>

