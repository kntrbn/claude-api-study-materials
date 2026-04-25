# 63. Defining tools with MCP

**URL:** https://anthropic.skilljar.com/claude-with-the-anthropic-api/287797
**Section:** 09 Model Context Protocol

---

## 📄 Page Content

Anthropic Academy
    
  

  
    
      Courses
    
  

    

    
      
      

      
        
          My Profile
        
        
      

      
      

      
        Sign Out
      
    
  

  

  

    
    
    
        
            
    
        
    

            
    
        
        
            
                
                    
                        
                            
                                
                            

                            
                                details
                            

                            
                        
                    
                
            
            
                
                
                
                    Defining tools with MCP
                    
                
                
                    
                        
                            
                                
                                    

    
    

    
    
        
            
        
        
            
                
                This video is still being processed. Please check back later and refresh the page.
            
        
        
            
                Uh oh! Something went wrong, please try again.
            
        
    

    

                                
                            
                        
                    
                
            
        
        
            

    
        
            
                
                    
                        
                            
                        
                    
                
            
            
                
                    Summary
                

                

            
        

        
            
                
                    
                        
                            Summary

                            
                                Building an MCP server becomes much simpler when you use the official Python SDK. Instead of manually writing complex JSON schemas for tools, the SDK handles all that complexity for you with decorators and type hints.

In this example, we're creating an MCP server that manages documents stored in memory. The server will provide two essential tools: one to read document contents and another to update them through find-and-replace operations.

Setting Up the MCP Server

The Python MCP SDK makes server creation incredibly straightforward. You can initialize a complete MCP server with just one line:

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("DocumentMCP", log_level="ERROR")

For this implementation, documents are stored in a simple Python dictionary where keys are document IDs and values contain the document content:

docs = {
    "deposition.md": "This deposition covers the testimony of Angela Smith, P.E.",
    "report.pdf": "The report details the state of a 20m condenser tower.",
    "financials.docx": "These financials outline the project's budget and expenditure",
    "outlook.pdf": "This document presents the projected future performance of the",
    "plan.md": "The plan outlines the steps for the project's implementation.",
    "spec.txt": "These specifications define the technical requirements for the equipment"
}

Tool Definition with Decorators

The SDK transforms tool creation from a verbose process into something clean and readable. Instead of writing lengthy JSON schemas, you use Python decorators and type hints.

Creating the Document Reader Tool

The first tool allows Claude to read any document by its ID. Here's the complete implementation:

@mcp.tool(
    name="read_doc_contents",
    description="Read the contents of a document and return it as a string."
)
def read_document(
    doc_id: str = Field(description="Id of the document to read")
):
    if doc_id not in docs:
        raise ValueError(f"Doc with id {doc_id} not found")
    
    return docs[doc_id]

The @mcp.tool decorator automatically generates the JSON schema that Claude needs. The Field class from Pydantic provides parameter descriptions that help Claude understand what each argument expects.

Building the Document Editor Tool

The second tool performs simple find-and-replace operations on documents:

@mcp.tool(
    name="edit_document",
    description="Edit a document by replacing a string in the documents content with a new string."
)
def edit_document(
    doc_id: str = Field(description="Id of the document that will be edited"),
    old_str: str = Field(description="The text to replace. Must match exactly, including whitespace."),
    new_str: str = Field(description="The new text to insert in place of the old text.")
):
    if doc_id not in docs:
        raise ValueError(f"Doc with id {doc_id} not found")
    
    docs[doc_id] = docs[doc_id].replace(old_str, new_str)

This tool takes three parameters: the document ID, the text to find, and the replacement text. The implementation uses Python's built-in string replace() method for simplicity.

Error Handling

Both tools include basic error handling to manage cases where Claude requests a document that doesn't exist. When an invalid document ID is provided, the tools raise a ValueError with a descriptive message that Claude can understand and potentially act upon.

Key Benefits of the SDK Approach

Automatic JSON schema generation from Python type hints
Clean, readable code that's easy to maintain
Built-in parameter validation through Pydantic
Reduced boilerplate compared to manual schema writing
Type safety and IDE support for development

The MCP Python SDK transforms what used to be a complex process of writing tool definitions into something that feels natural for Python developers. You focus on the business logic while the SDK handles the protocol details.

---

## 🎬 Transcript (English)

