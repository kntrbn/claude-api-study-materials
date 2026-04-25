# 61. MCP clients

**URL:** https://anthropic.skilljar.com/claude-with-the-anthropic-api/287775
**Section:** 09 Model Context Protocol

---

## 📄 Page Content

Anthropic Academy
    
  

  
    
      Courses
    
  

    

    
      
      

      
        
          My Profile
        
        
      

      
      

      
        Sign Out
      
    
  

  

  

    
    
    
        
            
    
        
    

            
    
        
        
            
                
                    
                        
                            
                                
                            

                            
                                details
                            

                            
                        
                    
                
            
            
                
                
                
                    MCP clients
                    
                
                
                    
                        
                            
                                
                                    

    
    

    
    
        
            
        
        
            
                
                This video is still being processed. Please check back later and refresh the page.
            
        
        
            
                Uh oh! Something went wrong, please try again.
            
        
    

    

                                
                            
                        
                    
                
            
        
        
            

    
        
            
                
                    
                        
                            
                        
                    
                
            
            
                
                    Summary
                

                

            
        

        
            
                
                    
                        
                            Summary

                            
                                The MCP client serves as the communication bridge between your server and MCP servers. Think of it as your access point to all the tools that an MCP server provides. When you need to use external tools or services, the client handles all the message passing and protocol details for you.

Transport Agnostic Communication

One of MCP's key strengths is being transport agnostic - a fancy way of saying the client and server can talk to each other using different communication methods. The most common setup runs both the MCP client and server on the same machine, where they communicate through standard input/output.

But you're not limited to that approach. MCP clients and servers can also connect over:

HTTP
WebSockets
Various other network protocols

Message Types

Once connected, the client and server exchange specific message types defined in the MCP specification. The main message types you'll work with are:

ListToolsRequest/ListToolsResult: The client asks the server "what tools do you provide?" and gets back a list of available tools.

CallToolRequest/CallToolResult: The client asks the server to run a specific tool with certain arguments, then receives the results.

Complete Flow Example

Here's how all the pieces work together in a real scenario. Let's say a user asks "What repositories do I have?" - here's the complete communication flow:

The process starts when a user submits a query to your server. Your server realizes it needs to provide Claude with a list of available tools before making the request.

Your server asks the MCP client for tools, which sends a ListToolsRequest to the MCP server and receives a ListToolsResult back.

Now your server has everything needed to make the initial request to Claude - both the user's question and the available tools.

Claude examines the tools and decides it needs to call one to answer the question. It responds with a tool use request.

Your server asks the MCP client to execute the tool Claude requested. The MCP client sends a CallToolRequest to the MCP server, which then makes the actual request to GitHub.

GitHub returns the repository data, which flows back through the MCP server as a CallToolResult, then to the MCP client, and finally to your server.

Your server sends the tool results back to Claude in a follow-up message. Claude now has all the information it needs to formulate a complete response.

Finally, Claude responds with the formatted answer, which your server passes back to the user.

Yes, this flow involves many steps, but each component has a clear responsibility. The MCP client abstracts away the complexity of server communication, letting you focus on building your application logic. As we implement our own MCP client and server, you'll see how each piece fits together in practice.

---

## 🎬 Transcript (English)

