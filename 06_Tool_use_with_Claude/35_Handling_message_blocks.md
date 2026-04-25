# 35. Handling message blocks

**URL:** https://anthropic.skilljar.com/claude-with-the-anthropic-api/287757
**Section:** 06 Tool use with Claude

---

## 📄 Page Content

Anthropic Academy
    
  

  
    
      Courses
    
  

    

    
      
      

      
        
          My Profile
        
        
      

      
      

      
        Sign Out
      
    
  

  

  

    
    
    
        
            
    
        
    

            
    
        
        
            
                
                    
                        
                            
                                
                            

                            
                                details
                            

                            
                        
                    
                
            
            
                
                
                
                    Handling message blocks
                    
                
                
                    
                        
                            
                                
                                    

    
    

    
    
        
            
        
        
            
                
                This video is still being processed. Please check back later and refresh the page.
            
        
        
            
                Uh oh! Something went wrong, please try again.
            
        
    

    

                                
                            
                        
                    
                
            
        
        
            

    
        
            
                
                    
                        
                            
                        
                    
                
            
            
                
                    Summary
                

                

            
        

        
            
                
                    
                        
                            Summary

                            
                                When working with Claude's tool functionality, you'll encounter a new type of response structure that's different from the simple text responses you've seen before. Instead of just getting back a single text block, Claude can now return multi-block messages that contain both text and tool usage information.

Making Tool-Enabled API Calls

To enable Claude to use tools, you need to include a tools parameter in your API call. Here's how to structure the request:

messages = []
messages.append({
    "role": "user",
    "content": "What is the exact time, formatted as HH:MM:SS?"
})

response = client.messages.create(
    model=model,
    max_tokens=1000,
    messages=messages,
    tools=[get_current_datetime_schema],
)

The tools parameter takes a list of JSON schemas that describe the available functions Claude can call.

Understanding Multi-Block Messages

When Claude decides to use a tool, it returns an assistant message with multiple blocks in the content list. This is a significant change from the simple text-only responses you've worked with before.

A multi-block message typically contains:

Text Block - Human-readable text explaining what Claude is doing (like "I can help you find out the current time. Let me find that information for you")
ToolUse Block - Instructions for your code about which tool to call and what parameters to use

The ToolUse block includes:

An ID for tracking the tool call
The name of the function to call (like "get_current_datetime")
Input parameters formatted as a dictionary
The type designation "tool_use"

Managing Conversation History with Multi-Block Messages

Remember that Claude doesn't store conversation history - you need to manage it manually. When working with tool responses, you must preserve the entire content structure, including all blocks.

Here's how to properly append a multi-block assistant message to your conversation history:

messages.append({
    "role": "assistant",
    "content": response.content
})

This preserves both the text block and the tool use block, which is crucial for maintaining the conversation context when you make subsequent API calls.

The Complete Tool Usage Flow

The tool usage process follows this pattern:

Send user message with tool schema to Claude
Receive assistant message with text block and tool use block
Extract tool information and execute the actual function
Send tool result back to Claude along with complete conversation history
Receive final response from Claude

Each step requires careful handling of the message structure to ensure Claude has the full context it needs to provide accurate responses.

Updating Helper Functions

If you've been using helper functions like add_user_message() and add_assistant_message(), you'll need to update them to handle multi-block content. The current versions likely only support single text blocks, but now they need to accommodate the more complex content structures that include tool use blocks.

This multi-block message handling is essential for building robust applications that can seamlessly integrate Claude's tool capabilities while maintaining proper conversation flow.

---

## 🎬 Transcript (English)

