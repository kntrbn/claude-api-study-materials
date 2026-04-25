# 69. Prompts in the client

**URL:** https://anthropic.skilljar.com/claude-with-the-anthropic-api/287786
**Section:** 09 Model Context Protocol

---

## 📄 Page Content

Anthropic Academy
    
  

  
    
      Courses
    
  

    

    
      
      

      
        
          My Profile
        
        
      

      
      

      
        Sign Out
      
    
  

  

  

    
    
    
        
            
    
        
    

            
    
        
        
            
                
                    
                        
                            
                                
                            

                            
                                details
                            

                            
                        
                    
                
            
            
                
                
                
                    Prompts in the client
                    
                
                
                    
                        
                            
                                
                                    

    
    

    
    
        
            
        
        
            
                
                This video is still being processed. Please check back later and refresh the page.
            
        
        
            
                Uh oh! Something went wrong, please try again.
            
        
    

    

                                
                            
                        
                    
                
            
        
        
            

    
        
            
                
                    
                        
                            
                        
                    
                
            
            
                
                    Summary
                

                

            
        

        
            
                
                    
                        
                            Summary

                            
                                Prompts in MCP define a set of user and assistant messages that can be used by the client. These prompts should be high quality, well-tested, and relevant to the overall purpose of the MCP server.

Implementing List Prompts

The first step is implementing the list_prompts method in your MCP client. This method retrieves all available prompts from the server:

async def list_prompts(self) -> list[types.Prompt]:
    result = await self.session().list_prompts()
    return result.prompts

This simple implementation calls the session's list_prompts method and returns the prompts array from the result.

Getting Individual Prompts

The get_prompt method retrieves a specific prompt with arguments interpolated into it. When you request a prompt, you provide arguments that get passed to the prompt function as keyword arguments:

async def get_prompt(self, prompt_name, args: dict[str, str]):
    result = await self.session().get_prompt(prompt_name, args)
    return result.messages

The method returns the messages from the result, which form a conversation that can be fed directly into Claude.

How Prompt Arguments Work

When you define a prompt function on the server side, it can accept parameters. For example, a document formatting prompt might expect a doc_id parameter:

def format_document(doc_id: str):
    # The doc_id gets interpolated into the prompt

When the client calls get_prompt, the arguments dictionary should contain the expected keys. The MCP server will pass these as keyword arguments to the prompt function, allowing dynamic content to be inserted into the prompt template.

Testing Prompts in the CLI

Once implemented, you can test prompts through the command-line interface. When you type a forward slash, available prompts appear as commands. Selecting a prompt may prompt you to choose from available options (like document IDs), and then the complete prompt gets sent to Claude.

The workflow looks like this:

User selects a prompt (like "format")
System prompts for required arguments (like which document to format)
The prompt gets sent to Claude with the interpolated values
Claude can then use tools to fetch additional data and complete the task

Prompt Best Practices

When creating prompts for your MCP server:

Make them relevant to your server's purpose
Test them thoroughly before deployment
Use clear, specific instructions
Design them to work well with your available tools
Consider what arguments users will need to provide

Prompts bridge the gap between predefined functionality and dynamic user needs, giving Claude structured starting points for complex tasks while maintaining flexibility through parameterization.

---

## 🎬 Transcript (English)

