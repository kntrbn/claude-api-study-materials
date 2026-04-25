# 56. Rules of prompt caching

**URL:** https://anthropic.skilljar.com/claude-with-the-anthropic-api/287770
**Section:** 08 Features of Claude

---

## 📄 Page Content

Anthropic Academy
    
  

  
    
      Courses
    
  

    

    
      
      

      
        
          My Profile
        
        
      

      
      

      
        Sign Out
      
    
  

  

  

    
    
    
        
            
    
        
    

            
    
        
        
            
                
                    
                        
                            
                                
                            

                            
                                details
                            

                            
                        
                    
                
            
            
                
                
                
                    Rules of prompt caching
                    
                
                
                    
                        
                            
                                
                                    

    
    

    
    
        
            
        
        
            
                
                This video is still being processed. Please check back later and refresh the page.
            
        
        
            
                Uh oh! Something went wrong, please try again.
            
        
    

    

                                
                            
                        
                    
                
            
        
        
            

    
        
            
                
                    
                        
                            
                        
                    
                
            
            
                
                    Summary
                

                

            
        

        
            
                
                    
                        
                            Summary

                            
                                Prompt caching in Claude works by storing the computational work done on your messages so it can be reused in follow-up requests. This makes subsequent requests both faster and cheaper to execute, but only when you're repeatedly sending identical content.

The process is straightforward: your initial request writes processing work to the cache, and follow-up requests can read from that cache instead of reprocessing the same content. The cache lives for one hour, so this feature is only useful if you're repeatedly sending the same content within that timeframe.

Cache Breakpoints

Caching isn't enabled automatically - you need to manually add cache breakpoints to specific blocks in your messages. Here's how it works:

Work done on messages is not cached automatically
You must manually add a 'cache breakpoint' to a block
Work done for everything before the breakpoint will be cached
Cache will only be used on follow-up requests if the content up to and including the breakpoint is identical

To add a cache breakpoint, you need to use the longhand form for writing text blocks instead of the shorthand:

The shorthand form doesn't provide a place to add the cache control field, so you must use the expanded format with the cache_control field set to {"type": "ephemeral"}.

How Cache Breakpoints Work

When you place a cache breakpoint in a message, Claude caches all the processing work up to and including that breakpoint. Content after the breakpoint is processed normally without caching.

For the cache to be useful in follow-up requests, the content must be identical up to the breakpoint. Even small changes like adding the word "please" will invalidate the cache and force Claude to reprocess everything.

Cross-Message Caching

Cache breakpoints can span across multiple messages and message types. If you place a breakpoint in a later message, all previous messages (user, assistant, etc.) will be included in the cached content.

This is particularly useful for conversations where you want to cache the entire context up to a certain point.

System Prompts and Tools

You're not limited to text blocks - cache breakpoints can be added to:

System prompts
Tool definitions
Image blocks
Tool use and tool result blocks

System prompts and tool definitions are excellent candidates for caching since they rarely change between requests. This is often where you'll get the most benefit from prompt caching.

Cache Ordering

Behind the scenes, Claude processes your request components in a specific order: tools first, then system prompt, then messages. Understanding this order helps you place breakpoints effectively.

You can add up to four cache breakpoints total. For example, you might cache your tools, then add another breakpoint partway through your conversation history. This gives you flexibility in what gets cached when different parts of your request change.

Minimum Content Length

There's a minimum threshold for caching: content must be at least 1024 tokens long to be cached. This is the sum of all messages and blocks you're trying to cache, not individual blocks.

A simple "Hi there!" message won't meet this threshold, but if you duplicate that content 500 times (or have a genuinely long prompt), it will exceed 1024 tokens and be eligible for caching.

The key to effective prompt caching is identifying which parts of your requests stay consistent across multiple calls and placing breakpoints strategically to maximize reuse while minimizing cache invalidation.

---

## 🎬 Transcript (English)

