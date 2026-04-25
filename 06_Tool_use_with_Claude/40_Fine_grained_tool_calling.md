# 40. Fine grained tool calling

**URL:** https://anthropic.skilljar.com/claude-with-the-anthropic-api/313160
**Section:** 06 Tool use with Claude

---

## 📄 Page Content

Anthropic Academy
    
  

  
    
      Courses
    
  

    

    
      
      

      
        
          My Profile
        
        
      

      
      

      
        Sign Out
      
    
  

  

  

    
    
    
        
            
    
        
    

            
    
        
        
            
                
                    
                        
                            
                                
                            

                            
                                details
                            

                            
                                
                                    
                                    2
                                    download
                                
                            
                        
                    
                
            
            
                
                
                
                    Fine grained tool calling
                    
                
                
                    
                        
                            
                                
                                    

    
    

    
    
        
            
        
        
            
                
                This video is still being processed. Please check back later and refresh the page.
            
        
        
            
                Uh oh! Something went wrong, please try again.
            
        
    

    

                                
                            
                        
                    
                
            
        
        
            

    
        
            
                
                    
                        
                            
                        
                    
                
            
            
                
                    Summary
                

                

            
        

        
            
                
                    
                        
                            Summary

                            
                                When you combine tool use with streaming in Claude, you get real-time updates as the AI generates tool arguments. This creates a more responsive user experience, but there are some important details to understand about how it works behind the scenes.

Basic Tool Streaming

With streaming enabled, Claude sends back different types of events as it processes your request. You're already familiar with events like ContentBlockDelta for regular text generation. For tool use, you'll also need to handle a new event type called InputJsonEvent.

Each InputJsonEvent contains two key properties:

partial_json - A chunk of JSON representing part of the tool arguments
snapshot - The cumulative JSON built up from all chunks received so far

Here's how you handle these events in your streaming pipeline:

for chunk in stream:
    if chunk.type == "input_json":
        # Process the partial JSON chunk
        print(chunk.partial_json)
        # Or use the complete snapshot so far
        current_args = chunk.snapshot

How JSON Validation Works

Here's where things get interesting. The Anthropic API doesn't immediately send you every chunk as Claude generates it. Instead, it buffers chunks and validates them first.

The API waits for complete top-level key-value pairs before sending anything. For example, if your tool expects this structure:

{
  "abstract": "This paper presents a novel...",
  "meta": {
    "word_count": 847,
    "review": "This paper introduces QuanNet..."
  }
}

The API will:

Wait until the entire abstract value is complete
Validate that key-value pair against your schema
Send all the buffered chunks for abstract at once
Repeat the process for the meta object

This validation process explains why you see delays followed by bursts of text, even with streaming enabled. The chunks are being held back until a complete, valid top-level key-value pair is ready.

Fine-Grained Tool Calling

If you need faster, more granular streaming - perhaps to show users immediate updates or start processing partial results quickly - you can enable fine-grained tool calling.

Fine-grained tool calling does one main thing: it disables JSON validation on the API side. This means:

You get chunks as soon as Claude generates them
No buffering delays between top-level keys
More traditional streaming behavior
Critical: JSON validation is disabled - your code must handle invalid JSON

Enable it by adding fine_grained=True to your API call:

run_conversation(
    messages, 
    tools=[save_article_schema], 
    fine_grained=True
)

With fine-grained tool calling, you might receive a word_count value much earlier in the stream, without waiting for the entire meta object to be completed.

Handling Invalid JSON

When using fine-grained tool calling, Claude might generate invalid JSON like "word_count": undefined instead of a proper number. Your application needs to handle these cases gracefully:

try:
    parsed_args = json.loads(chunk.snapshot)
except json.JSONDecodeError:
    # Handle invalid JSON appropriately
    print("Received invalid JSON, continuing...")

Without fine-grained tool calling, the API's validation would catch this error and potentially wrap problematic values in strings, which might not match your expected schema.

When to Use Fine-Grained Tool Calling

Consider enabling fine-grained tool calling when:

You need to show users real-time progress on tool argument generation
You want to start processing partial tool results as quickly as possible
The buffering delays negatively impact your user experience
You're comfortable implementing robust JSON error handling

