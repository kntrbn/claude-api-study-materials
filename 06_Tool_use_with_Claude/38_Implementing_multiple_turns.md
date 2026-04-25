# 38. Implementing multiple turns

**URL:** https://anthropic.skilljar.com/claude-with-the-anthropic-api/287758
**Section:** 06 Tool use with Claude

---

## 📄 Page Content

Anthropic Academy
    
  

  
    
      Courses
    
  

    

    
      
      

      
        
          My Profile
        
        
      

      
      

      
        Sign Out
      
    
  

  

  

    
    
    
        
            
    
        
    

            
    
        
        
            
                
                    
                        
                            
                                
                            

                            
                                details
                            

                            
                                
                                    
                                    1
                                    download
                                
                            
                        
                    
                
            
            
                
                
                
                    Implementing multiple turns
                    
                
                
                    
                        
                            
                                
                                    

    
    

    
    
        
            
        
        
            
                
                This video is still being processed. Please check back later and refresh the page.
            
        
        
            
                Uh oh! Something went wrong, please try again.
            
        
    

    

                                
                            
                        
                    
                
            
        
        
            

    
        
            
                
                    
                        
                            
                        
                    
                
            
            
                
                    Summary
                

                

            
        

        
            
                
                    
                        
                            Summary

                            
                                Building a conversation system with tools requires implementing a loop that keeps calling Claude until it stops requesting tool usage. When Claude no longer asks for tools, that signals it has a final response ready for the user.

Detecting Tool Requests

The key to knowing whether Claude wants to use a tool lies in the stop_reason field of the response message. When Claude decides it needs to call a tool, this field gets set to "tool_use". This gives us a clean way to check if we need to continue the conversation loop:

if response.stop_reason != "tool_use":
    break  # Claude is done, no more tools needed

The Conversation Loop

The main conversation function follows a simple pattern:

def run_conversation(messages):
    while True:
        response = chat(messages, tools=[get_current_datetime_schema])
        add_assistant_message(messages, response)
        print(text_from_message(response))
        
        if response.stop_reason != "tool_use":
            break
            
        tool_results = run_tools(response)
        add_user_message(messages, tool_results)
    
    return messages

This loop continues until Claude provides a final answer without requesting any tools.

Handling Multiple Tool Calls

Claude can request multiple tools in a single response. The message content contains a list of blocks, and we need to process each tool use block separately:

The run_tools function handles this by filtering for tool use blocks and processing each one:

def run_tools(message):
    tool_requests = [
        block for block in message.content if block.type == "tool_use"
    ]
    tool_result_blocks = []
    
    for tool_request in tool_requests:
        # Process each tool request...

Tool Result Blocks

Each tool use block must be answered with a corresponding tool result block. The connection between them is maintained through matching IDs:

The tool result block structure includes:

tool_result_block = {
    "type": "tool_result",
    "tool_use_id": tool_request.id,
    "content": json.dumps(tool_output),
    "is_error": False
}

Error Handling

Robust tool execution requires handling potential errors. When a tool fails, we still need to provide a result block to Claude:

try:
    tool_output = run_tool(tool_request.name, tool_request.input)
    tool_result_block = {
        "type": "tool_result",
        "tool_use_id": tool_request.id,
        "content": json.dumps(tool_output),
        "is_error": False
    }
except Exception as e:
    tool_result_block = {
        "type": "tool_result", 
        "tool_use_id": tool_request.id,
        "content": f"Error: {e}",
        "is_error": True
    }

Scalable Tool Routing

To support multiple tools, create a routing function that maps tool names to their implementations:

def run_tool(tool_name, tool_input):
    if tool_name == "get_current_datetime":
        return get_current_datetime(**tool_input)
    elif tool_name == "another_tool":
        return another_tool(**tool_input)
    # Add more tools as needed

This approach makes it easy to add new tools without modifying the core conversation logic.

Complete Workflow

The complete multi-turn conversation works like this:

Send user message to Claude with available tools
Claude responds with text and/or tool requests
Execute all requested tools and create result blocks
Send tool results back as a user message
Repeat until Claude provides a final answer