The next portion of model context protocol that we're going to investigate is the client. The purpose of the client is to provide a means of communication between your server and a MCP server. This client is going to be your access point to all the tools implemented by that server. Now MCP is transport agnostic. This is a fancy term that just says that the client and the server can communicate over a variety of different protocols. A very common way to run a MCP server right now is on the same physical machine as the MCP client. And if these two things are running on the same machine, then they can communicate over standard input output. And that's what we are going to be setting up later on inside this section. There are, however, other ways we can connect the MCP client with the MCP server. So they can also connect over HTTP or Web Sockets or any of a number of other varieties or techniques. Once a connection has been formed between the client and the server, they communicate by exchanging messages. The exact messages that are allowed are all defined inside of the MCP spec. Some of the message types that you and I are going to be focusing are the list tools request and the list tools result. As you guessed, list tools request is sent from the client to the server and asks the server to list out all the different tools that it provides. The server would then respond with a list tools result message, which contains a list of all the different tools that it can provide. Two other common message types that you and I are going to see are the call tool request and call tool result. The first will ask the server to run a tool with some particular arguments, and the second will contain the result of the tool run. Now, at this point in time, we've got this idea of a server and a client. But I suspect it's probably not really clear how all this stuff really works together. So here's what we're going to do in the remainder of this video. We are going to walk through a example call between a lot of different things. So it's going to be kind of an involved process. But we're going to imagine the communication that goes on between a user or a server that we're putting together. A MCP client, the MCP server, GitHub as some provider that we're trying to access some data from, and Claude. So let's get to it. Again, Stephen Grider, first thing we would expect to happen is a user to submit some kind of query or question to our server, like what repositories do I have? At this point, it would be up to our server to make a request off to Claude. But in that request, we want to list out all the different tools that Claude has access to. So before our server can make the request off to Claude, it's first going to go through a little side detour through the MCP client and the server. So here's what happens. The server is going to realize that it needs to see a list of tools to send off to Claude, along with the user's query. So it's going to ask the MCP client to get a list of tools. The MCP client, in turn, is going to send a list tools request off to the server, and the server will respond with a list tools result. Now that our MCP client has a list of the tools, it will give that list of tools back to the server. And now our server has everything it needs to make an initial request off to Claude. It has both the original message from the user and a list of tools to include. So our server can make a request off to Claude with that query and the set of tools. Claude is going to take a look at the tools and realize, you know what, in order to answer the user's original question right here, I really want to call a tool. So Claude would respond with some tool use message part. At this point, our server is going to realize that Claude wants to run a tool. But our server is no longer really in charge of executing any tools. Instead, our tools are going to be executed by the MCP server. So in order to run the tool that Claude is asking for, our server is going to ask the MCP client to run a tool with some particular arguments that were provided by Claude. The MCP client, however, doesn't actually run the tool. It's going to send a call tool request off to the MCP server. The MCP server will receive that request and make a follow request off to GitHub. So this is where we would actually be getting a list of repositories that belong to this particular user. GitHub would respond with that list of repositories. Then the MCP server would wrap up that data inside of a call tool result and send that back to the MCP client. Then the MCP client in turn would hand the result off to our server. Now our server has the list of repositories and it can make a follow up request to Claude with the tool result part inside of a user message. So this tool result would include the list of repositories that Claude was asking for. And now Claude has all the information it needs to formulate a final response. So it'll write out some text of something like your repositories are, and then send that back to our server, and our server would send it on back to our user. All right, so this flow, yes, it is rather complicated. The reason I want to show you this is that we are going to see all these different pieces as you and I start to implement our own custom MCP client and MCP server a little bit later on.

---

## 🎬 トランスクリプト（日本語）

