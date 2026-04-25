# 65. Implementing a client

**URL:** https://anthropic.skilljar.com/claude-with-the-anthropic-api/287793
**Section:** 09 Model Context Protocol

---

## 📄 Page Content

Anthropic Academy
    
  

  
    
      Courses
    
  

    

    
      
      

      
        
          My Profile
        
        
      

      
      

      
        Sign Out
      
    
  

  

  

    
    
    
        
            
    
        
    

            
    
        
        
            
                
                    
                        
                            
                                
                            

                            
                                details
                            

                            
                        
                    
                
            
            
                
                
                
                    Implementing a client
                    
                
                
                    
                        
                            
                                
                                    

    
    

    
    
        
            
        
        
            
                
                This video is still being processed. Please check back later and refresh the page.
            
        
        
            
                Uh oh! Something went wrong, please try again.
            
        
    

    

                                
                            
                        
                    
                
            
        
        
            

    
        
            
                
                    
                        
                            
                        
                    
                
            
            
                
                    Summary
                

                

            
        

        
            
                
                    
                        
                            Summary

                            
                                Now that we have our MCP server working, it's time to build the client side. The client is what allows our application to communicate with the MCP server and access its functionality.

Understanding the Client Architecture

In most real-world projects, you'll either implement an MCP client OR an MCP server - not both. We're building both in this project just so you can see how they work together.

The MCP client consists of two main components:

MCP Client - A custom class we create to make using the session easier
Client Session - The actual connection to the server (part of the MCP Python SDK)

The client session requires proper resource cleanup when we're done with it. That's why we wrap it in our custom MCP Client class - to handle all that cleanup automatically.

How the Client Fits Into Our Application

Remember our application flow? Our CLI code needs to do two main things with the MCP server:

Get a list of available tools to send to Claude
Execute tools when Claude requests them

The MCP client provides these capabilities through simple method calls that our application code can use.

Implementing the Core Methods

We need to implement two key methods in our client: list_tools() and call_tool().

List Tools Method

This method gets all available tools from the server:

async def list_tools(self) -> list[types.Tool]:
    result = await self.session().list_tools()
    return result.tools

It's straightforward - we access our session (the connection to the server), call the built-in list_tools() function, and return the tools from the result.

Call Tool Method

This method executes a specific tool on the server:

async def call_tool(
    self, tool_name: str, tool_input: dict
) -> types.CallToolResult | None:
    return await self.session().call_tool(tool_name, tool_input)

We pass the tool name and input parameters (provided by Claude) to the server and return the result.

Testing the Client

To test our implementation, we can run the client directly. The file includes a testing harness that connects to our MCP server and calls our methods:

async with MCPClient(
    command="uv", args=["run", "mcp_server.py"]
) as client:
    result = await client.list_tools()
    print(result)

When we run this test, we should see our tool definitions printed out, including the read_doc_contents and edit_document tools we created earlier.

Putting It All Together

Now that our client can list tools and call them, we can test the complete flow. When we run our main application and ask Claude about a document:

Our code uses the client to get available tools
These tools are sent to Claude along with the user's question
Claude decides to use the read_doc_contents tool
Our code uses the client to execute that tool
The result is sent back to Claude, who then responds to the user

For example, asking "What is the contents of the report.pdf document?" will trigger Claude to use our document reading tool, and we'll get back information about the 20m condenser tower document we set up in our server.

The client acts as the bridge between our application logic and the MCP server, making it easy to access server functionality without worrying about the underlying connection details.

---

## 🎬 Transcript (English)