This creates a seamless experience where Claude can use multiple tools across several turns to fully answer complex user requests. The conversation history maintains the complete context, allowing Claude to build upon previous tool results to provide comprehensive responses.
                            
                        
                    

                    
      

---

## 🎬 Transcript (English)

Now that we are done with that refactor, we are going to start to implement a function like this run conversation function. And reality, our real implementation is going to look almost identical to what you see here on the right-hand side. Remember, the entire goal of this function is to keep calling Claude until it no longer asks to use a tool. When it doesn't ask to use a tool anymore, that is a sign to us that Claude has a final response that is ready for us to send back to our users. And the first thing for us to really understand here is how we know if Claude wants to use a tool or not. We could just take a look at the response message and see if there's a tool use block inside there. But there's a little bit more convenient way of doing this. Back inside my notebook, I'm going to run that little sample again where I'm making use of client messages, create directly, not using our chat function. I can run that, and here's my message response. Now very inside of here, you'll notice that there is a field named Stop Reason, and it is set to a string of tool underscore use. So let me tell you about that field just a little bit. This field tells us about why Claude decided to stop generating any more text. Our current value of tool use is a sign to us that Claude has decided that it needs to call a tool. So if our response message, the assistant message that we get back from Claude has a stop reason of tool use, that is a very clear and immediate sign that Claude wants to use a tool. There are some other possible values of stop reason. And we could definitely check for these, but definitely the one you're going to check for the most is probably going to be tool use. So that's how we're going to implement that little if statement right there. All right, so let's go back over to our notebook. We're going to start to implement this run conversation function. So back over here. I'm going to clear out that cell. It was just there for demonstration purposes. I'm going to define my run conversation function. It's going to take in a list of messages, and then we will set up our loop. Inside of here, we will get a response from calling Claude through our newly upgraded chat function, which now supports tools. So I'll pass in my list of messages, along with some tools that Claude can call. In this case, we currently only have one tool. So I'll add in right here. It's our get current date time schema. Then I'm going to take that response I get back and add it into my message conversation history using the newly upgraded add assistant message function. I'm then going to print out that response using the text from message function we just put together. I'm printing it out just we have an understanding of what Claude is currently doing. So I'll print out text from message with response. Okay, now here is the part where we are going to use the stop reason. We need to take a look at the message that we just got back from Claude and understand whether or not Claude wants to use a tool. If it doesn't want to use a tool, then we want to immediately break out of this while loop. So we'll say if, response dot stop underscore reason is not equal to tool underscore use, then that is a sign that Claude is all done and it doesn't need to make use of any more tools. So we will immediately break. If we get past that if statement, then we know that Claude wants to call a tool. So we're going to put together a new function in just a moment. We're going to call it Run Tools. We're going to pass in the message that we just got back from Claude. The goal of Run Tools is to take a look at all the tool use blocks inside this message and run the appropriate tool for each one. I'm going to define the Run Tools function in a new cell right above Run Conversation. So up here, I will put together a new function called Run Tools, and this is going to take in a single message. Now this function is going to be just a little tricky to put together because we have to write it out assuming that there might be multiple tool calls inside of here. So let me show you a diagram to just make sure it's really clear what needs to happen inside of run tools. As a very quick reminder, whenever Claude gives us back an assistant message, it can possibly have more than one tool use block inside of it. And we took a look at this earlier. So if we ask Claude initially to add together 10 plus 10 and 30 plus 30, it can send back to us two separate tool use blocks. One might ask us to run a calculator tool to evaluate 10 plus 10. And the second tool use block might ask us to evaluate 30 plus 30. So we need to set up this run tools function, assuming that we might have more than one tool use block. So here's how this function is going to work. We're going to take a look at that message that we just got, specifically the content property on it. Remember that content property is going to be a list of blocks. Inside there, we might have a text block that tells us what Claude is currently thinking or what it's currently doing. We don't really care about that text block too much, so I'm going to delete it out of this diagram. And then we're left with just the two separate or possibly more for that matter, tool use blocks. So inside this RunTools function, we are going to iterate over all the different tool use blocks we got. And for each one, we're going to run the specified tool with a given inputs. So we'll take a look at this name field right here. We'll find the appropriate tool function to run, and we'll run it with the given input. Then we're going to take all the outputs from each of these different tool runs, and we're going to assemble them into separate tool result blocks. Remember, a tool result block is how we communicate the result of running a tool back over to Claude. Once we have assembled all these different tool-resolved blocks, we're going to put them all together into a list and return them from the Run Tools function. Okay, so let's try to implement this. I know it's confusing. I know there's a lot going on here, but the code itself is actually not as bad as it might seem initially. So back over here, inside of Run Tools, first thing I'm going to do is take a look at this message's content property. That is the list of blocks. And I'm going to extract only the tool use blocks. So I'll say tool request. is block for block in message.content if block.type is equal to tool use. So again, a little bit of a filter operation here. We are getting just the tool use blocks because those are the only ones we care about. And I'm calling this specifically tool request because I think it makes a little bit more sense than tool use. These are requests by Claude for us to use a tool. Then I'm going to make an empty list called tool result blocks. This is going to eventually contain all the different tool results that we create. Then I'm going to iterate over all these different tool requests. So for tool request in tool request. So now we are iterating over each individual tool request. So this is where we now need to run a specified tool with the given inputs. And we know which tool we want to run based upon this name property. So we will say if toolrequest.name is equal to curly the only tool that we have which is get current date time. Then I want to run the get current date time function with the star star inputs from the tool request. So tool request dot input. That's going to give me some tool output. And I'm now going to take this tool output and use it to assemble a brand new tool result block. It has been a while since we have made use of a tool result block, so let me just give you a quick reminder on what these things are. All right, so on the left hand side is a tool use block. This is what we are currently working with. This is Claude's request to use a tool. On the right hand side is a tool result block. So this is the response that we are formulating to Claude's request to run a tool. Remember that a tool result block has a couple of different properties that we need to assign to it. First, it's going to have a tool use ID. This needs to be exactly equal to the ID from the tool use block that is causing us to run a particular tool. Note here that the ID field over here on the left-hand side, it's called ID, and then on the tool result block, it's a totally different property. It's a tool use ID, but they need to be exactly equal. Then content is going to be the output from our tool run, so the actual tool function. We need to make sure we just encode it as a string, no problem there. We can then also add on that optional is air property, if an air occurred when we ran the tool. And then finally, we also need to add in a type of tool underscore result. All right, so back over here, now that we have our tool output, we're going to assemble our tool result block. And it's going to have all those properties I just pointed out to you. It will have a type of tool result, a tool use ID of the tool request.id. It will have a content And I'm going to take whatever I get out of my tool, and I'm going to encode it as JSON using JSON dump string. I need to make sure that I import JSON, so I'll do that at the top this cell. There we go. And then finally, the is air. I'm going to set that to false for right now, and we're going to add in a little bit more robust air handling in just a moment. So now that we have created our tool result block, we're going to add it into our list of two result blocks. So I'll then do a tool result, blocks append in tool result block. And then finally, outside of the for loop, I will return tool result blocks. Okay, so this is the start to our run tools function. So we've at least got an idea of what it does for us. We're going to filter out all the different tool use blocks for each one. We're going to run some given tool function and then put the result into a tool result block, assemble all the results and return that list. So now we're going to add in two quick improvements to this function. First, we're going to add in a little bit better air handling. So we are currently always saying that there is no air. That's definitely not accurate. There might be a scenario where we run into some kind of air when we are running our tool function. So I'm going to immediately make a small improvement here to capture any air that might occur as we run our tool to do so. I'm going to wrap that with a try. Except statement. I'm going to fix my indentation like so. And then if I get down into the accept statement down here, I still want to put together a tool result block and add it into this list. But now I want to have an is error of true. And I probably want to take the error message and put it into the content field right here so that Claude gets some better understanding of what error just occurred. So I'm going to copy tool result block right here, paste it down inside of the accept statement. I'm going to change is error to true. And then for content, I'm going to put in an F string where I put in air with E. So again, I'm providing some information back to Claude, help you understand why an air occurred. And remember, whenever an air does occur, Claude might try to run your tool again with some better arguments or better formed arguments. Okay, so that's our first improvement. Now, the second improvement I want to make right now, we only are considering one single type of tool, the get current date time tool. Remember, later on, we might have multiple different tools. So besides just get current date time, we're going to eventually support adoration to date time and set a reminder. And honestly, we're going to add in another one even after that. So using this pattern right here, where we have an if statement that's just checking for get current date time, not really going to scale too well. So to figure out what tool to run and actually run it, I'm going to make another helper function right above run tools. And I'm going to call it run tool. This is going to take in a tool name and an input to that tool. And then inside of here, this is where we are going to do a series of if statements or any kind of check to figure out which tool function we need to run and then actually run it and return the results. So if tool name is get current date time, Then I'm going to return, get current, date time, with star star, tool, input. So now with this approach, if we ever add in additional tools, we can just put in additional if checks right here. So if tool name is whatever other tool we have, we can run that particular tool function. So we are going to very shortly come back to run tool and add in some additional tools in just a little bit. All right, so now to make use of that function, I'll come back down here. I'm going to indent that block right there to the try, the accept, and the tool results. I'm going to remove the if statement and then replace get current daytime right here with run tool. And I'm going to pass into it our tool request.name and tool request.input. There we go. Okay, so this was a little bit of a painful refactor, but this is our run tools function. No more changes required. It's going to work pretty well. And we've also got our run tool function put together, also working pretty well. So now the very last thing we need to do is go back down to our conversation function and make use of run tools. So here's our call to run tools right here. So run tools is now going to return our list of tool result blocks. So I get tool results. I'm going to add that into my conversation history. So add user message with messages and tool results. then outside of the while loop, so I'm making sure them outside of while I'll return the list of messages. And that's it. Okay, so now this run conversation function captures that entire loop that we discussed. So whenever we go into run conversation, we're going to call Claude, we're going to get back some assistant message. If the assistant message is asking for any tools, then we're going to continue on past the if statement. We're going to run those tools, get the results, and add them in as a user message to our list of messages. Then we're going to go back up to the top of the while loop again, and call Claude another time with the list of tool results inside of those messages. And we're going to repeat this process over and over again until Claude doesn't ask for a tool use anymore. So now here's the point where hopefully everything's going to work. We'll do a quick test down here. So I'm going to make a list of messages. I'll add a user message to it. And I'm going to ask Claude to do something that's going to probably require two separate tool calls. So I'm going to ask Claude what the current time is in our hour, hour, minute format, and then same thing for second format. So in theory, Claude is probably going to break this up into two separate tool calls. I will then call run. conversation and passing the list messages. I'm going to rerun all the cells inside this notebook because we have now changed a tremendous amount, so we'll do a run all, and then we'll take a look at the response we get. So it looks like it definitely is the right answer right here, but I want to take a look at the list of messages to really understand what is happening. So initially, we have our user message. We then get the initial response back from Claude. It has a text block and a tool use block. So once again, a message with multiple blocks inside of it. And this is why it's so critical now to make sure that all of our code will correctly handle multiple different blocks. Inside this first message, we have a tool use block where Claude is trying to get the current time in our minute format. We then respond with a tool result. And then here's the interesting part. Claude then decides to make a second tool call back to us. So in the second tool call, we don't have a text part anymore, once again highlighting the importance of correctly handling multiple different tool parts inside of a single message. Inside this second message, we've now got a tool use block. Claude is now going to try to call get current daytime in seconds format. We then send the result back to Claude, and then we get a final response from Claude that has just a text block that says, here's the answer to your original query. So this is a perfect result that definitely highlights every step that we just went through. The entire process of running our conversation until we have a response that is not asking for tool use. And inside of our run tools function, the importance of taking a look at all the different blocks we get back, pulling out just the tool use blocks, and then running a tool for each of those blocks, formulating the response into a tool result, and then sending all the different tool results back into Claude. This video has been long and probably rather confusing, but we've now got an excellent example of multi-turn tool calling. So now the last thing for us to do inside of this project is make sure that we can support multiple different tools. We need to add and support for the adoration to daytime tool and the set reminder tool as well.

