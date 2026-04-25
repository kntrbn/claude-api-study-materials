# 06. Multi-Turn conversations

**URL:** https://anthropic.skilljar.com/claude-with-the-anthropic-api/287735
**Section:** 03 Accessing Claude with the API

---

## 📄 Page Content

Anthropic Academy
    
  

  
    
      Courses
    
  

    

    
      
      

      
        
          My Profile
        
        
      

      
      

      
        Sign Out
      
    
  

  

  

    
    
    
        
            
    
        
    

            
    
        
        
            
                
                    
                        
                            
                                
                            

                            
                                details
                            

                            
                        
                    
                
            
            
                
                
                
                    Multi-Turn conversations
                    
                
                
                    
                        
                            
                                
                                    

    
    

    
    
        
            
        
        
            
                
                This video is still being processed. Please check back later and refresh the page.
            
        
        
            
                Uh oh! Something went wrong, please try again.
            
        
    

    

                                
                            
                        
                    
                
            
        
        
            

    
        
            
                
                    
                        
                            
                        
                    
                
            
            
                
                    Summary
                

                

            
        

        
            
                
                    
                        
                            Summary

                            
                                When working with the Anthropic API and Claude, there's a crucial concept you need to understand: Claude doesn't store any of your conversation history. Each request you make is completely independent, with no memory of previous exchanges.

This means if you want to have a multi-turn conversation where Claude remembers context from earlier messages, you need to handle the conversation state yourself.

The Problem with Stateless Conversations

Let's say you ask Claude "What is quantum computing?" and get a good response. Then you follow up with "Write another sentence" - Claude has no idea what you're referring to. It will write a sentence about something completely random because it has no memory of the quantum computing discussion.

How Multi-Turn Conversations Work

To maintain conversation context, you need to do two things:

Manually maintain a list of all messages in your code
Send the complete message history with every request

Here's the flow that actually works:

Send your initial user message to Claude
Take Claude's response and add it to your message list as an assistant message
Add your follow-up question as another user message
Send the entire conversation history to Claude

Building Helper Functions

To make conversation management easier, you can create three helper functions:

def add_user_message(messages, text):
    user_message = {"role": "user", "content": text}
    messages.append(user_message)

def add_assistant_message(messages, text):
    assistant_message = {"role": "assistant", "content": text}
    messages.append(assistant_message)

def chat(messages):
    message = client.messages.create(
        model=model,
        max_tokens=1000,
        messages=messages,
    )
    return message.content[0].text

Putting It All Together

Here's how you use these functions to maintain a conversation:

# Start with an empty message list
messages = []

# Add the initial user question
add_user_message(messages, "Define quantum computing in one sentence")

# Get Claude's response
answer = chat(messages)

# Add Claude's response to the conversation history
add_assistant_message(messages, answer)

# Add a follow-up question
add_user_message(messages, "Write another sentence")

# Get the follow-up response with full context
final_answer = chat(messages)

Now Claude will understand that "Write another sentence" refers to expanding on the quantum computing definition, because you've provided the complete conversation context.

These helper functions will be useful throughout your work with Claude, making it much easier to build applications that can maintain meaningful conversations over multiple exchanges.

---

## 🎬 Transcript (English)

