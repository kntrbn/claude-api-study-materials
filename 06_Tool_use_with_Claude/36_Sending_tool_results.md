# 36. Sending tool results

**URL:** https://anthropic.skilljar.com/claude-with-the-anthropic-api/287752
**Section:** 06 Tool use with Claude

---

## 📄 Page Content

Anthropic Academy
    
  

  
    
      Courses
    
  

    

    
      
      

      
        
          My Profile
        
        
      

      
      

      
        Sign Out
      
    
  

  

  

    
    
    
        
            
    
        
    

            
    
        
        
            
                
                    
                        
                            
                                
                            

                            
                                details
                            

                            
                        
                    
                
            
            
                
                
                
                    Sending tool results
                    
                
                
                    
                        
                            
                                
                                    

    
    

    
    
        
            
        
        
            
                
                This video is still being processed. Please check back later and refresh the page.
            
        
        
            
                Uh oh! Something went wrong, please try again.
            
        
    

    

                                
                            
                        
                    
                
            
        
        
            

    
        
            
                
                    
                        
                            
                        
                    
                
            
            
                
                    Summary
                

                

            
        

        
            
                
                    
                        
                            Summary

                            
                                After Claude requests a tool call, you need to execute the function and send the results back. This completes the tool use workflow by providing Claude with the information it requested.

Running the Tool Function

When Claude responds with a tool use block, you extract the input parameters and call your function. Here's how to access the tool parameters:

response.content[1].input

This gives you a dictionary of the arguments Claude wants to pass to your function. Since your function expects keyword arguments rather than a dictionary, you use Python's unpacking syntax:

get_current_datetime(**response.content[1].input)

Tool Result Block

After running the tool function, you need to send the results back to Claude using a tool result block. This block goes inside a user message and tells Claude what happened when you executed the tool.

The tool result block has several important properties:

tool_use_id - Must match the id of the ToolUse block that this ToolResult corresponds to
content - Output from running your tool, serialized as a string
is_error - True if an error occurred

Handling Multiple Tool Calls

Claude can request multiple tool calls in a single response. For example, if a user asks "What's 10 + 10 and what's 30 + 30?", Claude might respond with two separate ToolUse blocks.

Each tool call gets a unique ID, and you must match these IDs when sending back results. This ensures Claude knows which result corresponds to which request, even if the results arrive in a different order.

Building the Follow-up Request

Your follow-up request to Claude must include the complete conversation history plus the new tool result. Here's the structure:

messages.append({
    "role": "user",
    "content": [{
        "type": "tool_result",
        "tool_use_id": response.content[1].id,
        "content": "15:04:22",
        "is_error": False
    }]
})

The complete message history now contains:

Original user message
Assistant message with tool use block
User message with tool result block

Making the Final Request

When sending the follow-up request, you must still include the tool schema even though you're not expecting Claude to make another tool call. Claude needs the schema to understand the tool references in your conversation history.

client.messages.create(
    model=model,
    max_tokens=1000,
    messages=messages,
    tools=[get_current_datetime_schema]
)

Claude will then respond with a final message that incorporates the tool results into a natural response for the user. The tool use workflow is now complete - you've successfully enabled Claude to access real-time information through your custom function.

---

## 🎬 Transcript (English)