---

## 🎬 トランスクリプト（日本語）

これでリファクタリングが完了したので、実装を開始します。 このランコンバーセーション関数のようなものです。そして 実際には、私たちの実際の Код はほぼ同じように見えます。 右側に見えるものと同じです。覚えておいてください、 この関数のすべての目標は、呼び出し続けることです。 Claude はツールを使わなくなります。 ツールを使わなくなると、それは私たちにとって兆候です。 Claude は最終的な応答を持っており、送信する準備ができています。 ユーザーに返します。そして最初に理解する必要があります。 ここで、Claude が望むかどうかを知る方法。 ツールを使用するかどうか。私たちは単にメッセージを確認できます。 応答メッセージを見て、ツール使用ブロックがあるかどうかを確認します。 しかし、もう少し便利な方法があります。 ノートブックに戻ります。 小さなサンプルをもう一度実行します。 クライアントメッセージ、直接作成、チャットは使用しません。 関数です。実行できます。ここにあります。 メッセージの応答。今、ここに非常に近い。 Stop Reason というフィールドがあることに注意してください。 それはツール使用という文字列に設定されています。 このフィールドについて少しお話させてください。これは Claude が停止を決定した理由について私たちに伝えます。 テキストの生成。現在の値は ツール使用は、Claude が決定したという兆候です。 ツールを呼び出す必要があること。だから私たちの応答は アシスタントメッセージ、Claude から返されるアシスタントメッセージが ツール使用の停止理由を持っている場合、それは非常に明確で 即時の兆候です。Claude はツールを使用したいと考えています。 停止理由には他にいくつかの可能な値があります。 そして、これらを確実にチェックできます。しかし、間違いなく最も頻繁にチェックするものは おそらくツール使用でしょう。 ですから、そこでその小さな if 文を実装する方法です。 さて、ノートブックに戻りましょう。始めます。 このランコンバーセーション関数を実装します。 ここに戻って、セルをクリアします。 デモンストレーションのためにそこにありました。 ランコンバーセーションを定義します。 メッセージのリストを受け取り、 次にループを設定します。 新しくアップグレードされたチャットを呼び出すことによって Claude から応答を得ます。 ツールをサポートするようになりました。 Claude が呼び出すことができるツールと一緒に、メッセージのリストを渡します。 この場合、現在 1 つしかありません。 ツールです。ここにそれを追加します。現在の 日時スキーマです。 次に、取得した応答を取り、メッセージに追加します。 新しくアップグレードされた会話履歴を使用して アシスタントメッセージを追加する関数。 次に、テキストを使用してその応答を印刷します。 関数から作成します。Claude が現在何をしているかを理解するために印刷します。 だから、テキストからメッセージを印刷します。 応答で。 OK、 今、これは停止理由を使用する部分です。 Claude から受け取ったばかりのメッセージを確認する必要があります。 Claude がツールを使用したいかどうかを判断します。 ツールを使用したくない場合は、すぐに停止します。 この while ループを抜け出します。だから、もし ドットストップアンダースコア理由が ツールアンダースコア使用と等しくない場合、 それは Claude が完了し、それ以上のツールを使用する必要がないという兆候です。 だからすぐに終了します。 その if 文を通過した場合、それは Claude が呼び出したいことを意味します。 ツール。したがって、私たちは新しいものをまとめます。 ランツールと呼ばれる関数。 Claude から受け取ったばかりのメッセージを渡します。 Run Tools の目的は、すべてのツールを調べることです。 このメッセージ内の使用ブロックを実行します。 それぞれに適切なツールを実行します。Run Tools を定義します。 Run Conversation のすぐ上の新しいセルで。 だからここに、Run と呼ばれる新しい関数を作成します。 ツール。これは単一の メッセージを受け取ります。この関数は 少しトリッキーになります。なぜなら、書く必要があるからです。 複数のツール呼び出しがここにある可能性があると仮定して。 なので、本当に明確にするために図を示します。 Run Tools 内で何が必要か。 非常に簡単なリマインダーとして、Claude がアシスタントメッセージを返した場合、 中に複数のツール使用ブロックがある可能性があります。 そして、私たちはそれを以前に見ました。だから Claude に最初に 10+10 を加えるように頼んだ場合 と 30+30 は、私たちに 2 つを返すことができます。 別々のツール使用ブロック。1 つは電卓ツールを実行して 10+10 を評価するように要求するかもしれません。 そして 2 番目のツール使用ブロックは、30+30 を評価するように要求するかもしれません。 だから、この Run Tools 関数を設定する必要があります。 複数のツール使用ブロックがある可能性があると仮定して。 だから、この関数は次のようになります。 受け取ったばかりのメッセージ、特にコンテンツを調べます。 プロパティ。そのコンテンツプロパティは ブロックのリストです。そこに、テキストブロックがあるかもしれません。 Claude が現在何を考えているかを教えてくれる こと、または何をしているかを教えてくれます。私たちはあまり気にしません。 テキストブロックなので、この図から削除します。 そして、私たちは 2 つの別々の、またはそれ以上の ツール使用ブロックだけを残します。だから この Run Tools 関数内で、私たちは反復します。 すべての異なるツール使用ブロックについて。 それぞれに対して、指定されたツールを実行します。 したがって、この名前フィールドを見ます。 適切なツール関数を見つけて それを実行し、指定された入力で実行します。 次に、これらの異なるツール実行からのすべての出力を取得します。 そしてそれらを個別のツール結果ブロックに組み立てます。 覚えておいてください、ツール 結果ブロックは、ツールの実行結果を Claude に伝える方法です。ツール結果ブロックを すべて組み立てたら、それらをリストにまとめて Run Tools 関数から返します。 OK、 これで Run Tools 関数の始まりです。 混乱していることは知っています。多くのことが起こっていることも知っています。 しかし、コード自体は 最初は見えるほど悪くはありません。 Run Tools の中で、最初に メッセージのコンテンツプロパティを調べます。 それはブロックのリストです。 そして、ツール使用ブロックのみを抽出します。 だから、ブロックごとにブロックをツール要求します。 ブロックのタイプがツール使用と等しい場合。 だから、再び、ここでは少しフィルター操作が行われます。 私たちはツール使用ブロックだけを取得しています。なぜならそれらは 私たちが気にする唯一のものだからです。そして私はこれを特別に呼びます ツールリクエスト。なぜならそれはツール使用よりも少し理にかなっていると思うからです。 これらは Claude から私たちへの要求です。 ツールを使用します。次に、私は作成します。 ツール結果ブロックという空のリスト。 これは最終的にすべての異なるツール結果を保持します。 私たちが作成するものです。次に、私は これらの異なるツール要求すべてを反復します。 だからツール要求について ツール要求内で。だから今、私たちは反復しています。 個々のツール要求ごとに。だから、ここで 指定されたツールを指定された 入力で実行する必要があります。そして私たちはツールを実行したいのかを知っています。 この名前プロパティに基づいて。だから、もし ツールリクエストの名前が 私たちが持っている唯一のツールである現在の 日時である場合。次に、 現在の datetime 関数を実行します。 ツールリクエストからの入力の ** だからツールリクエストの入力。 それは私にいくつかのツール出力を与えます。 そして今、私はこのツール出力を取って、それを使用して組み立てます。 ブランドの新しいツール結果ブロック。 ツール結果ブロックを使用してからしばらく経ちました。 だから、これらのものが何であるかを簡単に思い出させてください。 さて、左側はツール使用ブロックです。これは 現在取り組んでいるものです。これは Claude の要求です。 ツールを使用すること。右側は ツール結果ブロックです。だから、これは応答です。 Claude のツール実行要求に対する応答を形成しています。 ツール。ツール結果ブロックは いくつか異なるプロパティがあり、それらを割り当てる必要があります。まず、 ツール使用 ID があります。これは それを引き起こしているツール使用ブロックのIDと正確に一致する必要があります。 特定のツールを実行します。ここに注意してください。 左側の ID フィールドは ID と呼ばれ、 ツール結果ブロックでは、それは完全に異なるプロパティです。それはツールです。 使用 ID、しかしそれらは正確に一致する必要があります。次に コンテンツはツールからの出力になります。 実行、だから実際のツール関数。エンコードする必要があることを確認してください。 文字列として、問題ありません。次にオプションの is_error プロパティを追加することもできます。 もし air が発生した場合。 ツールを実行したとき。 そして最後に、私たちはまた ツールアンダースコア結果のタイプを追加する必要があります。 OK、 これでツール結果ブロックができました。ツール結果ブロックを組み立てます。 そして、これらのすべてのプロパティをそれに含めます。 ツール結果のタイプ、 ツール要求のIDです。 ツール要求のID。 コンテンツがあります。そして私は ツールから取得したものを使用します。 JSON にエンコードします。JSON を使用して。 ダンプ文字列。 JSON をインポートする必要があることを確認します。だからこれを一番上にします。 セル。 よし。 そして、今はしばらくの間、エラーを偽に設定しています。すぐにさらに堅牢なエラー処理を追加します。 これでツール結果ブロックを作成したので、それをツール結果ブロックに追加します。 だから、ツール結果ブロックを追加します。 次に、ツール結果ブロックを 追加します。 そして、ループの外で、返します。 ツール結果ブロックのリスト。 OK、 だから、これは私たちのランツール関数の一部です。 だから、少なくともそれが私たちに何をするかのアイデアを得ました。私たちは すべての異なるツール使用ブロックをフィルタリングします。それぞれについて。 指定されたツール関数を実行します。 そして、結果をツール結果ブロックに配置します。 すべての結果を組み立てて、そのリストを返します。 したがって、この関数に 2 つのクイック改善を追加します。まず、 より良いエラー処理を追加します。だから、私たちは 常にエラーがないと言っています。それは 正確ではありません。ツール関数を実行するときに何らかのエラーに遭遇する可能性があります。 だから、すぐにそれをキャプチャするように小さな改善を行います。 ツールを実行するときに発生する可能性のあるエラー。 そうするために。私はそれをラップします。 トライ・エクセプトステートメントで。 インデントを修正します。 だから、そして受け入れステートメントにドロップした場合。 ツール結果ブロックをまとめます。 そして、リストに追加します。しかし、今私は エラーの真実をエラーにする必要があります。 そしておそらくエラーメッセージを取得してコンテンツフィールドに配置したいです。 Claude が発生したエラーをよりよく理解できるように。 だから、ツール結果ブロックをコピーします。 受け入れステートメントに貼り付けます。 エラーを真実に変更します。 そしてコンテンツについては、F 文字列に入れます。 その中にエラーを E で入れます。 だから、再び、私は Claude に情報を戻しています。エラーが発生した理由を理解するのに役立ちます。 そして覚えておいてください、エラーが発生した場合、Claude はツールを再度実行しようとするかもしれません。 より良い引数またはより適切に形成された引数で。 OK、だからそれは私たちの最初の改善です。さて、2 番目の 改善は今すぐ行いたいことです。現在、私たちはただ 単一のツールタイプ、現在の 日時ツールを検討しています。覚えておいてください、後で 複数の異なるツールがあるかもしれません。だから、現在の 日時ツールに加えて、私たちは日付への加算をサポートする予定です。 そしてリマインダーを設定します。そして正直に言って、私たちは それ以降にもう一つ追加する予定です。だからこの パターンを使用します。ここにある if 文はちょうど 現在の datetime をチェックするだけですが、実際にはうまくスケーリングしません。 だから、どのツールを実行するかを判断するには そしてそれを実行します。私は Run Tools のすぐ上に別のヘルパー関数を作成します。 そしてそれを実行ツールと呼びます。これは ツール名と入力 を受け取ります。そして、ここで、これは私たちの if 文のシリーズを行う場所です。 どのツール関数を実行する必要があるかを判断し、次に実行します。 それを実行して結果を返します。だからもしツール 名が現在の時間です。 次に返します。 ツール入力の **。 だから、このアプローチにより、追加のツールを追加した場合。 ここにさらに if チェックを追加できます。だから もしツール名が他のどのツールでも、 その特定のツール関数を実行できます。だから私たちは すぐにランツールに戻って、さらにツールを追加します。 少しだけ。さて、それを利用するために。 ここに戻ります。 あのブロックをインデントします。 トライ、エクセプト、ツール結果に。 if 文を削除し、 そして現在の datetime をここに置き換えます。 ツールを実行します。そしてそれを呼び出します。 ツール要求の名前とツール要求の入力。 よし。 これは少しばかり面倒なリファクタリングでしたが、 これが私たちのランツール関数です。もう変更は必要ありません。 うまく機能します。そして、私たちの ランツール関数もまとめてあります。うまく機能しています。 だから、私たちが今しなければならない最後のことは、 会話関数に下に戻ることです。 ランツールを使用します。 だから、ランツールへの呼び出しは次のとおりです。 これでツール結果ブロックのリストが返されます。 だから、ツール結果を取得します。会話履歴に追加します。 だから、ユーザーメッセージを追加します。 メッセージとツールで 結果。次に、 while ループの外側、while ループの外側にいることを確認します。 メッセージのリストを返します。 それだけです。OK、 だから今、このランコンバーセーション関数は議論したループ全体をキャプチャします。 だから、ランコンバーセーションに入ると、呼び出します。 Claude、アシスタントメッセージを取得します。 アシスタントメッセージがツールを要求している場合、 if 文を通過して続行します。ツールを実行します。 結果を取得し、それらを ユーザーメッセージとしてメッセージリストに追加します。次に while ループの先頭に戻ります。 ツール結果のリストを含む メッセージで Claude を呼び出します。 そして、このプロセスを Claude が ツール使用を要求しなくなるまで繰り返します。だから 今、すべてが機能することを願っています。ここに簡単なテストを行います。 だから、メッセージのリストを作成します。ユーザーメッセージを追加します。 そして、Claude に 2 つの別々のツール呼び出しが必要になるであろうことを依頼します。 だから、Claude に現在の時刻を時時分形式で尋ねます。 そして、秒形式でも同じように尋ねます。だから理論的には Claude は これを 2 つの別々のツール呼び出しに分割するでしょう。 次にランコンバーセーションを呼び出します。 メッセージに渡します。 ノートブック内のすべてのセルを再実行します。 なぜなら、私たちは非常に多くのことを変更したからです。だから実行します。 すべてを実行し、次に取得した応答を確認します。 だから、それは確かに正しい答えのようです。しかし、私は 何が起こっているのかを本当に理解するために、メッセージのリストを確認したいと思います。 だから最初に、ユーザーメッセージがあります。次に取得します。 Claude からの最初の応答。それはテキストブロックと ツール使用ブロックを持っています。だから再び、メッセージ は中に複数のブロックがあります。だからこそ、今やることが重要です。 すべてのコードが複数の異なるブロックを正しく処理することを確認すること。 この最初のメッセージ内で、ツール 使用ブロックがあります。Claude は現在の時間を取得しようとしています。 分形式で。次に ツール結果で応答します。そして、ここで興味深いのは 部分です。Claude は次に 2 番目のツールを呼び出すことを決定しました。 私たちに戻ります。だから 2 番目のツール呼び出しでは、 もうテキスト部分はありません。 単一のメッセージ内の複数のツール部分を正しく処理することの重要性を強調します。 この 2 番目のメッセージ内で、ツール使用 ブロックがあります。Claude は現在、現在の datetime を呼び出そうとしています。 秒形式で。次に 結果を Claude に返します。 そして、最終応答を取得します。 Claude からのテキストブロックのみです。ここに あなたの元のクエリへの答えがあります。だから、これは すべてを行われたステップを強調する完璧な結果です。 応答が得られるまで会話を実行するプロセス全体。 ツール使用を要求していません。 そして、私たちのランツール関数内で、 受け取るすべてのブロックを確認することの重要性。 ツール使用ブロックだけを抽出します。 そして、これらの各ブロックに対してツールを実行します。 応答をツール結果にフォーマットします。 そして、すべての異なるツール結果を Claude に戻します。 このビデオは長くて混乱していたかもしれませんが、私たちは マルチターンのツールの優れた例を持っています。 呼び出し。だから、私たちにできる最後のことは 複数の 異なるツールをサポートすることです。日付への加算をサポートする必要があります。 日時ツールとセットリマインダーツールも同様に。
