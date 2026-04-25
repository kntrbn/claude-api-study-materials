# 37. Multi-turn conversations with tools

**URL:** https://anthropic.skilljar.com/claude-with-the-anthropic-api/287750
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
                                
                            
                        
                    
                
            
            
                
                
                
                    Multi-turn conversations with tools
                    
                
                
                    
                        
                            
                                
                                    

    
    

    
    
        
            
        
        
            
                
                This video is still being processed. Please check back later and refresh the page.
            
        
        
            
                Uh oh! Something went wrong, please try again.
            
        
    

    

                                
                            
                        
                    
                
            
        
        
            

    
        
            
                
                    
                        
                            
                        
                    
                
            
            
                
                    Summary
                

                

            
        

        
            
                
                    
                        
                            Summary

                            
                                When building applications with multiple tools, you need to handle scenarios where Claude might need to call several tools in sequence to answer a single user question. For example, if a user asks "What day is 103 days from today?", Claude needs to first get the current date, then add 103 days to it.

This creates a multi-turn conversation pattern where Claude makes multiple tool requests before providing a final answer. Your application needs to handle this automatically.

The Multi-Turn Tool Pattern

Here's what happens behind the scenes when Claude needs multiple tools:

User asks: "What day is 103 days from today?"
Claude responds with a tool use block requesting get_current_datetime
Your server calls the function and returns the result
Claude realizes it needs more information and requests add_duration_to_datetime
Your server calls that function and returns the result
Claude now has enough information to provide the final answer

Building a Conversation Loop

To handle this pattern, you need a conversation loop that continues until Claude stops requesting tools:

def run_conversation(messages):
    while True:
        response = chat(messages)
        
        add_user_message(messages, response)
        
        # Pseudo code
        if response isn't asking for a tool:
            break
            
        tool_result_blocks = run_tools(response)
        add_user_message(tool_result_blocks)
        
    return messages

Refactoring Helper Functions

Before implementing the conversation loop, you need to update your helper functions to handle multiple message blocks properly.

Updating Message Handlers

Your add_user_message and add_assistant_message functions currently assume you're always working with plain text. Update them to handle full message objects:

from anthropic.types import Message

def add_user_message(messages, message):
    user_message = {
        "role": "user",
        "content": message.content if isinstance(message, Message) else message
    }
    messages.append(user_message)

This allows you to pass in either a string, a list of blocks, or a complete message object.

Updating the Chat Function

Modify your chat function to accept a list of tools and return the full message instead of just text:

def chat(messages, system=None, temperature=1.0, stop_sequences=[], tools=None):
    params = {
        "model": model,
        "max_tokens": 1000,
        "messages": messages,
        "temperature": temperature,
        "stop_sequences": stop_sequences,
    }
    
    if tools:
        params["tools"] = tools
        
    if system:
        params["system"] = system
        
    message = client.messages.create(**params)
    return message

Extracting Text from Messages

Since you're now returning full message objects, create a helper to extract text when needed:

def text_from_message(message):
    return "\n".join(
        [block.text for block in message.content if block.type == "text"]
    )

This function finds all text blocks in a message and joins them together, which is useful when you need to display the final response to users.

Key Improvements

These refactoring steps prepare your code for robust tool handling:

Flexible message handling - Your helper functions can now work with different message formats
Tool support in chat - The chat function can receive and pass through tool schemas
Full message returns - You get complete message objects instead of just text, preserving all blocks
Text extraction utility - Easy way to get readable text from complex messages

With these foundations in place, you're ready to implement the conversation loop that handles multiple tool calls automatically, creating a seamless experience where Claude can use as many tools as needed to answer user questions.
 

---

## 🎬 Transcript (English)

