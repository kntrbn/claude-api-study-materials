# 68. Defining prompts

**URL:** https://anthropic.skilljar.com/claude-with-the-anthropic-api/287784
**Section:** 09 Model Context Protocol

---

## 📄 Page Content

Anthropic Academy
    
  

  
    
      Courses
    
  

    

    
      
      

      
        
          My Profile
        
        
      

      
      

      
        Sign Out
      
    
  

  

  

    
    
    
        
            
    
        
    

            
    
        
        
            
                
                    
                        
                            
                                
                            

                            
                                details
                            

                            
                        
                    
                
            
            
                
                
                
                    Defining prompts
                    
                
                
                    
                        
                            
                                
                                    

    
    

    
    
        
            
        
        
            
                
                This video is still being processed. Please check back later and refresh the page.
            
        
        
            
                Uh oh! Something went wrong, please try again.
            
        
    

    

                                
                            
                        
                    
                
            
        
        
            

    
        
            
                
                    
                        
                            
                        
                    
                
            
            
                
                    Summary
                

                

            
        

        
            
                
                    
                        
                            Summary

                            
                                Prompts in MCP servers let you define pre-built, high-quality instructions that clients can use instead of writing their own prompts from scratch. Think of them as carefully crafted templates that give better results than what users might come up with on their own.

Why Use Prompts?

Let's say you want Claude to reformat a document into markdown. A user could just type "convert report.pdf to markdown" and it would work fine. But they'd probably get much better results with a thoroughly tested prompt that includes specific instructions about formatting, structure, and output requirements.

The key insight is that while users can accomplish these tasks on their own, they'll get more consistent and higher-quality results when using prompts that have been carefully developed and tested by the MCP server authors.

How Prompts Work

Prompts define a set of user and assistant messages that clients can use directly. When a client requests a prompt, your server returns a list of messages that can be sent straight to Claude.

The basic structure looks like this:

Define prompts using the @mcp.prompt() decorator
Add a name and description for each prompt
Return a list of messages that form the complete prompt
These prompts should be high quality, well-tested, and relevant to your MCP server's purpose

Building a Format Command

Here's how to implement a document formatting prompt. First, you'll need to import the base message types:

from mcp.server.fastmcp import base

Then define your prompt function:

@mcp.prompt(
    name="format",
    description="Rewrites the contents of the document in Markdown format."
)
def format_document(
    doc_id: str = Field(description="Id of the document to format")
) -> list[base.Message]:
    prompt = f"""
Your goal is to reformat a document to be written with markdown syntax.

The id of the document you need to reformat is:

{doc_id}

Add in headers, bullet points, tables, etc as necessary. Feel free to add in extra formatting.
Use the 'edit_document' tool to edit the document. After the document has been reformatted...
"""
    
    return [
        base.UserMessage(prompt)
    ]

Testing Your Prompts

You can test prompts using the MCP Inspector. Navigate to the Prompts section, select your prompt, and provide any required parameters. The inspector will show you the generated messages that would be sent to Claude.

This lets you verify that your prompt interpolates variables correctly and produces the expected message structure before using it in a real application.

Best Practices

When creating prompts for your MCP server:

Focus on tasks that are central to your server's purpose
Write detailed, specific instructions rather than vague requests
Test your prompts thoroughly with different inputs
Include clear descriptions so users understand what each prompt does
Consider how the prompt will work with your server's tools and resources

Remember that prompts are meant to provide value that users couldn't easily get on their own - they should represent your expertise in the domain your MCP server covers.

---

## 🎬 Transcript (English)