On to step three, we're going to call Claude with his JSON schema and some user message. So from our server, we're going to make a request off to Claude just as we've been doing before, but now we're going to also include this tool schema. This helps Claude understand that there is a tool available to it. Let's go back over to our notebook and we're going to try to make this request by hand without using any of those helper functions we previously put together, like the chat function. Okay, so back over here, I'm going to go down and create a new cell. I'm going to make an empty list of messages. I'm going to append in there manually a new message with a role of user and a content of what is the exact time formatted as our minute seconds. Then, underneath that, I'm going to do a call off to the clientmessages.create function. So I get a response from clientmessagescreate, all designate my model, my max tokens, My list of messages, and now we want to also include this JSON schema that tells Claude that it has a tool available to it. To do so, we'll include a Tools keyword argument. This is going to be a list, and inside of it is going to be all the different JSON schema specs that we have created. At this point in time, you and I have only created one, and it's called Get Current Daytime Schema. So we're going to take that and put it in right here. Then I'm going to print out response at the very bottom and let's run this and see what happens. We're going to get a response message back here that has a structure that we have not quite seen before. All the messages that we have ever received before would have a content field that has a list and inside there would be a text block. And as I mentioned many times before inside the text block is the text that we actually want to display to the user. But now that we are making use of tools, this content list is going to be a little bit different. So you might notice that inside the content list, there's a second block called a tool use block. So here's that entire structure right here. Let me show you a diagram just to make sure this thing is really clear. Okay, so this is our first experience with a multi-block message. Remember, a message is either an assistant message or a user message. We are often going to have some amount of text stored inside of a message, and that's what we've always seen previously. But in addition to just text, there are other types of data that can be stored inside of a message. When Claude decides to make use of a tool, it's very often going to send us back an assistant message that contains both a text block and a tool use block. The text block is intended to be some text that is displayed to the user to help them understand what is going on. So in this case, the text block might contain something like, I can help you find the current time. Let me find that information for you. Then in addition to this text block is the tool use block. This tool use block is a sign to a UNI as developers that Claude wants to make use of a tool. The tool use block is going to list out the name of the tool function that it wants to call. So in this case, Claude wants to call the Get Current Daytime function we put together. And then it also provides some inputs or essentially arguments that we need to pass into that function. So the next thing we're going to do as a part of this entire process is to find the appropriate tool and actually run it. But before that, there's something really critical that we need to take care of around this idea of having a content list with multiple blocks inside of it. Okay, so here's just a quick reminder for you. At this point in time, we have made a request from our server off to Claude, and in that request we had a single user message that also included a tool schema. We have now gotten a response back. And inside this response, there is the assistant message, and it has two separate blocks inside the content list, a text block and a tool use block. Now, there's something I want to remind you about Claude. Remember that Claude does not store any message history or anything about the conversation you are having. If you ever want to maintain a conversation or a history with Claude, you have to manage it manually. And what this means is that when we eventually take this tool use block and eventually call some actual function, we need to eventually respond back to Claude. And when we do so, here's the critical part, we need to make sure we include the entire conversation history just as we've been doing throughout the course. So we already have an idea of how to do this. The only difference this time around is that we need to make sure that we deal with messages that might have multiple blocks inside them. So let me show you how we would do this by hand. And then eventually a little bit later on inside this section, we are going to go back to our helper functions, specifically add user message and add assistant message and make sure that these can support messages that have multiple blocks inside them. Because right now they only support single text blocks. Okay, so to manage these messages, I'm going to go back down to our bottom code cell where we are currently getting our response. I'm going to take our response and make sure I append in a new assistant message to our list of messages. So I'm going to delete response right there. We'll say messages dot append. I'm going to put in a new role of assistant. And then our content is going to be the exact list of content blocks out of the response we just got back. So all we have to do is add in response dot content. There we go. So now if I print out messages and run the cell again, We should see that we end up with our user. So that's our original message right there. We now have our assistant message. And inside there is a text block and the tool use block. So now we are correctly building up our conversation history over time by including all the different blocks from all these different messages that we are collecting. So once again, I just want to remind you that we are going to eventually have to go back to the add user message and add assistant message, those two helper functions, and update them to account for dealing with multiple blocks like this.

---

## 🎬 トランスクリプト（日本語）

