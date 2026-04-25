# 70. MCP review

**URL:** https://anthropic.skilljar.com/claude-with-the-anthropic-api/287790
**Section:** 09 Model Context Protocol

---

## 📄 Page Content

Anthropic Academy
    
  

  
    
      Courses
    
  

    

    
      
      

      
        
          My Profile
        
        
      

      
      

      
        Sign Out
      
    
  

  

  

    
    
    
        
            
    
        
    

            
    
        
        
            
            
                
                
                
                    MCP review
                    
                
                
                    
                        
                            
                                
                                    

    
    

    
    
        
            
        
        
            
                
                This video is still being processed. Please check back later and refresh the page.
            
        
        
            
                Uh oh! Something went wrong, please try again.

---

## 🎬 Transcript (English)

We are all done with our project, but before we move on, I want to do a quick recap on the three server primitives that we learned about. So tools, resources, and prompts. In particular, I want to highlight something interesting about each of these. Namely, what part of an app is really responsible for running each? In other words, in a typical application, who is really running each of these things and who benefits from them? Well, we would say that tools are model controlled. This means that Claude alone is really responsible for deciding when to run a given tool. Resources are app controlled. In other words, some code running inside of your app is going to decide that it needs some data provided by a resource. It will be your app's code that decides to execute a resource and use the return data in some way, maybe by using that data in the UI or something like that. In our case, we fetch a resource and then use that data inside the UI to provide a list of autocomplete options. We also fetch a resource to augment a prompt. Both of those things were really application-related code that was authored by you and I to put together. And finally, prompts are really user-controlled. So a user decides when a prompt is going to run. A user might start the invocation of a prompt by clicking on some UI element, like a button or a menu option, or they might make use of a slash command, which is what we did. The reason I highlight what is controlling each of these is to give you some idea of their purpose. So if you ever need to add capabilities to Claude, you're probably going to want to look at implementing some tools inside of your MCP server or consuming some server's tools through your MCP client. If you ever want to get some data into your app for the purposes of showing content in UI or something similar, then you probably want to use a resource. And if you ever want to implement some kind of predefined workflow, you probably want to look at prompts. Now you can see examples of all these ideas inside of the official Claude interface at Claude.ai. So here's what it currently looks like for me. You'll notice that underneath the main chat input are some buttons right here. If I click on one, and then click on one of these examples, you'll see that I immediately dove into a chat. So this was a user-controlled action. I, as the user, decided to start off this particular workflow, and I'm making use of a prompt that was probably already written ahead of time and probably has been optimized in some way. So to implement that list of buttons right there, we would probably want to put together a series of different prompts inside of an MCP server. Likewise, if I go back and maybe click on this little tab right here, the plus button, you'll notice that I have an add from Google Drive button. Now, I'm not going to click on it because it's going to show some of my internal documents. But if I click on that button, I'm going to see some documents that I can add into this chat as some context. Knowing what documents to actually render in that list, and then whenever I click on one, automatically injecting its contents into the context of this chat, that is all application-related code. So it is solely the application that needs to know the list of documents to render here. And that's, again, specifically UI-related elements. So to implement that listing of documents from Google Drive, I would probably look at implementing a resource inside of an MCP server. And then, finally, if I enter in a message to this chat of something like, "what is 3 squared?" Use JavaScript to calculate the value and send it off, I'm clearly expecting Claude to somehow execute some JavaScript code, which would likely be done through the use of a tool. In this case, the decision to use a tool was 100% model controlled. It is the model that decided to use some JavaScript tool execution. To implement something like this inside of an MCP server, we'd likely want to, you guessed it, provide a tool. So in total, that's our three different server primitives. And each one is really intended to be used by a different portion of your overall application. So we got tools which are generally going to serve your model, resources, which are generally going to serve your app, and prompts which are going to serve your users. And once again, these are high-level guidelines. And the only reason I mentioned them is to just give you a sense of when you should use each of these primitives, depending upon what you are trying to put together.

---

## 🎬 トランスクリプト（日本語）