Last major focus we're going to have inside of our MCP server is going to be on prompts. Once again, just like we did with resources, we're going to implement a small feature inside of our project. And we're going to use this feature to understand what prompts are all about, just like we did with resources a moment ago. Let me tell you about the feature we're going to add into our program. We're going to add in support for slash commands. So for example, I want to have a format command. I've got some screenshots over here of how it's going to work. Whenever user types into slash, we're going to list out some number of commands that are supported by our application. For right now, we're going to have just one command called format. So if I type in just slash, I should see a little autocomplete right here, and the only autocomplete option should be format. If I then select Format, I should be prompted to add in some document ID after it. So one of our different document names like report.pdf or whatever else. Then whenever user runs this command, the goal is to get Claude to reformat this document using Markdown syntax. So in other words, take the plain string that we have without any special formatting tied to it inside of each of our documents right now. Remember, inside of our MCP server, our current document content is just plain text. We want to feed this into Claude and somehow get Claude to rewrite it using Markdown syntax. So I would expect to see some output like this, something that says, I'll help you reform out the document. Claude is then going to use a tool to read the contents of the document. And then finally, inside the final response, I want to see the content of that document rewritten down here in Markdown syntax. Now, there's something interesting about this feature that I want to point out. The real core of this feature, like the real goal here, is to allow a user to reformat a document into Markdown syntax. And that is an operation that actually doesn't require you and I, the developers, to write out any code to implement. What do I mean by that? Well, a user can already launch our CLI and say something like reformat the report.pedia file in markdown syntax. I use your can already do this. No issue whatsoever. And Claude is going to do a reasonable job of it. It's going to take the contents of our document and reformat it into markdown. And as you can see right here, it worked entirely perfectly. So what are we really doing with this feature? Well, the thought process here is that if we just left this up to users and allowed them to manually type in something like convert this to Markdown, they might get a OK result, but they might get much better result if they had a really strong prompt that is custom tailored for this particular scenario of converting a document into Markdown. So a user might be a lot happier if you and I sat down as the MCP server authors and wrote out and tested and evaluated and went through the entire process of evaluating our really thorough, fantastic prompts like the one you see on the right hand side. So again, just repeat, yes, a user can execute this entire workflow on their own, but if they use this fancy prompt over here, instead, well, I think they would be all the better. This is the real goal of the prompts future inside of MCP servers. The thought here is that ahead of time, we can define a set of prompts inside of our server that are custom tailored to whatever our server is really specialized to do. In our case, our server is all about managing documents, reading documents, editing documents, and so on. So we might decide to add in a set of prompts that are very high quality that have been evaluated and tested, and we know that they work in a wide variety of different scenarios. We can then expose these prompts for use inside of any client application, like the CLI app that we are putting together right now. Now, one thing I want to point out here is that we could develop this prompt and just put it directly into our CLI code base. That is totally possible. We could do that, obviously. But again, the thought here is that your MCP server that might specialize in some particular task might expose some number of prompts that people can just come and use without having to worry about developing them ahead of time. To define a prompt inside of our MCP server, we're going to write out a little bit of syntax very similar to the tools and resources we have already put together. We will use the prompt decorator. We'll add a name to the prompt and optionally a description as well. Then whenever the client asks for this prompt, we'll send back a list of messages. These are actual user and assistant messages. So we can take the messages and send them off to Claude directly. All right, so let's go over to our server, and we're gonna try putting together our own prompt. And just like you see right here, it's gonna be all about taking the contents of a document and somehow rewriting it in Markdown format. Okay, so back inside my editor, I'm gonna find my MCP server file. I'm gonna go down a little bit to the comment about rewriting a document in Markdown format. I'll delete that to do, and then I'll add in a MCP prompt, the name of format, and a description of rewrites the contents of the document in Markdown format. I'll then add in an actual implementation. So format document, I can receive as an argument a doc ID, and then optionally we can add in a field description here as well, just like we did with our tool earlier on. So I can optionally add in a field with a description of ID of the document to format. And I'm also going to add in a type annotation of string. Just make sure that's really clear as well. From this function, we are going to return a list of messages. I'm going to make sure I add in an import for this base thing at the top right away. So right underneath the existing MCP server import, I will add in from MCP server fast MCP prompts import base. then back down at the bottom. Inside of here, we're going to define our very well-tested, very well-evaluated prompt. I wrote a prompt out ahead of time. I'm going to paste it in like so. So this prompt is just asking Claude to take in a document ID. Implicitly, we are kind of asking Claude to fetch the document ID's contents using the redocument tool. And then after getting that document, just go ahead and rewrite it with Markdown syntax. And finally, after rewriting it, edit the document as well to save those updates inside of our server. Now, after defining this prompt, we're then going to return a list of messages. So down here, I'm going to return a list with base user message, and I'm going to feed in our prompt that we just wrote out to it, like so. Now I'm going to save this file, and then let's go start up our MCP development inspector and test out this prompt from that interface. So at my terminal, I'll run that same command again, and then navigate to that address inside of my browser. I'll make sure I connect to my server. I'll then find the prompts section. I'm going to list out all the different prompts that are available to us. And at this point in time, we have one prompt, just format. So I click on format, and then I have to enter in a document ID right here. Let's, this time around, maybe we'll put in a document ID of how about outlook.pdf. So I'll put that in. And then get prompt. And then here is our list of messages. So these have been put together ahead of time. I've got one message part here. So a text part with our full prompt right there. We could see that the document ID was interpolated into it. Now that we have these messages, we can send them off to Claude. and hopefully we're going to get back some appropriate kind of response. So once again, the entire idea here behind these prompts, we might implement inside of our MCP server, is that the prompts we are defining are going to be well-tested, well-evaluated, really specialized to one particular use case.

