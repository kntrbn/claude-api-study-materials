# 66. Defining resources

**URL:** https://anthropic.skilljar.com/claude-with-the-anthropic-api/287782
**Section:** 09 Model Context Protocol

---

## 📄 Page Content

Anthropic Academy
    
  

  
    
      Courses
    
  

    

    
      
      

      
        
          My Profile
        
        
      

      
      

      
        Sign Out
      
    
  

  

  

    
    
    
        
            
    
        
    

            
    
        
        
            
                
                    
                        
                            
                                
                            

                            
                                details
                            

                            
                        
                    
                
            
            
                
                
                
                    Defining resources
                    
                
                
                    
                        
                            
                                
                                    

    
    

    
    
        
            
        
        
            
                
                This video is still being processed. Please check back later and refresh the page.
            
        
        
            
                Uh oh! Something went wrong, please try again.
            
        
    

    

                                
                            
                        
                    
                
            
        
        
            

    
        
            
                
                    
                        
                            
                        
                    
                
            
            
                
                    Summary
                

                

            
        

        
            
                
                    
                        
                            Summary

                            
                                Resources in MCP servers allow you to expose data to clients, similar to GET request handlers in a typical HTTP server. They're perfect for scenarios where you need to fetch information rather than perform actions.

Understanding Resources Through an Example

Let's say you want to build a document mention feature where users can type @document_name to reference files. This requires two operations:

Getting a list of all available documents (for autocomplete)
Fetching the contents of a specific document (when mentioned)

When a user types @, you need to show available documents. When they submit a message with a mention, you automatically inject that document's content into the prompt sent to Claude.

How Resources Work

Resources follow a request-response pattern. Your client sends a ReadResourceRequest with a URI, and the MCP server responds with the data. The URI acts like an address for the resource you want to access.

Types of Resources

There are two types of resources:

Direct Resources: Static URIs that don't change, like docs://documents
Templated Resources: URIs with parameters, like docs://documents/{doc_id}

For templated resources, the Python SDK automatically parses parameters from the URI and passes them as keyword arguments to your function.

Implementing Resources

Resources are defined using the @mcp.resource() decorator. Here's how to create both types:

Direct Resource (List Documents)

@mcp.resource(
    "docs://documents",
    mime_type="application/json"
)
def list_docs() -> list[str]:
    return list(docs.keys())

Templated Resource (Fetch Document)

@mcp.resource(
    "docs://documents/{doc_id}",
    mime_type="text/plain"
)
def fetch_doc(doc_id: str) -> str:
    if doc_id not in docs:
        raise ValueError(f"Doc with id {doc_id} not found")
    return docs[doc_id]

MIME Types

Resources can return any type of data - strings, JSON, binary, etc. The mime_type parameter gives clients a hint about what kind of data you're returning:

application/json - Structured JSON data
text/plain - Plain text content
Any other valid MIME type for different data formats

The MCP Python SDK automatically serializes your return values. You don't need to manually convert to JSON strings.

Testing Resources

You can test your resources using the MCP Inspector. Run your server with:

uv run mcp dev mcp_server.py

Then connect to the inspector in your browser. You'll see:

Resources: Lists your direct/static resources
Resource Templates: Shows templated resources that accept parameters

Click on any resource to test it and see the exact response structure your client will receive.

Key Points

Resources expose data, tools perform actions
Use direct resources for static data, templated resources for parameterized queries
MIME types help clients understand response format
The SDK handles serialization automatically
Parameter names in templated URIs become function arguments

Resources provide a clean way to make data available to MCP clients, enabling features like document mentions, file browsing, or any scenario where you need to fetch information from your server.

---

## 🎬 Transcript (English)