プロジェクトはすべて完了しましたが、次に進む前に、 学んだ3つのサーバープリミティブについて簡単に振り返りたいと思います。 つまり、ツール、リソース、プロンプトです。 特に、それぞれについて興味深い点を強調したいと思います。 つまり、アプリのどの部分が実際に それぞれを実行する責任を負っているのかということです。言い換えれば、 通常のアプリケーションでは、誰が実際にそれぞれを 実行していて、誰がそれらの恩恵を受けているのでしょうか？さて、 ツールはモデル制御であると言えるでしょう。これは 、Claudeが単独で、いつ特定のツールを実行するかを決定する責任を 負っていることを意味します。リソースは アプリ制御です。つまり、アプリ内で実行されている コードの一部が、リソースによって提供されるデータが必要だと 判断することになります。リソースを実行し、その 返されたデータを使用することを決定するのは、あなたのアプリのコードであり、 例えばUIでそのデータを使用するといったことでしょう。 私たちの場合は、リソースを取得し、 そのデータをUI内で使用してオートコンプリートオプションの リストを提供しました。また、プロンプトを 補強するためにもリソースを取得しました。 これら両方のことは、あなたと私が zusammen put togetherした、本当に アプリケーション関連のコードでした。 そして最後に、プロンプトは 本当にユーザー制御です。したがって、ユーザーが いつプロンプトを実行するかを決定します。ユーザーは、ボタンや メニューオプションのようなUI要素をクリックして プロンプトの呼び出しを開始するかもしれませんが、 あるいは私たちがやったようにスラッシュコマンドを利用するかもしれません。 それぞれを何が制御しているかを強調する理由は、その目的を 理解してもらうためです。 したがって、Claudeに機能を追加する必要がある場合は、 おそらくMCPサーバー内にツールを実装するか、 MCPクライアント経由でサーバーのツールを利用することを 検討するでしょう。UIでコンテンツを表示するなどの目的で データをご自身のアプリに取り込みたい場合は、 おそらくリソースを使用したいと思うでしょう。 そして、定義済みのワークフローを実装したい場合は、 おそらくプロンプトを検討するでしょう。 これらのアイデアの例はすべて、 Claude.aiの公式Claudeインターフェースで見ることができます。 現在の私の画面は次のようになっています。 メインのチャット入力の下に、いくつかのボタンがあります。 もし私がそのうちの1つをクリックし、 そしてこれらの例のうちの1つをクリックすると、 すぐにチャットに入ったのがわかるでしょう。 これはユーザー制御のアクションでした。私、ユーザーとして、 この特定のワークフローを開始することを決定し、 おそらく事前に書かれて最適化されたプロンプトを 利用しています。 したがって、あのボタンのリストを実装するには、 MCPサーバー内にいくつかの異なるプロンプトを配置することを 検討するでしょう。同様に、もし戻って この小さなタブ、プラスボタンをクリックすると、 Google Driveから追加するボタンがあるのがわかります。 内部のドキュメントが表示されるので、クリックしませんが、 あのボタンをクリックすると、 コンテキストとしてチャットに追加できるドキュメントが表示されます。 実際にリストにレンダリングするドキュメントを知り、 そして、それらのうちの1つをクリックすると、自動的にその 内容をチャットのコンテキストに挿入することは、すべて アプリケーション関連のコードです。ですから、 ここに表示するドキュメントのリストを知る必要があるのは、 まさにアプリケーションだけです。そして、それは再び、 UI関連の要素です。したがって、 Google Driveからのドキュメントのリストを実装するには、 MCPサーバー内にリソースを実装することを検討するでしょう。 そして、最後に、このチャットに 「3の2乗は？」といったメッセージを入力し、 JavaScriptを使用して値を計算して送信すると、 明らかにClaudeにJavaScriptコードを実行してほしいと思っています。 これはおそらくツールを使用して行われるでしょう。 この場合、ツールを使用するという決定は100%モデル制御でした。 JavaScriptツールの実行を使用すると決定したのはモデルです。 MCPサーバー内でこのようなものを実装するには、 おそらく、お察しの通り、ツールを提供することになるでしょう。 したがって、合計で3つの異なるサーバープリミティブになります。 そしてそれぞれは、全体的なアプリケーションの 異なる部分によって使用されることを目的としています。 ですから、ツールは一般的にモデルに役立ち、 リソースは一般的にアプリに役立ち、 プロンプトはユーザーに役立ちます。 そして、これらはあくまで一般的なガイドラインであり、 私がそれらを言及した唯一の理由は、何を 実装しようとしているかによって、各プリミティブをいつ使用すべきか という感覚を与えるためです。