Let's start to make an MCP server for our CLI chatbot. As you saw, the CLI itself already works, and we can already chat with Claude, but there's no additional functionality around the MCP server tied to it just yet. So we're going to work on adding in this MCP server that is going to have two tools in it for right now. It's going to have one tool to read a document and one tool to update the contents of a document. The implementation of the server is going to be placed into the MCP server.py file inside of the root project directory. Inside of here, I've already gone through a little bit of work to set up a basic MCP server. And then I defined a collection of documents that are going to exist only in memory. And then finally, I put together some different to-do items. So these are different tasks that you and I are going to complete inside of this file. For right now, as I just mentioned, we're going to be working only on these first two items, writing out two tools. Now we have authored tools in the past, and we saw that, oh, there's a lot of syntax there. There's those big JSON schemas. But I got good news for you here. In this project, we're making use of the official MCP Python SDK. So that's what this MCP packages we're making use inside of here. This MCP package is going to create our MCP server for us with just one line of code, like what you see right there. This SDK also makes it really easy to define tools. To define a tool, all we have to do is write out what you see on the right-hand side over here. This will make a tool named add integers with this description and two arguments that are going to be required to be passed into it. Once we write out a tool definition like this, behind the scenes, MCP is going to generate a tool JSON schema for us, which we can take and pass off to Claude. So right away, as you can see, it starts to get a lot easier to do some basic things like defined tools. Now, as I mentioned, our first task is going to be to implement these two different tools. So let's go back over to our MCP server.py file right away, and we're going to start to implement the first tool of reading a document. So the only goal here is to take in the name of some document and return the contents of it. All of our documents are already placed inside of this docs dictionary. The keys are the IDs or essentially names of a document, and the value is a document's contents. So our tool is really simple. We're going to take in one of these strings, look up the appropriate value inside this docs dictionary, and then return it. That's all we need to do. So to implement this, I'm going to find the first to do and right underneath it, I'm going to define a new tool by writing out at mcp.tool. I'm going to give this tool a name of read_contents and a description of read the contents of a document and return it as a string. And remember, in a perfect world, we put in a really fleshed out description right here to make sure it's super clear to Claude, exactly when to use this tool. But right now, just as usual, to save a little bit of time and keep you from having to type out a bunch of text here, I'm just going to leave in a very simple description. then I will define my actual tool function. So this is the function to run whenever we decide to run this tool. I will call it read_document. It's going to take in a argument of doc_id that is going to be a string. I'm going to set that to a field with a description of ID of the document to read. And then we need to make sure that we import this field class at the top. So I'm going to go up to the top and add an import from pydantic import field. then back down here inside of the function body, I'm going to put in my actual implementation. So the first thing I'm going to do is just make sure I handle the case in which Claude asks for a document that doesn't actually exist. So I'll say if doc_id not in docs. So in other words, if the provided document ID is not found as a key inside of this dictionary, then I'm going to raise a value error with an f-string of "doc with id {doc_id} not found". ID not found. And then if we get past that check, I'll go ahead and return the actual document. So I'll return docs[doc_id]. And that's it, that's all it takes to define a tool. So we've specified the name of the tool, its description, the argument that is expected, its type, and a description for that argument as well. All these different decorators and field types and whatnot are all going to be taken together by this Python MCP SDK, and it's going to generate a JSON schema for us. Now that we've implemented this first tool, I'm going to remove the to-do right there. And then we will implement our other tool, the one to edit a document. So we're going to repeat the exact same process. I'll say MCP dot tool. I'll give it a name of edit_document with a description of edit a document by replacing a string in the documents context or semi content with a new string. Then for the implementation, I'll call this function edit_doc. Or so we'll be consistent, call edit_document. And then we're going to take in a couple of different arguments here. First is going to be a document ID and then a old string to find and then a new string to replace the old string with. So let's write this all out. We're going to have a doc_id. That will be a string with a description of ID of the document. that will be edited. old_string will be a string with a description of the text to replace must match exactly including white space. And then our new_string. the new text to insert in place of the old text. So our document editing here is just a very simple find and replace. That's it. Once again, inside of here, I'm going to make sure that Claude is asking for a document that actually exists. So if doc_id not in docs, raise value_error with an f-string of "doc with id {doc_id} not found". And then if we do find the correct document, here's how we will do our edit. We'll say docs [doc_id] = docs[doc_id]. replace(old_string, new_string). And that's it. All right. So just like that, we have put together two tool implementations really, really quickly. I can't repeat it enough defining tools with this MCP Python SDK is a lot easier than writing out the schema definition manually. Now that we've got both tools put together, I'm going to delete the Tudu right there. Okay, so this is a good start. We have put together our MCP server and we've implemented two tools inside of it.

---

## 🎬 トランスクリプト（日本語）

