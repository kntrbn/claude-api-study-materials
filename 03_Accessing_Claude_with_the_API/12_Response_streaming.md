# 12. Response streaming

**URL:** https://anthropic.skilljar.com/claude-with-the-anthropic-api/287734
**Section:** 03 Accessing Claude with the API

---

## 📄 Page Content

Anthropic Academy
    
  

  
    
      Courses
    
  

    

    
      
      

      
        
          My Profile
        
        
      

      
      

      
        Sign Out
      
    
  

  

  

    
    
    
        
            
    
        
    

            
    
        
        
            
                
                    
                        
                            
                                
                            

                            
                                details
                            

                            
                        
                    
                
            
            
                
                
                
                    Response streaming
                    
                
                
                    
                        
                            
                                
                                    

    
    

    
    
        
            
        
        
            
                
                This video is still being processed. Please check back later and refresh the page.
            
        
        
            
                Uh oh! Something went wrong, please try again.
            
        
    

    

                                
                            
                        
                    
                
            
        
        
            

    
        
            
                
                    
                        
                            
                        
                    
                
            
            
                
                    Summary
                

                

            
        

        
            
                
                    
                        
                            Summary

                            
                                When building chat applications with Claude, there's a significant user experience challenge: responses can take 10-30 seconds to generate, leaving users staring at a loading spinner. The solution is response streaming, which lets users see text appear chunk by chunk as Claude generates it, creating a much more responsive feel.

The Problem with Standard Responses

In a typical chat setup, your server sends a user message to Claude and waits for the complete response before sending anything back to the client. This creates an awkward delay where users have no feedback that anything is happening.

How Streaming Works

With streaming enabled, Claude immediately sends back an initial response indicating it has received your request and is starting to generate text. Then you receive a series of events, each containing a small piece of the overall response.

Your server can forward these text chunks to your client application as they arrive, allowing users to see the response building up word by word. All of these events are part of a single request to Claude.

Understanding Stream Events

When you enable streaming, Claude sends back several types of events:

MessageStart - A new message is being sent
ContentBlockStart - Start of a new block containing text, tool use, or other content
ContentBlockDelta - Chunks of the actual generated text
ContentBlockStop - The current content block has been completed
MessageDelta - The current message is complete
MessageStop - End of information about the current message

The ContentBlockDelta events contain the actual generated text that you'll want to display to users.

Basic Streaming Implementation

To enable streaming, add stream=True to your messages.create call:

messages = []
add_user_message(messages, "Write a 1 sentence description of a fake database")

stream = client.messages.create(
    model=model,
    max_tokens=1000,
    messages=messages,
    stream=True
)

for event in stream:
    print(event)

Simplified Text Streaming

Rather than manually parsing events, you can use the SDK's simplified streaming interface that extracts just the text content:

with client.messages.stream(
    model=model,
    max_tokens=1000,
    messages=messages
) as stream:
    for text in stream.text_stream:
        print(text, end="")

This approach automatically filters out everything except the actual text content, which is usually what you need for displaying responses to users.

Getting the Complete Message

While streaming individual chunks is great for user experience, you often need the complete message for storage or further processing. After streaming completes, you can get the assembled final message:

with client.messages.stream(
    model=model,
    max_tokens=1000,
    messages=messages
) as stream:
    for text in stream.text_stream:
        # Send each chunk to your client
        pass
    
    # Get the complete message for database storage
    final_message = stream.get_final_message()

This gives you the best of both worlds: real-time streaming for users and a complete message object for your application logic.

---

## 🎬 Transcript (English)