In this video, we're going to move on to the next major feature inside of MCP servers, which is Resources. To help you understand resources, we're going to be implementing another feature inside of our project. Here's what we're going to add in. I want to allow a user to mention a document by putting in an add symbol and then the name of a document. Whenever they do so, I want to automatically fetch the contents of that document and insert it into the prompt that we send off to Claude. So in total, there's kind of two aspects to this feature. Whenever user types out the at symbol inside the message, we're going to automatically show a list of all the different documents that they can mention inside of a little autocomplete window. Then whenever user submits a message with a mention inside of it, we're going to automatically get the contents of that document and insert it into the prompt that we send off to Claude. So for example, if a user says something like what's in the atchreport.pdf file, I would want to assemble a prompt like this and send it to Claude. So we're going to have the query inside there from the user, and then we're also going to tell Claude that the user might have referenced some document, and here is the contents of the document. So the approach here or the idea here is that we will not have to rely upon Claude to go and make use of some tool to figure out what is inside of the report.pdf file. Instead, the user can just preemptively mention the file, and we're going to automatically insert some context ahead of time. Now, one thing I want to clarify here is that we're kind of talking about two separate features. The first feature is that whenever a user types in the at symbol, we really need the MCVP server to give us a list of all the different documents that the user can possibly mention. And then the second aspect here is that whenever a user submits a message that contains a mention, then we need the MCP server to give us the contents of a single document. To get this information out of our MCP server, we are going to be making use of resources. Resources allow our MCP server to expose some amount of data to the client. We usually define one resource for each distinct read operation. So in our example, we need to get a list of documents and read the contents of a single document. So we would probably end up making two separate resources. One resource would be responsible for returning just a list of document names so we can put them inside the autocomplete, and then we would probably make another resource that will expose the contents of a single document based upon its document ID. When we define these resources, they are going to be accessed through our MCP client. So the entire flow that we're going to eventually put together here, whenever user types in something like what's in the app and then presumably they're going to put in something right there, as soon as they type in that app character, we need to display a list of document names to put in the auto complete. So our code is going to reach out to the MCP client, which in turn is going to send a read resource request off to the MCP server. Inside of that read resource request, we're going to include something called the URI. That is essentially the address of the resource we want to read. This URI gets defined whenever we put together our resource initially. So the URI is that right there. When we send off this read resource request, the MCP server is going to look at the exact URI that we put inside of here, and then run the function we put together right there. Take the result and send it back to us inside of a read resource result message. We can then take the data inside there and display it inside of our autocomplete or do whatever else we need to do with it. There are two different types of resources, direct and templated. You'll also sometimes see direct resources referred to as static resources. A direct resource just has a static URI, so it's always going to be the exact same thing, such as docs, colon slash slash documents. A templated resource will have one or more parameters inside of its URI. So for example, we might have documents slash, and then kind of a wild card right here. So we can put in any document ID we want to. And whenever we ask for this resource, that document ID right there inside the URI will be automatically parsed by the Python MCP SDK and provided as a keyword argument to our function. The keyword argument will have the exact same name of whatever string you put in right there. So Doc ID right there will be Doc ID right there. As you can probably guess, we'll make use of templated resources anytime that we want to allow a little bit more selection or variety or customization in what someone is asking for out of our MCP server. Implementing resources is pretty straightforward. So let's go back over to our editor and we're going to add in some resources to our server right away. All right, so back over inside my editor, I will find the MCP server.py file. I'm then going to scroll down a little bit and I'm going to find some comments for writing a resource to return all document IDs and writing a resource to return the contents of a particular document. Now for this first one right here, I put in the comment document IDs. Remember for us, our document IDs are essentially the name of the document. So for us, we're really just returning these IDs. They're going to serve the purpose of the name. That means we can put them directly into that autocomplete element. All right, so to make our resource, I'm going to delete that to do. and then I'll add in a MCP.resource. The first argument is going to be the URI for accessing this thing. Again, it's kind of equivalent to a route handler. So I will use docs, colon slash slash documents, and I'm also going to add in a MIME type of application slash JSON. A resource can return any type of data, so it can be plain text, it can be JSON, it can be binary data, anything. is up to us to kind of give our client a hint as to what kind of data we are returning. To do so, we're going to define this MIME type. A MIME type of application slash JSON is a hint to our client, who's eventually going to ask for this resource right here, that we're going to be sending back a string that contains some structured JSON data. And so it would be up to our client to de-serialize that data, or essentially turn it into some usable data structure. Underneath that decorator, I'll write out my function of list docs, and I'm going to return a list of strings. And then inside there, I will return list docs keys. So just take all the keys out of that dictionary and turn it into a list, and I'm going to return it. Now, you'll notice that we are not returning distinct JSON here. In other words, we're not actually returning a string. The MCP Python SDK is going to automatically take whatever we return and turn it into a string for us. All right, let's take care of our second resource. So I'm going to delete that comment and then replace it with MCP resource, docs, colon slash slash documents. And then this time I want a templated resource because I'm putting in this wildcard right here. And then my mind type this time around, just for a little bit of variety, I'm going to be returning plain text because it's going to be just the contents of the document. And I'm not going to wrap it up in any kind of structure. Now, just so you know, in a real application, something like read a document, I would probably return an entire document record. So some kind of dictionary that contains maybe the ID, the content, the author name, the author ID, and stuff like that. But just for the sake of an example, I'm going to return just the text at the document to show you how we would normally return plain text. So in this scenario, my MIME type would be text plane, and then I will make fetch doc. I'm going to take doc ID, which is going to be a string, and I'm going to return a string. Once again, whatever word you put right there, it's going to show up as a keyword argument inside of your function. If we added in some additional parameters inside of here, such as maybe doc type or something like that, it would just show up as an additional keyword argument like so. Then inside of here, I'm going to first make sure that the ID that this person is asking for actually exists. So if doc ID not in docs, I'm going to raise a value error with a F string that says doc with ID not found. And then if we get past that check, I'll return docs doc ID. And that's it. Now let's try testing this stuff out inside of our MCP Inspector once again. So remember at our terminal, we can run the command UVRun, MCPDev, MCPServer.py. That's going to start up a web server at port 6277 or see me 6274 as the default. So I'm going to make sure I open that up inside my browser. Here we go. I'll click connect. I'll then find resources. And then I should be able to list out all the different resources that are available. Now when I list out resources, this is going to be specifically static or direct resources. So I'll see only docs slash documents. And then I can separately list out all my different resource templates. And so I'll see that I have one resource template of FetchDoc. I can first try to run the slash documents right here. We'll see what we get back. So this is the actual message, the exact structure that gets returned from our MCP server. You'll notice that it has a text property and inside there is all the data that we are returning serialized as JSON string. So again, it would be up to us inside of our CLI application to take this text right here and deserialize it from this JSON string into a usable list of strings. Then we can also test out fetch doc. So I'll click on that. I have to enter a doc ID. So I'm going to put it in. I want to read the report.pdf file. And I'll read the resource. And now I should see the contents of that particular document. And you'll notice this I'm around. Once again, I get a text plain. So that's a hint to me that this is plain text. And I should not attempt to deserialize it from JSON in any way.

