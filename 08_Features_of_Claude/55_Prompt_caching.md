# 55. Prompt caching

**URL:** https://anthropic.skilljar.com/claude-with-the-anthropic-api/287772
**Section:** 08 Features of Claude

---

## 📄 Page Content

Anthropic Academy
    
  

  
    
      Courses
    
  

    

    
      
      

      
        
          My Profile
        
        
      

      
      

      
        Sign Out
      
    
  

  

  

    
    
    
        
            
    
        
    

            
    
        
        
            
                
                    
                        
                            
                                
                            

                            
                                details
                            

                            
                        
                    
                
            
            
                
                
                
                    Prompt caching
                    
                
                
                    
                        
                            
                                
                                    

    
    

    
    
        
            
        
        
            
                
                This video is still being processed. Please check back later and refresh the page.
            
        
        
            
                Uh oh! Something went wrong, please try again.
            
        
    

    

                                
                            
                        
                    
                
            
        
        
            

    
        
            
                
                    
                        
                            
                        
                    
                
            
            
                
                    Summary
                

                

            
        

        
            
                
                    
                        
                            Summary

                            
                                Prompt caching is a feature that speeds up Claude's responses and reduces the cost of text generation by reusing computational work from previous requests. Instead of throwing away all the processing work after each request, Claude can save and reuse it when you send similar content again.

How Claude Normally Processes Requests

To understand prompt caching, let's first look at what happens during a typical request without caching enabled.

When you send a message to Claude, it doesn't immediately start generating a response. Instead, Claude does a tremendous amount of preprocessing work on your input:

Tokenizes the prompt into smaller pieces
Creates embeddings for each token
Adds context based on surrounding text
Only then generates the actual output text

After sending you the response, Claude throws away all this computational work - the tokenization, embeddings, and context analysis all get discarded.

The Problem with Discarding Work

This becomes inefficient when you make follow-up requests that include the same content. For example, in a conversation where you're asking Claude to refine a summary of the same long text:

Claude has to repeat all the same preprocessing work on content it just analyzed moments ago. As Claude might think to itself: "I just processed that message and threw away all the work I did - I could have reused it!"

How Prompt Caching Solves This

Prompt caching changes this workflow by saving the preprocessing work instead of discarding it:

When you make an initial request, Claude performs all the usual preprocessing but stores the results in a cache instead of throwing them away. The cache acts like a lookup table that says "If I ever see this message again, I'll reuse this work I already did."

Key Benefits and Limitations

Prompt caching offers several advantages:

Faster responses: Requests using cached content execute more quickly
Lower costs: You pay less for the cached portions of your requests
Automatic optimization: The initial request writes to the cache, follow-up requests read from it

However, there are important limitations to keep in mind:

Cache duration: Cached content only lives for one hour
Limited use cases: Only beneficial when you're repeatedly sending the same content
High frequency requirement: Most effective when the same content appears extremely frequently in your requests

Prompt caching works best for scenarios like document analysis workflows, where you're asking multiple questions about the same large document, or iterative editing tasks where the base content remains constant while you refine specific aspects.

---

## 🎬 Transcript (English)

The next feature that we are going to focus on is prompt caching. Prompt caching is used to speed up Claude's response and decrease the cost of text generation. To help you understand how prompt caching works, we're going to walk through what happens inside of Claude during a typical request that we make without any kind of prompt caching enabled at all. So again, this is just a normal request. And we've already spoken a little bit about normal requests on the entire flow. But don't worry, this time, I'm going to add in a little bit of detail on what happens inside of Claude itself. As usual, everything begins with us sending a message off to Claude. And when Claude receives this message, before actually generating any output text at all, it does a tremendous amount of work on the input message. In other words, Claude is going to internally create a tremendous number of internal data structures and do a tremendous number of calculations solely on the input text. It will then eventually generate the output text using all that earlier work it did, and then send a response back to us in the form of some assistant message. After the response is sent off to us, Claude is going to then take the output text and the result of all those earlier calculations that were done on the input message and just throw them all into the trash. A way it all goes, we see all that work kind of go up in smoke entirely. Once Claude has gone through all that cleanup, it declares the world I am ready to process the next request. Now, let's imagine for a moment that after making this initial request, we then make a follow-up request. And in this follow-up request, let's just imagine that we are continuing this conversation. So we're going to attach a list of messages. The first one will be the exact same message we had sent in a moment ago, and then the assistant message response we got back, and then some new user message that we're going to attach just to further the conversation along. So we're going to take all these messages and send them into Claude. And internally, Claude is probably going to be a little bit frustrated when it sees that first message. Because Claude is going to see that first message and think to itself, of course, isn't quite what happens. We can imagine this is kind of what's going on behind the scenes. Claude is going to see that first message and say, I just saw this message. I just did so much work to process it. And then I threw away all those calculations. And Claude is going to think to itself, I really wish I could reuse all that work that I did just 10 seconds ago and threw away. If Claude had saved that work that it threw away just a moment ago, it would probably be able to send us back a response much more quickly because it doesn't have to repeat all that work. So now that we have seen this problem, let's think of some possible way to solve it. Well, here's one possible way that we could handle this problem. Maybe we could say that whenever we make an initial request off to Claude, and Claude goes through all that initial work on our user message that we are sending in, rather than taking the results of all that analysis and throwing into the trash, maybe we could instead cache all that work or put it into some temporary data store. Then if we ever make a follow-up request and we include the exact same input user message, Claude could go into its cache and say, hey, I just saw this exact same message a moment ago and I saved the work of all the analysis around that particular message. So rather than re-analyze the message again, it could reuse all the work that it did previously. And hopefully this would dramatically speed up the process of generating some out of text because again, we are reusing some work that we had already done. This idea of saving some work from request to be used later on is exactly what prompt caching is all about. So let's come back in just a moment and we're going to walk through some of the implementation details of prompt caching and really understand how it is implemented by Claude.