I want to think back to the original chat interface example that we looked at earlier on inside this section. So remember, the thought process here is that we've got a chat window running inside of a web app or a mobile app. A user is going to enter a question. That's going to be submitted to our server. We're thinking of stuff that into a user message and send it off to Claude. Claude is then going to send us back an assistant message. We are going to extract the text from it and send it back down to our mobile app or web app. And hopefully, that content is going to appear on the screen. Now, this all sounds pretty straightforward and easy at this point in time, but there's one little issue here that we haven't really addressed just yet. You see, the time between sending that user message to Claude and then eventually getting an assistant message back can very easily take a lot more time than we expect. In some cases, it might take 10 seconds or all the way up to 30 seconds depending upon the size of the input user message and the output assistant message. Now during this entire time that the user is waiting for a response, we could just show a spinner on the screen. But that's not really a great user experience. Most users' expectations are that whenever they enter in some kind of initial message, like what is quantum computing, they should almost immediately start to see some response up here on the screen. To get this better user experience, we are going to use a technique known as streaming. So let me tell you a little bit about how streaming works. Our server is still going to send an initial user message off to Claude, but then Claude is going to almost immediately send back an initial response to us. This initial response doesn't actually contain any text content. Instead, it is really just a sign to our server that Claude has received our initial request and that Claude is about to start to generate some amount of text. We are then going to start to receive a stream of events. We're going to go into a lot of detail around exactly what these events are, but right now, just understand that they contain pieces of the generated response that we want to send back and eventually display to our users. The number of events that we receive depends upon how much text we are generating. Each event is going to contain just a little bit of the overall message that is being generated. So maybe the first event just has the text, quantum, and then the second one says computing, and the third one is, and so on. Now each event doesn't just contain one word. It might contain many words, or even in entire sentence. It really just depends upon how much time it takes for Claude to generate each little bit of text. Now, as I mentioned, our server is going to receive these events and our server can optionally take the text out of each event and immediately send it back down to our web app or mobile app or whatever else where we can display that little chunk of text on the screen. We can then repeat this process for each additional event that we receive on our server. So the net effect is that a user is going to start to see some text, start to appear chunk by chunk in the chat interface. Let's now go back over to our notebook and we're going to write out a little bit of code to better understand how streaming works. All right, so back inside of my notebook, I still have these three helper functions put together. Now, we are going to ignore the chat function inside of this video, because when we start to use streaming, it doesn't work quite so well with the chat function as we have implemented it. So I'm going to instead, down here, make a list of messages, and then manually call the clientmessages.create function. So I'm going to make an empty list of messages. I'll add in a user message to messages. And I'm going to ask Claude to write a one sentence description of a fake database. I'm then going to call client messages create. I will pass in the name of the model. Still need to provide a max tokens. Provide our list of messages. And then finally, we'll put in an additional keyword argument here of stream is true. And this is going to give us back not a final answer, but instead we're going to get a stream of different events. We can iterate through this thing because it is a normal iterator. So we can say for event in stream and then print out event. Now, if I run this, we're going to very quickly see a stream of different events up here on screen. So each of these represents a different little chunk of data that is being sent back to us by Claude. You'll notice that we start off with a event named raw message store event. We then get a raw content block start, a raw content block delta. We get several of those as a matter of fact. And then, down towards the bottom, we eventually get a content block stop event, a message delt event, any message stop event. So these are all events that are being sent back to us inside of the context of a single request, all coming from Claude. Each of these different events has some meaning in the context of the overall response that we are getting back from Claude. However, there is one event type that we usually care about a little bit more than all the others, and that is the raw, content block Delta event. This event is what contains the actual text that is being generated by Claude and sent back to us chunk by chunk. In practice, we usually end up getting the same sequence of events over and over. So when we get a response back from Claude, we're almost always going to start off with getting a message start, then a content block start, and then we are going to get a sequence of content block deltas. And again, those are what contain the actual text. So we usually want to collect all those different events and extract the text from them and send that text back down to our web app or mobile app or whatever else we are using. Now, back inside of our notebook, inside this for loop right here, we could add in a check to take a look and figure out what kind of event we are dealing with. And then if it is one of those raw content block delta events, we could reach into it and get the text we actually care about. But that would require a lot of extra code from us. Thankfully, the Anthropic SDK exposes a different way of creating a stream than what I'm showing to you right here. This alternative way of creating a stream, which I'm going to show you in just one moment, makes it a lot easier to just get the text out of the response. And again, the text is usually the part of the response that we really care about. So let me show you an alternative way of streaming a response. I'm going to go down to the next code cell. So down here, I'm going to again make a list of messages, add a user message with a write a one sentence description of a fake database. And then we're going to call a slightly different function and wrap it inside of a with block. So say with client messages dot stream. And inside of here, we will again put in our model, our max tokens, and our messages. But we do not need to add in the stream to true argument. We'll then say as stream, colon, all then indent, and inside of here, it will say for textinstream.textstream, like so. So now text is gonna be just the text part of those different events. So just the text we actually care about, again, that's almost always the thing that we actually really care about when we are streaming our response from clot. Now to show you how this actually works, I'm going to add in a print statement and log out that text. I'm going to add in a end true of empty string. And true of empty string, just make sure that these print statements are not going to add in a new line character to the end of the print statement. So we'll see each bit of text logged out next to each other. Now I'm going to run this and it's going to occur really quickly, but you'll see that now we are getting a response streamed back to us chunk by chunk. So let me do that again. So run again. I'll see chunk, chunk, chunk. There we go. You'll notice that each chunk contains multiple different words. So again, we're not guaranteed to just get back one single word inside of each event. We might get several. There is one last feature here that I want to show you. Now, as I've mentioned, we very often want to stream a response back to a mobile app or a web app so that a user can see each chunk of text appear on the screen as soon as possible. But something else we very often want to do after completing a stream is take the entire message and maybe store it inside of a database. So we have a record of the entire conversation that was had with a particular user. Let me show you how we can collect all these different events and present them all assembled together inside of one single final message. I'm going to replace this print statement right here with a pass, just so we don't have any printing there. And then after it, I'll do a stream.getfinalmessage. And now if I run this again, we are still streaming back a response and we could print it if we wanted to, but we're also going to take all the individual events we get back and assemble them together into one final message, which we could then store inside the database or do whatever else we need to do with it.