---

## 🎬 トランスクリプト（日本語）

この動画では、MCPサーバー内の次の主要機能に進みます。 それはリソースです。リソースを理解するために、 別の機能を実装します。追加する機能は次のとおりです。 追加する機能は次のとおりです。 ユーザーがドキュメントを参照できるようにしたいです。 @記号とドキュメント名を入力することで。 そうすると、自動的に そのドキュメントの内容を取得し、プロンプトに挿入します。 Claudeに送信するものです。合計で、 この機能には2つの側面があります。ユーザーが入力するたびに メッセージ内で@記号を入力すると、自動的に 参照できるすべてのドキュメントのリストを表示します。 小さな自動補完ウィンドウ内で。次に、 参照を含むメッセージを送信すると、 そのドキュメントの内容を取得し、 Claudeに送信するプロンプトに挿入します。 たとえば、ユーザーが「〇〇には何が入っていますか？」と @atchreport.pdfファイルには、 以下のようなプロンプトを組み立ててClaudeに送信します。 そこにはユーザーからのクエリが含まれ、 また、Claudeにユーザーが参照した可能性のある ドキュメントについて、そしてドキュメントの内容を伝えます。 ここでのアプローチ、またはアイデアは、 Claudeにツールを使用して report.pdfファイルの中身を調べるように 依存しないことです。代わりに、ユーザーは単に ファイルを事前に指定でき、私たちは自動的に 事前にコンテキストを挿入します。ここで明確にしたいのは、 2つの別々の機能について話しているということです。 最初の機能は、ユーザーが@記号を入力すると、 MCPサーバーがユーザーが参照できるすべての ドキュメントのリストを提供する必要があるということです。 そして第二の側面は、ユーザーが参照を含むメッセージを送信すると、 MCPサーバーが単一の ドキュメントの内容を提供する必要があるということです。 この情報をMCPサーバーから取得するために、 リソースを利用します。リソースは MCPサーバーがクライアントにデータを公開することを 許可します。通常、1つのリソースは 各個別の読み取り操作に対して定義します。 したがって、私たちの例では、ドキュメントのリストを取得し、 単一のドキュメントの内容を読み取る必要があります。 したがって、2つの別々のリソースを作成することになるでしょう。 1つのリソースは、ドキュメント名のリストを返すことに 責任を持ち、自動補完に入れます。 そして、もう1つのリソースを作成します。これは、 ドキュメントIDに基づいて単一のドキュメントの内容を公開します。 これらのリソースを定義する際、 MCPクライアントからアクセスされます。 したがって、私たちが最終的に構築する全体のフローは、 ユーザーが「app」などと入力したときに、 その後、そこに入力するものがあります。 アプリ文字を入力するとすぐに、ドキュメント名のリストを 自動補完に表示する必要があります。 したがって、私たちのコードはMCPクライアントにアクセスし、 MCPクライアントは読み取りリソースリクエストを MCPサーバーに送信します。 その読み取りリソースリクエスト内には、 URIが含まれます。それは本質的に 読み取りたいリソースのアドレスです。 このURIは、リソースを最初に作成したときに定義されます。 したがって、URIはまさにそれです。 この読み取りリソースリクエストを送信すると、 MCPサーバーは、私たちが入れたURIを調べ、 そこで作成した関数を実行します。 結果を取得し、読み取りリソース 結果メッセージとして返します。それから、 そこにあるデータを取得し、自動補完に 表示するか、その他必要なことをします。 リソースには2つの異なるタイプがあります。 直接リソースとテンプレート化リソースです。 直接リソースは、静的リソースと呼ばれることもあります。 直接リソースには静的なURIがあり、常に同じです。 例えば、docs://documentsなどです。 テンプレート化リソースには、URIに1つ以上のパラメータがあります。 したがって、例えば、documents/と ワイルドカードがあります。 任意のドキュメントIDを入力できます。 そして、このリソースを要求するたびに、 URI内のドキュメントIDは Python MCP SDKによって自動的に解析され、 関数のキーワード引数として提供されます。 キーワード引数は、そこで入力した文字列と まったく同じ名前になります。 したがって、Doc IDはそこにあります。 推測できるように、選択肢やバリエーション、 カスタマイズを少しでも可能にしたい場合は、 テンプレート化リソースを利用します。 リソースの実装は非常に簡単です。 エディターに戻り、すぐにサーバーにリソースを追加しましょう。 はい、エディターに戻りました。 MCPサーバー.pyファイルを見つけます。 次に少しスクロールダウンして、 すべてのドキュメントIDを返すリソースの作成、 特定のドキュメントの内容を返すリソースの作成に関するコメントを見つけます。 この最初のコメントには「ドキュメントID」と書きました。 覚えておいてください。 私たちにとって、ドキュメントIDは本質的に ドキュメントの名前です。したがって、私たちにとって、 私たちはこれらのIDを返しているだけです。それらは 自動補完要素に直接配置できる名前として機能します。 はい、リソースを作成するために、 「TODO」を削除し、MCP.resourceを追加します。 最初の引数は、この要素にアクセスするためのURIです。 再び、ルートハンドラと同等です。 したがって、docs://documentsを使用し、 MIMEタイプをapplication/jsonにすることも追加します。 リソースは任意のタイプのデータを返せます。 プレーンテキスト、JSON、バイナリデータなど、何でも構いません。 クライアントにどのようなデータを提供しているかを 示唆することは私たち次第です。 そのために、このMIMEタイプを定義します。 application/jsonのMIMEタイプは、 このリソースを要求するクライアントに対して、 構造化されたJSONデータを含む文字列を送信するというヒントになります。 そして、クライアントはそれを逆シリアル化する、 つまり、利用可能なデータ構造に変換することになります。 そのデコレータの下に、list_docsという関数を書き、 文字列のリストを返します。そして、 その中に、list_docs.keysを返します。 辞書からすべてのキーを取得し、 リストに変換して返します。 ここで、明らかにJSONを返しているわけではありません。 つまり、文字列を返しているわけではありません。 MCP Python SDKは、私たちが返したものを すべて文字列に変換してくれます。 さて、2番目のリソースを取り上げましょう。 コメントを削除し、MCP resource、docs://documentsに置き換えます。 そして今回、テンプレート化されたリソースが欲しいのです。 このワイルドカードを入力するためです。 そして、MIMEタイプは、 ここでは、バリエーションのために、プレーンテキストを返します。 それは単にドキュメントの内容なので。 それを構造にラップしません。 さて、実際のアプリケーションでは、 ドキュメントの読み取りのようなものは、 ドキュメントレコード全体を返すでしょう。 ID、コンテンツ、著者名、著者IDなどが含まれる 辞書のようなもの。 しかし、例として、ドキュメントのテキストだけを返します。 プレーンテキストを通常どのように返すかを示すために。 したがって、このシナリオでは、MIMEタイプはtext/plainになり、 それからfetch_docを使います。 doc_idを取得します。それは文字列になります。 そして、文字列を返します。もう一度、 そこで入力した単語は、関数内のキーワード引数として 表示されます。 例えば、doc_typeのような追加のパラメータを ここに追加した場合、それは 追加のキーワード引数として表示されます。 このようになります。 そしてここで、まず、この人が要求しているIDが実際に存在するかどうかを確認します。 したがって、doc_idがdocsにない場合、 「IDが見つかりません」というF文字列とともに ValueErrorを発生させます。 そして、そのチェックを通過した場合、 docs[doc_id]を返します。 そして、それだけです。 では、MCP Inspectorでテストしてみましょう。 ターミナルで、uvicornコマンドを実行できることを思い出してください。 python mcp_server.pyです。 これはポート6277でWebサーバーを起動します。 またはデフォルトとして6274です。 したがって、ブラウザで開く必要があります。 ここです。接続をクリックします。次に リソースを見つけます。そして、利用可能な すべてのリソースを一覧表示できるはずです。 リソースを一覧表示すると、これは静的リソースまたは 直接リソースになります。そのため、docs/documentsのみが表示され、 次に、すべてのリソーステンプレートを個別に一覧表示できます。 そして、FetchDocという1つのリソーステンプレートがあることがわかります。 まず、ここにある/documentsを試してみましょう。 何が得られるか見てみましょう。 これは実際のメッセージです。MCPサーバーから 返される正確な構造です。 textプロパティがあり、その中に 返しているすべてのデータがJSON文字列としてシリアル化されていることがわかります。 したがって、再び、このテキストを取得して このJSON文字列から利用可能な文字列リストに 逆シリアル化するのは、CLIアプリケーション内で行う必要があります。 次に、FetchDocもテストできます。 それにクリックします。doc_idを入力する必要があります。 report.pdfファイルを読み込みたいです。 そしてリソースを読みます。 そして、そのドキュメントの内容が表示されるはずです。 そして、これもtext/plainであることがわかります。 それは私がプレーンテキストであることを知るためのヒントです。 そして、JSONから逆シリアル化しようとすべきではありません。 いずれの方法でも。
