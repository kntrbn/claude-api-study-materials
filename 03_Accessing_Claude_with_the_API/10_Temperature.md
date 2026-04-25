# 10. Temperature

**URL:** https://anthropic.skilljar.com/claude-with-the-anthropic-api/287728
**Section:** 03 Accessing Claude with the API

---

## 📄 Page Content

Anthropic Academy
    
  

  
    
      Courses
    
  

    

    
      
      

      
        
          My Profile
        
        
      

      
      

      
        Sign Out
      
    
  

  

  

    
    
    
        
            
    
        
    

            
    
        
        
            
                
                    
                        
                            
                                
                            

                            
                                details
                            

                            
                        
                    
                
            
            
                
                
                
                    Temperature
                    
                
                
                    
                        
                            
                                
                                    

    
    

    
    
        
            
        
        
            
                
                This video is still being processed. Please check back later and refresh the page.
            
        
        
            
                Uh oh! Something went wrong, please try again.
            
        
    

    

                                
                            
                        
                    
                
            
        
        
            

    
        
            
                
                    
                        
                            
                        
                    
                
            
            
                
                    Summary
                

                

            
        

        
            
                
                    
                        
                            Summary

                            
                                Temperature is a powerful parameter that controls how predictable or creative Claude's responses will be. Understanding how to use it effectively can dramatically improve your AI applications.

How Claude Generates Text

Before diving into temperature, it helps to understand Claude's text generation process. When you send Claude a prompt like "What do you think?", it goes through three key steps:

Tokenization - Breaking your input into smaller chunks
Prediction - Calculating probabilities for possible next words
Sampling - Choosing a token based on those probabilities

In this example, Claude might assign a 30% probability to "about", 20% to "would", 10% to "of", and so on. The model then selects one token and repeats this entire process to build complete sentences.

What Temperature Does

Temperature is a decimal value between 0 and 1 that directly influences these selection probabilities. It's like adjusting the "creativity dial" on Claude's responses.

At low temperatures (near 0), Claude becomes very deterministic - it almost always picks the highest probability token. At high temperatures (near 1), Claude distributes probability more evenly across options, leading to more varied and creative outputs.

Interactive Temperature Demo

You can see temperature in action with Claude's interactive demo. Watch how the probability distribution changes as you adjust the temperature slider:

At temperature 0.0, "about" gets 100% probability - completely deterministic. At temperature 1.0, probabilities spread more evenly across all possible tokens, introducing randomness and creativity.

Choosing the Right Temperature

Different tasks call for different temperature ranges:

Low Temperature (0.0 - 0.3)

Factual responses
Coding assistance
Data extraction
Content moderation

Medium Temperature (0.4 - 0.7)

Summarization
Educational content
Problem-solving
Creative writing with constraints

High Temperature (0.8 - 1.0)

Brainstorming
Creative writing
Marketing content
Joke generation

Implementing Temperature in Code

Adding temperature support to your chat function is straightforward. Here's how to modify your existing function:

def chat(messages, system=None, temperature=1.0):
    params = {
        "model": model,
        "max_tokens": 1000,
        "messages": messages,
        "temperature": temperature
    }
    
    if system:
        params["system"] = system
    
    message = client.messages.create(**params)
    return message.content[0].text

The key changes are adding temperature=1.0 as a parameter and including "temperature": temperature in the params dictionary.

Testing Temperature Effects

To see temperature in action, try generating movie ideas with different settings:

# Low temperature - more predictable
answer = chat(messages, temperature=0.0)

# High temperature - more creative  
answer = chat(messages, temperature=1.0)

At temperature 0.0, you might consistently get responses like "A time-traveling archaeologist must prevent ancient artifacts from being stolen." At temperature 1.0, you'll see much more variety in themes, characters, and plot elements.

Key Takeaways

Remember that temperature doesn't guarantee different outputs - it just changes the probability of getting them. Even at high temperatures, Claude might occasionally produce similar responses. The key is matching your temperature choice to your specific use case:

