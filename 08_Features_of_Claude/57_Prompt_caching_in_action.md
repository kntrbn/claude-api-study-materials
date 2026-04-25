# 57. Prompt caching in action

**URL:** https://anthropic.skilljar.com/claude-with-the-anthropic-api/287774
**Section:** 08 Features of Claude

---

## 📄 Page Content

Anthropic Academy
    
  

  
    
      Courses
    
  

    

    
      
      

      
        
          My Profile
        
        
      

      
      

      
        Sign Out
      
    
  

  

  

    
    
    
        
            
    
        
    

            
    
        
        
            
                
                    
                        
                            
                                
                            

                            
                                details
                            

                            
                                
                                    
                                    1
                                    download
                                
                            
                        
                    
                
            
            
                
                
                
                    Prompt caching in action
                    
                
                
                    
                        
                            
                                
                                    

    
    

    
    
        
            
        
        
            
                
                This video is still being processed. Please check back later and refresh the page.
            
        
        
            
                Uh oh! Something went wrong, please try again.
            
        
    

    

                                
                            
                        
                    
                
            
        
        
            

    
        
            
                
                    
                        
                            
                        
                    
                
            
            
                
                    Summary
                

                

            
        

        
            
                
                    
                        
                            Summary

                            
                                Prompt caching is a powerful optimization feature that makes your API requests both faster and cheaper when you're repeatedly sending the same content to Claude. Let's explore how to implement it effectively in your applications.

How Prompt Caching Works

When you enable prompt caching, the first request writes content to a cache that lives for one hour. Follow-up requests can then read from this cache instead of processing the same content again. This is particularly valuable when you're sending:

Large system prompts (like a 6K token coding assistant prompt)
Complex tool schemas (around 1.7K tokens for multiple tools)
Repeated message content

The key insight is that caching only helps if you're repeatedly sending identical content - but in many applications, this happens extremely frequently.

Setting Up Tool Schema Caching

To cache your tool schemas, you need to add a cache control field to the last tool in your list. Here's the proper way to do it without modifying your original tool definitions:

if tools:
    tools_clone = tools.copy()
    last_tool = tools_clone[-1].copy()
    last_tool["cache_control"] = {"type": "ephemeral"}
    tools_clone[-1] = last_tool
    params["tools"] = tools_clone

This approach creates copies of both the tools list and the last tool schema before adding the cache control field. While you could directly modify tools[-1]["cache_control"], the copying approach prevents issues if you later reorder your tools.

System Prompt Caching

For system prompts, you need to structure them as a text block with cache control:

if system:
    params["system"] = [
        {
            "type": "text",
            "text": system,
            "cache_control": {"type": "ephemeral"}
        }
    ]

This converts your system prompt from a simple string into a structured format that supports caching.

Understanding Cache Behavior

When you run requests with caching enabled, you'll see different usage patterns in the response:

First request: cache_creation_input_tokens=1772 - Claude writes to cache
Follow-up requests: cache_read_input_tokens=1772 - Claude reads from cache
Changed content: New cache creation tokens appear

The cache is extremely sensitive - changing even a single character in your tools or system prompt invalidates the entire cache for that component.

Cache Ordering and Breakpoints

You can set multiple cache breakpoints in a single request. The order matters:

Tools (if provided)
System prompt (if provided)
Messages

If you change your system prompt but keep the same tools, you'll see a partial cache read (for tools) and a cache write (for the new system prompt). This granular caching means you only pay for processing the parts that actually changed.

Practical Considerations

Prompt caching is most effective when you have:

Consistent tool schemas across requests
Stable system prompts
Applications that make multiple requests with similar context

Remember that the cache only lasts for one hour, so it's designed for applications with relatively frequent API usage rather than long-term storage.
                            
                        
                    

                    
                        
                            Downloads
                            
                                
                                    
                                        
                                            
                                            
                                                003_caching.ipynb
                                                (opens in new tab)

---

## 🎬 Transcript (English)