---

## 🎬 トランスクリプト（日本語）

最初のチャットインターフェースの例を振り返りたいと思います。 このセクションで先ほど見たものです。覚えていますが、 ここでの思考プロセスは、チャットウィンドウが内部で実行されているということです。 ウェブアプリまたはモバイルアプリ。ユーザーが質問を入力します。 それは私たちのサーバーに送信されます。私たちはそれを ユーザーメッセージとして扱い、Claudeに送信します。Claudeは アシスタントメッセージを返送します。私たちは そこからテキストを抽出し、それをモバイルアプリまたはウェブアプリに 送信します。そしてうまくいけば、そのコンテンツは 画面に表示されます。さて、これはすべて非常に 単純で簡単なように聞こえますが、 まだ対処していない小さな問題が一つあります。 ユーザーメッセージをClaudeに送信してから、アシスタント メッセージが返ってくるまでの時間は、 予想よりもはるかに長くかかる可能性があります。 場合によっては、入力ユーザーメッセージのサイズと 出力アシスタントメッセージのサイズによっては、 10秒から30秒かかることもあります。 ユーザーが応答を待っている間、このすべての時間に 画面にスピナーを表示するだけでよいのですが、それは あまり良いユーザーエクスペリエンスではありません。ほとんどのユーザーは 初期メッセージを入力したときに、量子コンピューティングとは何か、などと入力すると すぐに何らかの応答が画面に表示され始めることを期待しています。 このより良いユーザーエクスペリエンスを得るために、 ストリーミングと呼ばれるテクニックを使用します。 ストリーミングがどのように機能するかを説明しましょう。 私たちのサーバーは引き続き初期ユーザーメッセージをClaudeに送信しますが、 Claudeはほぼ即座に最初の応答を返します。 この最初の応答には、実際のテキストコンテンツは含まれていません。 代わりに、これはClaudeが私たちの最初の要求を受け取り、 Claudeがテキストを生成しようとしていることをサーバーに知らせるためのものです。 そして、私たちはイベントのストリームを受信し始めます。 これらのイベントが正確に何であるかについては、詳細に説明しますが、 現時点では、それらに含まれるのは 生成された応答の一部であり、それを返送して 最終的にユーザーに表示したいものです。 受け取るイベントの数は、生成するテキストの量によって異なります。 各イベントには、生成されているメッセージのほんの一部が含まれます。 たとえば、最初のイベントには「Quantum」というテキストが含まれ、 2番目のイベントは「Computing」で、3番目は「and」となります。 同様に続きます。各イベントには1つの単語だけでなく、 複数の単語や全文が含まれる場合もあります。 それは単にClaudeが各テキストの断片を生成するのにかかる時間に 依存します。さて、述べたように、私たちのサーバーはこれらのイベントを受信し、 サーバーはオプションで各イベントからテキストを抽出し、 それをすぐにウェブアプリやモバイルアプリ、 または表示できる他の場所に送信できます。 その小さなテキストのチャンクを画面に表示します。 その後、サーバーで受信した追加のイベントごとに このプロセスを繰り返すことができます。 つまり、ユーザーはチャットインターフェースにテキストが少しずつ表示され始めるのを 見ることになります。 それでは、私たちのノートブックに戻り、ストリーミングが どのように機能するかをよりよく理解するために、コードを記述しましょう。 さて、私のノートブックに戻りましょう。まだこれらの3つのヘルパー 関数があります。このビデオではチャット関数は無視します。 なぜなら、ストリーミングを使用し始めると、 実装されているチャット関数とはうまく機能しないからです。 そこで、代わりにメッセージのリストを作成し、 クライアントメッセージの作成関数を直接呼び出します。 空のメッセージリストを作成します。 メッセージにユーザーメッセージを追加します。 そして、Claudeに偽のデータベースの 1文の説明を書くように依頼します。 次にクライアントメッセージの作成を呼び出します。 モデルの名前を渡します。 最大トークンを提供する必要があります。 メッセージリストを提供します。 そして最後に、 ストリームをtrueとして、追加のキーワード引数を挿入します。 そして、これは最終的な回答ではなく、 イベントのストリームを受け取ります。 これは通常のイテレータなので、これを反復処理できます。 たとえば、イベントをストリームと呼び、 イベントを出力します。 これを実行すると、画面上にさまざまなイベントのストリームが 非常に速く表示されます。 これらはそれぞれ、Claudeが私たちに送信しているさまざまなデータチャンクを表しています。 最初に、raw message storeイベントと呼ばれるイベントがあり、 次に、raw content block start、raw content block deltaがあります。 実際、いくつものそれらを受け取ります。 そして、下の方にはcontent block stopイベント、message delt イベント、およびmessage stopイベントがあります。 これらはすべて、単一の要求のコンテキストで私たちに送信されているイベントです。 すべてClaudeから来ています。 これらの異なるイベントはそれぞれ、Claudeから受け取っている 全体的な応答のコンテキストで意味を持っています。 しかし、他のすべてのイベントよりも少しだけ気にする イベントタイプが一つあります。 それはraw content block Deltaイベントです。 このイベントには、Claudeによって生成され、 少しずつ私たちに送信されている実際のテキストが含まれています。 実際には、Claudeから応答を受け取るときは、 常にmessage start、content block start、そして content block deltasのシーケンスを受け取ります。 そして再び、それらが実際のテキストを含んでいます。 したがって、通常はこれらの異なるイベントをすべて収集し、 それらからテキストを抽出し、そのテキストを ウェブアプリやモバイルアプリ、または使用しているその他のものに 送信したいです。さて、ノートブックに戻り、 このforループの中で、 私たちが扱っているイベントのタイプを確認して判断するためのチェックを追加できます。 そして、それがraw content block deltaイベントの一つであれば、 それにアクセスして、実際に必要なテキストを取得できます。 しかし、それは私たちにとって多くの追加コードを必要とします。 幸いなことに、Anthropic SDKは、ここで示しているものとは異なる ストリームを作成する方法を提供しています。 私がすぐにあなたに見せるこの代替方法は、 応答からテキストを取得するのをはるかに簡単にします。 そして再び、テキストは通常、私たちが本当に気にする応答の部分です。 したがって、応答をストリーミングする別の方法を示しましょう。 次のコードセルに移動します。 ここに、メッセージのリストを再び作成します。 ユーザーメッセージに 偽のデータベースの1文の説明を書きたいと追加します。 そして、少し異なる関数を呼び出し、 それをwithブロックでラップします。 したがって、with client messages.streamと記述します。 そしてその中に、モデル、 最大トークン、 そしてメッセージを再び含めます。 しかし、stream to true引数を追加する必要はありません。 次にas stream：と書き、 すべてインデントします。そしてその中に、text in stream.textstreamと 書きます。 さて、テキストはさまざまなイベントのテキスト部分だけになります。 つまり、私たちが実際に気にするテキストです。 繰り返しますが、それは応答をストリーミングするときに私たちが本当に気にするものであることがほとんどです。 これが実際にどのように機能するかを示すために、 印刷文を追加して、 そのテキストをログに記録します。 print文の末尾に改行が追加されないように、 end trueの空文字列、end trueの空文字列を追加します。 したがって、テキストの各部分が隣り合ってログに記録されるのを見ます。 さて、これを実行すると、非常に速く起こりますが、 今度は応答がチャンクごとにストリーミングされているのがわかります。 もう一度やりましょう。 もう一度実行します。チャンク、チャンク、チャンクが見えます。 できました。各チャンクには複数の単語が含まれているのがわかります。 したがって、繰り返しますが、各イベントで1単語だけが返されるとは限りません。 数個含まれることもあります。 ここで示したい最後の機能が一つあります。 述べたように、ユーザーが各テキストチャンクをできるだけ早く画面に 表示できるように、モバイルアプリやウェブアプリに 応答をストリーミングすることがよくあります。 しかし、ストリームを完了した後によく行うもう一つのことは、 メッセージ全体を取得し、データベースに保存することです。 これにより、特定のユーザーとの会話全体の記録を保持できます。 これらのさまざまなイベントをすべて収集し、 それらをすべて1つの最終メッセージにまとめる方法を示しましょう。 ここにある印刷文を パスに置き換えます。これで印刷されなくなります。 そしてその後に、stream.getfinalmessageを呼び出します。 これをもう一度実行すると、応答は引き続きストリーミングされ、 必要であれば印刷することもできますが、 受け取った個々のイベントすべてを収集し、 それらを1つの最終メッセージにまとめています。 それをデータベースに保存したり、必要に応じて他の処理を行ったりできます。