We've now gone through an example of wiring up one single tool to Claude. But as a reminder, the goal of this project is to wire up multiple different tools to Claude. So we want to have three different tools in total. I want to think about what's going to happen inside of our code when we wire up three different tools to Claude. So let's go through a quick example. Let's imagine that we submit a user message to Claude asking it what day is 103 days from today. Now to answer this, Claude needs to use two separate tools. First, it needs to use Get Current Date Time to find out what the current date is, and then it needs to use Add duration to date time to add 103 days to that. So here's what's gonna go on behind the scenes. Initially, Claude is going to immediately respond back to us with a tool use block asking us to call Get Current Date Time. We will call that function, and then respond back to Claude, telling it what the current date is. After that, Claude is going to realize that it doesn't quite have enough information to answer the user's original question. It now needs to take the current date and add 103 days to it. So Claude is then going to respond to us with another separate tool use block asking us to call add duration to date time. We will call it, and then pass the response back onto Claude. And now Claude has enough information to respond to our actual query. Now here's why I'm showing you this example in particular. If we are getting our input for our original user message from an actual user, like an actual person, we can't always predict exactly what they are going to be asking of Claude. So a user might ask some wild query that's going to require multiple different tool calls in order to actually answer. So when we add tool calling into our application, we really need to allow for this kind of situation. Whenever we submit some query to Claude, we need to assume that Claude might want to use multiple tools in a row. And whenever Claude responds to us, we need to take a look at the response and see if Claude is asking to use a tool. If it isn't, then we know that we have a final response that we can finally deliver back to our user. Here's a pseudo code example of how we might implement this. We could make a function called something like Run Conversation that would take in an initial list of messages. Then inside of a while loop, we'll reach out to Claude, get a response back. We'll then take a look at that response. And if Claude is not asking for a tool use, then we know that we have some response we're ready to send back to a user. Otherwise, if Claude does want to use a tool, we can run the tool, get the resulting tool, result blocks, add them into a user message, and then run Claude all over again, still inside of the while loop. In the remainder of this video, we are going to spend some time to refactor our notebook, to build up a function just like this. So we are going to build out a function like run conversation that's going to go through the exact same series of operations. In order to put this function together, however, we are going to have to do a little bit of work. We're going to have to do a little bit of a refactor on our add user message and add assistant message helpers and the chat function as well. I've put together a list of all the things that we're going to do inside of our notebook to get ready for defining this run conversation function. In step one, we are going to upgrade our add user message and add assistant message helper functions so that they can better deal with multiple message blocks. Remember that whenever we start working with tools, we are going to get back responses from Claude that might have multiple different blocks inside them. And at present, our add user message and add assistant message helper functions are entirely set up, always assuming that we are always working with a plain text block and nothing else. So let's take care of that back inside of our notebook right away. Back over here, I'm still inside of the exact same notebook we have been working on. I just deleted a couple of the cells at the bottom that had some of the example tool calls, just so you can better see what I'm doing on the screen. All right, so I'm going to expand the helper function cell. I'm going to find add user message and add assistant message. So once again, right now we are assuming that we are always getting back some piece of text and we are assigning that directly to the content property. So now we want to allow for a little bit more flexibility here. So here's how we are going to do it. At the top of the cell, I'm going to add an import from Anthropic.types. I will import message. Then I'm going to rename the second argument right here. Instead of text, I'm going to call it message. I'm going to expand this dictionary like so. And I'm going to update text to be message.content if isinstance(message, Message) else message else message assistant message as well. So down here, I'm going to rename that to message. I will expand the dictionary. And then to save time, I will copy that statement right there to right there. All right, so now I'm going to rerun the cell and I'll show you what this refactor is going to do for us. So back down here. I'm going to add in a quick example call like so. So I'm just asking Claude to print out the current time in our minute second format. And I'm providing our get current daytime tool. I'm then going to print out the message or response we get back. So if I run this, we'll see that we get the usual message like so. And inside there is the content property that has both a text block and a tool use block. So now to very easily add this in to my message history as a assistant message, I would call Add Assistant Message with Messages, and then I can now put in that entire response, the entire message that I just got back. So I'll call that and then print out Messages on the next cell down. And there we go. I've got my entire message history being built up. Another way that I could run this is to put in response.content, like so. This will work just as well. So if I do that, and then printout messages, I still get the correct thing. And then, of course, if I want to, I could always put in a plain string here as well. And printout messages. And we'll see that yep, still building up that response history. So now we have a much more flexible helper function in add user message and add assistant message. We could put in a plain string or a list of blocks or an entire message and it will deconstruct the thing for us. This is going to make dealing with a message that has some tool use blocks inside of it much easier down the line. Onto step two of our refactor. We are going to update the chat function to receive a list of tool schemas. And we'll take that list of schemas and pass it through to the client messages create function call. In addition, from the chat function, we are no longer going to return plain text out of the first block that comes inside of the assistant message. Instead, we will return the entire message that we got back from Claude. Once again, this is because we are now anticipating getting back responses from Claude that have multiple blocks inside them. And at present, our chat function is always assuming that we are only ever getting back one block, just a single text block and nothing else. So back over here, here's the chat function. I'm going to add in a tools. They'll be defaulted to be none. And then we are going to wire it up in the same way that we did system right here. So we'll say if there are any tools that were passed in, we will add that in as the tools parameter. Next up, I'm going to go down to the return statement. So right here. As I just mentioned a moment ago, our chat function is currently set up assuming that we're always going to get back a single block from Claude, and that the block is always going to be a text block. That's why we have this code right here. We are making a really big assumption that we're always getting back that one single block and it's always going to contain some text. Because we are now making use of tools, that is no longer the case. We might get back a message that has multiple blocks inside it, so multiple entries inside this content list. One of them might be a text block, but we don't necessarily have a guarantee. So rather than always making this assumption, I'm now going to return the entire message. This is going to be a little bit less convenient for us because now if we ever want to get access to the text, we're going to have to do a little bit more work, but it's definitely a lot safer because again, this really reflects reality. Okay, that's that. So now on that same kind of note, we're going to now add in a little helper function. We're going to call it text from message. And the goal here is to take a look at a message, take a look at all the blocks, find all the text blocks, and just extract the text from those. So this is kind of replacing the functionality that we just removed. It's going to make it a lot easier to extract all the text out of a given message. So I'm going to add in that helper function right underneath chat. I'll call it text from message. It's going to receive a message. And inside of here, I'm going to return a new log new line that is going to join together a comprehension with block.text.for block in message.content if block.type is equal to text. So this is going to take a look at all the different blocks inside of a message. And if the block is a text block, then we're going to just extract the blocks text and then join all the block text together and return it. So again, just a helper function to make it a little bit easier to get all the text out of a particular message. All right, so we've taken care of most of our refactor. So now the last step, which we're going to take care of in just a moment, is add in support for multiple tool calls inside of a single conversation. So essentially, we need to implement a function like this. We need to make a function that's going to take in the list of messages, and then continue calling Claude until we get back a sign that Claude doesn't want to call a tool anymore.