For most applications, the default behavior with validation is perfectly adequate. But when you need that extra responsiveness, fine-grained tool calling gives you the control to get chu

---

## 🎬 Transcript (English)

In this video, we're going to take a look at combining together tool use with streaming. You'll recall that we discussed streaming from the API earlier. Streaming allows us to give users a better idea of what's going on in our app. So whenever we have streaming enabled and we make a request off to Claude, we're going to get back some initial response, and then we'll receive a series of different events. And each event will have some additional piece of text that we might want to display to the user. You might recall that there are many different types of events that we might need to handle inside of our application, and a very common one that we need to be on the lookout for is Content Block Delta. To make use of tools with streaming, we're going to add in an additional type of event that we need to handle. And it's called the input JSON event. So now, if we turn on streaming and try to make use of tools, Claude might send back a new type of event to us called the input JSON event. This object is going to have two important properties on it. First, there's going to be a partial JSON, which is going to be a piece of JSON that represents a part of an argument that Claude wants to send into our tool. We're also going to get something called a snapshot, which is a cumulative sum of all the different partial JSON pieces that we have received so far. To give you a better idea of how this works, I put together a new notebook called 003 tool streaming. It's attached to this lecture. This notebook contains a modified run conversation function. It's going to use a new function called chat stream to open up a response stream from the Anthropic API. Then for every chunk in that stream, we're going to process each one depending upon the type of chunk it is. In the case of receiving an input JSON chunk, all we're going to do right now is print it out. So I'm going to go down to the bottom where I've already put together a prompt along with a new tool called save article schema. I'm going to run this notebook and let's just see what happens. Pretty quickly, we'll see each chunk of the response come in, including the arguments for the tool call. You'll notice that this notebook is also generating a scholarly article, just with a few different properties compared to what we had previously. Now, to be honest, there isn't really a lot more to tool streaming beyond this. We really just need to make sure that we handle that additional type of event. Having said that, there is one other aspect of tool streaming that I would like to tell you about, but it's around a very, very particular feature that you might not ever need to make use of. So let me give you a very quick overview, and then you can decide if you want to hear about this very specialized feature or not. If I rerun this notebook, you might notice that it appears that we are getting streaming behavior. Text is appearing chunk by chunk. But for our tool call arguments in particular, you'll notice that we have to sit around and wait for a few seconds. And then all of a sudden, a giant chunk of text appears. The fact that there's this really big delay and then we get a giant chunk of text might not be a big deal to you at all. However, you might be working on an application where it's really important to show very precise content updates to your users as soon as possible. Or perhaps you want to receive portions of a tool call as quickly as possible so you can start doing some processing work as fast as you possibly can. So in the remainder of this video, I'm going to help you understand why there is that big delay and then a giant chunk of text appears. And I'm going to show you a feature in the Anthropic API to get rid of that delay. So let's get to it. The first thing I would like to do is clarify the tool that I have added into this notebook. So I've slightly adjusted the tool that we had previously that was generating a scholarly article. We're still generating an article, but now it has a slightly different input structure to it. I've got an example of the expected input on the bottom left hand side. So we expect to receive a key of abstract that's kind of like a summary of a scholarly paper and a meta object. And the meta object is going to have a word count and a review. And the review in the theories can be some long review of the particular paper that's been generated. Now, out of this example input right here, there's something that I really just want to examine really quickly or just kind of point out. In this big object that we get, we're going to have two top level keys. In other words, the top level keys inside the entire big object. There's abstract and there's meta. So we would refer to those as top level keys. Meta is going to point to an object that has some additional key value pairs inside of it, but again, the top level keys are abstract and meta. So just keep then your head for a little bit. So now I want to help you understand what goes on behind the scenes inside the Anthropic API whenever we generate some arguments for a tool call in streaming mode. So it doesn't quite behave as you might expect. In this diagram on the top left-hand side, I've got our call being sent off to the Anthropic API. Once it receives our request, Claude will start to generate some JSON, which will be the input to our tool call. The JSON isn't generated all at once. Instead, it is created chunk by chunk. Now, something kind of surprising happens at this point. The Anthropic API doesn't immediately take these chunks and send them right back to our server immediately. Instead, it's going to hang on to them for a little bit of time. The reason for hanging onto these chunks is that Claude can sometimes generate invalid JSON. So rather than immediately sending each chunk to us, the API is going to attempt to do a validation step, where it makes sure that it is sending us valid JSON. Let me show you how the validation step works. First, as a reminder, we have two top-level keys for our tool call, abstract and meta. So the API isn't going to wait for the entire object to be generated to do the validation. Instead, it will wait for a single top-level key value pair to be generated. So in the case of the abstract key, the Anthropic API will wait until it sees a closing quote for the abstract value string. As soon as it sees that closing quote on the very far right-hand side on chunk number four, then the API knows that it has at least one key value pair generated. In this case, the abstract key value pair. The API will then attempt to validate just that key value pair in isolation. It's going to compare it against the JSON schema that we provided and make sure that valid JSON has been produced. If it is valid, then each of the original chunks that were produced will be sent back down to our server. Note that we do get each individual chunk, not the entire key value pair as one single chunk. If you're to log out all the different chunks that we receive inside of our notebook, you will see that we do in fact receive a ton of different individual chunks. They just all happen to arrive at our server at just about the same time, because the chunks have been buffered on the API so that it can go through this validation step. Then this generation process is going to continue with the meta top level key. So once again, the API will wait until the entire meta top level key value pair is generated. It's then going to validate it and then send us each of the individual chunks back down to our server. So this is why, even with streaming enabled, we end up getting these really big pauses as the chunks are buffered on the API. And then all of a sudden, we see a big group of chunks appear or big chunk of text appear all at once, all of a sudden. Now, again, this behavior might be okay for you. You might not mind this buffering and validation step. But if you are building a UI where you want to show users updates as soon as possible, or if you want to do some tool processing as soon as possible, then this big pause might be a little irritating. Now, if that's the case, I do have good news. There is a feature in the API called Fine-Grained Tool Calling. At its core, Fine-Grained Tool Calling does really just one thing. It disables the JSON validation step. So if you enable fine-grained tool calling, the API will wait for Claude to generate a couple of chunk chunks. It's going to join them together and then send that big chunk down to your server. So this feature, you will see a more traditional streaming output when generating tool inputs. I do want to repeat with fine-grained tool calling JSON validation on the API is disabled. So your code running on your server now really should assume that you might be given invalid JSON and you should implement some appropriate error handling. The notebook that we were working on is set up for fine-grained tool calling. So let's see what happens to our response when we turn it on. I'm going to go down to the run conversation call right here and I'm going to add in a fine-grained tool like so. I'm going to run this. And now we're going to see that when we eventually get down to the tool call, we're going to get a lot more kind of classic streaming experience here, where we get chunked by chunk just a little bit of text at a time. So again, this would allow us to process some part of the tool call much more quickly. Let's say, for example, that the word count value right here was really important to us. Without fine-grained tool calling, we would have to wait for all this text right here to be generated before we ever got access to the word count. But if I run this again with fine-grained tool calling, we'll see that now we can get that word count value much more quickly. We don't have to wait for all this additional text to be generated. Now, you might be kind of curious what does happen exactly when we get some invalid JSON generated. Well, I put together a prompt that's going to just about guarantee that we will get some invalid JSON generated. I'm going to copy paste it in here really quickly. And then I'm also going to add in an additional argument to the run conversation function. Just make sure that we do, in fact, get that invalid JSON generated. So the extra argument I added on here is just a force tool call. I'm forcing the model to always call the save article model that we've put together. So I'm going to run this. And we'll see that initially everything is going to go fine, but then very quickly we're going to end up getting an error. So the reason we're getting an error and what this prompt right here really does, we just saw that word count value. So word count is supposed to be a number. This prompt is going to force a word count value of undefined. And just so you know, undefined is not a valid value in JSON. The equivalent JSON value would be null. So if we ever get a value in JSON of undefined, that would be invalid JSON. And we'd cause a parsing error. And so that's exactly what we see down here. If I scroll down a little bit more, I'll see an error something around. Yeah, we've got some invalid JSON. And specifically is because we got a word count of undefined. And it might be kind of curious what would happen here if we were not using fine-grained tool calling. You just might be a little bit curious. So if I comment that out and I run this again. So now the validation step is going to occur. So let's see how this gets treated. So what the API ends up doing here is it's still going to put in that meta object. But instead of actually being an object, it's going to wrap the entire thing in a string. So now technically, we're really not following the JSON spec in the response here. Our JSON schema, the one we provided, said meta must be an object that had a word count that's a number and a review that's a string. So now meta is a string instead of an object. All right, so let's wrap things up. Once again, tool streaming by itself, not too crazy. We can easily add it into any kind of streaming pipeline you might have already put together. With default tool streaming, if you're generating a large top-level key-value pair, there will be a delay in that generation because the API does some validation step. And if that's a big deal to you, you can always turn on fine-grained tool streaming, which is going to give you a little bit more classic streaming experience, but at the cost of that validation step.

