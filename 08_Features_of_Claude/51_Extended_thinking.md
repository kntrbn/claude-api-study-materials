# 51. Extended thinking

**URL:** https://anthropic.skilljar.com/claude-with-the-anthropic-api/287773
**Section:** 08 Features of Claude

---

## 📄 Page Content

Anthropic Academy
    
  

  
    
      Courses
    
  

    

    
      
      

      
        
          My Profile
        
        
      

      
      

      
        Sign Out
      
    
  

  

  

    
    
    
        
            
    
        
    

            
    
        
        
            
                
                    
                        
                            
                                
                            

                            
                                details
                            

                            
                                
                                    
                                    2
                                    download
                                
                            
                        
                    
                
            
            
                
                
                
                    Extended thinking
                    
                
                
                    
                        
                            
                                
                                    

    
    

    
    
        
            
        
        
            
                
                This video is still being processed. Please check back later and refresh the page.
            
        
        
            
                Uh oh! Something went wrong, please try again.
            
        
    

    

                                
                            
                        
                    
                
            
        
        
            

    
        
            
                
                    
                        
                            
                        
                    
                
            
            
                
                    Summary
                

                

            
        

        
            
                
                    
                        
                            Summary

                            
                                Important Note: Extended Thinking is not compatible with some other features, notable message pre-filling and temperature. See the full list of restrictions here: https://docs.anthropic.com/en/docs/build-with-claude/extended-thinking#feature-compatibility
 
Extended thinking is Claude's advanced reasoning feature that gives the model time to work through complex problems before generating a final response. Think of it as Claude's "scratch paper" - you can see the reasoning process that leads to the answer, which helps with transparency and often results in better quality responses.
How Extended Thinking Works
When extended thinking is enabled, Claude's response changes from a simple text block to a structured response containing two parts:

With thinking enabled, you get both the reasoning process and the final answer:

The key benefits include:

Better reasoning capabilities for complex tasks
Increased accuracy on difficult problems
Transparency into Claude's thought process

However, there are important trade-offs:

Higher costs (you pay for thinking tokens)
Increased latency (thinking takes time)
More complex response handling in your code

When to Use Extended Thinking
The decision is straightforward: use your prompt evaluations. Run your prompts without thinking first, and if the accuracy isn't meeting your requirements after you've already optimized your prompt, then consider enabling extended thinking. It's a tool for when standard prompting isn't quite getting you there.
Response Structure and Security
Extended thinking responses include a special signature system for security:

The signature is a cryptographic token that ensures you haven't modified the thinking text. This prevents developers from tampering with Claude's reasoning process, which could potentially lead the model in unsafe directions.
Redacted Thinking
Sometimes you'll receive a redacted thinking block instead of readable reasoning text:

This happens when Claude's thinking process gets flagged by internal safety systems. The redacted content contains the actual thinking in encrypted form, allowing you to pass the complete message back to Claude in future conversations without losing context.
Implementation
To enable extended thinking in your code, you need to add two parameters to your chat function:
def chat(
    messages,
    system=None,
    temperature=1.0,
    stop_sequences=[],
    tools=None,
    thinking=False,
    thinking_budget=1024
):
The thinking budget sets the maximum tokens Claude can use for reasoning. The minimum value is 1024 tokens, and your max_tokens parameter must be greater than your thinking budget.
Add the thinking configuration to your API parameters:
if thinking:
    params["thinking"] = {
        "type": "enabled",
        "budget": thinking_budget
    }
Then call it with thinking enabled:
chat(messages, thinking=True)
Testing Redacted Responses
For testing purposes, you can force Claude to return a redacted thinking block by sending a special trigger string. This helps ensure your application handles redacted responses gracefully without crashing.
Extended thinking is a powerful feature when you need Claude to tackle complex reasoning tasks, but use it judiciously given the cost and latency implications. Start with standard prompting, optimize thoroughly, then add thinking when you need that extra reasoning capability.
                            
                        
                    

                    
                        
                            Downloads
                            
                                
                                    
                                        
                                            
                                            
                                    

---

## 🎬 Transcript (English)