The code we've written out so far simulates a very simple exchange with our model. And we can kind of visualize this conversation inside of a chat box like this. We sent in a request asking something like what's quantum computing, answer in one sentence. And we got a very simple single sentence reply. Naturally, we might want to continue this conversation at some point in time. So we might want to be able to send in a follow up asking something like write another sentence. And we would then expect to get back a response that expands on quantum computing in some way. To have a multi-message conversation like this, there's something really critical that you need to understand around the Anthropic API and Claude itself. And that is that the Anthropic API and Claude do not store any messages that you send to it. None of the messages you send get stored in any way, and none of the responses that you get back are stored in any way. So if you ever want to have some kind of conversation going on, where you have multiple messages that kind of maintain a context or flow, then there are two things that you need to do. You need to manually, inside of your code, maintain a list of all the messages that you are exchanging. And second, you need to make sure that you provide that entire list of messages with every follow-up request that you make. So let's go into some detail on this entire idea, just make sure it's really clear and you understand what's going on here. The first thing I want to do is write out a little bit of sample code just to prove to you that Claude doesn't store any messages or anything like that. And I can prove this by trying to simulate this kind of conversation where I first ask what quantum computing is and then ask right another sentence. So back inside of my notebook, I'm going to go to the cell where I initially asked what is quantum computing. And I want to paste in a second request to Claude that I wrote out ahead of time. So in this second request, I'm asking Claude to write another sentence, and I'm going to print out the text inside of that follow-up request. So now we've kind of got a simulation of what's going on right here, where we ask that first question and then send in a follow-up. And we're going to see that we don't get back any kind of legible or any usable text here. So I'm going to run this and we'll see what happens. So back over here, I'm going to run that cell now and we're going to see that we get back something that has absolutely nothing to do with quantum computing at all. So again, to make sure that it's really clear why we are seeing this result and not seeing something about quantum computing, let's go over a couple of diagrams. All right, so in this diagram, I'm going to first show you exactly what's going on with the query code that I've written out, where we are getting back a response that has nothing to do with quantum computing. So initially, I make a similar quest to Claude, where I have one user message, and I'm asking Claude to define quantum computing in one sentence. I then get back a response that is exactly what I would expect. Claude gives me back a one-sense definition of quantum computing. Then I make a second request where I have only one message inside the body. And the only message is asking Claude to write another sentence. When I send this in, Claude has no memory of any past conversation or any previous messages that I exchanged with it. So Claude is just going to do the best it can to fulfill my request. It's going to write out some sentence, but it definitely is probably not going to be about quantum computing. So now let me show you what we need to do to fix this problem. Here's how we're going to solve the issue. First, we're going to once again make that initial request with just one user message. Then we're going to take that assistant message that we get back and append it into a list of messages. So we're going to take the assistant right there and we can imagine we're going to add it into our list on the left-hand side. Then, when we want to follow up on this conversation or continue it in some way, we're going to append on a user message at the bottom. So now we can read this as like a real conversation. I asked to find quantum computing, I got back a response, and now I'm adding in another question or another query that I want to ask Claude. In this case, write another sentence. Now when I send in this list of messages to Claude, it will have the entire context and history of the whole conversation. It's seen all the previous messages that we've exchanged around this line of questioning. And hopefully, Claude will be able to give us back a more reasonable answer, hopefully a one sentence follow up that's going to extend its previous answer a little bit more. To see this entire flow in action, I'm going to go back over to my notebook and we're going to try to write out some code that will allow us to maintain the full context for a conversation. Back inside of my notebook, I'm going to get started by making three different helper functions that are going to aid us in maintaining the history or context of a conversation. We're going to end up using these helper functions quite a bit throughout the remainder of this course. So in this cell right here, I'm going to give myself a little bit of space at the top and then define our first helper function that will aid us in maintaining this history. I'm going to name this function add user message. It's going to take in a list of messages and some text. I'm then going to make a variable of user message. That's going to have a role of user and some content of whatever text we pass in. And then I'm going to append this new user message into the list of messages. Next, I'm going to add in a second helper function that's going to specialize in adding in assistant messages to a history. So I'm going to copy this function right here just to save a little bit of time. I'll rename it to add assistant message. And I'll go through and wherever I see the word user, I'm gonna change it out to assistant. So right there, right there, and right there. Okay, now onto our third helper function. I'm going to take our messages.create function call down here. And I'm going to rename it to chat. Whenever I call chat, I'm gonna pass in a list of messages. So this is gonna be like my message history. Then I'm going to indent our call right here. I'm going to replace messages with the Messages argument, and then return from this function is going to be message content at zero dot text. All right, so here are the three helper functions. And again, we're going to use these quite a bit throughout the remainder of this entire course. These helper functions are going to make it significantly easier for us to have a conversation that maintains some history or context over time. So now let me give you a demonstration of how we're going to put them to use. All right, so down here in the next cell down, I'm gonna write in a couple of comments that she's gonna guide us through the process of maintaining a conversation that has some history tied to it. I'll first begin by making an empty list of messages. So this message is variable right here, we can imagine is storing our entire conversation history. Over time, we're gonna add in a collection of different user and assistant messages to it. Next, I'm going to add in my initial user message. So I will call the add user message function. I'll pass in the list of messages that I'm appending messages to, and then my user text is going to be define quantum computing in one sentence. Now, just to make sure we're going down the right path here, I'm going to print out the list of messages and run the cell. And we can see right away that we have a correct structure of messages. So I have a list. It has a dictionary inside of it with a role of user and a content that contains something that I want to feed into Claude. So now we can easily call Claude by making use of that chat function that we just put together. I'm going to call chat and pass in my list of messages. And then out of that, we'll get back some kind of answer. I'm going to print out the answer and run the cell again. So we get the response, we should see a sentence here about quantum computing. So now we are in this situation. We have sent an initial message into Claude and gotten an assistant message back in response. Now we need to take this answer and append it into our conversation history. So we need to add in or append it in by making use of the add assistant message function that we just defined. So back over here. I'm going to call add assistant message. I want to add into our list of messages and I want to add in specifically the content out of the answer that we just got back. So now let's do another check and make sure that our list of messages is looking correct. If I print out messages, I should see my user message, then the followup assistant with the content that we got back from Claude. Okay, so that looks good. So now onto the last step. We're going to append in one last user message and send the entire conversation history into Claude once again. So for that, I'll do another add user message with my list of messages. And then my followup question here or my followup request is going to be write another sentence. I'm then going to call chat again with the updated list of messages. I'll assign that to answer, and then I will print answer out. So let's now run this and see how we are doing. All right, after a brief pause, we get what is definitely a follow-up message that is definitely still about quantum computing. And so it appears that we have correctly maintained our entire conversation history. All right, so this is looking pretty good. We now have three reusable helper functions that we're going to continue to make use of throughout the remainder of the course.