次に調査するモデルコンテキストプロトコルの部分 はクライアントです。クライアントの目的は 、サーバーとMCPサーバーとの間の通信手段を 提供することです。このクライアントは 、そのサーバーによって実装されたすべてのツールへの アクセスポイントとなります。 MCPはトランスポートに依存しません。これは 、クライアントとサーバーがさまざまなプロトコルで 通信できることを意味する、格好の良い言葉です。 現在、MCPサーバーを実行する非常に一般的な方法として は、MCPクライアントと同じ物理マシン上で実行することです。 これらの2つのものが同じマシンで実行されている場合 、標準の入出力で通信できます。そして、それこそが 、このセクションで後ほど設定するものになります。 しかし、MCPクライアントとMCPサーバーを接続する他の方法も あります。例えば、HTTPやWebソケットなどを介して 接続することもできますし、他にも多くの方法や技術が あります。 一度クライアントとサーバー間の接続が確立されると、 、それらはメッセージを交換することによって通信します。 許可される正確なメッセージはすべてMCPの仕様で定義されています。 あなたと私が焦点を当てるメッセージの種類の一部は、ツール一覧リクエストと ツール一覧結果です。 ご推察の通り、ツール一覧リクエストはクライアントからサーバーへ 送信され、サーバーに提供しているすべての異なるツールを 一覧表示するように要求します。サーバーは次に 、ツール一覧結果メッセージで応答します。このメッセージには、提供できるすべての 異なるツールのリストが含まれています。 あなたと私が次に目にする一般的なメッセージタイプの他に 、ツール呼び出しリクエストとツール呼び出し結果があります。 前者は特定の引数でツールを実行するようにサーバーに依頼し 、後者はツールの実行結果を含みます。 さて、この時点でサーバーとクライアントという考え方はありますが 、これらのものがすべてどのように連携して機能するのか、おそらく明確ではないでしょう。 そこで、このビデオの残りの部分でこれから行うことは 、さまざまなものの間の呼び出し例を歩いていくことです。 なので、かなり手間のかかるプロセスになりますが 、ユーザーと、私たちが構築しているサーバーとの間の通信を想像してみましょう。 MCPクライアント、MCPサーバー、GitHub 、データからアクセスしようとしているプロバイダー、そして Claudeです。それでは始めましょう。再びStephen Griderです。 最初に期待されるのは、ユーザーが私たちのサーバーに 「私のリポジトリは何ですか？」といったクエリや質問を送信することです。 この時点で、Claudeにリクエストを行うのは私たちのサーバーの仕事ですが 、そのリクエストでClaudeがアクセスできるすべての異なるツールを 一覧表示したいのです。したがって、私たちのサーバーがClaudeにリクエストを行う前に 、MCPクライアントとサーバーを介して、まず少し寄り道します。 なので、起こることは次のとおりです。サーバーは 、ユーザーのクエリとともにClaudeに送信するツールのリストが必要であることを認識します。 そこで、MCPクライアントにツールのリストを取得するように依頼します。 次に、MCPクライアントはツール一覧リクエストをサーバーに送信し 、サーバーはツール一覧結果で応答します。 これでMCPクライアントがツールのリストを取得したので 、そのツールのリストをサーバーに渡します。そして 、私たちのサーバーは、Claudeに最初の要求を行うために必要なすべてを持っています。 ユーザーからの元のメッセージと含めるツールのリストの両方です。 ですから、私たちのサーバーはそのクエリとツールのセットでClaudeにリクエストを行うことができます。 Claudeはツールを見て、ユーザーの元の質問に答えるために 、ツールを呼び出したいと気づくでしょう。したがって、Claudeは ツール使用メッセージの一部で応答するでしょう。 この時点で、私たちのサーバーはClaudeがツールを実行したいことを認識しますが 、私たちのサーバーはもはやツールの実行を管理していません。 代わりに、私たちのツールはMCPサーバーによって実行されます。 ですから、Claudeが要求しているツールを実行するために 、私たちのサーバーはMCPクライアントに、Claudeによって提供された 特定の引数でツールを実行するように依頼します。 しかし、MCPクライアントは実際にはツールを実行しません。 ツール呼び出しリクエストをMCPサーバーに送信します。 MCPサーバーはそのリクエストを受け取り、GitHubに フォローリクエストを行います。 ここで、この特定のユーザーに属するリポジトリのリストを取得します。 GitHubはそのリポジトリのリストで応答します。 その後、MCPサーバーはそのデータをツール呼び出し結果に ラップし、それをMCPクライアントに返送します。 次に、MCPクライアントは、その結果を私たちのサーバーに渡します。 これで、私たちのサーバーはリポジトリのリストを取得し 、ツール結果の一部をユーザーメッセージに含めて Claudeにフォローアップリクエストを行うことができます。 したがって、このツール結果には、Claudeが求めていた リポジトリのリストが含まれます。 これでClaudeは最終的な応答を作成するために必要なすべての情報を得ました。 そこで、例えば「あなたのリポジトリは」といったテキストを書き 、それを私たちのサーバーに送信します。そして、私たちのサーバーはそれを 私たちのユーザーに送り返します。さて、このフローは 、確かに非常に複雑です。私がこれをお見せしたいのは 、もう少し後に私たちが独自のカスタムMCPクライアントとMCPサーバーを実装し始めるとき に、これらすべての異なるコンポーネントを目にすることになるからです。 。