---

## 🎬 トランスクリプト（日本語）

次に焦点を当てる機能はプロンプト キャッシングです。プロンプトキャッシングは応答を高速化し、 テキスト生成のコストを削減するために使用されます。 プロンプトキャッシングがどのように機能するかを理解するために、 Claude内で何が起こるかを、プロンプトキャッシングを有効にしない通常の リクエストで見ていきましょう。なので、繰り返しになりますが、 これは通常の単なるリクエストです。そして、私たちは すでにフロー全体について通常の要求について少し話しました。しかし、 心配しないでください。今回は、Claudeの内部で何が起こるかに少し詳細を 追加します。いつものように、 すべてはClaudeにメッセージを送信することから始まります。 Claudeがこのメッセージを受け取ると、実際に 何らかの出力テキストを生成する前に、 入力メッセージに対して膨大な作業を行います。 つまり、Claudeは内部的に膨大な数の 内部データ構造を作成し、膨大な数の計算を 入力テキストのみに対して実行します。その後、それ以前に行った すべての作業を使用して出力テキストを生成し、 応答をアシスタントメッセージとして返します。 応答が私たちに送信された後、Claudeは 出力テキストと、入力メッセージに対して行われたこれらすべての以前の計算の結果を 取得し、すべてゴミ箱に捨てます。 すべてがこのように無駄になるのを見てください。Claudeが すべてのクリーンアップを終えると、 「私は次のリクエストを処理する準備ができました」と宣言します。さて、 この最初の要求を出した後、フォローアップ要求を 行うと想像してみましょう。そして、このフォローアップ要求では、 会話を続けていると想像してください。 したがって、メッセージのリストを添付します。最初のメッセージは、 先ほど送信したメッセージとまったく同じもので、 そしてアシスタントからの応答メッセージ、そして 会話をさらに進めるための新しいユーザーメッセージです。 これらのすべてのメッセージを取得してClaudeに送信します。 そして内部では、Claudeは最初のメッセージを見たときに 少しイライラするかもしれません。なぜなら、Claudeは 最初のメッセージを見て、「まあ、そうなるよね？」と考えるからです。 これは裏側で起こっていることだと想像できます。Claudeは 最初のメッセージを見て、「このメッセージはさっき見たばかりだ。 処理するためにものすごく多くの作業をして、 そして計算結果をすべて捨ててしまった。 Claudeは「10秒前にやった作業を再利用できたらいいのに」と考えるでしょう。 Claudeが先ほど捨ててしまった作業を保存していたら、 すべてをやり直す必要がないので、 より速く応答を返せたはずです。 このように問題を見たので、解決策を考えてみましょう。 さて、これに対処する一つの方法があります。 最初の要求をClaudeに送信するとき、 そしてClaudeが送信したユーザーメッセージに対して すべての初期作業を行ったとき、 すべての分析結果をゴミ箱に捨てるのではなく、 代わりに、その作業をキャッシュしたり、 一時的なデータストアに保存したりできるかもしれません。 次にフォローアップ要求を行い、まったく同じ入力ユーザーメッセージを含めた場合、 Claudeはキャッシュに入って、「おお、このメッセージはさっき見たばかりだ。 この特定のメッセージに関するすべての分析の作業を保存した。」と言うことができます。 したがって、メッセージを再分析するのではなく、 以前に行ったすべての作業を再利用できます。 これにより、テキスト生成プロセスが劇的に高速化されるはずです。 なぜなら、私たちはすでに一度行った作業を再利用しているからです。 このように、あるリクエストからの作業を保存して後で 使用できるようにするという考えこそが、プロンプトキャッシングのすべてです。 では、しばらくしてから戻って、 プロンプトキャッシングの実装の詳細を説明し、 Claudeによってどのように実装されているかを本当に理解しましょう。 キャッシングできるはずです。 では、プロンプト キャッシングとは何でしょうか。 なので、少しお待ちください。 プロンプト キャッシングの実装の詳細を説明します。 そして、それをどのように実装するかを説明します。 はい。そのため、これをすべて削除して、 そして、キャッシング プロンプトでそれを修正しましょう。 それでは、これは少し良いでしょう。 さて、これらすべてです。 次に、キャッシュとは何かを説明しましょう。 そして、それをどのように実装するかを説明します。 ですので、次回までお待ちください。 そして、プロンプトキャッシングを説明します。 そして次にそれを実装します。