Now that we understand the theory, we are going to explore how prompt caching Claude actually works. The core idea of prompt caching is identical to what we discussed in the last video. We will make an initial request off to Claude. Claude is going to do some processing on that initial message, and then Claude is going to save all that work into a temporary cache. Then if we make a fault request at some future point in time and include the identical exact same message, rather than processing that message all over again, Claude is going to instead look into the cache, find the work that it had already saved, and load it up. Just to be clear, the work that be saved the cache does not persist forever. It is only stored there for one hour. You're going to find prompt caching is most useful any time that you are repeatedly sending the same content over to Claude again and again and again, because it really is this kind of two phase process. We have to make that initial request to write some data into the cache, and then only the follow up requests are going to be able to take advantage of that work that was done ahead of time. This caching system is not enabled by default with Claude. Instead, to turn on caching, we have to manually add a cache breakpoint to a block inside of one of our different messages. And I've showed an example of that on the right-hand side in this example user message. So all we have to do to turn on caching is put in that little cache control field. And there's a lot of rules around what that cache control thing actually does. But before we go into those rules and really explain what's going on, I want to give you a little tip here, something that's going to make your life a little bit easier. Throughout this course, we've been making use of a little shorthand for writing out text blocks very frequently. And I'm showing that on the left hand side. So this is a user message that is using the shorthand for defining a text block. If we have a user message that only has a little bit of text signed to it, we can assign a string directly to that content field. There is another way in which we can write out a text block, and I'm showing this alternative way of writing out a text block on the right-hand side. So the alternative method is to write out a content field, assign a list to it, and then side there put a dictionary that has a type of text, and then a text field that contains your actual text. Now we have not really been making use of that long-hand form, but if you want to use cache control, you want to turn on this prompt caching feature, you have to write out these text fields in long form. So you can actually add on that cache control field. In other words, we have to write out cache control somewhere, and over here on the right-hand side, we have some place to put it. If we use the short form, there's no place for us to put it. When we add a breakpoint into a block, all the content in our entire request is going to be cached up to and including that breakpoint. So in this scenario, if we send in a request like this where the first block has a breakpoint, Claude is going to do some amount of work processing this text right here. And it's going to result in some amount of work done. Because this text block has a breakpoint, this work is going to be stored inside the cache. But this later work is after the breakpoint, so it's not going to be cache. If we then send a follow-up request later on, Claude is going to take a look into the cache and find that some work was already done for processing this very first block. So it's going to retrieve that work and use it to save itself a little bit of effort. One thing to keep in mind is that our follow-up request must have identical content inside of it all the way up to that breakpoint. So for example, if our initial text block right here that had a breakpoint, if we added in just the word please to it. No longer is this content identical, and so this work would not have been used as out of the cache. Instead, Claude would reprocess this entire block and all the content before it. Cache breakpoints can span across multiple different messages and multiple different blocks. So for example, if we send in a user message and then an assistant and then another user, and the very last message here has a block with a breakpoint, Everything is going to be cached up to and including this block right here. So we'd imagine that the work that is done to process all three of those messages is going to be stored inside the cache. Then when we make our follow request later on, as long as everything up to an including that break point is identical, the work is going to be retrieved out of the cache. And again, we're going to save ourselves a little bit of effort. We are not restricted to adding cache points onto text blocks. We can also add them onto almost any other type of block, like an image block or a tool use or a tool result. We can also add these onto tool schemas and onto system prompts as well. And I've shown an example of both those on the right hand side. You are very often going to enable caching for your tools and for your system prompt as well. Because it turns out that for most applications, not all, but for many applications, your system prompt and your list of tools don't end up changing. So these are excellent places to place a cache breakpoint. In total, we can apply a breakpoint to tool schemas, system prompts, and message blocks. Now, these are not three separate cache systems. And let me show you exactly what I mean by that. Whenever you add in tools, a system prompt, and messages, behind the scenes, these all get joined together when they are fed into Claude, and they get joined together in that particular order. It is first the tools, then the system prompt, and then your list of messages. So if you place a cache breakpoint on your very last tool, everything up to and including that last tool will be cached. But the system prompt and your list of messages will not be cached. So if we then make a follow request and we change that assistant message right there, toy fine. We're still going to save ourselves a little bit of work because the list of tools was cached ahead of time. Last thing I want to mention very quickly is that we can add in multiple different cash breakpoints, up to four in total. So I might decide to add in a cash breakpoint at the last tool schema that I pass in, and then maybe I add in a cash breakpoint on this assistant message down here. If I then make a follow request and I change the user message down here, no problem. We're going to save ourselves the work of having to reprocess the entire list of tools and system prompt and user message as well. Likewise, if we change the first user message, well, then we're going to invalidate the cache for everything down here, but we'll still have the cache work for our list of tools. So we are very often going to add in multiple different cache breakpoints if appropriate. We might decide to cache our entire list of tools and the system prompt and maybe some number of messages as well. Exactly where you place these different breakpoints really just comes down to your particular application. The very last thing I want to share with you is that there is a minimum content length for caching. So in order to cache some amount of content, we must cache at least 1,024 tokens. So on the top right-hand example, I've got a cache breakpoint on a message that has only the text high there. This is definitely not 1,024 tokens long, so this content would not be written to the cache. But if I took that text block and duplicated 500 times, now I've probably got greater than 1,024 tokens, so this entire list of different blocks would be cached.