Let's examine one of Claude's more advanced features known as extended thinking. Extended thinking gives Claude time to reason about the user's query before generating a final response. In many chat UIs, this will be displayed as a separate thinking process, which the user can optionally look at to get better idea of how Claude is approaching their problem. Now in general, enabling extended thinking will allow Claude to tackle more complex tasks with greater accuracy, but there are some big trade-offs here. You are charged for tokens generated by Claude during the thinking phase, and the phase itself takes some amount of time to complete. So with increased intelligence comes increased cost, and there's increased latency as well. Now a common issue around extended thinking is deciding when to enable it. And the answer to this is really simple. You're going to rely on your prompt eVals. So you're going to write out a prompt. You're going to run an eVal on it. And if the accuracy is not where you want it to be, and you've already spent some good amount of effort on improving your prompt in the first place, that is when you would want to consider enabling extended thinking. The use of extended thinking is fairly straightforward. Remember, when we normally use Claude, we send over a user message that might contain a text block. And then we're going to get back an assistant message that contains a text block as well. When we start to enable extended thinking, the response we get back is going to contain a new block type that we have not seen before called a thinking block. Inside of this thinking block is going to be the text that was generated while Claude was thinking. There's something really interesting around this thinking block that I want to show you right away, because you're going to see it really quickly as soon as you start writing out some code and making requests with extended thinking turned on. On the right-hand side, I've got an example of an assistant message that includes a thinking block and a text block. Inside the thinking block, you'll notice that there is something called a signature. The signature is a cryptographic token, and here's what it does. If you want to take this message and send it back to Claude as a piece of the conversation in the future, Claude wants to make sure that you did not modify the text in the thinking block in any way. The signature is used to make sure that you did not change the text. Claude doesn't want you changing that text at all because it is relied upon very heavily during response generation. And if developers were allowed to modify that text, they could possibly steer Claude in an unsafe direction. There's one other aspect of thinking related to this idea. In some cases, you might get back a thinking block that has a field of redacted content without any thinking text at all. This occurs whenever Claude generates some thinking text that gets flagged by some internal safety system. The redacted content is the actual thinking text, but in a fully encrypted form. It is provided to you so you can give this full message back to Claude in the future as part of a conversation without Claude losing any context on his previous thinking. To really understand extended thinking, we need to write out a little bit of code. So let's go back over to our Jupyter notebooks. I've made a new notebook called 001 thinking. Once again, it has a lot of the similar code that we've been working on throughout the course, but I've added one or two very special things. So I would encourage you to make sure you download this notebook. It is attached to this lecture. In order to enable thinking, we need to find our chat function. We're going to provide some additional arguments to the chat function that will eventually be added into this params object. So I'm going to add in thinking. with a default value of false, and then a thinking underscore budget of 1024. The thinking budget is the number of tokens that we want to allow Claude to use in generating a thinking portion of the response. The minimum value here is 1024, so we cannot have a thinking budget less than 1024. It's entirely possible that Claude will not spend 1024 tokens on thinking, but again, this is the minimum that we can specify as the budget. There's one other very important fact you need to understand around the thinking budget. And that is, that max tokens must be greater than your thinking budget. So for example, if we have a thinking budget of 1024, max tokens must be at least 1025. And that's only going to leave one token remaining to actually apply to generating some text. So usually you're going to want to have a max tokens value that is generally significantly larger than your thinking budget. So in my case, I'm going to increase my max tokens here to 4,000. And now I've got a pretty big buffer. This means that I can generate a response that has 1,000 tokens allocated to thinking, and then a remaining 3,000 tokens can be allocated to actually generating some text. Once we have added in these two keyword arguments, we're then going to add in some additional parameters to the params dictionary. So scroll down a little bit and down here. I'll say if thinking is enabled, then I want to add in a new key to my params dictionary, specifically thinking. This is going to be a nested dictionary with a type of enabled and a budget tokens of whatever we passed in as the thinking budget, like so. And that's it. So I'm going to run the cell, I'll then scroll down to the bottom so we can test this out. I'm going to ask Claude to write out a one paragraph guide to recursion. I'll then make sure that I update my chat function call right here to enable thinking by passing in thinking true. I'll then run this and let's see how we do. And here's our response. So in the response, I get two separate blocks. First, I have my thinking block, and then a little bit lower down right there is the start of my text block. Inside the thinking block, I do in fact have a signature. And along with it, I've got my thinking text. Remember, the goal of the signature is to make sure that we don't tap or tamper with the thinking text in any way. And of course, our text block right here contains the actual guide that we ask Claude to write. Now the last thing I want to show you is something that you might use when you are initially building and testing out your application. As a reminder, there might be some scenarios where Claude sends back a redacted thinking block. As you are building out your application, you might want to make sure that your code works correctly whenever a redacted thinking block is sent to you. So we can actually force Claude to send us back a redacted thinking block. All we have to do is send in a message that includes a very, very specially formatted string. So if you scroll up to the very top of the second cell inside of here, you'll notice I put in thinking test string. And then it has a value of Anthropic, magic string triggered redacted thinking, and then a bunch of special numbers and letters after it. If you send exactly this string into Claude, you are guaranteed to get back a redacted thinking block. Again, we would just do this for testing purposes to make sure that we can handle that kind of response. So let me just show you this to you really quickly. I'm going to go back down to the bottom cell. I'm going to add in a user message that contains just that thinking test string. I'll then send this in. And now we should be getting back a response that's going to have a redacted thinking block inside of it. There we go. So I've got my redacted thinking block and it has nothing but a data and a type of redacted thinking. So now, like I said, we could just use this to make sure that our application doesn't crash when receiving this kind of unexpected thinking block in response.

