# 67. Accessing resources

**URL:** https://anthropic.skilljar.com/claude-with-the-anthropic-api/287783
**Section:** 09 Model Context Protocol

---

## 📄 Page Content

Anthropic Academy
    
  

  
    
      Courses
    
  

    

    
      
      

      
        
          My Profile
        
        
      

      
      

      
        Sign Out
      
    
  

  

  

    
    
    
        
            
    
        
    

            
    
        
        
            
                
                    
                        
                            
                                
                            

                            
                                details
                            

                            
                        
                    
                
            
            
                
                
                
                    Accessing resources
                    
                
                
                    
                        
                            
                                
                                    

    
    

    
    
        
            
        
        
            
                
                This video is still being processed. Please check back later and refresh the page.
            
        
        
            
                Uh oh! Something went wrong, please try again.
            
        
    

    

                                
                            
                        
                    
                
            
        
        
            

    
        
            
                
                    
                        
                            
                        
                    
                
            
            
                
                    Summary
                

                

            
        

        
            
                
                    
                        
                            Summary

                            
                                Resources in MCP allow your server to expose data that can be directly included in prompts, rather than requiring tool calls to access information. This creates a more efficient way to provide context to AI models like Claude.

Understanding Resource Requests

When you've defined resources on your MCP server, your client needs a way to request and use them. The client acts as a bridge between your application and the MCP server, handling the communication and data parsing automatically.

The flow is straightforward: when a user wants to reference a document (like typing "@report.pdf"), your application uses the MCP client to fetch that resource from the server and include its contents directly in the prompt sent to Claude.

Implementing Resource Reading

The core functionality requires a read_resource function in your MCP client. This function takes a URI parameter identifying which resource to fetch:

async def read_resource(self, uri: str) -> Any:
    result = await self.session().read_resource(AnyUrl(uri))
    resource = result.contents[0]

The response from the MCP server contains a contents list. You typically only need the first element, which contains the actual resource data along with metadata like the MIME type.

Handling Different Content Types

Resources can return different types of content, so your client needs to parse them appropriately. The MIME type tells you how to handle the data:

if isinstance(resource, types.TextResourceContents):
    if resource.mimeType == "application/json":
        return json.loads(resource.text)
    
    return resource.text

This approach ensures that JSON resources are properly parsed into Python objects, while plain text resources are returned as strings. The MIME type acts as your hint for determining the correct parsing strategy.

Required Imports

To make this work properly, you'll need these imports in your MCP client:

import json
from pydantic import AnyUrl

The json module handles parsing JSON responses, while AnyUrl ensures proper type handling for the URI parameter.

Testing Resource Access

Once implemented, you can test the functionality through your CLI application. When you type something like "What's in the @report.pdf document?", the system should:

Show available resources in an autocomplete list
Allow you to select a resource
Fetch the resource content automatically
Include that content in the prompt to Claude

The key advantage is that Claude receives the document content directly in the prompt, eliminating the need for tool calls to access the information. This makes interactions faster and more efficient.

Integration with Your Application

Remember that the MCP client code you write gets used by other parts of your application. The read_resource function becomes a building block that other components can call to fetch document contents, list available resources, or integrate resource data into prompts.

This separation of concerns keeps your code clean: the MCP client handles communication with the server, while your application logic focuses on how to use that data effectively.

---

## 🎬 Transcript (English)

We have defined two separate resources inside of our MCP server. So now our client needs the ability to request these resources. To do so, we're going to add in a single function inside of our MCP client. And remember, this MCP client is going to have some functionality that we're putting together that is going to be used by the rest of our application. And I've already put together that code already. So somewhere else inside this project, something is going to try to make use of this function that we're about to add into the MCP client. To get started, I'm going to open up the MCP client file again. I'm going to scroll down and find read resource right here. So our goal inside here is to read a particular resource by making a request off to our MCP server and then parse the contents that come back depending upon its mime type and then just return whatever data we get. So you'll notice that a argument to it is the URI. This is going to be the URI of the resource that we want to fetch from the server. In order to make request, just to get all of our types nicely, we're going to add two imports at the very top of the file. I'm going to add in an import for the JSON module. And from PyDientTik, I will import AnyURL. Then I'll go back down. to our read resource function. I'm going to clear out the comment in the return statement. Then I'll get a result from calling await. self. session. I want to read resource. And then again, this is really just to get the types to work out. We're going to put in an AnyURL with the input URI. Then I'm going to take from that result. response or excuse me, result.contents at zero. And I want to make this clear right here why we were adding this in. So just a moment ago inside of our inspector, we saw the response we get back. So this is essentially that result variable. Result has a contents list. And there's going to be a list of elements inside there. We really only care about the very first one. So I want to get the first dictionary. I want to access the type property and the mime type. I want specifically the MIME type because it's going to help me understand what kind of data we got back. If it is JSON, then I want to make sure I parse the text as JSON and return that result. So let me show you how we're going to do that. I'm going to add in a if isinstance(resource.contents[0], ResourceTypeText) and resource.mime_type == "application/json": # This is our hint. If the server told us that it's giving us back some JSON, we need to make sure that we parse the text content as JSON. So I will return in that case json.loads(resource.text). And then otherwise, if we don't fall into that if statement and return early, I want to just return resource.text. So in this scenario, we'd be returning the text as just plain text or not parsing anything. So this would really be the case in which we get back the contents of a single document. All right, so that should really be it. We've got our read resource put together. Now again, I want to remind you, I know I've said this several times, but I just want to remind you because I think it might be a little bit unclear. The code that we're writing inside of the MCP client is being used from several other places inside of this code base. So somewhere else in this code base, we're going to be calling that function that we just put together to get the list of document names and then eventually get the contents of a document to put into a prompt. So at this point, everything should essentially work because the rest of the work has already been done for us. So with that in mind, let's go back over to our terminal and we're gonna test out our CLI application again and see if this mention feature works. Okay, so back over here, I'll do a `uvicorn main:app --reload` and now I should be able to say something like what's in the at and there we go, I see my list of resources and I can use the arrow key to scroll through. Once I am at a resource, I like, I'll just hit space and we'll insert that resource. So what's in the report.pdf document? And now, I can tell you that everything is working as expected here. In other words, the contents of this document is being sent off to Claude inside the prompt. So if I submit this, I should see an immediate response and it's going to tell me what is inside of Report PDF. So this time around, Claude did not have to use a tool to read the contents of the document. All right, so that is resources. Again, we make use of resources to expose some amount of information from our MCP server.