On to step four, where we run the tool function that Claude requested us to run. Remember, in the last step, we got back a response from Claude, that included a tool use block. Let's print that out inside of our notebook really quickly. So back over here, remember we've got this response variable, I'm going to go down, create a new cell, and print out response. Now inside of here, we get back a message that has a content property, and the second block inside that list is a tool use block. So to access that thing, I would do response content at one. Then inside of here, we're given a input field. This is the input or the arguments that Claude is requesting that we pass into the get current date time function. So to get that dictionary right there, we would chain on a dot input. Now when we add on the dot input, you might end up getting a type error here. We're going to ignore type errors just in this video when we're going to come back very, very quickly and fix all the type errors. But just so you know, if you see any type errors in this video, totally fine. Just ignore them for right now. So now our goal is to take this dictionary right here and provide it to our get current date time function. Just one thing to be aware of here. Remember our get get current date time function. defined back up here doesn't take in a dictionary. It takes in a keyword argument of date format. So to convert that dictionary into a list of keyword arguments and apply them to the function, here's what we would do. I'm going to call it get current date time star star and the response content one input. And now if I run that, I'll get back my current date time in the real world. So for me, it's 241 or 1441. Besides the type error that we need to fix up, that ended up being pretty easy. So let's now move on to step five. So in step five, we are now going to send a follow-up request back to Claude. This request is going to include our full conversation history. So we'll have our original user message. It'll have the assistant message that we just processed with a tool use block. And now we are going to append onto the very end another user message. This user message is going to have a new kind of block that we have not seen before called the tool result block. Let me tell you about how this block works. The tool result block is going to be placed inside of a user message. The tool result is going to contain the result of running a tool. So we're essentially taking whatever we get back from the tool function that we just called and we are feeding it right back into Claude. The tool result block is going to have a couple of different keys inside of it. And it's important for you to understand exactly what these keys are doing. The first one is probably the trickiest to understand, the tool use ID. So let me very quickly tell you what the tool use ID is all about. I want you to imagine for just a moment that we create a new tool called calculator. And this tool is meant to evaluate a math expression. And then maybe a user sends in a message of something like, what's 10 plus 10? Also, what's 30 plus 30? In this case, Claude might want to make two separate calls to the calculator tool. One call to solve 10 plus 10 and a second to solve 30 plus 30. To do so, Claude will respond with an assistant message that has multiple tool use blocks inside of it. So we might have tool use block one right here, where the expression that we need to evaluate is 10 plus 10. And then in the second, we might have an expression of 30 plus 30. We would then execute our calculator tool twice, once for this expression and once for this expression. And then we would send a follow request back to Claude. Inside of our follow request, we would add in a user message that has two separate tool result blocks. So we'd have to result one and to result two. Now when we send these back into Claude, Claude needs to be able to figure out which result belongs with which request. So we've got request one and request two, and then result one and result two. Claude doesn't want to just rely upon these things being ordered in the same order. Instead, it's going to make use of IDs. So inside the original tool use, we have an ID up here of AB3. And then in a second, we have the ID of PO9. Inside of our follow-up request, we send back to Claude. We need to make sure that the ID, so we put down here, match up with the output. So in other words, PO9. being tied to 30 plus 30, then we would want to make sure that we have P09 tied to 60 down here. And likewise, AB3 with 10 plus 10, we'd want to have that tied to AB3 with an output of 20. So that's what the tool use ID is all about. It helps us tie tool use requests to tool result outputs. The other properties on here that you need to be aware of is content, so asking me whatever output you get from your tool function. Even if your tool function will return something like a number or a dictionary or a list, you're just going to turn it into a string, usually by just converting into plain JSON. And then finally, optionally, we can also put in an is-air field. If anything goes wrong with running your tool function, you will set this to be true. By default, it's always going to be false. Now that we have a better idea of what this tool result block is all about, I want to give you a quick reminder of what we need to do next. So we just got back an assistant message from Claude that asked us to run a tool. We know that was asking us to run a tool because it had a tool use block inside of it. We then executed our tool with the provided arguments. So now that we have the result of the tool function, we need to make a follow-up request back to Claude. Inside of this request, we're going to include our full message history. So it's going to be our original user message, the assistant message with a tool use block inside of it. And now we are going to append in one additional message, a user message, that has a tool-result block. That's what we just discussed. So it's this thing right here. Inside of this tool result block, it's going to have the result of the actual function call. So let's now go back over to our notebook and we're going to get our list of messages and add in this new user message with the tool result block inside of it. All right, so back inside of my notebook, I'm going to get my list of messages. I'm going to append in a new message that has a role of user. And then a content list that will contain just one block, it's going to have a tool result block. So we'll give it a type of tool underscore result. a tool use ID that matches the ID of this tool use block right here. To get access to that ID right there, we will refer to response content 1.ID. And when I put that in, I'm going to once again get a type error. Remember, we are toiliocave type errors for right now. We're going to ignore it and we'll fix it up very shortly. I'll then add in some content. So that's going to be the result of calling my function right here. So I'm going to assign the result of calling get current daytime to how about just result. You're going to rerun that. And then I'll refer to content result. And then finally, when we ran this function, there was no error. So I'll put in is error false, not strictly necessary, because that is the default, but I'll put it in there. Anyways, Okay, so now that we have updated our list of messages, I'm going to print out the list. just to make sure we are doing everything correctly. So now we have our entire conversation history here. We have the original user request. We've got Claude's request for us to use a tool. And now we have appended in a new user message that has a tool result block inside of it. So now the last thing you need to do is take this list of messages and send it back into Claude. I'm going to add in another code cell down here at the bottom. And once again, call Claude messages create with my model max_tokens. the list of messages. And then whenever we make a follow up request that includes some tool use, we need to also include the original tool schema. Even though we are not probably going to use any tools here, we still have to tell Claude about the existence of this tool because we are referring to it inside of the tool use block right here and the tool result block right here as well. So we need to make sure that we still include our list of tools, which would be a list of get current date time schema. And that should be it. So now let's run this. And we should see a final response out of Claude. And so there it is right there. Here's our final response. We have a text block that says the current time is 1504. Well, that is a successful tool call. So we've gone through the entire process. Let's do a very quick review. So everything began with us writing out a tool function and then writing a tool schema to describe it. The goal of the tool schema was to help Claude understand the different tools available to it and how to actually call those different tools. We have to include that tool schema with every request that we make from here on out. So that's why I'm showing it right here and down here as well. When Claude responded to us, it sent back an assistant message that had two separate blocks inside of it. So a text block right here and a tool use block right here. The text block is intended to be displayed to a user, so the user understands what's going on. And the tool use block includes some information about a tool that Claude wants to call. So it includes the name of the tool it wants to call along with some input arguments to it. Then on our server, we executed the tool function, and then we sent a follow-up request back to Claude. The follow-up request included the entire conversation history, along with the list of tool schemas as well. The final message inside of our request was a user message, then included a tool result block. The tool result block is used to inform Claude about the result of running some tool function. So inside this block, we put the current time, which is what Claude was really asking for. then Claude sent us one final result that was just an assistant message with only a text block. And it made use of the input that we fed into it through this tool result block.