---

## 🎬 トランスクリプト（日本語）

私たちは今、単一のツールをClaudeに接続する例を見てきました。 しかし、おさらいとして、このプロジェクトの目標は、 複数の異なるツールをClaudeに接続することです。したがって、合計で3つ の異なるツールを持たせることを目指します。3つの異なるツールを Claudeに接続したときに、私たちのコード内で何が起こるかを考えてみましょう。 では、簡単な例を見てみましょう。想像してみてください。 Claudeにユーザーメッセージを送信して、今日から103日後は 何日目かを尋ねるとします。さて、 これを答えるために、Claudeは2つの別々のツールを使用する必要があります。まず、 現在の日時を取得して、現在の日付を確認する必要があり、 次に、現在の日時に103日を加えるために、[Add duration to date time]を使用する必要があります。 だから、舞台裏ではこのようなことが起こります。 最初に、Claudeはすぐに私達にツール使用ブロックを介して応答し、 [Get Current Date Time]を呼び出すように依頼してきます。 私たちはその関数を呼び出し、 Claudeに現在の年月日を伝えて応答します。その後、Claudeは ユーザーの元の質問に答えるには情報が不十分であることに気づきます。 今度は、現在の日に103日を加える必要があります。 したがって、Claudeは別のツール使用ブロックで応答し、 [Add duration to date time]を呼び出すように依頼してきます。 私たちはそれを呼び出し、 その結果をClaudeに渡します。これでClaudeは 私たちの元のクエリに応答するのに十分な情報を持つことになります。 さて、私がこの例を特に示している理由はここにあります。 実際のユーザーから元のユーザーメッセージの入力を取得している場合、 ユーザーが何をClaudeに尋ねるかを正確に予測することはできません。 したがって、ユーザーは、 答えるために複数の異なるツール呼び出しを必要とするような、 奇妙なクエリを尋ねるかもしれません。 したがって、ツール呼び出しをアプリケーションに追加する際には、 この種の状況を許容する必要があります。 Claudeにクエリを送信する際には常に、 Claudeが連続して複数のツールを使用したい可能性があると想定する必要があります。 そして、Claudeが私たちに応答する際には、 応答を見て、Claudeがツールを使用するように要求しているかどうかを確認する必要があります。 そうでない場合は、ユーザーに最終的な応答を返せる 最終的な応答があることを知っています。 ここに擬似コードの例があります。 会話を実行する関数を作成し、初期メッセージのリストを渡します。 次に、whileループ内で、Claudeにアクセスして応答を取得します。 次に、その応答を確認します。Claudeが ツール使用を要求していない場合、 ユーザーに送信する応答があることがわかります。それ以外の場合は、 Claudeがツールを使用したい場合は、ツールを実行し、 結果のツール結果ブロックを取得し、 それらをユーザーメッセージに追加し、 Claudeを再度実行します。 すべてwhileループ内で行います。 このビデオの残りの部分では、ノートブックをリファクタリングして、 まさにこのような関数を構築します。 したがって、[Run conversation]のような関数を構築し、 全く同じ一連の操作を実行します。 しかし、この関数をまとめるためには、少し作業が必要です。 [Add user message]および [Add assistant message]ヘルパーをリファクタリングし、 チャット関数も同様に行う必要があります。 ノートブックで定義する準備として行うことのリストをまとめました。 ステップ1では、 [Add user message]および [Add assistant message]ヘルパー関数をアップグレードして、 複数のメッセージブロックをより適切に処理できるようにします。 ツールを使い始めると、Claudeから 複数のブロックが含まれる応答が返ってくることを覚えておいてください。 そして現在、私たちの [Add user message]および [Add assistant message]ヘルパー関数は完全に設定されており、 常にプレーンテキストブロックのみを扱っていると仮定しています。 それ以外は何もありません。 したがって、それをノートブックで早速処理しましょう。 ここでは、引き続き同じノートブックを使用しています。 画面で何をしているかをよりよく見せるために、 末尾にあったいくつかのサンプルツール呼び出しセルを削除しました。 さて、ヘルパー関数セルを拡張します。 [Add user message]と [Add assistant message]を見つけます。 つまり、現在、常に テキストを取得して、それを直接コンテンツプロパティに割り当てていると仮定しています。 したがって、今度はここで少し柔軟性を持たせたいです。 そこで、このように行います。 セルの先頭に、Anthropic.typesから Messageをインポートします。 次に、ここにある2番目の引数を変更します。 テキストではなく、messageと呼びます。 この辞書をこのように展開します。 そして、テキストを message.contentに更新します。 もしmessageがMessage型なら、そうでなければmessage。 Assistant messageも同様です。ここで、 これをmessageに変更し、辞書を展開します。そして、時間を節約するために、 そのステートメントをここにコピーします。 さて、このセルを再度実行します。 At the top of the cell, I'm going to add an import from Anthropic.types. I will import message. Then I'm going to rename the second argument right here. Instead of text, I'm going to call it message. I'm going to expand this dictionary like so. And I'm going to update text to be message.content if isinstance(message, Message) else message assistant message as well. So down here, I'm going to rename that to message. I will expand the dictionary. And then to save time, I will copy that statement right there to right there. All right, so now I'm going to rerun the cell and I'll show you what this refactor is going to do for us. So back down here. I'm going to add in a quick example call like so. So I'm just asking Claude to print out the current time in our minute second format. And I'm providing our get current daytime tool. I'm then going to print out the message or response we get back. So if I run this, we'll see that we get the usual message like so. And inside there is the content property that has both a text block and a tool use block. So now to very easily add this in to my message history as a assistant message, I would call Add Assistant Message with Messages, and then I can now put in that entire response, the entire message that I just got back. So I'll call that and then print out Messages on the next cell down. And there we go. I've got my entire message history being built up. Another way that I could run this is to put in response.content, like so. This will work just as well. So if I do that, and then printout messages, I still get the correct thing. And then, of course, if I want to, I could always put in a plain string here as well. And printout messages. And we'll see that yep, still building up that response history. So now we have a much more flexible helper function in add user message and add assistant message. We could put in a plain string or a list of blocks or an entire message and it will deconstruct the thing for us. This is going to make dealing with a message that has some tool use blocks inside of it much easier down the line. Onto step two of our refactor. We are going to update the chat function to receive a list of tool schemas. And we'll take that list of schemas and pass it through to the client messages create function call. In addition, from the chat function, we are no longer going to return plain text out of the first block that comes inside of the assistant message. Instead, we will return the entire message that we got back from Claude. Once again, this is because we are now anticipating getting back responses from Claude that have multiple blocks inside them. And at present, our chat function is always assuming that we are only ever getting back one block, just a single text block and nothing else. So back over here, here's the chat function. I'm going to add in a tools. They'll be defaulted to be none. And then we are going to wire it up in the same way that we did system right here. So we'll say if there are any tools that were passed in, we will add that in as the tools parameter. Next up, I'm going to go down to the return statement. So right here. As I just mentioned a moment ago, our chat function is currently set up assuming that we're always going to get back a single block from Claude, and that the block is always going to be a text block. That's why we have this code right here. We are making a really big assumption that we're always getting back that one single block and it's always going to contain some text. Because we are now making use of tools, that is no longer the case. We might get back a message that has multiple blocks inside it, so multiple entries inside this content list. One of them might be a text block, but we don't necessarily have a guarantee. So rather than always making this assumption, I'm now going to return the entire message. This is going to be a little bit less convenient for us because now if we ever want to get access to the text, we're going to have to do a little bit more work, but it's definitely a lot safer because again, this really reflects reality. Okay, that's that. So now on that same kind of note, we're going to now add in a little helper function. We're going to call it text from message. And the goal here is to take a look at a message, take a look at all the blocks, find all the text blocks, and just extract the text from those. So this is kind of replacing the functionality that we just removed. It's going to make it a lot easier to extract all the text out of a given message. So I'm going to add in that helper function right underneath chat. I'll call it text from message. It's going to receive a message. And inside of here, I'm going to return a new log new line that is going to join together a comprehension with block.text.for block in message.content if block.type is equal to text. So this is going to take a look at all the different blocks inside of a message. And if the block is a text block, then we're going to just extract the blocks text and then join all the block text together and return it. So again, just a helper function to make it a little bit easier to get all the text out of a particular message. All right, so we've taken care of most of our refactor. So now the last step, which we're going to take care of in just a moment, is add in support for multiple tool calls inside of a single conversation. So essentially, we need to implement a function like this. We need to make a function that's going to take in the list of messages, and then continue calling Claude until we get back a sign that Claude doesn't want to call a tool anymore.