Time to get our hands dirty with prompt caching. I've created a new notebook called 003 caching. You will of course find it attached to this lecture. Inside here, you'll find a section called prompt with 6K tokens. So this is meant to serve as a system prompt. We're going to use it in a little bit. In addition, there is a tool schema section. It has several different tool schemas to find inside of it. All these different tool schemas put together total it to about 1.7K tokens. We're going to work on updating our chat function, which is inside the cell up here called helper functions. We're going to make sure that our chat function always enables prompt caching for our tool schemas and our system prompt by default. So let me show you how you would do that. Inside the helper function cell, I'm going to scroll down to our chat function. Here it is right here. I'm going to scroll down a little bit further and you'll notice I added in two to-do items. First, if a tools list is provided, I want to always cache the list of tools. Secondly, if we provide a system prompt, I want to cache that as well. Remember that we can have multiple different cache breakpoints inside of a single request. So if we end up passing both a system prompt and a list of tools, we're going to set two different cache breakpots. Let's first take care of caching our list of tools. Now, to do so, remember, we need to modify the very last tool schema that we pass into Claude. We need to, in particular, add on that cache control field. But we could do something like this. We could just say tools, negative one, and then set a cache control field on it of type ephemeral. Like so. As we definitely work, but it's not the best coding technique. You see, this will actually modify our tool schema by adding in the cache control field to it. There might be some scenario in our application where we later on decide to change the order of our tool schemas that we're passing in. And if we did so, we would then end up with multiple different cache breakpoints being set up inside of our tool schema, which might not be exactly what we desire. So a little bit better way of doing this would be to first create a copy of our tools list. Then we will clone the last tool schema inside there and add the cache control field to it. So let me see how to do that. I'm going to make a new variable called tools clone, which will come from calling tools.copy. So that's going to make a total copy of the list. Next, I'm going to copy the very last tool inside there. I'm then going to add on the cache control field to the last tool schema. So that will be type ephemeral. Then I'm going to overwrite the last element inside tools clone with the tool schema copy that I just made tools. clone at negative one will be the last tool. And I'm going to assign my tools clone to the tools program. Now, just to repeat here really quickly, all this copulogic I have inside of here is not strictly necessary. It's just good practice, again, in case we ever decide to change our list of tools at some point in time. Next up, we'll take care of the second to do. So if we pass in a system prompt, I want to make sure that we always set a cache breakpoint on it. To do so, I'm going to remove the comment. I will replace system with a list. We're going to put inside of here a text block. So we'll be a dictionary with a type of text, text of system, and then finally a cache control type ephemeral. And that's it. Alright, so let's now run the cell. We're going to go down to the very bottom and test out this caching that we have set up. So down here at the very bottom, I've already defined a list of tools. These are tool schemas that are defined inside the cell right above. We've also got that very large system prompt right here of code prompt. So let's first try just passing in nothing at all. So no list of tools, no prompt whatsoever. We're just going to see the number of tokens that are used to process the message of was one plus one and generate a response. So if I run this, I'll get back in output and we can notice that there is a usage field inside of here. So it looks like we sent in 14 tokens and we got 11 out. Let's now try adding in our list of tools. So when I add that in and run this, we're now going to see a very different usage field. Now our usage has a cache creation input tokens of 1700. That means that Claude has seen that we want to do cache our schemas. So it has written into the cache a total of about 1700 tokens. So now if we make a follow-up request immediately, without changing anything about it, we'll see that we are now going to read a certain number of tokens out of our cache. So now we've got a cache read of 1700. That means that we have successfully stored our schemas inside the cache and then retrieve them at some point in time in the future. Now, if we change our user message here in any way, maybe by deleting that question mark at the end, and then rerun this, we are still going to read out of the cache because remember the caching order is the list of tools, then our system prompt, and then our different messages. So we'll still read out of the cache like so. However, if we change any of our tools in any way whatsoever, we're going to invalidate the cache. So if I go to my list of tools, I'm going to change the description on the very first tool. I'm going to remove the S on the word ads. So now let's just add a specified duration. Now if I rerun cell, I've changed my tool schema. And that means that the cache breakpoint that we have applied to all of our different tools is no longer going to apply. If I run the very bottom cell again, we'll see an updated value of usage. So now we're going to have a cache write once again. So no longer reading. We're now back to writing because we have sent in a list of tools that as far as Claude is concerned is completely different. All right, so now let's try adding in our system prompt. I'm going to go to our chat function, and I'll add in system code prompt. So now when we make this request, remember the order of caching, it is tools, then the system prompt, and then our list of messages. Because we are leaving our list of tools completely identical, but we are changing the system prompt, I would expect to see a partial cache read and then a cache write at the same time. The cache read that we're going to see is because we are making use of the same list of tools. And the cache write is going to because we are sending up a new cache breakpoint by sending in this new prompt. So I'm going to run this. And now we should see a, there we go, a cache read of 1700 and a cache write of 6.3. Now, just like our list of tools, if we go up to our system prompt and we change this prompt in any way, maybe by just removing the word builder at the very end here and then rerunning that cell. Now, once again, as far as Claude is concerned, if we send in another request, this will be a completely different system prompt. So we are going to lose out on all the cache data we had previously around the system prompt. So now I'll send this again, and we will once again see a cache read of about 1.7, there we go. And then we are once again writing this brand new system prompt, so that's another 6.3. All right, my friends, that is prompt caching. Again, you're going to very often use prompt caching anytime you are sending in identical content, either in the form of the same list of messages, the same tool schemas, or the same system prompt.