---

## 🎬 トランスクリプト（日本語）

MCPサーバー内に2つの個別のリソースを定義しました。 クライアントはこれらのリソースを要求する機能を必要とします。 そのために、MCPクライアント内に1つの関数を追加します。 このMCPクライアントには、アプリケーションの他の部分で使用される機能が 含まれることになります。 そして、すでにそのコードを作成しました。 したがって、このプロジェクト内のどこかで、これから追加する関数を 利用しようとします。 始めるために、MCPクライアントファイルを再度開きます。 スクロールして、 ここにある`read resource`を見つけます。 私たちの目標は、 MCPサーバーにリクエストを送信して、 特定のリソースを読み取ることです。 そして、MIMEタイプに応じて返された内容を解析し、 受け取ったデータを返します。 ご覧の通り、引数はURIです。 これはサーバーから取得したいリソースのURIになります。 リクエストを行うために、 すべての型を適切に取得するには、 ファイルの先頭に2つのインポートを追加します。 JSONモジュールのインポートを追加し、 PyDientTikからAnyURLをインポートします。 次に、下に移動して read resource関数に戻ります。 returnステートメントのコメントをクリアします。 次に、await.self.session.read resourceを呼び出して 結果を取得します。 また、これは本当に型を機能させるためだけです。 入力URIを持つAnyURLを記述します。 次に、 その結果のresponse、 またはexcuse me、result.contentsの最初の要素を取得します。 そして、なぜこれ追加したのかをここで明確にしたいと思います。 ほんの少し前、インスペクター内で受け取ったレスポンスを見ました。 これは基本的にその結果変数です。 結果にはcontentsリストがあります。 そして、その中に要素のリストがあります。 私たちは最初のものだけを気にします。 最初の辞書を取得したいのです。 typeプロパティとMIMEタイプにアクセスしたいです。 MIMEタイプ、なぜなら 受け取ったデータの種類を理解するのに役立つからです。 JSONであれば、テキストをJSONとして解析し、 その結果を返したいです。 その方法を示しましょう。 次を追加します。 if isinstance(resource.contents[0], ResourceTypeText) and resource.mime_type == "application/json": # これはヒントです。 サーバーがJSONを返していると指示した場合、 テキストコンテンツをJSONとして解析する必要があることを確認する必要があります。 その場合、 json.loads(resource.text)を返します。 それ以外の場合、 早期に返さなかった場合は、 resource.textを返します。 このシナリオでは、テキストをプレーン テキストとして返すか、何も解析しません。 これは、単一の ドキュメントの内容を取得する場合に当てはまります。 これで完了です。 read resourceが作成されました。 繰り返しになりますが、何度か言いましたが、 MCPクライアント内に記述しているコードが このコードベースのいくつかの場所から使用されていることを 思い出させたいと思います。 したがって、コードベースのどこかで、作成した関数を呼び出して ドキュメント名のリストを取得し、 最終的にドキュメントの内容を取得して プロンプトに入れることになります。 この時点では、すべて機能するはずです。 残りの作業はすでに完了しているためです。 それを念頭に置いて、 ターミナルに戻り、CLIアプリケーションを再度テストして、 このメンション機能が機能するかどうかを確認します。 ここで `uvicorn main:app --reload` を実行します。 `what's in the at` のようなものを言うと、 うまくいきました。リソースのリストが表示され、 矢印キーでスクロールできます。 リソースに到達したら、スペースキーを押すと挿入されます。 report.pdfドキュメントの何が含まれていますか？ さて、すべてが期待通りに機能していることをお伝えできます。 つまり、このドキュメントのコンテンツはプロンプト内でClaudeに送信されています。 送信すると、即座に応答が表示されるはずです。 そして、Report PDFに何が含まれているかを教えてくれます。 今回は、Claudeはドキュメントのコンテンツを読み取るために ツールを使用する必要がありませんでした。 さて、それがリソースです。 再び、リソースを使用して、MCPサーバーからの情報を公開します。