---

## 🎬 トランスクリプト（日本語）

このビデオでは、ツールをストリーミングと組み合わせて使用する方法を見ていきます。 以前、APIからのストリーミングについて説明したことを覚えているでしょう。 ストリーミングにより、アプリで何が起こっているかをユーザーに よりよく理解してもらうことができます。 したがって、ストリーミングが有効になっていて、Claudeにリクエストを送信すると、 最初の応答が返ってきて、その後、一連の異なるイベントを受信します。 各イベントには、表示したい追加のテキストが含まれます。 アプリケーション内で処理する必要があるイベントには、さまざまな種類があることを 覚えているかもしれません。そして、私たちが注意すべき非常に一般的なものは Content Block Delta です。 ツールをストリーミングと組み合わせて使用するために、 処理する必要がある追加のイベントタイプを導入します。 それはInput JSONイベントと呼ばれます。 したがって、ストリーミングをオンにしてツールを使用しようとすると、 ClaudeはInput JSONイベントと呼ばれる新しいタイプのイベントを 返してくる可能性があります。 このオブジェクトには、2つの重要なプロパティがあります。 まず、Partial JSONがあります。これは、Claudeが ツールに送信したい引数の一部を表すJSONの断片です。 また、Snapshotも取得します。これは、 これまで受信したすべてのPartial JSON断片の累積合計です。 これがどのように機能するかをよりよく理解するために、 003 tool streaming という新しいノートブックを用意しました。 これはこの講義に添付されています。 このノートブックには、変更されたRun conversation関数が含まれています。 これは、Anthropic APIからの応答ストリームを開くための 新しい関数Chat streamを使用します。 次に、そのストリーム内の各チャンクについて、 チャンクのタイプに応じてそれぞれを処理します。 Input JSONチャンクを受信した場合、 現時点では、それを出力するだけです。 したがって、プロンプトとSave article schemaという新しいツールを 一緒に用意した下部まで移動します。 このノートブックを実行して、何が起こるか見てみましょう。 すぐに、応答の各チャンクが表示され、 ツール呼び出しの引数も含まれます。 このノートブックでは、以前よりも わずかに異なるプロパティで学術論文を生成していることに注意してください。 以前のものと比較して。 正直なところ、ツールストリーミングにはこれ以上 あまりありません。追加のイベントタイプを処理する必要があるだけです。 とはいえ、ツールストリーミングには もう1つの側面がありますが、これはあなたが 必要としないかもしれない非常に、非常に特定の機能に関するものです。 ですから、非常に簡単な概要を説明します。 そうすれば、この非常に特殊な機能について 聞きたいかどうかを自分で決めることができます。 このノートブックを再度実行すると、 ストリーミング動作を行っているように見えることに気づくかもしれません。 テキストはチャンクごとに表示されます。 しかし、特にツール呼び出しの引数については、 数秒待つ必要があります。 そして突然、大量のテキストが表示されます。 この大きな遅延があり、その後、 大量のテキストが表示されるという事実は、 あなたにとって問題ないかもしれません。 しかし、ユーザーにできるだけ早く 正確なコンテンツ更新を表示することが 本当に重要なアプリケーションで作業している場合、 またはできるだけ早くツール呼び出しの部分を受信して 処理作業をできるだけ速く開始したい場合。 この大きな遅延があり、その後、 大量のテキストが表示される理由を説明します。 そして、Anthropic APIの その遅延をなくす機能を紹介します。 では、始めましょう。 まず、このノートブックに追加したツールを 明確にしたいと思います。 以前の学術論文を生成していたツールをわずかに調整しました。 まだ論文を生成していますが、 入力構造がわずかに異なります。 左下隅に期待される入力の例があります。 したがって、Abstractというキーがあり、 それは学術論文の要約のようなもので、 Metaオブジェクトがあります。 そして、Metaオブジェクトには、単語数とレビューが含まれます。 そして、Reviewには、生成された特定の論文の 長いレビューが含まれる場合があります。 この例の入力から、 すぐに確認したい、または指摘したいことがあります。 この大きなオブジェクトには、2つのトップレベルキーがあります。 つまり、オブジェクト全体のトップレベルキーです。 AbstractとMetaがあります。 したがって、それらをトップレベルキーと呼びます。 Metaは、追加のキーと値のペアを含むオブジェクトを指します。 しかし、繰り返しますが、トップレベルキーはAbstractとMetaです。 ですから、しばらく頭に入れておいてください。 それでは、Anthropic APIの内部で ツール呼び出しの引数を生成するときに 何が起こるかを理解するのに役立ちます。 それはあなたの期待通りには動作しません。 左上のこの図では、Anthropic APIに 呼び出しが送信されているのがわかります。 リクエストを受け取ると、ClaudeはJSONの生成を開始します。 これはツール呼び出しの入力になります。 JSONは一度にすべて生成されるわけではありません。 代わりに、チャンクごとに作成されます。 ここで何かが起こります。 Anthropic APIは、これらのチャンクを すぐにサーバーに返しません。 代わりに、しばらく保持します。 これらのチャンクを保持する理由は、 Claudeが不正なJSONを生成することがあるためです。 そのため、APIは各チャンクを すぐに送信するのではなく、 検証ステップを実行しようとします。 それは、有効なJSONを送信していることを確認します。 検証ステップがどのように機能するかをお見せしましょう。 まず、リマインダーとして、ツール呼び出しには AbstractとMetaという2つのトップレベルキーがあります。 したがって、APIはオブジェクト全体が 生成されるのを待って検証を実行するわけではありません。 代わりに、単一のトップレベルキー 値のペアが生成されるのを待ちます。 つまり、Abstractキーの場合、Anthropic APIは Abstract値の文字列の閉じ引用符を見るまで待機します。 チャンク4の右端にあるその閉じ引用符を見るとすぐに、 APIは、少なくとも1つのキー 値のペアが生成されたことを知ります。 この場合、Abstractキーと値のペアです。 APIは、そのキーと値のペアだけを 個別に検証しようとします。 提供されたJSONスキーマと比較して、 有効なJSONが生成されたことを確認します。 有効であれば、生成された元のチャンクは すべてサーバーに返されます。 個々のチャンクごとに取得することに注意してください。 単一のチャンクとしてではなく。 ノートブック内で受信したすべての異なるチャンクを ログアウトすると、実際には多数の 個々のチャンクを受信していることがわかります。 それらはすべてほぼ同時にサーバーに到着します。 APIでチャンクがバッファリングされているため、 この検証ステップを実行できます。 次に、この生成プロセスは、 Metaトップレベルキーで続行されます。 したがって、再度、APIは Metaトップレベルキーと値のペア全体が 生成されるまで待機します。 その後、検証を実行し、 個々のチャンクをサーバーに返します。 したがって、これが、ストリーミングが有効になっていても、 APIでチャンクがバッファリングされている間、 本当に大きな一時停止が発生し、 その後、突然、大きなチャンクのグループが表示される理由です。 または、大量のテキストが一度に突然表示されます。 繰り返しになりますが、この動作は問題ないかもしれません。 このバッファリングと検証ステップを気にしないかもしれません。 しかし、ユーザーにできるだけ早く更新を表示したいUIを構築している場合、 またはできるだけ早くツール処理を実行したい場合、 この大きな一時停止は少しイライラするかもしれません。 その場合、良いニュースがあります。 Fine-Grained Tool CallingというAPIの機能があります。 その中心において、Fine-Grained Tool Callingは 本当に1つのことしか行いません。JSON検証ステップを無効にします。 したがって、Fine-Grained Tool Callingを有効にすると、 APIはClaudeがいくつかのチャンクを生成するのを待って、 それらを結合してから、その大きなチャンクを サーバーに送信します。 したがって、この機能により、ツール入力を生成する際に より伝統的なストリーミング出力が表示されます。 Fine-Grained Tool CallingでAPIのJSON検証が 無効になっていることを繰り返したいと思います。 したがって、サーバーで実行されているコードは 無効なJSONを受け取る可能性があると想定し、 適切なエラー処理を実装する必要があります。 私たちが作業していたノートブックは、 Fine-Grained Tool Calling用に設定されています。 ですから、それをオンにしたときの応答に何が起こるか見てみましょう。 Run conversation の呼び出しまで移動して、 Fine-Grained Tool のようなものを追加します。 実行します。 そして今、ツール呼び出しにたどり着いたときに、 より古典的なストリーミング体験が得られるでしょう。 つまり、ツール呼び出しの一部を より速く処理できるようになります。 たとえば、この単語数値が 私たちにとって非常に重要だったとしましょう。 Fine-Grained Tool Calling がなければ、 単語数にアクセスする前に、このすべてのテキストが 生成されるのを待たなければなりませんでした。 しかし、Fine-Grained Tool Calling でこれを再度実行すると、 今ではその単語数値をより速く取得できることがわかります。 この追加のテキストが生成されるのを待つ必要はありません。 さて、無効なJSONが生成されたときに 正確に何が起こるのか、気になっているかもしれません。 無効なJSONが生成されることをほぼ保証する プロンプトを用意しました。 それをここにコピー＆ペーストして、 Run conversation 関数に 追加の引数を追加します。 Force Tool Call という追加の引数を追加しました。 モデルに、用意したSave Articleモデルを常に呼び出すように強制しています。 実行します。 最初はすべてうまくいきますが、 すぐにエラーが発生します。 エラーが発生する理由と、このプロンプトが 実際に行うことは、単語数値を 見たことです。単語数は数値であるはずです。 このプロンプトは、単語数値をUndefinedに強制します。 ご存知のように、UndefinedはJSONの有効な値ではありません。 JSONでの同等の値はNullです。 したがって、JSONでUndefinedの値が得られた場合、 それは無効なJSONであり、解析エラーが発生します。 そして、まさにここで見られることです。 もう少し下にスクロールすると、エラーが見つかります。 無効なJSONがあります。 そして、それはUndefinedの単語数を得たことが原因です。 また、Fine-Grained Tool Calling を 使用していなかった場合に何が起こるか、 少し気になるかもしれません。 ですから、それをコメントアウトして、 もう一度実行します。 したがって、検証ステップが実行されます。 これがどのように扱われるかを見てみましょう。 APIが行うことは、Metaオブジェクトを まだ配置することですが、 オブジェクトの代わりに、全体を文字列でラップします。 したがって、技術的には、 ここでは応答でJSON仕様に従っていません。 提供したJSONスキーマは、 Metaは数値の単語数と 文字列のレビューを持つオブジェクトでなければならないと述べていました。 したがって、今ではMetaはオブジェクトではなく文字列です。 さて、まとめましょう。 ツールストリーミング自体は、それほどクレイジーではありません。 すでに構築している可能性のある ストリーミングパイプラインに簡単に組み込むことができます。 デフォルトのツールストリーミングでは、 大きなトップレベルキーと値のペアを生成している場合、 APIが検証ステップを実行するため、 その生成に遅延が発生します。 それがあなたにとって大きな問題であれば、 Fine-Grained Tool Streaming をオンにすることができます。 これにより、より古典的なストリーミング体験が 得られますが、その検証ステップの コストがかかります。