---

## 🎬 トランスクリプト（日本語）

これまで記述したコードは、非常にシンプルなやり取りをシミュレートするものです。 この会話を、このようなチャットボックス内で視覚化することができます。 私たちは何かを尋ねるリクエストを送りました。例えば、「量子コンピューティングとは何ですか？」 「一文で答えてください。」と。 そして、非常に簡単な単一の文の返答を得ました。 当然ながら、私たちは会話を続けたいと思うかもしれません。 ですから、何かを尋ねるフォローアップを送信したいかもしれません。 例えば、「もう一文書いてください。」と。 そして、私たちは 量子コンピューティングを何らかの形で拡張する応答を得ることを期待するでしょう。 このようにマルチメッセージの会話を行うためには、Anthropic APIとClaude自体について 理解する必要がある非常に重要なことがあります。 それは、Anthropic APIとClaudeは、あなたが送信したメッセージを 保存しないということです。 あなたが送信したメッセージはどれも、 一切保存されませんし、あなたが受け取る応答も 一切保存されません。 したがって、もしあなたが会話を続けるようなことがしたいのであれば、 複数のメッセージがコンテキストや流れを維持する場合、 あなたは2つのことを行う必要があります。 コード内で、交換するすべてのメッセージのリストを 手動で維持する必要があります。 そして第二に、フォローアップリクエストのたびに そのメッセージのリスト全体を提供するようにする必要があります。 それでは、このアイデア全体について詳しく見ていきましょう。 それが本当に明確であることを確認するために そして何が起こっているかを理解していることを確認するために。 まず最初に行いたいのは、少しサンプルコードを書いて Claudeがメッセージを保存していないことを証明することです。 そして、量子コンピューティングとは何かを尋ね、 次に「もう一文書いてください」と尋ねる 会話をシミュレートすることで、これを証明できます。 ですから、ノートブックに戻って、最初に 量子コンピューティングとは何かを尋ねたセルに移動します。 そして、事前に作成した2番目のリクエストをClaudeに貼り付けたいと思います。 この2番目のリクエストでは、 Claudeにもう一文書いてくれるように頼んでいます。 そして、そのフォローアップ リクエスト内のテキストを印刷します。 これにより、ここで何が起こっているかのシミュレーションが得られます。 最初の質問をして、 その後フォローアップを送信します。 そして、ここで読み取り可能または使用可能な テキストが得られないことがわかります。 ですから、これを実行するとどうなるか見てみましょう。 さて、ここではそのセルを実行します。 そして、量子コンピューティングとは全く関係のないものが返ってくるのがわかるでしょう。 ですから、もう一度、この結果が見られる理由と 量子コンピューティングに関するものが見られない理由を明確にするために、 いくつかの図を見てみましょう。 この図では、まず私が書いたクエリコードで 何が起こっているのかを示します。そこでは、返答が 量子コンピューティングとは全く関係のないものになっています。 最初に、私はClaudeに似たリクエストをします。 ユーザーメッセージは1つで、Claudeに量子コンピューティングを 一文で定義するように求めています。 そして、期待通りの返答を得ます。 Claudeは量子コンピューティングの一文での定義を返します。 次に、ボディにメッセージが1つしかない 2番目のリクエストを行います。 その唯一のメッセージは、Claudeにもう一文書くように依頼することです。 これを送信すると、Claudeは過去の会話や、 以前のメッセージの記憶を持っていません。 したがって、Claudeは私のリクエストを最大限に満たすように努めるだけです。 何か一文を書くでしょうが、 おそらく量子コンピューティングに関するものではないでしょう。 では、この問題を解決するために何が必要かを示しましょう。 この問題に対処する方法は以下の通りです。 まず、ユーザーメッセージが1つだけの 最初の要求を再び行います。 次に、受け取ったアシスタントメッセージを メッセージのリストに追記します。 ですから、右側のアシスタントを取得し、それを左側のリストに追加すると想像してください。 次に、この会話をフォローアップしたり、 何らかの方法で継続したりする場合、 下部にユーザーメッセージを追記します。 これで、実際の会話のように読むことができます。 私は量子コンピューティングを定義するように求め、返答を得ました。 そして今、別の質問や クエリを追加しています。 この場合、「もう一文書いてください。」 これをClaudeに送信すると、 会話全体とその履歴のコンテキストがすべて含まれます。 私たちは、この質問ラインに関する 以前のメッセージをすべて見てきました。 そしてうまくいけば、Claudeは より妥当な回答、できれば以前の回答を 少し拡張するような一文のフォローアップを 提供できるでしょう。 この全体のフローを実際に見るために、 ノートブックに戻り、完全な コンテキストを維持できるようなコードを書いてみましょう。 ノートブックに戻ります。まず、会話の履歴や コンテキストの維持に役立つ 3つのヘルパー関数を作成します。 これらのヘルパー関数は、このコースの残りの部分で かなり頻繁に使用することになります。 ですから、このセルでは、 上部に少しスペースを空けて、 この履歴の維持に役立つ最初のヘルパー関数を定義します。 この関数をadd user messageと名付けます。 メッセージのリストとテキストを受け取ります。 そして、user messageという変数を作成します。 この変数にはroleがuserで、 contentには渡されたテキストの内容が含まれます。 そして、この新しいuser messageを メッセージのリストに追記します。次に、 履歴にアシスタントメッセージを追加することに特化した 2番目のヘルパー関数を追加します。 少し時間を節約するために、この関数をコピーします。 これをadd assistant messageに名前変更します。 そして、userという単語を見るところすべて assistantに変更します。そこで、そこで、そこでです。 OK。 では、3番目のヘルパー関数に進みます。 messages.create関数を ここに持ってきて、chatに名前変更します。 chatを呼び出すたびに、メッセージのリストを渡します。 これはメッセージ履歴のようになります。その後 この呼び出しをインデントします。 messagesをMessages引数に置き換えます。 そして、この関数からの戻り値は message content at zero dot textになります。 これで、3つのヘルパー関数が揃いました。 そして、これらの関数は、このコースの残りの部分で かなり頻繁に使用することになります。 これらのヘルパー関数により、会話の履歴やコンテキストを 維持する会話を、はるかに容易に行うことができます。 では、それらをどのように活用するかのデモンストレーションをします。 さて、次のセルでは、 履歴を持つ会話を維持するプロセスをガイドしてくれる いくつかのコメントを記述します。 まず、空のメッセージリストを作成します。 ですから、このメッセージ変数には 会話履歴全体が格納されていると想像してください。 時間をかけて、さまざまなユーザーメッセージやアシスタントメッセージを それに追加していきます。 次に、最初のユーザーメッセージを追加します。 add user message関数を呼び出します。 メッセージを追加しているメッセージのリストを渡します。 そして、ユーザーテキストは 「量子コンピューティングを一文で定義してください」となります。 ここで正しい方向に進んでいることを確認するために、 メッセージのリストを印刷してセルを実行します。 そして、正しいメッセージ構造がすぐにわかります。 リストがあり、その中にロールがuserで、 内容にClaudeにフィードしたいものが含まれる辞書があります。 これで、先ほど作成したchat関数を活用して Claudeに簡単に呼び出すことができます。 chatを呼び出し、メッセージのリストを渡します。 そして、そこから何らかの回答が得られます。 回答を印刷して、再度セルを実行します。 返答を得るので、ここに一文が表示されるはずです。 量子コンピューティングについて。 さて、私たちは今この状況にいます。 Claudeに最初のメッセージを送信し、 アシスタントからの返答を受け取りました。 今、この回答を会話履歴に 追記する必要があります。 ですから、定義したadd assistant message関数を使って 追記する必要があります。 戻って、add assistant messageを呼び出します。 メッセージのリストに追加したいのですが、 特に受け取った回答のコンテンツを追加したいです。 では、メッセージリストが 正しくなっているか再度確認しましょう。 メッセージを印刷すると、ユーザーメッセージ、 そしてClaudeから受け取ったコンテンツのアシスタントの フォローアップが見えるはずです。 これで最後のステップに進みます。 最後のユーザーメッセージを追記し、 会話履歴全体を再度Claudeに送信します。 そのために、もう一度 add user messageをメッセージリストで呼び出します。 そして、フォローアップの質問は 「もう一文書いてください」です。 そして、chatを再度 更新されたメッセージリストで呼び出します。 それをanswerに代入し、answerを印刷します。 それでは、これを実行して、私たちの進捗を確認しましょう。 少し待った後、間違いなく フォローアップメッセージであり、 間違いなく量子コンピューティングに関するものです。 したがって、会話履歴全体を正しく維持できたようです。 さて、これはかなりうまくいっています。 これからコースの残りの部分で引き続き使用する 3つの再利用可能なヘルパー関数があります。