Our last major task is to implement some functionality inside of our MCP client and allow us to list out all the different prompts that are defined inside the MCP server and also get a particular prompt with some variables interpolated into it. So let's first implement list prompts. I will delete the comment and replace it with a result is await, self, session, list prompts, and then I will return result dot prompts. And that's pretty much it. And then get prompt. Now to be clear, when we get a individual prompt, we're going to be given some number of arguments. These arguments will eventually show up inside of our prompt function. So for example, inside a format document right here, we expect to receive a document ID. Inside of this args dictionary, the expectation is that there will be a document ID key. And that will be passed in to the appropriate function over here. And then we will get that value interpolated into the prompt itself. So inside the get prompt function, I will get a result from self session, get prompt. I'm going to pass in the prompt name. That's the name of the prompt I want to retrieve. And then I'll pass in the arguments. And then I will return result dot messages. So those are the messages coming back. They form some kind of conversation that we want to feed directly into Claude. And that's it. That's all we have to do for our client. So now we can test this out inside of the CLI itself. I'll flip back over, run the project again. And now if I put in a slash right here, I'll see that I can access this format command. Now format is really just the name of the prompt that we're going to invoke. So if I select that and then hit space, I'll then be asked to select one of the different documents and you'll go with plan.md. I'll hit enter. And then we're taking that entire prompt, really just that single user message, and feeding it directly into Claude. So Claude now has the instructions to go and reformat a document into Markdown syntax. And it has also been given the ID of the document that we want to reformat. So the first thing it needs to do here is go and fetch that document's contents. And it will do so by using the Git document tool. And then finally, Claude is going to respond with the markdown version of this document. So here is the document with a bunch of markdown syntax inside of it. All right, since it looked like this work just fine, let's do a quick recap on prompts and make sure we understand what they are all about. We begin by writing out an e-evaluating a prompt that has some relevancy to our MCP server's purpose. In our case, we were making a document server. So having some functionality or something about rewriting a document in a different style, I think it kind of makes sense. Once we have put our prompt together, we'll define a prompt inside the MCP server. And then our client can ask for that prompt at any point in time. When we ask for the prompt, we will put in some number of arguments that will be provided to this prompting function right here as keyword arguments. And then our function can make use of those keyword arguments inside the prompt itself.

---

## 🎬 トランスクリプト（日本語）

私たちの次の主なタスクは、MCPクライアント内にいくつかの機能 を実装し、MCPサーバー内に定義されているさまざまなプロンプトを リスト表示できるようにし、 また、特定のプロンプトに変数を埋め込んで取得できるようにすることです。 まず、プロンプトのリスト機能を実装しましょう。 コメントを削除し、result は await, self, session, list prompts に置き換えます。そして result.prompts を返します。 それがほぼすべてです。 そして、get prompt です。明確にしておくと、 個別のプロンプトを取得する場合、いくつかの引数が与えられます。 これらの引数は、最終的にプロンプト関数内に表示されます。 例えば、format document の中では、 document ID を受け取ることを期待しています。 この args の辞書の中では、document ID というキーがあり、それが適切な関数に渡されます。 そして、その値を取得してプロンプト自体に埋め込みます。 したがって、get prompt 関数内では、 result は self session, get prompt から取得します。 取得したいプロンプトの名前であるプロンプト名を渡します。そして引数も渡します。 そして、result.messages を返します。 それらがメッセージです。 それらは、私たちが Claude に直接フィードしたい会話を形成します。 それがすべてです。これがクライアントのために行うすべてです。 これで、CLI 自体でこれをテストできます。 プロジェクトをもう一度実行します。 そして今、ここにスラッシュを入力すると、 format コマンドにアクセスできることがわかります。 format は、実際に呼び出すプロンプトの名前です。 それを選択してスペースをヒットすると、 さまざまなドキュメントの 1 つを選択するように求められます。 そして plan.md を選択します。Enter キーを押します。 そして、このプロンプト全体を、実際には この単一のユーザーメッセージを Claude に直接フィードします。 Claude は今、 ドキュメントを Markdown 構文にリフォーマットするように指示されています。 そして、リフォーマットしたいドキュメントの ID も与えられています。 ですから、まずここで行う必要があるのは、 そのドキュメントの内容を取得することです。 そして、Git ドキュメントツールを使用してそれを行います。 そして最終的に、Claude はこのドキュメントの Markdown バージョンで応答します。 ここに Markdown 構文が含まれたドキュメントがあります。 さて、これはうまくいったようなので、 プロンプトの簡単な復習をして、それが何であるかを理解していることを確認しましょう。 まず、MCP サーバーの目的に関連性のある プロンプトを評価して記述します。 私たちの場合は、ドキュメントサーバーを作成していました。 したがって、ドキュメントを別のスタイルに書き直す機能や 何かがあるのは、理にかなっていると思います。 プロンプトを作成したら、MCP サーバーでプロンプトを定義します。 そして、クライアントはいつでもそのプロンプトを要求できます。 プロンプトを要求するとき、いくつかの引数を渡します。 それらはこのプロンプト関数にキーワード引数として提供されます。 そして、私たちの関数は、プロンプト自体の これらのキーワード引数を利用できます。
