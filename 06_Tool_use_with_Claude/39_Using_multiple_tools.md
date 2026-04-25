# 39. Using multiple tools

**URL:** https://anthropic.skilljar.com/claude-with-the-anthropic-api/287749
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
                                
                            
                        
                    
                
            
            
                
                
                
                    Using multiple tools
                    
                
                
                    
                        
                            
                                
                                    

    
    

    
    
        
            
        
        
            
                
                This video is still being processed. Please check back later and refresh the page.
            
        
        
            
                Uh oh! Something went wrong, please try again.
            
        
    

    

                                
                            
                        
                    
                
            
        
        
            

    
        
            
                
                    
                        
                            
                        
                    
                
            
            
                
                    Summary
                

                

            
        

        
            
                
                    
                        
                            Summary

                            
                                Adding multiple tools to your Claude implementation becomes straightforward once you have the core tool-handling infrastructure in place. This tutorial shows how to integrate additional tools by following a simple pattern.

The Tools We're Adding

We need three main capabilities for our reminder system:

Get current date time - Claude needs to know the current date and time
Add duration to date time - Claude isn't perfect with date time addition
Set a reminder - Need a way to set a reminder

The good news is that most of the implementation work is already done. The add_duration_to_datetime function and set_reminder function are provided, along with their corresponding schemas.

Adding Tools to the Conversation

First, update the run_conversation function to include the new tool schemas in the tools list:

response = chat(messages, tools=[
    get_current_datetime_schema,
    add_duration_to_datetime_schema,
    set_reminder_schema
])

This tells Claude about all three available tools it can use during the conversation.

Updating the Tool Router

Next, modify the run_tool function to handle the new tool calls. Add elif cases for each new tool:

def run_tool(tool_name, tool_input):
    if tool_name == "get_current_datetime":
        return get_current_datetime(**tool_input)
    elif tool_name == "add_duration_to_datetime":
        return add_duration_to_datetime(**tool_input)
    elif tool_name == "set_reminder":
        return set_reminder(**tool_input)

The pattern is simple: check the tool name, call the corresponding function with the provided input, and return the result.

Testing Multiple Tool Usage

To test the system, try a request that requires multiple tools: "Set a reminder for my doctors appointment. Its 177 days after Jan 1st, 2050."

This request forces Claude to:

Calculate the date (using add_duration_to_datetime)
Set the reminder (using set_reminder)

Claude handles this by first explaining what it needs to do, then making the appropriate tool calls in sequence. The conversation shows Claude calculating June 27, 2050 as the target date, then setting the reminder for that date.

Understanding the Message Flow

When you examine the conversation history, you'll see the complete message structure:

User message with the request
Assistant message containing both text and tool use blocks
Tool result messages
Follow-up assistant messages

This demonstrates how Claude can include multiple blocks in a single message - combining explanatory text with tool usage requests.

The Simple Pattern for Adding Tools

Once you have the core tool infrastructure, adding new tools follows this pattern:

Create the tool function implementation
Define the tool schema
Add the schema to the tools list in run_conversation
Add a case for the tool in run_tool

This modular approach makes it easy to expand your AI assistant's capabilities without restructuring existing code. Each new tool integrates seamlessly with the existing conversation flow and tool-handling logic.
                            
                        
                    

                    
                        
                            Downloads
                            
                                
                                    
                                        
                                            
                                            
                                                001_tools_009.ipynb
                                                (opens in new tab)

---

## 🎬 Transcript (English)

The last thing we need to do is add in the Add Duration to DateTime tool and the Set Reminder tool. This is going to be a little bit anti-climactic because last video was rather challenging. This one is going to be really easy, short and straightforward. Turns out I've already put together a lot of the code that we need for this inside of the Tools and Schemas cell. You'll find that I've already got an implementation of add_duration_to_datetime, but together inside of here. And if you scroll down, you'll see I've also got our set_reminder function put together. Now the set_reminder doesn't actually set a reminder or anything like that. It's just going to print out a statement that says, hey, we set a reminder at this time with some given content. I've also provided us a add_duration_to_date time schema and a set_reminder schema. So all we really need to do is pass these two schemas into Claude, and we also need to make sure that if Claude ever asked to use either tool, we call the appropriate tool function. So let's get to it. Should be pretty straightforward. First off, I'm going to find the run_conversation function. Inside of here, I'm going to find the list of tools, and I'm going to add into it, add_duration_to_date time schema, and the set_reminder schema as well. So now Claude is aware of the existence of these two other tools. Next, all I have to do is go up a little bit here to the run_tool function. So this is the function where we're going to get a tool name and some arguments. All we have to do is find the appropriate tool function call, call it, and return result. So adding into the thing is really easy. Let's add in an if case. So check and see if the tool name is add_duration_to_date time. And if it is, we'll return a call to add_duration_to_date time and **tool_input. I'll then repeat that for the other tool. So the tool name is set_reminder return set_reminder with **tool_input. And that's it. So set_reminder with tool input. And that's it. So as soon as you put together this run_tool function and the run_conversation function, after that initial difficulty, everything around tool use starts to become really easy and straightforward, because adding in additional tools is super simple. Just update run_tool, add in a tool schema, add in an implementation for the actual tool function itself, and that's it. You're all done. So now let's test this out. I'm going to make sure I rerun that cell. I'm going to rerun run_conversation. And then down here at the very bottom, let's update our query. I'm going to ask Claude to set a reminder. And I'm going to say that the reminder needs to be set 177 days after January 1st, 2050. This is definitely going to result in more than one tool call. Claude is going to first have to add_duration_to_datetime, and then set a reminder after that. Let's then run this and see how it does. Claude initially tells us that it needs to figure out 177 days after January 1st. Once it figures that out, it's then going to attempt to set the reminder. Then we see a log statement right here. This log statement is coming from the set_reminder function. Remember, set_reminder doesn't actually do anything, it just prints out the argument that it's given. And then finally, we get a response from Claude telling us that our appointment has been set on the correct date of Monday, June 27th of 2050. We can also go down to the message conversation history. So once again, we've got the user message, the assistant right here that has a text block. And in addition to the text block, once again, a tool use block. So yet again, we're seeing an example here of a message with multiple different blocks inside of it. We then respond with the tool results. We then get some follow up. And from there, I think you understand the process. All right, so that's it. We have wired in multiple different tools to our notebook. Excellent progress.