Need consistent, factual responses? Use low temperature
Want creative brainstorming? Dial up the temperature
Somewhere in between? Medium temperatures work well for most general tasks

Temperature is one of the most practical parameters you can adjust to fine-tune Claude's behavior for your specific needs.

---

## 🎬 Transcript (English)

Earlier on inside this course, we spoke very briefly about how Claude actually generates text. Remember, we feed some amount of text into Claude, like the words, what do you think. Claude is then going to tokenize this text or break it up into smaller chunks. Claude is then going to go through a prediction phase where it decides what possible words could come next and assign a probability to each of those different options. Finally, in the sampling phase, a token is actually chosen based upon these probabilities. So in this diagram I have on the screen, given inputs of what do you think possible next tokens might be about, wood, and so on. Everything you see here on the right-hand side. Each of these gets assigned a probability. And then maybe in this case, Claude settles on about as being the best possible next token. So we would end up with a phrase, what do you think about? This entire process is then repeated to complete the sentence or complete the entire message. Now just to make sure things are really clear, the numbers I'm showing here are probabilities, the percentage chance of each token being selected. And just to make things a little bit more clear with these probabilities, I'm going to display them in a chart for the rest of this video. So still the same probability is just in a format that's easier for us to understand. You also notice I've kind of sorted them from left to right. There's no actual internal sorting going on. I'm just sorting them greatest to these probability just to make this chart a little bit easier to understand. So now that we have a reminder on how Claude generates text, I want to show you one way that we can directly influence these probabilities and control which token Claude might actually decide to select. So we can control these probabilities using a parameter called temperature. Temperature is a decimal value between 0 and 1 that we provide when we make our model call. So whenever we call that converse function, temperature is going to influence the exact distribution of probabilities. This is a little bit tricky to understand. So you can look at the plot or these charts I've got right here. Or alternatively, I put together a quick little demo with plot itself just to give you a better idea of what's going on. So let me show you that demo. Okay, so this is the same chart we were just looking at in that diagram a moment ago. Whenever we provide a temperature value going down to zero, as you'll see, I got temperature right here, the highest probability becomes more likely to occur. So our highest probability was about, and it's going to increase all the way up to 100%. So at temperatures of zero, we start to get what we call a deterministic output, where we always select the token that has the highest initial probability. Then, as we start to increase our temperature, it increases the chances of us selecting a token that has a lower initial probability. So we go from maybe having a 0% chance of selecting we as the next token, although it to say 9%. So this is the theory behind temperature, but what does this actually mean in the real world? Well, we start to use different values of temperature, given the actual task that we're trying to complete. These are some example ranges and tasks that might fit into each sample range. For something like, say, data extraction, we really don't want a lot of randomness or creativity. If we give Claude a big chunk of text and ask it to extract very specific pieces of information, no real creativity required there whatsoever. We just want Claude to look at the exact text we provided and pull out the most relevant information. And then on the higher temperature side, this is where we start to get more creative. And we start to see less common tokens being used. We probably are going to want to use higher temperatures anytime we are doing any kind of really creative focus task, such as brainstorming, writing, maybe doing some really creative marketing, or something like a joke where a lot of jokes really depend upon using words in ways that are not always quite expected. Now that we understand what temperature is all about, let's go back over to our notebook and understand how we can adjust temperature on the fly. I would like to update our chat function so that it takes in a temperature argument that we're going to pass through to our create function call. So inside of the list of arguments, I'm going to add in temperature and I'm going to default my temperature to be 1.0. So I want to fall on the more creative side of things. Then I'm going to take in that argument and add it into the Params object as temperature. And that's all we have to do to add in support for adjusting the temperature inside of our application. So now to test this out, I'm going to rerun this cell. I'm then going to go down to the next cell, and I'm going to ask Claude to generate a one sentence movie idea. And initially, I'm going to provide a temperature of 0.0. So now in theory, I should be getting back movie ideas that always tend to be a little bit similar in nature. So I'm going to run this. And the first time, I'm going to get back a time-traveling archeologist. You're going to see that this is a very common pattern, at least for me. I very often, when I have a temperature of zero, get movie ideas that are about a time-traveling something. So if I run this again, I'm probably going to see another time-traveling thing. Yep, same thing. Maybe one more time. And yeah, same kind of idea, a jaded time-traveling historian. Let's now try adjusting our temperature a little bit to hopefully encourage Claude to give us some more original or creative ideas. I'm going to try adjusting my temperature up to 1.0. Now if I run this again, I hopefully will not get an idea about a jaded time traveler or something like that. And almost immediately you can see that I do. So this is something to be aware of. Just because you dial up the temperature doesn't mean you're always going to get dramatically different ideas. It just increases the chances of getting a different one. So if I run this again, I might end up seeing out more creative idea. Okay, that's definitely more creative. Nothing about time travel this time and be one more test year. And there we go, again, not about a time traveler or anything like that. All right, so that is temperature. Now remember, there's some general guidance here. Whenever we are doing tasks that require less creativity, or whenever we want to have a very deterministic output, we want to use that lower temperature value. And whenever we have a task that requires a little bit more creativity, that's when we want to start to think about dialing up the temperature a little bit.