---

## 🎬 トランスクリプト（日本語）

それでは、プロンプトキャッシングを実際に試してみましょう。 003 caching という新しいノートブックを作成しました。 このノートブックは、もちろんこの講義に添付されています。この中に 「prompt with 6K tokens」というセクションがあります。 これはシステムプロンプトとして使用するものです。 後でこれを使用します。それに加えて、 ツールスキーマのセクションもあります。ここにはいくつかの異なるツールスキーマが 含まれています。これらの異なるツールスキーマをすべて合わせると、 合計で約1.7Kトークンになります。 チャット機能を更新していきます。 このチャット機能は、上のセルの「helper functions」の中にあります。 このチャット機能が、ツールスキーマとシステムプロンプトの プロンプトキャッシングを常に有効にするようにします。 その方法をお見せします。 「helper function」のセクション内で、 チャット関数までスクロールします。ここにあります。 もう少しスクロールすると、 2つの「to-do」項目を追加したことに気づくでしょう。まず、 ツールリストが提供された場合、 ツールのリストを常にキャッシュします。次に、システムプロンプトを 提供した場合、それもキャッシュします。 単一のリクエスト内に複数の異なるキャッシュブレークポイントを 持つことができることを覚えておいてください。したがって、 システムプロンプトとツールのリストの両方を渡す場合、 2つの異なるキャッシュブレークポイントを設定します。 まず、ツールのリストのキャッシュを行います。 そのために、Claudeに渡す最後のツールスキーマを 変更する必要があることを思い出してください。 特にキャッシュ制御フィールドを追加する必要があります。 例えば、次のようにすることができます。 ツール、マイナス1、 そしてキャッシュ制御フィールドを エフェメラルというタイプで設定します。 このように。動作はしますが、 最高のコーディング技術ではありません。これは キャッシュ制御フィールドを追加することでツールスキーマを実際に変更します。 後でツールスキーマの順序を変更することを決定するシナリオがあるかもしれません。 その場合、ツールスキーマ内に複数の異なるキャッシュブレークポイントが設定されることになりますが、 それは必ずしも望ましいとは限りません。 したがって、より良い方法は まずツールのリストのコピーを作成することです。 次に、そこにある最後のツールスキーマをクローンし、 キャッシュ制御フィールドを追加します。 どうすればよいか見てみましょう。 新しい変数「tools clone」を作成します。これは 「tools.copy」を呼び出して取得します。 これによりリスト全体がコピーされます。次に、 そこにある最後のツールをコピーします。 そしてキャッシュ制御フィールドを追加します。 最後のツールスキーマに。 したがって、それはエフェメラルなタイプになります。 次に、ツールクローン内の最後の要素を 先ほど作成したツールスキーマのコピーで上書きします。 tools.cloneの マイナス1は最後のツールになります。 そして、ツールクローンをツールプログラムに割り当てます。 ここで繰り返しになりますが、 ここにあるすべてのコピーロジックは 厳密には必要ありません。 いつかツールリストを変更することを決定した場合に備えて、 これは単に良い習慣です。 いつかツールリストを変更することを決定した場合に備えて、 これは単に良い習慣です。次に、2番目のto-doを処理します。 システムプロンプトを渡した場合、 常にキャッシュブレークポイントを設定するようにします。 そのためにコメントを削除します。 システムをリストに置き換えます。ここには テキストブロックを配置します。 タイプがテキストの辞書になります。 テキストはシステム、そして最後に キャッシュ制御タイプのエフェメラルです。 これで完了です。さて、 このセルを実行しましょう。一番下まで移動して 設定したキャッシングをテストします。 ここに、ツールリストを既に定義しました。これらは 直前のセルのツールスキーマです。また、 この非常に大きなシステムプロンプト、 コードプロンプトもあります。まず、何も渡さない 場合を試してみましょう。ツールリストもプロンプトも 全くありません。メッセージを処理するために使用されるトークン数を見て、 「1+1は？」と応答を生成します。 これを実行すると、出力が得られ、使用状況フィールドがあることに気づくでしょう。 14トークンを送信して11トークンを受け取ったようです。 それでは、ツールリストを追加してみましょう。 それを追加して実行すると、 使用状況フィールドが大きく異なります。 今、使用状況には キャッシュ作成入力トークンが1700あります。 これは、Claudeが スキーマをキャッシュしたいと認識したということです。 したがって、約1700トークンをキャッシュに書き込みました。 だから、もし私たちがフォローアップリクエストをすれば すぐに、何も変更せずに、 キャッシュから一定数のトークンを読み取ることになります。 だから今、キャッシュ読み取りが1700です。 つまり、スキーマをキャッシュに保存し、 その後、将来のある時点で取得できたということです。 ユーザーメッセージを変更した場合 例えば、最後の疑問符を削除した場合、 そしてこれを再度実行すると、 まだキャッシュから読み取ります。なぜなら、キャッシュの順序は ツールのリスト、次にシステムプロンプト、そしてメッセージ だからです。 ツールのリストは完全に同じですが、システムプロンプトを変更しているので、 部分的なキャッシュ読み取りと同時にキャッシュ書き込みが発生すると予想されます。 キャッシュ読み取りは、同じツールのリストを使用しているためです。 そしてキャッシュ書き込みは、この新しいプロンプトを送信することで 新しいキャッシュブレークポイントを送信するためです。 これを実行しましょう。そして、 キャッシュ読み取りが1700、キャッシュ書き込みが6.3になるはずです。 さて、ツールリストのように、 システムプロンプトに移動して、このプロンプトを 変更した場合、例えば最後の単語「builder」を削除した場合、 そしてそのセルを再度実行すると、 Claudeにとって、これは完全に異なるシステムプロンプトになります。 そのため、以前のシステムプロンプトに関するすべてのキャッシュデータを失うことになります。 そこで、もう一度送信すると、 約1.7のキャッシュ読み取りと 6.3の書き込みが見られます。 これで完了です。皆さん、これがプロンプトキャッシングです。 ユーザーメッセージを変更した場合、 例えば疑問符を削除した場合、 そしてこれを再度実行すると、 キャッシュから読み取ります。なぜなら、キャッシュの順序は ツールのリスト、次にシステムプロンプト、そしてメッセージ だからです。 ツールのリストは完全に同じですが、システムプロンプトを変更しているので、 部分的なキャッシュ読み取りと同時にキャッシュ書き込みが発生すると予想されます。 キャッシュ読み取りは、同じツールのリストを使用しているためです。 そしてキャッシュ書き込みは、この新しいプロンプトを送信することで 新しいキャッシュブレークポイントを送信するためです。 これを実行しましょう。そして、 キャッシュ読み取りが1700、キャッシュ書き込みが6.3になるはずです。 さて、ツールリストのように、 システムプロンプトに移動して、このプロンプトを 変更した場合、例えば最後の単語「builder」を削除した場合、 そしてそのセルを再度実行すると、 Claudeにとって、これは完全に異なるシステムプロンプトになります。 そのため、以前のシステムプロンプトに関するすべてのキャッシュデータを失うことになります。 そこで、もう一度送信すると、 ユーザーメッセージを変更した場合、 例えば疑問符を削除した場合、 そしてこれを再度実行すると、 まだキャッシュから読み取ります。なぜなら、キャッシュの順序は ツールのリスト、次にシステムプロンプト、そしてメッセージ だからです。 ツールのリストは完全に同じですが、システムプロンプトを変更しているので、 部分的なキャッシュ読み取りと同時にキャッシュ書き込みが発生すると予想されます。 キャッシュ読み取りは、同じツールのリストを使用しているためです。 そしてキャッシュ書き込みは、この新しいプロンプトを送信することで 新しいキャッシュブレークポイントを送信するためです。 これを実行しましょう。そして、 キャッシュ読み取りが1700、キャッシュ書き込みが6.3になるはずです。 さて、ツールリストのように、 システムプロンプトに移動して、このプロンプトを 変更した場合、例えば最後の単語「builder」を削除した場合、 そしてそのセルを再度実行すると、 Claudeにとって、これは完全に異なるシステムプロンプトになります。 そのため、以前のシステムプロンプトに関するすべてのキャッシュデータを失うことになります。 そこで、もう一度送信すると、 約1.7のキャッシュ読み取りと 6.3の書き込みが見られます。 さて、皆さん、これがプロンプトキャッシングです。 同じメッセージリスト、同じツールスキーマ、 または同じシステムプロンプトの形で、 同一の内容を送信する場合、 プロンプトキャッシングを非常によく使用します。 同一の内容を送信する場合、 プロンプトキャッシングを非常によく使用します。