---

## 🎬 トランスクリプト（日本語）

ステップ4に進みます。ここで、Claudeが実行するよう依頼したツール関数を実行します。 前のステップで、Claudeからツールユースブロックを含む応答を受け取ったことを思い出してください。 それをノートブック内で素早く表示しましょう。 さて、ここにいるのを思い出してください。response変数があります。 下に移動して、新しいセルを作成し、responseを表示します。 ここで、contentプロパティを持つメッセージが返されます。 そして、そのリスト内の2番目のブロックはツールユースブロックです。 それをアクセスするには、response.content[1]とします。 そして、ここに inputフィールドが与えられます。これは、Claudeが現在の 日時関数に渡すよう要求している入力または引数です。 そこで、その辞書を右に表示するには、.inputをチェーンします。 さて、.inputを追加すると、型エラーが発生する可能性があります。 この動画では型エラーを無視し、すぐに戻って すべての型エラーを修正します。 ですから、もしこの動画で型エラーを見ても、まったく問題ありません。 今は、この辞書を取得して 現在の Сurrent DateTime 関数に渡すことが目標です。 ここに注意点があります。 Get Curent DateTime 関数は辞書ではなく、キーワード引数 date format を受け取ることを思い出してください。 つまり、その辞書をキーワード引数のリストに変換し、 それらを関数に適用するには、次のようにします。 Get current date time（スター、スター）とresponse.content[1]を呼び出します。 そしてそれを実行すると、実際の現在の Сurrent DateTime が返されます。 つまり、私にとっては24時1分、または14時41分です。 型エラーを修正する必要がある他に、それはかなり簡単でした。 では、ステップ5に進みましょう。 ステップ5では、フォローアップリクエストをClaudeに送信します。 このリクエストには、会話履歴全体が含まれます。 つまり、元のユーザーメッセージがあり、ツールユースブロックが含まれる アシスタントメッセージがあります。 そして今、最後にユーザーメッセージを追加します。 このユーザーメッセージには、これまで見たことのない ツール結果ブロックという新しい種類のブロックが含まれます。 このブロックの仕組みを説明しましょう。 ツール結果ブロックは、ユーザーメッセージ内に配置されます。 ツール結果には、ツールの実行結果が含まれます。 つまり、ツール関数を呼び出して得られたものを Claudeにフィードバックしていることになります。 ツール結果ブロックには、いくつかの異なるキーが含まれます。 これらのキーが何をしているのかを正確に理解することが重要です。 最初のものは理解するのが最も難しい、ツールユースIDです。 ツールユースIDについてすぐに説明しましょう。 カレンダーという新しいツールを作成したと想像してください。 このツールは数式の評価用です。 そして、ユーザーが「10 + 10 は？」や「30 + 30 は？」といったメッセージを送るとします。 この場合、Claudeはカレンダーツールに2回別々に呼び出す必要があるかもしれません。 1回は10 + 10 を解くため、 もう1回は30 + 30 を解くためです。 それを実行するために、Claudeはアシスタントメッセージで応答します。 そこには複数のツールユースブロックがあります。 例えば、ツールユースブロック1があり、 評価する必要のある式は10 + 10 です。 そして2番目には、30 + 30 の式があるかもしれません。 次にカレンダーツールを2回実行します。 この式とこの式のために。そして、フォローアップリクエストをClaudeに送り返します。 フォローアップリクエスト内には、 2つの別々のツール結果ブロックを持つユーザーメッセージを追加します。 つまり、結果1と結果2です。 これらをClaudeに送り返すと、 どの結果がどのリクエストに対応するかをClaudeは理解する必要があります。 つまり、リクエスト1とリクエスト2があり、 結果1と結果2があります。 Claudeはこれらのものが同じ順序で並んでいることに頼りたくありません。 代わりにIDを使用します。 つまり、元のツールユースでは、 ここにIDのAB3があります。 そして2番目に、IDのPO9があります。 フォローアップリクエストでClaudeに送り返す際に、 ここに配置したIDが出力と一致するように する必要があります。つまり、PO9が30 + 30 に紐づいている場合、 ここにPO9が60に紐づいていることを確認したいです。 同様に、AB3が10 + 10 に紐づいている場合、 20という出力を持つAB3に紐づけたいです。 それがツールユースIDの意味するところです。 ツールユースリクエストとツール結果出力を紐づけます。 他に知っておくべきプロパティはコンテンツです。 ツール関数から得られた出力は何であれ、 たとえツール関数が数値、辞書、またはリストを返すとしても、 それを文字列に変換します。通常はプレーンJSONに変換するだけです。 そして最後に、オプションでis_errorフィールドを入れることができます。 ツール関数を実行中に何か問題が発生した場合、これをtrueに設定します。 デフォルトでは常にfalseです。 ツール結果ブロックの意味をよりよく理解できたので、 次に何をする必要があるか、簡単に思い出させてください。 Claudeからツールを実行するように求めるアシスタントメッセージを受け取りました。 それはツールユースブロックを含んでいたので、ツールを実行するように求めていることを知っています。 次に、提供された引数でツールを実行しました。 ツール関数の結果が得られたので、 Claudeにフォローアップリクエストを送信する必要があります。 このリクエストには、メッセージ履歴全体を含めます。 つまり、元のユーザーメッセージ、ツールユースブロックを含む アシスタントメッセージです。 そして今、追加のメッセージを1つ追加します。 ツール結果ブロックを持つユーザーメッセージです。 それは私たちが議論したことです。だから、ここにあります。 このツール結果ブロック内には、 実際の関数呼び出しの結果が含まれます。 では、ノートブックに戻りましょう。 メッセージのリストを取得し、 ツール結果ブロックを含む新しいユーザーメッセージを追加します。 さて、ノートブックに戻って、 メッセージのリストを取得します。 ロールがユーザーで、 contentリストが1つのブロックのみを含む新しいメッセージを追加します。 ツール結果ブロックです。 タイプはツール_結果です。 ツールユースIDは、このツールユースブロックの IDと一致します。 右のIDにアクセスするには、 response.content[1].IDを参照します。 そしてそれを入力すると、再び型エラーが発生します。 型エラーは現時点では無視することにしています。すぐに修正します。 コンテンツを追加します。だから、これは私の関数の呼び出し結果です。 Get current date timeの呼び出し結果を、例えば結果とします。 もう一度実行します。 そしてコンテンツ結果を参照します。 そして最後に、この関数を実行したとき、エラーはありませんでした。 だから、is_errorをfalseとします。 これは厳密には必要ありません、それがデフォルトなので。 しかし、とにかく入れておきます。 さて、メッセージリストを更新したので、 正しく行っていることを確認するためにリストを表示します。 これで、会話履歴全体があります。 元のユーザーリクエスト、ツールユースブロックを含む Claudeのリクエスト、 そして今、ツール結果ブロックを持つ新しいユーザーメッセージを追加しました。 それが私たちが議論したものです。 したがって、今、このメッセージリストをClaudeに送信する必要があります。 下に別のコードセルを追加します。 そして、もう一度Claudeに、 max_tokens、メッセージリストで作成します。 そして、ツールユースを含むフォローアップリクエストを作成するたびに、 元のツールのスキーマも含まれる必要があります。 ここではツールを使用しないかもしれませんが、 ツールユースブロックとツール結果ブロックで参照しているため、 Claudeにツールの存在を伝える必要があります。 そのため、ツールのリストをここでも含める必要があります。 それはGet current date timeのスキーマのリストになります。 これで完了です。 では、これを実行しましょう。 そして、Claudeから最終的な応答が表示されるはずです。 そして、それはここにあります。これが最終的な応答です。 現在の時刻は1504です、というテキストブロックがあります。 これは成功したツール呼び出しです。 これでプロセス全体が完了しました。簡単にレビューしましょう。 すべては、ツール関数を書き出し、次にそれを記述するツールスキーマを 書くことから始まりました。 ツールスキーマの目的は、Claudeが利用可能なさまざまなツール とそれらのさまざまなツールを実際に呼び出す方法を理解できるようにすることでした。 このツールスキーマは、今後行うすべてのリクエストに含める必要があります。 だから、ここでそしてここでもそれを示しています。 Claudeが私たちに応答したとき、それは 2つの別々のブロックを持つアシスタントメッセージを返しました。 つまり、テキストブロックと ツールユースブロックです。 テキストブロックはユーザーに表示されることを意図しており、 ユーザーは何が起こっているのかを理解します。 そしてツールユースブロックには、 Claudeが呼び出したいツールに関する情報が含まれています。 つまり、呼び出したいツールの名前といくつかの 入力引数が含まれます。 次にサーバー側で、 ツール関数を実行し、 フォローアップリクエストをClaudeに送り返しました。 フォローアップリクエストには、会話履歴全体が含まれていました。 ツールのスキーマのリストも含まれています。 リクエスト内の最後のメッセージはユーザーメッセージであり、 ツール結果ブロックが含まれていました。 ツール結果ブロックは、ツール関数を実行した結果を Claudeに通知するために使用されます。 だから、このブロックの中には、 Claudeが本当に求めていた現在の時間を入れました。 次にClaudeは、テキストブロックのみを持つ 最終的な結果を送ってきました。 そして、それは私たちがツール結果ブロックを通して フィードした入力を使用しました。