---

## 🎬 トランスクリプト（日本語）

このコースの冒頭で、ごく簡単に話しました Claudeがどのようにテキストを生成するのかについて。覚えていますか？ Claudeにテキストを少量入力します。「What do you think?」のような 単語です。Claudeはその後、そのテキストをトークン化するか より小さなチャンクに分割します。Claudeは 次に予測フェーズに入り、次に どの単語が来る可能性があるかを決定し、それぞれの 異なるオプションに確率を割り当てます。 最後に、サンプリングフェーズで、これらの確率に基づいて トークンが実際に選択されます。画面上の この図では、「what do you think?」という入力に対して、 次にくる可能性のあるトークンは 「about」、「wood」などで、 右側に見えるすべてがそれに相当します。これら それぞれに確率が割り当てられます。そしておそらく この場合は、Claudeが「about」を 次にくる最適なトークンとして選択したとします。 その結果、「What do you think about?」というフレーズになります。 このプロセス全体が繰り返され、文または メッセージ全体が完成します。さて、 物事を明確にするために、ここで示している数字は 確率、つまり各トークンが選択される確率（パーセンテージ）です。 そして、これらの確率をもう少し分かりやすくするために、 このビデオの残りの部分では、それをグラフで表示します。 ですので、同じ確率ですが、 より理解しやすい形式になっています。 左から右へソートしていることにも気づくでしょう。 実際には内部でソートは行われていません。ただ このグラフを少し分かりやすくするために、 確率の高い順にソートしているだけです。 Claudeがテキストをどのように生成するかの復習は終わり、 これで、これらの確率を直接影響させ、 Claudeが選択する可能性のあるトークンを制御する方法を 1つお見せしたいと思います。 これらの確率を制御するために、 温度（temperature）と呼ばれるパラメータを使用できます。温度とは モデルを呼び出す際に提供する、0から1の間の 小数値です。モデルを呼び出すたびに、 `converse`関数を呼び出すとき、温度は 確率の分布に影響を与えます。 これは少し理解が難しいので、グラフを見るか、 ここにあるチャートを見ることができます。または、代わりに、 実際に何が起こっているのかをよりよく理解するために、 簡単なデモを作成しました。では、そのデモを見せましょう。 はい、これは先ほどの図で見ていたのと同じグラフです。 温度値を ゼロに近づけると、ご覧のように、ここにある温度設定で、 最も確率の高いものがより発生しやすくなります。 私たちの最も高い確率は「about」でしたが、 それは100%まで増加します。 つまり、温度がゼロの場合、決定論的な 出力と呼ばれるものになります。これは常に最も高い 初期確率を持つトークンを選択します。次に、温度を上げ始めると、 より低い初期確率を持つトークンを選択する確率が増加します。 つまり、例えば、次にくるトークンとして 「we」を選択する確率が0%だったものが、 例えば9%になるのです。これが温度の理論ですが、 実際の世界ではどういう意味でしょうか？ さて、温度の値を色々変えていくと、 実行しようとしているタスクに応じて変わってきます。 これらは例の範囲と、それに合う可能性のあるタスクです。 例えば、データ抽出のようなものでは、あまりランダム性や 創造性は望みません。Claudeに大量のテキストを 与えて、非常に具体的な情報を抽出するように求めた場合、 全く創造性は必要ありません。 Claudeには提供した正確なテキストを見て、 最も関連性の高い情報を抜き出してほしいだけです。 そして、より高い温度の側では、ここからより 創造的になり、あまり一般的でないトークンが 使われるようになります。おそらく ブレインストーミング、執筆、クリエイティブなマーケティング、 またはジョークのような、多くのジョークが 言葉を必ずしも予想通りでない方法で使用することに 依存しているような、創造的なタスクを行うときは 高い温度を使用したいと思うでしょう。 さて、温度について理解したところで、 ノートブックに戻って、温度をリアルタイムで調整する方法を 理解しましょう。チャット関数を更新して、 温度引数を受け取るようにしたいと考えています。 これは`create`関数呼び出しに渡されます。 引数のリストの中に、温度を追加します。 そして、私の温度はデフォルトで1.0に設定します。 つまり、私はもう少し創造的な側に寄りたいと思います。 次に、その引数を受け取り、それを`params`オブジェクトに 温度として追加します。 これで、アプリケーション内で温度調整をサポートするために 必要なすべてが揃いました。 では、これをテストするために、 このセルを再度実行します。次に、 Claudeに1文の映画のアイデアを生成するように依頼します。 そして最初に、温度を0.0に設定します。 理論的には、映画のアイデアは 常に少し似通ったものになるはずです。 では、これを実行します。 最初に出てくるのは、タイムトラベルする考古学者です。 これは非常に一般的なパターンで、少なくとも 私にとってはそうです。温度がゼロの場合、 よくタイムトラベルする何かにまつわる映画のアイデアを得ます。 なので、もう一度実行すると、おそらく別のタイムトラベルするものが 見えるでしょう。はい、同じです。もう一度だけ。 そして、ええ、同じようなアイデア、疲れた タイムトラベルする歴史家です。では、 もう少し独創的で創造的なアイデアを引き出すために、 温度を少し調整してみましょう。 温度を1.0に調整してみます。 これをもう一度実行すると、疲れたタイムトラベラーに関するアイデアは 出てこないことを期待します。 そして、ほぼ即座に見ることができます。そうです。 これは認識しておくべきことです。温度を上げても、 必ずしも劇的に異なるアイデアが得られるとは限りません。 異なるアイデアを得るチャンスが増えるだけです。 なので、これをもう一度実行すると、より創造的なアイデアが見られるかもしれません。 これは確かに、より創造的です。今回はタイムトラベルについては何もありません。 そしてもう一度テストします。 そして、それはありました。また、タイムトラベラーや そのようなものに関するものではありません。 さて、これが温度です。 ここで一般的なガイダンスを思い出してください。 創造性がそれほど必要ないタスクを行うとき、または 決定論的な出力を得たいときは、低い温度値を使用します。 そして、もう少し創造性が必要なタスクの場合は、 温度を少し上げることを検討するときです。 さて、温度について理解したところで、 ノートブックに戻って、温度をリアルタイムで調整する方法を 理解しましょう。チャット関数を更新して、 温度引数を受け取るようにしたいと考えています。 これは`create`関数呼び出しに渡されます。 引数のリストの中に、温度を追加します。 そして、私の温度はデフォルトで1.0に設定します。
