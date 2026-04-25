# 64. The server inspector

**URL:** https://anthropic.skilljar.com/claude-with-the-anthropic-api/287781
**Section:** 09 Model Context Protocol

---

## 📄 Page Content

Anthropic Academy
    
  

  
    
      Courses
    
  

    

    
      
      

      
        
          My Profile
        
        
      

      
      

      
        Sign Out
      
    
  

  

  

    
    
    
        
            
    
        
    

            
    
        
        
            
                
                    
                        
                            
                                
                            

                            
                                details
                            

                            
                        
                    
                
            
            
                
                
                
                    The server inspector
                    
                
                
                    
                        
                            
                                
                                    

    
    

    
    
        
            
        
        
            
                
                This video is still being processed. Please check back later and refresh the page.
            
        
        
            
                Uh oh! Something went wrong, please try again.
            
        
    

    

                                
                            
                        
                    
                
            
        
        
            

    
        
            
                
                    
                        
                            
                        
                    
                
            
            
                
                    Summary
                

                

            
        

        
            
                
                    
                        
                            Summary

                            
                                When building MCP servers, you need a way to test your functionality without connecting to a full application. The Python MCP SDK includes a built-in browser-based inspector that lets you debug and test your server in real-time.

Starting the Inspector

First, make sure your Python environment is activated (check your project's README for the exact command). Then run the inspector with:

mcp dev mcp_server.py

This starts a development server on port 6277 and gives you a local URL to open in your browser. The inspector interface will load, showing the MCP Inspector dashboard.

Important Note About the Interface

The MCP inspector is actively being developed, so the interface you see might look different from current screenshots. However, the core functionality for testing tools, resources, and prompts should remain similar.

Connecting and Testing Tools

Click the "Connect" button on the left side to start your MCP server. Once connected, you'll see a navigation bar with sections for Resources, Prompts, Tools, and other features.

To test your tools:

Navigate to the Tools section
Click "List Tools" to see all available tools
Select a tool to open its testing interface
Fill in the required parameters
Click "Run Tool" to execute and see results

Testing Document Operations

For example, to test a document reading tool, you'd enter a document ID (like "deposition.md") and run the tool. The inspector shows the result, including any returned content or success messages.

You can chain operations to verify functionality. For instance, after editing a document by replacing text, you can immediately run the read tool again to confirm the changes were applied correctly.

Development Workflow

The inspector creates an efficient development loop:

Make changes to your MCP server code
Test individual tools through the inspector
Verify results without needing a full application setup
Debug issues in isolation

This tool becomes essential as you build more complex MCP servers. It eliminates the need to wire up your server to Claude or another application just to test basic functionality, making development much faster and more focused.

---

## 🎬 Transcript (English)

We have put together some functionality inside of our MCP server, but we have no idea if it works, so it'd be really great if we could test this out somehow. It turns out that by using this Python SDK, we automatically get access to an in-browser debugger, so we can make sure that this server is working as expected. Let me show you how to use it really quickly. Back inside my terminal, I went to make sure that I have my Python environment activated. Remember, the ReadMe document goes into detail on the exact command to run to make sure that you have activated that environment. Once you are sure that it is activated, we'll run MCP, Dev, and then the name of the file that contains our server. In this case, it is MCPServer.py. Once I run that, I'll then be told that I have a server listening on port 6277, and I'll be given a direct address to actually access it. I'm going to open up that address inside my browser. And once you go there, you'll see something that looks like this. This is the MCP Inspector. Now right away, there's something important I want you to understand here. This inspector is in active development. So by the time you are watching this video, what you see on the screen right now might be very, very different than what I am showing. Nonetheless, it's probably still going to have some very similar functionality. On the left-hand side, you'll see a Connect button. That is going to start up your MCP server, so that file that we just edited. I'm going to click on Connect, and then right away, we'll see a couple of different things on the screen appear. I first want you to notice the top menu bar up here. It lists out resources, prompts, tools, and some other stuff. Again, the UI might change by the time you watch this video, so if you do not see this menu bar up here, all we are really looking for here is some Tools section. Once I click on Tools, I will click on List Tools, and I'll see the name of the tools that we just put together. If I click on one, the right-hand panel is then going to change. And I can use this panel over here to manually invoke one of my tools to make sure that it is working as expected. So this is how we can do some live development on our MCP server without actually having to wire it up to a real application. In order to use the Read.Contents tool, all we have to do is put in a document ID. If I go back over to my editor and go up to the docs dictionary right here, I can copy one of these document IDs so I will take out deposition.md. I will put it in as the doc ID and then click on run tool. I should then see run tool of success with the contents of the document. And that is it right there. I can verify it. So same exact string is what I see right there. We can use this same exact technique to test out the other tool as well. So I will change over to the edit document tool. Now I'll put in my document ID. My old string that I want to replace, how about replace the word deposition? Actually, I have an easier word to type out. How about just this? That'll be a little bit easier. So my old string is this. Remember, that is going to be case sensitive, and I'm going to replace it with a report. And if I run the tool, I'll then be given a success. Remember, that tool does not actually return the document's contents. It just edits the document. So now to verify that the edit was done correctly, I can go back over to the Read.Contents tool, run that one again with the same document ID, and I should see a report deposition, and then blah, blah, blah. All right, so as you can see, this MCP inspector allows us to very easily debug an MCP server that we are implementing without actually having to wire the server up to an actual application. As you start building your own MCP servers, I expect you'll be using this inspector tool quite a bit. And we'll probably use it a little bit more inside of this module, just to make sure that our server development is going along pretty well.

---

## 🎬 トランスクリプト（日本語）

MCPサーバー内に機能を追加しましたが、それが機能するかどうかは全くわかりません。 そのため、何らかの方法でテストできれば非常に良いでしょう。 Python SDKを使うことで、ブラウザ内デバッガに自動的にアクセスできるようになります。 これにより、このサーバーが期待どおりに機能していることを 確認できます。 使い方のデモを簡単に行います。 ターミナルに戻り、Python環境が有効になっていることを確認します。 ReadMeドキュメントには、 その環境を有効にするために実行するコマンドの詳細が記載されています。 環境が有効になっていることを確認したら、MCP、 Dev、そしてサーバーを含むファイル名を run します。 この場合は MCPServer.py です。 それを実行すると、ポート6277でリッスンしているサーバーがあることが通知され、 それにアクセスするための直接のアドレスが提供されます。 そのアドレスをブラウザで開きます。 そこに行くと、このようなものが見えるはずです。 これが MCP インスペクターです。 すぐに理解していただきたい重要なことがあります。このインスペクターは現在開発中です。 そのため、このビデオを見ている時点で、 画面に表示されている内容は、私が表示しているものとは大きく異なる可能性があります。 しかし、それでも非常に似た機能を持っているでしょう。 左側には「Connect」ボタンが表示されます。 これは MCP サーバーを起動します。つまり、先ほど編集したファイルです。 「Connect」をクリックすると、画面にいくつかの異なるものが表示されます。 まず、ここにあるトップメニューバーに注目してください。リソース、プロンプト、ツールなどがリストされています。 これもビデオを見る頃には UI が変更されている可能性があります。 もしこのメニューバーが見当たらない場合は、 探しているのは「Tools」セクションです。 「Tools」をクリックし、「List Tools」をクリックすると、 先ほど作成したツールの名前が表示されます。 いずれかをクリックすると、右側のパネルが変更されます。 このパネルを使って、 手動でツールを呼び出し、期待通りに機能するかどうかを確認できます。 これにより、実際のアプリケーションに接続することなく、 MCP サーバーのライブ開発を行うことができます。 Read.Contents ツールを使用するには、ドキュメントIDを入力するだけです。 エディタに戻り、 docs ディクショナリに移動します。 これらのドキュメントIDのいずれかをコピーできます。 deposition.md をコピーします。 これを doc ID として入力し、Run tool をクリックします。 ドキュメントの内容と共に Run tool of success が表示されるはずです。 これです。確認できます。 全く同じ文字列が表示されています。 この同じ技術を使って、他のツールもテストできます。 edit document ツールに切り替えます。 次にドキュメントIDを入力します。 置き換えたい古い文字列。 例えば、「deposition」という単語を置き換えます。 入力しやすい単語があります。例えばこれだけで十分です。 古い文字列はこれです。 大文字小文字を区別することに注意してください。 「report」に置き換えます。 ツールを実行すると、成功というメッセージが表示されます。 このツールはドキュメントの内容を返しません。 ドキュメントを編集するだけです。 編集が正しく行われたことを確認するには、 Read.Contents ツールに戻り、 同じドキュメントIDで再度実行します。 「report deposition」と表示されるはずです。 それから、 blah blah blah。 さて、ご覧のように、この MCP インスペクターは、 実際のアプリケーションに接続することなく、 実装している MCP サーバーを非常に簡単にデバッグできます。 独自の MCP サーバーを構築する際には、 このインスペクターツールをかなり頻繁に使用することになるでしょう。 そして、このモジュールでもう少し使用して、 サーバー開発が順調に進んでいることを確認します。