---

## 🎬 トランスクリプト（日本語）

理論を理解したところで、プロンプトが どのように実際に機能するかを見ていきましょう。プロンプト キャッシュのコアアイデアは、前回の 動画で説明したことと同じです。まず、最初の リクエストをClaudeに行います。Claudeは、 その初期メッセージに対して処理を行い、 その作業すべてを一時キャッシュに保存します。 その後、将来のある時点で 同じ全く同じメッセージを含む フォローアップのリクエストを行った場合、 メッセージ全体を再度処理する代わりに、 Claudeはキャッシュを参照して、 既に保存した作業を見つけてロードします。 明確にしておくと、キャッシュに保存された作業は 永久に保持されるわけではありません。 1時間だけ保存されます。プロンプトキャッシュは、 同じコンテンツを何度もClaudeに送信する場合に 最も役立ちます。なぜなら、これは2段階のプロセスであり、 まずキャッシュにデータを書き込むために初期リクエストを 行う必要があり、その後はフォローアップリクエストのみが 事前に行った作業を活用できるからです。 このキャッシングシステムは、Claudeではデフォルトで 有効になっていません。代わりに、キャッシュをオンにするには、 メッセージ内のブロックにキャッシュブレークポイントを 手動で追加する必要があります。 この例では、右側にその例を示しています。 キャッシュをオンにするには、この小さなキャッシュコントロールフィールドを 挿入するだけです。 このキャッシュコントロールが実際に何をするかについては、多くのルールがあります。 これらのルールに入る前に、少しヒントを差し上げたいと 思います。あなたの生活を少し楽にするものです。 このコース全体で、テキストブロックを 非常に頻繁に記述するための短い表記法を利用してきました。 左側にあるものを示しています。これは、テキストブロックを 定義するための短い表記法を使用しているユーザーメッセージです。 テキストが少量しかないユーザーメッセージがある場合、 コンテンツフィールドに直接文字列を割り当てることができます。 テキストブロックを書き出す別の方法があります。 右側にあるテキストブロックを書き出すこの代替方法を示しています。 したがって、代替方法はコンテンツフィールドを書き出し、 それにリストを割り当て、その中にテキストタイプの 辞書と、実際のテキストを含むテキストフィールドを 置くことです。 私たちはこの長い形式をあまり利用していませんでしたが、 キャッシュコントロールを使用したい場合、 このプロンプトキャッシング機能をオンにしたい場合は、 これらのテキストフィールドを長い形式で書き出す必要があります。 したがって、キャッシュコントロールフィールドを追加することもできます。 つまり、どこかにキャッシュコントロールを書き出す必要があり、 右側にはそれを置く場所があります。 短い形式を使用する場合、それを配置する場所はありません。 ブロックにブレークポイントを追加すると、 リクエスト全体のすべてのコンテンツが そのブレークポイントまでキャッシュされます。 このシナリオでは、最初のブロックにブレークポイントがある場合、 Claudeはこのテキストの処理にいくらかの作業を行います。 そして、ある程度の作業が行われます。 このテキストブロックにブレークポイントがあるため、 この作業はキャッシュ内に保存されます。 しかし、この後続の作業はブレークポイントの後にあるため、 キャッシュされません。その後、フォローアップリクエストを送信した場合、 Claudeはキャッシュを確認し、 最初のブロックの処理のために既に作業が行われていることを発見します。 したがって、その作業を取得し、 少しの労力を節約するために使用します。 覚えておくべきことの1つは、フォローアップリクエストが ブレークポイントまでのすべてのコンテンツが 同一である必要があるということです。 例えば、ブレークポイントがあった最初のテキストブロックに、 「please」という単語を追加した場合。 このコンテンツはもう同一ではなくなるため、 この作業はキャッシュから使用されません。 代わりに、Claudeはこのブロック全体と それ以前のすべてのコンテンツを再処理します。 キャッシュブレークポイントは、複数の異なるメッセージや 複数の異なるブロックにまたがることができます。 例えば、ユーザーメッセージ、アシスタントメッセージ、 そして別のユーザーメッセージを送信し、 最後のメッセージにブレークポイントのあるブロックがある場合、 ブレークポイントまで、およびそれを含むすべてが キャッシュされます。 したがって、3つのメッセージすべてを処理するために 行われる作業がキャッシュに保存されると想像できます。 その後、後続のリクエストを行ったとき、 ブレークポイントまでおよびそれを含むすべてが 同一である限り、作業はキャッシュから取得されます。 そして再び、私たちは少しの労力を節約します。 キャッシュポイントをテキストブロックに追加することに限定されません。 画像ブロックやツール使用、ツール結果にも 追加できます。 ツールスキーマやシステムプロンプトにも 追加できます。右側には両方の例を示しています。 ツールやシステムプロンプトのキャッシュを 有効にすることが非常に多いです。 ほとんどのアプリケーションでは、すべてではありませんが、多くのアプリケーションでは、 システムプロンプトとツールのリストは変更されません。 したがって、これらはキャッシュブレークポイントを 配置するのに優れた場所です。 合計で、ツールスキーマ、システムプロンプト、メッセージブロックに ブレークポイントを適用できます。 これらは3つの別々のキャッシュシステムではありません。 そして、それが何を意味するのかを正確に示しましょう。 ツール、システムプロンプト、メッセージを追加すると、 それらはすべてClaudeに渡されるときに結合され、 その特定の順序で結合されます。 まずツール、次にシステムプロンプト、 そしてメッセージのリストです。 最後のツールにキャッシュブレークポイントを配置した場合、 最後のツールまで、およびそれを含むすべてが キャッシュされます。しかし、システムプロンプトと メッセージのリストはキャッシュされません。 その後、フォローアップリクエストを行い、 アシスタントメッセージを変更した場合、 ツールのリストが事前にキャッシュされていたため、 少しの労力を節約できます。 最後に素早く言及したいことは、複数のキャッシュブレークポイントを 合計4つまで追加できるということです。 例えば、渡す最後のツールにキャッシュブレークポイントを 追加し、次にこのアシスタントメッセージにブレークポイントを 追加するかもしれません。 その後フォローアップリクエストを行い、 ユーザーメッセージを変更した場合、 問題ありません。ツール、システムプロンプト、 ユーザーメッセージ全体の再処理を節約できます。 同様に、最初のユーザーメッセージを変更した場合、 下にあるすべてのキャッシュが無効になりますが、 ツールのリストのキャッシュは引き続き利用できます。 したがって、適切であれば、複数のキャッシュブレークポイントを 追加することがよくあります。 ツールのリスト全体、システムプロンプト、 そしていくつかのメッセージをキャッシュすることを決定するかもしれません。 これらの異なるブレークポイントをどこに配置するかは、 まさにあなたのアプリケーション次第です。 最後に共有したいのは、キャッシュには最小コンテンツ長があるということです。 したがって、コンテンツをキャッシュするには、 少なくとも1,024トークンをキャッシュする必要があります。 右上にある例では、キャッシュブレークポイントを 「Hi there」というテキストしかないメッセージに置いています。 これは明らかに1,024トークンではありません。 したがって、このコンテンツはキャッシュに書き込まれません。 しかし、そのテキストブロックを取得して 500回複製した場合、 おそらく1,024トークンを超えているため、 これらの異なるブロック全体がキャッシュされます。