---

## 🎬 トランスクリプト（日本語）

私たちがMCPサーバー内で持つ最後の大きな焦点は プロンプトになります。リソースの場合と同様に 小さな機能を実装します。 そして、この機能を使って プロンプトがどのようなものかを理解します。リソースについても 先ほどそうしたように。プログラムに追加する機能についてお話ししましょう。 スラッシュコマンドのサポートを追加します。 例えば フォーマットコマンドがあるとします。その動作方法についてのスクリーンショットがここにいくつかあります。 ユーザーがスラッシュを入力すると、いくつかの コマンドが表示されます。これらはアプリケーションでサポートされているコマンドです。 現時点では、フォーマットという一つのコマンドのみとします。 スラッシュだけを入力した場合、小さなオートコンプリートが ここで表示されるはずです。そして、唯一のオートコンプリートオプションはフォーマットです。 その後フォーマットを選択すると、ドキュメントIDの入力を促されます。 例えば report.pdfのようなドキュメント名のいずれかです。 あるいは他のものでも。 ユーザーがこのコマンドを実行すると 目標は、Claudeに このドキュメントをMarkdownシンタックスで 再フォーマットさせることです。つまり、プレーンな 文字列を取り出し 特別なフォーマットなしで、各ドキュメント内の 私たちのMCPサーバー内では、現在のドキュメント コンテンツは単なるプレーンテキストです。それを Claudeに渡し、Claudeに Markdownシンタックスで書き直させるようにします。 だから、以下のような出力が表示されるはずです。「ドキュメントを再フォーマットします。 Claudeはその後、ツールを使って ドキュメントの内容を読み取ります。 そして最終的なレスポンスで、ドキュメントの内容が Markdownシンタックスでここに書き直されているのを見たいです。 この機能には興味深い点があります。 この機能の本当の核心、つまり本当の目標は ユーザーがドキュメントを Markdownシンタックスに再フォーマットできるようにすることです。 そしてそれは、開発者である私たちに コードを書かせる必要のない操作です。 それはどういう意味でしょうか？ ユーザーはすでに CLIを起動して、リフォーマットして report.pediaファイルを Markdownシンタックスで行うように言えます。 ユーザーはすでにこれを行うことができます。全く問題ありません。 そしてClaudeはそれを適切に処理します。ドキュメントの 内容を取り出し、Markdownに再フォーマットします。 そしてご覧のように、完全にうまくいきました。 では、この機能で具体的に何をしているのでしょうか？ ここでの考え方は、もしこれをユーザーに任せて 手動で何かを入力させるだけだと 「Markdownに変換して」のような結果はまあまあかもしれませんが より良い結果が得られるかもしれません もしカスタムされた強力なプロンプトがあれば この特定シナリオ、つまりドキュメントを Markdownに変換するための、カスタム化されたプロンプトがあれば。 ですから、ユーザーはもっと満足するかもしれません もし私たち、MCPサーバーの作成者が 時間をかけて、テスト、評価し、評価プロセス全体を通して 右側にあるような、非常に徹底した、素晴らしいプロンプト を作成すれば。 繰り返しますが、ユーザーは自分の力でこのワークフロー全体を実行できますが 代わりにこの派手なプロンプトを使うと より良くなるでしょう。 これがMCPサーバー内のプロンプト機能の本当の目標です。 考え方は、 事前にサーバー内に一連のプロンプトを定義できるということです。 私たちのサーバーが専門としていることに合わせて カスタム化されたものです。私たちの場合は ドキュメントの管理、読み取り、 編集などです。そのため 高品質で、評価・テスト済みの プロンプトのセットを追加するかもしれません。 そして、それらが様々なシナリオで機能することがわかっているプロンプトです。 これらのプロンプトを、 クライアントアプリケーションから使用できるように公開できます。 現在作成中のCLIアプリのような。 ここで指摘したいのは、このプロンプトを開発して CLIのコードベースに直接組み込むこともできるということです。 それは完全に可能です。もちろん、そうすることもできます。 しかし、ここでの考え方は、特定のタスクに 特化したMCPサーバーが 人々が開発の手間をかけずに利用できる プロンプトを公開する可能性があるということです。 MCPサーバー内にプロンプトを定義するには ツールやリソースと同様の簡単なシンタックスを記述します。 プロンプトデコレーターを使用します。 プロンプトに名前を付け、オプションで説明も追加します。 その後、クライアントがこのプロンプトをリクエストすると メッセージのリストを返します。 これらは実際のユーザーとアシスタントのメッセージです。 だから、メッセージを受け取ってClaudeに直接送信できます。 さて、サーバーに移りましょう。 独自のプロンプトを作成してみましょう。 そして、ご覧のように、ドキュメントの内容を Markdownフォーマットで書き直すことになります。 OK、エディタに戻ります。 MCPサーバーファイルを見つけます。 ドキュメントをMarkdownフォーマットで書き直すというコメントまで下にスクロールします。 そのTODOを削除し、 MCPプロンプトを追加します。 名前はフォーマット、 説明は「ドキュメントの内容を Markdownフォーマットで書き直します」とします。 そして実際の機能を実装します。 フォーマットドキュメントでは、引数として doc IDを受け取ることができます。 そしてオプションでフィールドの説明も追加できます。 さっきツールでしたように。 ですから、オプションでフィールドを追加できます。 ドキュメントのIDをフォーマットするための説明付きのフィールドです。 そして型注釈も文字列として追加します。 それを明確にしておきます。この関数から メッセージのリストを返します。 これは、この基本クラスのインポートを すぐに追加します。 MCPサーバーのインポートのすぐ下に、 MCPサーバーファストMCPから プロンプトをインポートします。ベース、そして 再び下に戻って、ここに、 非常にテストされ、評価されたプロンプトを定義します。 事前にプロンプトを作成しました。ここに貼り付けます。 このプロンプトはClaudeに ドキュメントIDを受け取るように求めています。暗黙的に、 ドキュメントIDの コンテンツをredocumentツールを使って取得するように求めています。 そしてそのドキュメントを取得した後、単にMarkdownシンタックスで書き直してください。 そして書き直した後、ドキュメントを編集して サーバー内にその変更を保存します。 このプロンプトを定義した後、 メッセージのリストを返します。 ベースユーザーメッセージでリストを返します。 そして作成したばかりのプロンプトを 渡します。 ファイルを保存し、MCP開発インスペクターを起動して そのインターフェースからこのプロンプトをテストしましょう。 ターミナルで同じコマンドをもう一度実行し ブラウザのアドレスに移動します。 サーバーに接続していることを確認します。 プロンプトセクションを見つけます。 利用可能なプロンプトをすべてリスト表示します。 そして現時点では、フォーマットというプロンプトが1つあります。 フォーマットをクリックすると ドキュメントIDを入力する必要があります。 今回は、Outlook.pdfという ドキュメントIDを入れてみましょう。 それを入力して、プロンプトを取得します。 そしてここにメッセージのリストがあります。 これらは事前に作成されています。メッセージ部分が1つあります。 テキスト部分に 完全なプロンプトがあります。 ドキュメントIDが挿入されているのがわかります。 これらのメッセージが得られたので、Claudeに送信できます。 そして、適切な応答が得られることを期待しましょう。 もう一度言うと、これらのプロンプトの背後にある全体的な考え方は MCPサーバー内に実装するものは 定義するプロンプトは、テスト済みで 評価済みで、特定の ユースケースに特化していることです。