---

## 🎬 トランスクリプト（日本語）

Claudeの高度な機能の1つである、拡張思考について見ていきましょう。 拡張思考とは、 Claudeがユーザーのクエリについて推論する時間を確保し、その後 最終的な回答を生成するものです。多くのチャットUIでは、 これは個別の思考プロセスとして表示され、ユーザーは任意でそれを参照することで Claudeがどのように問題に取り組んでいるかをより深く理解できます。 Claudeがどのように問題に取り組んでいるかをより深く理解できます。 一般的に、拡張思考を有効にすると、Claudeは より複雑なタスクを、より高い精度で処理できるようになります。しかし、ここには いくつかの大きなトレードオフがあります。思考フェーズ中にClaudeが生成したトークンに 対して課金され、フェーズ自体も完了までに時間がかかります。 思考フェーズ自体も完了までに時間がかかります。 したがって、知性の向上に伴い、コストとレイテンシも増加します。 知性の向上に伴い、コストとレイテンシも増加します。 また、レイテンシも増加します。 拡張思考を有効にするかどうかを決める際に一般的な問題は、 いつ有効にするかということです。そしてその答えは非常にシンプルです。 プロンプトの評価に依存します。プロンプトを作成し、 それを評価します。そして、その精度が望むレベルに達しておらず、 すでに最初のプロンプト改善にかなりの労力を費やしている場合、 それが拡張思考の有効化を検討すべき時です。 拡張思考の利用は非常に簡単です。覚えておいてください、 通常のClaudeの使用では、テキストブロックを含むユーザーメッセージを送信し、 アシスタントメッセージとしてテキストブロックが返ってきます。 通常のClaudeの使用では、テキストブロックを含むユーザーメッセージを送信し、 アシスタントメッセージとしてテキストブロックが返ってきます。拡張思考を有効にし始めると、返ってくる応答には これまで見たことのない新しいブロックタイプが含まれます。 それは思考ブロックと呼ばれます。 この思考ブロックの中には、Claudeが思考中に生成したテキストが含まれています。 この思考ブロックには、本当に興味深いものがあり、すぐに示したいと思います。 コードを書き始め、要求を行うとすぐにこれが見られるからです。 拡張思考をオンにしている場合。右側には、 思考ブロックとテキストブロックを含むアシスタントメッセージの例があります。 思考ブロックの中に、署名と呼ばれるものがあることに注意してください。 署名は暗号化されたトークンです。そしてこれが何をするかというと、 このメッセージを将来の会話の一部としてClaudeに送り返したい場合、 Claudeは、あなたが思考ブロック内のテキストを変更していないことを確認したいと考えています。 署名は、あなたがテキストを変更していないことを確認するために使用されます。 Claudeはあなたがそのテキストを変更することを望んでいません。なぜならそれは 応答生成において非常に重視されているからです。 そしてもし開発者がそのテキストを変更することを許可されていたら、 彼らはClaudeを安全でない方向に導く可能性があります。 これに関連して、思考に関するもう1つの側面があります。 場合によっては、 思考テキストなしで、 redacted content というフィールドを持つ思考ブロックを受け取る可能性があります。 これは、Claudeが生成した思考テキストが内部の安全システムによってフラグ付けされた場合に発生します。 redacted content は実際の思考テキストですが、 完全に暗号化された形式です。これは、あなたがこのメッセージ全体を 将来の会話の一部としてClaudeに返せるように提供されます。 Claudeが以前の思考の文脈を失うことなく。 拡張思考を本当に理解するために、私たちは少しコードを書く必要があります。 それでは、Jupyter Notebookに戻りましょう。 001 thinking という新しいノートブックを作成しました。 繰り返しになりますが、コースを通して作業してきたコードの多くは同様ですが、 1つか2つの非常に特別なものを追加しました。 ですから、このノートブックをダウンロードすることを強くお勧めします。 この講義に添付されています。思考を有効にするには、 チャット関数を見つける必要があります。チャット関数に 追加の引数を提供します。これらは最終的にこのparamsオブジェクトに追加されます。 なので、thinking を追加します。 デフォルト値はfalse、そしてthinking_budgetは1024にします。 thinking_budgetは、Claudeに思考部分の生成に 使用させたいトークンの数です。 最小値は1024です。 したがって、thinking_budgetを1024未満にすることはできません。 Claudeが思考に1024トークンを費やさない可能性も十分にありますが、 これは指定できる最小の予算です。 thinking_budgetに関して理解すべきもう1つの非常に重要な事実があります。 それは、max_tokensがthinking_budgetより大きくなければならないということです。 たとえば、thinking_budgetが1024の場合、max_tokensは少なくとも1025でなければなりません。 そして、テキスト生成に適用できるのは1トークンだけです。 したがって、通常はmax_tokens値をthinking_budgetより大幅に大きくしたいでしょう。 したがって、私の場合は、max_tokensを4000に増やします。 これでかなりのバッファができました。 これは、1000トークンを思考に割り当て、 残りの3000トークンを実際のテキスト生成に割り当てることができることを意味します。 これら2つのキーワード引数を追加したら、params辞書に 追加のパラメータを追加します。 少し下にスクロールして、ここにあります。 思考が有効になっている場合、params辞書に 新しいキー、具体的にはthinkingを追加します。 これは、タイプ enabled、そしてbudget tokens が thinking_budgetとして渡された値であるネストされた辞書になります。 このようになります。これで完了です。 セルを実行します。次に、テストするために下にスクロールします。 Claudeに再帰に関する1段落のガイドを書くように依頼します。 次に、ここにあるチャット関数呼び出しを更新して、 thinking=True を渡して思考を有効にします。 そしてこれを実行して、どうなるか見てみましょう。 これが私たちの応答です。応答には2つの別々のブロックがあります。 まず、思考ブロックがあり、その下にテキストブロックがあります。 思考ブロックの中には、署名があります。そしてその横には思考テキストがあります。 署名の目標は、私たちが思考テキストに触れたり改ざんしたりしないようにすることです。 そしてもちろん、ここにあるテキストブロックには、 Claudeに書くように依頼した実際のガイドが含まれています。 最後に紹介したいのは、アプリケーションを初期に構築およびテストする際に使用する可能性があるものです。 注意点として、Claudeが redacted thinking block を返すシナリオがあるかもしれません。 アプリケーションを構築する際に、 redacted thinking block が 渡されたときにコードが正しく動作することを確認したいと思うかもしれません。 そのため、実際に redacted thinking block を返すようにClaudeに強制できます。 非常に特別にフォーマットされた文字列を含むメッセージを送信するだけです。 したがって、2番目のセルの先頭までスクロールすると、 thinking_test_string という値を挿入したことがわかります。 そしてそれは Anthropic, magic string triggered redacted thinking、そして多くの 特殊な数字と文字の後ろに続きます。この文字列を正確にClaudeに送信すると、 redacted thinking block を受け取ることが保証されます。 再度、これは、この種の応答を処理できることを確認するためだけのテスト目的で使用します。 ですので、これを本当に簡単に示したいと思います。 一番下のセルに戻ります。 思考テスト文字列を含むユーザーメッセージを追加します。 そしてこれを送信します。そして今、 redacted thinking block が含まれる応答を受け取るはずです。 これで完了です。 redacted thinking block があり、 それにはデータと redacted thinking というタイプしかありません。 これで、先ほど述べたように、この redacted thinking block を受け取っても アプリケーションがクラッシュしないことを確認するために使用できます。 これで完了です。
