# claude-code-practice

これは[MVA 2025 サテライト特別チュートリアル 大学・企業研究所PIのためのAI活用入門](https://sites.google.com/view/mva2025-ai-tutorial/home) のための練習用リポジトリです。

## claude codeのインストール

- GitHubにログインした状態で、Codeボタンをクリックし、Codespacesタブを選択して、Codespaceを作成してください。
- 作成されたCodespaceに接続したら、以下のコマンドを実行して、claude codeをインストールしてください。

```bash
$ npm install -g @anthropic-ai/claude-code
```

## claude codeの起動と初回実行

1. ターミナルから`claude`を実行して、claude codeを起動します
2. Choose the text style that looks best with your terminal -> 適当に設定します
3. Select login method -> 今回は2. Anthropic Console account を選択します
4. Anthropic Consoleが開くのでAuthorizeします。localhostにつながってしまった場合、codespaceのターミナルからもう一度 https://console.anthropic.com/oauth/authorize? ... のリンクを踏んで同様の手続きを実行します
5. Codeが出るのでコピーしてcodespace側でペーストしてください。あとはすべてデフォルトの選択肢を選択していきます

## やってみよう

以下の指示を出してみましょう
- `Check if detect.py works.`
- `Retrieve an image from the web which is suitable for object detection tasks.`
- `Extend detect.py to visualize outputs.`
- `what is uv? explain it in Japanese.`