---

## 🎬 トランスクリプト（日本語）

最後に行うのは、Add Duration to DateTime ツールと Set Reminder ツールを追加することです。これは 少しばかり地味な内容になります。なぜなら、前回の 動画はかなり大変でしたが、今回は非常に簡単で、 短く、分かりやすいものになるからです。既に、 このために必要なコードの多くを Tools and Schemas のセルに まとめたことがわかりました。`add_duration_to_datetime` の実装は 既に組み込んでありますが、ここにあります。そして、下にスクロールすると、 `set_reminder` 関数も組み込んであるのが見えるでしょう。 `set_reminder` は実際にリマインダーを設定するものではありません。 ただ、「この時間で、指定された内容でリマインダーを設定しました」という メッセージを出力するだけです。 また、`add_duration_to_date` time スキーマと、`set_reminder` スキーマも提供しています。 ですから、やるべきことは、これらの2つのスキーマを Claude に渡すことと、Claude がどちらかのツールを使うように指示してきたら、 適切なツール関数を呼び出すことを確認することだけです。 では、始めましょう。非常に簡単なはずです。 まず、`run_conversation` 関数を探します。 この中で、ツールのリストを探し、そこに `add_duration_to_date` time スキーマと、`set_reminder` スキーマも追加します。これで Claude は これら2つのツールが存在することを認識しました。次に、 少し上にスクロールして `run_tool` 関数に行きます。これは、 ツール名と引数を受け取る関数です。私たちがやるべきことは、 適切なツール関数呼び出しを見つけて、 それを呼び出し、結果を返すことです。ですから、 これに追加するのは非常に簡単です。if 文を 追加しましょう。なので、ツール名が `add_duration_to_date` time であるかどうかを確認し、そうであれば `add_duration_to_date` time(**tool_input) を呼び出して返します。もう一方のツールも同様に行います。 つまり、ツール名は `set_reminder` で、 `set_reminder`(**tool_input) を返します。これで終わりです。 つまり、`set_reminder`(**tool_input) です。これで終わりです。 ですから、この `run_tool` 関数と `run_conversation` 関数をセットアップすると、最初の 困難の後、ツール利用に関するあらゆることが非常に 簡単で分かりやすくなります。なぜなら、追加のツールを 追加するのは非常に簡単だからです。`run_tool` を更新し、 ツールスキーマを追加し、実際の ツール関数の実装を追加するだけです。それで完了です。では、 テストしてみましょう。セルを再度実行したことを確認します。 `run_conversation` を再度実行します。そして、 一番下の方にあるクエリを更新しましょう。Claude にリマインダーを設定するように依頼します。 そして、リマインダーは2050年1月1日から 177日後に設定する必要があると伝えます。これは間違いなく 複数のツール呼び出しにつながるでしょう。Claude はまず `add_duration_to_datetime` を呼び出し、その後 リマインダーを設定する必要があります。では、これを実行して どのように動作するか見てみましょう。Claude は最初に、 1月1日から177日後を計算する必要があると述べています。 それが終わると、リマインダーの設定を試みます。そして、ここにログメッセージが表示されます。 このログメッセージは `set_reminder` 関数からのものです。思い出してください、 `set_reminder` は実際には何もせず、与えられた引数を 出力するだけです。そして最後に、Claude からの応答があり、 私たちの予定は2050年6月27日月曜日に設定されたと伝えられます。 メッセージの会話履歴にも行くことができます。 改めて、ユーザーメッセージがあり、その後に テキストブロックを持つアシスタントがあります。 そして、テキストブロックに加えて、またしてもツール 使用ブロックがあります。つまり、ここでも複数のブロックを持つメッセージの例を見ることができます。次に、 ツール結果で応答します。その後、フォローアップがあります。そして、 そこから、プロセスを理解できたと思います。 さて、これで終わりです。ノートブックに複数のツールを 組み込みました。素晴らしい進歩です。