MCPサーバーを作り始めましょう。私たちの CLIチャットボット用です。ご覧の通り、 CLI自体はすでに動作しており、チャットもできます。 Claudeとですが、MCPの周りに追加機能はありません。 現時点ではサーバーはまだ接続されていません。そこで作業するのは、 このMCPサーバーに追加することです。このサーバーには2つのツールが 含まれます。現時点では、ドキュメントを読み取るためのツールが1つと、 ドキュメントの内容を更新するためのツールが1つです。 サーバーの実装は、MCPの MCP server.py ファイルに配置されます。プロジェクトのルート ディレクトリの中にあります。このファイルの中には、すでに少し 作業をして、基本的なMCPサーバーをセットアップしました。そして 、存在するドキュメントのコレクションを定義しました。これらは メモリ上にのみ存在します。そして最後に、いくつかの 異なるタスクアイテムをまとめました。これらは、あなたが と私がこのファイル内で完了する、異なるタスクです。 現時点では、先ほど述べたように、最初の 2つのアイテム、つまり2つのツールを作成することに焦点を当てます。 私たちは過去にツールを作成したことがありますし、それを 見てきました。ああ、そこに多くの構文がありますね。あの大きなJSON スキーマです。しかし、あなたに良いニュースがあります。この プロジェクトでは、公式のMCPを Python SDKを利用しています。ですから、このMCP パッケージがそれです。私たちはここでそれを利用しています。この MCPパッケージは、わずか1行のコードでMCPサーバーを 作成してくれます。そこで見ているもののようなものです。この SDKはまた、ツールを定義することを 非常に簡単にします。ツールを定義するために、私たちがすべきことは、右側で 見ているものを記述することだけです。これは、 add integersという名前のツールを作成し、この説明と 2つの引数を持っており、これらは必須で渡される必要があります。 これらの引数です。このようなツール定義を作成したら、 バックグラウンドでは、MCPが ツールJSONスキーマを生成してくれます。これを 取得してClaudeに渡すことができます。 ですから、すぐにわかるように、基本的なことを定義するのがずっと簡単になります。 例えば、ツールを定義することです。さて、先ほど 述べたように、私たちの最初のタスクは、これらの2つの 異なるツールを実装することです。MCP server.py ファイルに戻りましょう。そして、最初の ツール、つまりドキュメントを読み取るツールを実装し始めます。 ここでの唯一の目標は、ドキュメントの名前を取得し、 その内容を返すことです。私たちのドキュメントはすべて、 この`docs`辞書の中にすでに配置されています。 キーはドキュメントのID、つまり本質的には名前であり、 値はドキュメントの内容です。 ですから、私たちのツールは非常にシンプルです。これらの文字列の1つを受け取り、 この辞書内の適切な値を探し、それを返します。それだけです。 ですから、これを実装するために、 最初のto-doを見つけて、そのすぐ下に 新しいツールを定義します。`@` mcp.tool`と書いて。 このツールに `read_contents` という名前を付け、 説明は「ドキュメントの内容を読み取り、 文字列として返す」とします。そして 、理想的な世界では、Claudeにいつこのツールを使うべきかを 明確にするために、非常に詳細な説明をここに含めます。 しかし現時点では、いつものように、 時間を節約し、タイプ入力の手間を省くために、 非常にシンプルな説明のままにしておきます。その後、実際の ツール関数を定義します。これは、このツールを実行することに なったときに実行される関数です。 `read_document`と呼びます。 これは `doc_id` という引数を取ります。 これは文字列で、説明は 「読み取るドキュメントのID」とします。 そして、このフィールドクラスを一番上にインポートする必要が あります。ですから、一番上に行ってインポートを追加します。 `from pydantic import field`。 その後、関数の本体に戻って、実際の処理を記述します。 まず、実際には存在しないドキュメントをClaudeが要求した場合の ケースを処理するようにします。 ですから、もし `doc_id` が `docs` の中にない場合、つまり提供された ドキュメントIDがこの辞書内にキーとして見つからない場合、 `ValueError` を発生させます。 f-stringで「doc with id {doc_id} not found」とします。 見つかりません。そして 、このチェックを通過した場合、実際の ドキュメントを返します。`docs[doc_id]`を返します。 これで完了です。ツールを定義するには、これだけが必要です。 ツールの名前、その説明、 期待される引数、その型、 そしてその引数の説明も指定しました。 これらのデコレータやフィールド型などはすべて、 このPython MCP SDKによって取得され、JSON スキーマを生成します。この最初のツールを実装したので、 そこにあるto-doを削除します。 そして、もう一方のツール、つまりドキュメントを編集するツールを実装します。 全く同じプロセスを繰り返します。`@` mcp.tool`と書きます。`edit_document`という名前を付け、 説明は「ドキュメントを編集し、 ドキュメントの内容内の文字列を新しい文字列で 置き換える」とします。 実装としては、この関数を `edit_doc` と呼びます。 一貫性を保つために、`edit_document`と呼びましょう。そして 、ここでいくつかの引数を取ります。まず 、ドキュメントID、そして置換する古い文字列、 そして古い文字列を置き換える新しい文字列です。これらをすべて 書き出しましょう。`doc_id` があり、 それは文字列で、説明は「編集される ドキュメントのID」となります。 `old_string` は文字列で 、説明は「置換するテキストで、 空白文字を含めて正確に一致する必要があります。」とします。 そして `new_string` は 、古いテキストの代わりに挿入する新しいテキストです。 ですから、私たちのドキュメント編集は 非常にシンプルな検索と置換です。それだけです。 ここでは、Claudeが実際に存在するドキュメントを 要求していることを確認します。ですから、もし `doc_id` が `docs` にない場合は、 f-stringで「doc with id {doc_id} not found」と `ValueError` を発生させます。 正しいドキュメントが見つかった場合、ここでは編集を行います。`docs` `[doc_id]` を `docs[doc_id]` の `replace(old_string, new_string)` で更新します。 これで完了です。 このようにして、私たちは2つのツール実装を 非常に迅速に作成しました。何度でも言いますが、このMCP Python SDKでツールを定義することは、 手動でスキーマ定義を書くよりもはるかに簡単です。 両方のツールが完成したので、そこにあるto-doを削除します。 これは良いスタートです。MCPサーバーを作成し、 その中に2つのツールを実装しました。