Now that our server is in a good place, we're going to shift gears a little bit and start working on our MCP client. The client can be found inside the MCP client.py file inside the root project directory. Now before we do anything inside this file, I just want to give you a very quick reminder here. Remember what I told you about earlier. Usually in a typical project, we are either making use of a client or we are implementing a server. It's just in this one particular project that we are working on that we are doing both. Again, just so you can see both sides of the puzzle. Now the MCP client itself inside of this file is consisting of a single class. You'll notice there is a lot of code inside of here and it doesn't look quite as pretty as some of the code we just wrote out inside of the server. So let me tell you exactly what's going on inside this file and exactly why it is so large. Okay, so inside this file, we are making the MCP client class. This class is going to wrap up something called a client session. The client session is the actual connection to our MCP server. This client session is a part of the Anthropic Python SDK. So again, this session is what gives us this connection to the outside server. The session itself requires a little bit of resource cleanup. In other words, whenever we close down our program or decide that we don't need the server anymore, we have to go through a little bit of a cleanup process. And I have already written out a lot of that cleanup code inside of the MCP client class. So that's really why this class exists at all, just to make that cleanup a little bit easier. You can see some of that cleanup code inside of the Connect function and down a little bit lower. at the cleanup, async enter, and async exit functions as well. So it's very common practice to not just make use of this client session directly, instead very common to wrap it up inside of a larger class that's going to manage some of this different resource stuff for you. The next thing I want to clarify is why this client exists at all. So in other words, what is the client really doing for us here? Well, remember, this full that we looked at a little bit ago. So we had our code right here. And at certain points in time, we needed, say, a list of tools to send off to Claude. And then later on after that, we also needed to run a tool that was requested by Claude. In order to reach out to our MCP server and get this list of tools or to run a tool, that's where we are making use of the MCP client. So we can imagine that this client is exposing some functionality that belongs to the server to the rest of our codebase. So inside of our codebase, inside this project, specifically inside of the core directory, there is a lot of code already inside there that I put together that is making use of this class. So there is some other code that's going to call Some of the different functions you see inside of here, like list tools, call tool, list prompts, get prompt, and so on. For right now, in this video, we're going to focus on implementing two functions, list tools and call tool. So as you just saw in the diagram, we looked at a moment ago, these two functions are going to be used in different parts of our code base to get a list of tools to provide off to Claude, and then eventually call a tool whenever Claude requests to call a tool. Implementing these two functions is going to be really simple and straightforward. So let me show you how we're going to do it. We'll first begin with list tools. I'm going to remove the two do inside there and replace it with result is await self.session. I'm going to call that like a function list underscore tools. And then I will return result dot tools. And that's it. So this is going to get access to our session, which is our actual connection to the MCP server. It's going to call a built-in function to get a definition or a list of all the different tools that are implemented by that server. I'm going to get back result and then just return the tools and that's it. Then we can implement call tool right here in a very similar fashion. So this will be return a waitself.session, call tool, tool name, and tool input. Once again, getting access to the session, that is our connection to the server, and I'm going to attempt to call a very specific tool, the name the tool we passed in, along with the input parameters or input arguments to it, that were provided by Claude. Now, at this point in time, I would like to test out these two functions really quickly. To do so, we're going to go down to the bottom of this file, where I put together a very small testing harness for us. So down here, you'll notice I put together this testing block, so we can run this MCP client.py file directly. And if we do so, we're going to form a connection to our MCP server, and then we can just run some commands against it and just see what we get back. Notice that in your version of the code, there's a comment in there about changing the command and args right here in case you are not making use of UV. So if you're not using UV, make sure you take a look at that comment. Inside of this with block, I'm going to add in a little bit of testing code. So I'll say result is await underscore client list tools. And then I'm going to just print out the result that we get back. So this should start up a copy of our MCP server, then attempt to get a list of all the different tools that are defined by it, and then just print out the result. To test this out, I will flip back over to my terminal and do a UV run, MCP underscore client.py. And as usual, if you are not making use of UV, you'll just do a Python MCP client.py. Okay, so I'll run that, and there is our list of tool definitions. So I can see inside of here that I have the read.contents tool, which we put together a little bit ago, and our edit document tool as well. Each one has a description and a input schema as well. So this is our tool definition, which will eventually be passed off to Claude. Now before we move on, there's one other thing I want to test. Remember, we just implemented the function that's going to allow us to list out some tools and pass them off to Claude and the function that's going to allow us to call a tool that is implemented by the MCP server and then pass the result off to Claude as well. I have already implemented the code that is going to call list tools and call tool for us somewhere else inside this project. So now that we have added in this functionality, now that we have defined these tools and the ability to call a particular tool, we can now run our CLI again and attempt to get Claude to make use of these tools. In other words, we can ask Claude to inspect the contents of some particular document and even edit a document. So let me show you how we do that. Inside of my MCP server, I just want to give you a reminder that there is a document with a ID of report.pdf, and it has some texture of something like a 20 meter condenser tower. I'm going to go back over to my terminal, and I'm going to run my project with a UV run main.py. And then I'm going to ask Claude what is the contents of the report.pdf document. And make sure you put in exactly report.pdf here. And when we run this, we're sending off along with the request our list of tools. Claude is going to decide to use the read document tool. And it's going to get the contents of the document. And then we will see that yes, Claude was able to get the contents of that document. We are told that the report is something about a 20 meter condenser tower. All right, so at this point, we have added in some functionality around our client. Remember, the client is what allows us to access some functionality that is implemented inside of the MCP server. At this point in time, we have been able to list out some tools that are created by the server and execute a tool that has been implemented by the server.