ステップ3に進みます。Claudeに呼び出すのは、 JSONスキーマとユーザーメッセージです。したがって、 サーバーからClaudeにリクエストを送信します。まさに これまで行ってきたようにですが、今回は このツールスキーマも追加します。これにより、Claudeは ツールが利用可能であることを理解できます。ノートブックに戻り、 このリクエストを手動で作成してみましょう。 以前に作成したヘルパー関数、例えば チャット関数などは使用しません。OK、ではこちらに戻って、 新しいセルを作成します。 空のメッセージリストを作成します。そこに 新しいロールがユーザーで コンテンツが「正確な時刻はいつですか」という メッセージを 分秒のフォーマットで手動で追加します。 その後、その下に、clientmessages.create関数を呼び出します。 なので、clientmessagescreateから応答を取得します。 モデル、最大トークン数、 メッセージリストを指定します。そして今、私たちは これらを含めたい JSONスキーマもです。これはClaudeに ツールが利用可能であることを伝えます。それを行うには、 Toolsというキーワード引数を含めます。これは リストになります。そしてその中に、私たちが作成した すべての異なるJSONスキーマの仕様が入ります。現時点で、 私たちは一つだけ作成しました。それはGet Current Daytime Schemaと呼ばれます。それを ここに挿入します。そして、最後に 応答を出力します。これを実行して何が起こるか見てみましょう。 応答メッセージが 返ってきます。これは、これまであまり見てこなかった 構造を持っています。これまで受け取ったすべてのメッセージには、 コンテンツフィールドがあり、その中にリストがあり、その中に テキストブロックが含まれていました。そして、私が何度も 説明したように、テキストブロックの中には、実際に ユーザーに表示したいテキストがあります。しかし、今 ツールを使用しているので、このコンテンツリストは 少し異なります。コンテンツリストの中に、 ツール使用ブロックと呼ばれる2番目のブロックが あることに気づくかもしれません。ここにその 全体の構造があります。このことが本当に明確になるように、 図で示しましょう。 さて、これはマルチブロックメッセージとの最初の経験です。 メッセージは、アシスタントメッセージまたはユーザーメッセージの どちらかであることを思い出してください。私たちはしばしば メッセージ内に一定量のテキストを格納しますが、それは これまで見てきたものです。しかし、テキストに加えて、 メッセージ内に格納できる他のタイプのデータもあります。 Claudeがツールを使用すると決定した場合、多くの場合、テキストブロックと ツール使用ブロックの両方を含むアシスタントメッセージを 返してきます。テキストブロックは、 ユーザーが何が起こっているかを理解するのに役立つテキストとして 意図されています。この場合、テキストブロックには、 例えば「現在の時刻を見つけるのを手伝えます。その情報を探します」といった 内容が含まれる可能性があります。次に、 このテキストブロックに加えて、ツール使用ブロックがあります。 このツール使用ブロックは、Claudeがツールを使用したいということを 開発者である皆様に知らせるためのものです。 ツール使用ブロックには、呼び出したいツール 関数の名前がリストされます。この場合、Claudeは 私たちが作成したGet Current Daytime関数を 呼び出したいと思っています。そして、その関数に 渡す必要がある入力、つまり引数も提供します。したがって、 次にやるべきことは、適切なツールを見つけて実際に実行することです。 しかしその前に、コンテンツリストが 複数のブロックを持つことに関して、非常に重要なことがあります。 それを処理する必要があります。 OK。 これは簡単なリマインダーです。 現時点で、サーバーからClaudeにリクエストを送信しました。 そしてそのリクエストには、ツールスキーマを含む単一のユーザーメッセージが ありました。そして応答を受け取りました。この応答には、 アシスタントメッセージがあり、そのコンテンツリスト内に テキストブロックとツール使用ブロックの2つの別個のブロックがあります。 さて、Claudeについて思い出してほしいことがあります。Claudeは 会話の履歴や、会話に関する何も保存しないことを思い出してください。 Claudeとの会話や履歴を維持したい場合は、 手動で管理する必要があります。これは、 このツール使用ブロックを最終的に 実際の関数呼び出しに使用し、最終的にClaudeに 応答する必要があることを意味します。そしてその際に、 重要な部分は、コース全体を通して行ってきたように、 会話の履歴全体を含める必要があるということです。 この方法は既に分かっています。今回違うのは、 複数のブロックを持つメッセージに対処する必要があることを 確実にすることです。手動でどのように行うか示し、 その後、このセクションの少し後で、 ヘルパー関数、特にadd user messageと add assistant messageに戻り、これらが 複数のブロックを扱えるように更新する必要があることを確認します。 なぜなら、現在では単一のテキストブロックしかサポートしていないからです。 OK。 これらのメッセージを管理するために、 現在応答を取得している下のコードセルに戻ります。 応答をメッセージリストに新しいアシスタントメッセージとして 追加します。なので、そこに応答を削除して、 messages.appendとします。 ロールをアシスタントにして、 そしてコンテンツは、まさに受け取った 応答からのコンテンツブロックのリスト全体になります。 なので、response.contentを追加するだけです。 これで完了です。 さて、メッセージを出力してセルをもう一度実行すると、 ユーザーメッセージが表示されるはずです。 それが元のメッセージです。そしてアシスタントメッセージがあり、 その中にはテキストブロックと ツール使用ブロックがあります。このようにして、 私たちは、収集しているこれらのさまざまなメッセージの すべての異なるブロックを含めることで、 会話の履歴を正しく構築しています。 もう一度、add user messageと add assistant messageという2つのヘルパー関数に 戻り、このように複数のブロックを処理できるように 更新する必要があることを思い出してください。 なぜなら、それらは現在、複数のブロックを扱うこと をサポートするように更新する必要があるからです。 OK。 したがって、私たちが応答を取得している下のコードセルに 戻ります。応答を取得し、それを新しい アシスタントメッセージとしてメッセージリストに追加します。 なので、応答を削除して、