---

## 🎬 トランスクリプト（日本語）

サーバーの準備ができたので、少しギアを切り替えて MCPクライアントの作業を開始します。 クライアントはMCPクライアント.py内の ファイルで見つけることができます。さて、この ファイル内で何かを行う前に、非常に簡単なリマインダーを 差し上げたいと思います。以前お話ししたことを思い出してください。通常、 一般的なプロジェクトでは、クライアントを利用するか、 サーバーを実装しています。この 特定のプロジェクトだけが、両方を行っています。繰り返しますが、 パズルの両面を見ていただけるように。さて、 MCPクライアント自体は、この ファイル内に1つのクラスで構成されています。 ここには多くのコードがありますが、先ほどサーバー内で記述した コードほどきれいに見えません。 そこで、このファイル内で何が起こっているのか、そしてなぜそれほど 大きいのかを正確に説明します。さて、 このファイル内で、MCP クライアントクラスを作成しています。このクラスは、 クライアントセッションと呼ばれるものをラップします。クライアントセッションは MCPサーバーへの実際の接続です。 このクライアントセッションは、Anthropic Python SDKの一部です。ですから、このセッションは 外部サーバーへの接続を提供するものです。 セッション自体には、リソースのクリーンアップが少し必要です。 つまり、プログラムを終了するときや、 サーバーが不要になったと判断したとき、私たちは 少しクリーンアッププロセスを経る必要があります。そして、私はすでに そのクリーンアップコードの多くを MCPクライアントクラス内に記述しました。ですから、このクラスが 存在する理由はまさにそれです。クリーンアップを少し 簡単にするためです。そのクリーンアップコードの一部は、 Connect関数と、もう少し下にある cleanup、async enter、async exit関数でも見ることができます。ですから、これは非常に一般的な 慣例です。この クライアントセッションを直接利用するだけでなく、代わりに、いくつかの リソース管理を行うより大きなクラスにラップするのが 一般的です。次に明確にしたいのは、このクライアントが そもそも存在する必要がある理由です。つまり、クライアントが 実際には何をしているのかということです。さて、少し前に見た このファイル全体を思い出してください。私たちのコードは ここにありました。そして、特定の時点で、例えば、Claudeに送信するための ツールリストが必要でした。そしてその後、Claudeによって要求された ツールを実行する必要もありました。 このツールのリストを取得したり、ツールを実行したりするために、 MCPサーバーに接続するために、 そこでMCPクライアントを利用します。つまり、この クライアントがサーバーの機能を 公開していると想像できます。私たちのコードベースの残りの部分に。ですから、 私たちのコードベース内、このプロジェクト内、特に コアディレクトリ内に、私がまとめた多くのコードがあり、それは このクラスを利用しています。ですから、他のコードが ここに表示されているさまざまな関数のいくつかを 呼び出します。例えば、list tools、call tool、list prompts、get promptなどです。 現時点では、この動画では、list toolsとcall toolの 2つの関数を実装することに焦点を当てます。 ですので、先ほどの図でご覧いただいたように、これらの 2つの関数は、コードベースのさまざまな部分で使用されます。 ツールリストを取得してClaudeに渡すために、 そして最終的にClaudeがツールを呼び出すように要求したときに ツールを呼び出すために。これらの2つの関数を実装することは 非常にシンプルでわかりやすいでしょう。では、どのように行うかをお見せします。まずlist toolsから始めます。 そこに表示されている2つのTODOを削除し、 それを result is await self.session.と置き換えます。 それを function list underscore toolsと呼びます。そして、result .toolsを返します。それだけです。 これは、私たちのセッション、つまり MCPサーバーへの実際の接続にアクセスします。それは サーバーによって実装されているすべての異なるツールの定義またはリストを取得するための 組み込み関数を呼び出します。私は resultを受け取り、次にtoolsを返します。それだけです。 次に、call toolを非常に同様の方法で実装できます。 これは return a wait self.session, call tool, tool name, and tool inputを返します。 もう一度、サーバーへの接続であるセッションにアクセスし、 渡されたツール名とClaudeによって提供された入力パラメータまたは入力引数とともに、 特定のツールを呼び出そうとします。 この時点まで来たら、この2つの関数をすぐにテストしたいと思います。 そうするために、このファイルの一番下にある 私がまとめた非常に小さなテストハーネスに行きます。 ここに、この テストブロックを配置しましたので、このMCP クライアント.pyファイルを直接実行できます。そして、そうすれば、 MCPサーバーのコピーを起動し、 次にコマンドを実行して、何が得られるかを確認できます。 あなたのコードバージョンでは、UVを使用しない場合に変更する必要がある コマンドと引数についてのコメントがあることに注意してください。 したがって、UVを使用しない場合は、そのコメントを確認してください。 このwithブロック内で、テストコードを追加します。 result is await underscore client list toolsと入力します。 そして、取得した結果を印刷します。 これにより、MCPサーバーのコピーが起動され、 定義されているすべてのツールのリストを取得しようとします。 そして、結果を印刷します。 これをテストするために、ターミナルに戻り、 UV run MCP underscore client.pyを実行します。 そしていつものように、UVを使用しない場合は、Python MCP client.pyを実行します。さて、実行しましょう。 そして、ここにツール定義のリストがあります。 ここに、先ほど作成したread contentsツールと、 edit documentツールもあります。それぞれに説明と 入力スキーマがあります。 これがツール定義です。最終的にClaudeに渡されます。 さて、先に進む前に、もう一つテストしたいことがあります。 ツールをリスト表示してClaudeに渡す機能と、 MCPサーバーによって実装されたツールを呼び出して、 その結果をClaudeに渡す機能を実装したことを思い出してください。 私はすでに、list toolsとcall toolを 呼び出すコードを実装しました。 このプロジェクトのどこか他の場所で。ですから今 この機能を追加し、これらのツールと特定のツールを呼び出す機能を定義したので、 CLIを再度実行して、Claudeにこれらのツールを使用させることができます。 つまり、Claudeに特定のドキュメントの内容を調べさせたり、 ドキュメントを編集させたりすることができます。 それでは、どのように行うかお見せします。私の MCPサーバー内では、report.pdfというIDのドキュメントと、 20メートルコンデンサタワーのようなテキストがあることを思い出させてください。 ターミナルに戻ります。 そして、UV run main.pyでプロジェクトを実行します。 そしてClaudeに、report.pdfドキュメントの内容は何ですか？と尋ねます。 そして、ここに正確にreport.pdfと入力するようにしてください。 そしてこれを実行すると、 リクエストとともにツールリストを送信しています。 Claudeはread documentツールを使用することを決定します。 そしてドキュメントの内容を取得します。そして私たちが見るのは Claudeがその ドキュメントの内容を取得できたということです。レポートは20メートルコンデンサタワーに関するものだと 私たちに伝えられます。 さて、この時点で、クライアントに関する機能を追加しました。 クライアントは、MCPサーバー内に実装されている機能に アクセスできるようにするものであることを思い出してください。 この時点で、サーバーによって作成されたツールを リスト表示し、サーバーによって実装されたツールを実行する機能 を実行することができました。
