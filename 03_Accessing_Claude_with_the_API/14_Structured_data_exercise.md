# 14. Structured data exercise

**URL:** https://anthropic.skilljar.com/claude-with-the-anthropic-api/287729
**Section:** 03 Accessing Claude with the API

---

## 📄 Page Content

Anthropic Academy
    
  

  
    
      Courses
    
  

    

    
      
      

      
        
          My Profile
        
        
      

      
      

      
        Sign Out
      
    
  

  

  

    
    
    
        
            
    
        
    

            
    
        
        
            
            
                
                
                
                    Structured data exercise
                    
                
                
                    
                        
                            
                                
                                    

    
    

    
    
        
            
        
        
            
                
                This video is still being processed. Please check back later and refresh the page.
            
        
        
            
                Uh oh! Something went wrong, please try again.

---

## 🎬 Transcript (English)

Let's go through a very quick exercise just to make sure the idea of stop sequences and message prefilling are super clear. So in this exercise, I'd like you to write out the exact code I've got right here on the screen. All this code should be really familiar. If you take a look at the prompt, it says generate three different sample AWS CLI commands. Now, when you run this code, you're probably going to get back some output that looks vaguely like this right here. Just make it a little bit easier to read. I rendered it as markdown down here. So here's the sample starting output that I get. You'll notice that it does give us three different sample commands, but has a lot of commentary around them. So I've got a header and then some numbers listing out each individual command. For this exercise, I would like you to take this code and using only message prefilling and stop sequences, I want you to get all three different commands in a single response, all right next to each other without any additional comments or explanation or anything like that. And I'd like you to do this using only message prefilling and stop sequences, so no adjusting this prompt at all. So go ahead and give this a shot. I did put a little hint on here, just as a reminder, with message prefilling, it's not limited just using characters like the backticks. You can put any kind of prefill response you want. I would encourage you to pause this video now and give this an exercise a shot. Otherwise, I'll go over a solution right away. So here we go. Here's how we're going to solve this. To solve this, the first thing I recommend you do is take a look at the output without any kind of pre-filling or stop sequences or anything like that. So if we take a look at what we have right here, we'll notice that each of our three commands are wrapped in a series of three backticks. So a good place to get started would probably be to put in a pre-filled message of three backticks to kind of tell Claude, just go right into the command writing right away and skip any initial commentary. And then we might also decide to put in a stop sequence of three backticks as well. Let's see how far that gets us. So I'll put in an assistant message. And I'll start everything off with three backticks. And I'll put in a stop sequence of closing three backticks. Let's run this and see how far it gets us. My initial output looks kind of reasonable, but it's not perfect just yet. I do get three commands. There's one, two, and three. But you'll notice that I also get the word bash added at the very start. So where's that word coming from exactly? Well, let me show you what Claude is really trying to do here. We provided the initial assistant message of those three backticks. Whenever you put down three back ticks, it's kind of indicating that you are writing out some markdown. And when you are writing a markdown code block with back ticks, you can optionally put in a language identifier right here. If you choose to put one in, that whenever you render this as markdown, the content inside of those back ticks, we rendered using that language's syntax highlighting. So in this case, Claude decided to put in bash right here just to say, hey, we should use bash styles syntax highlighting when we render this stuff out. Now for us, we don't want that at all. So one way we could address this would be to adjust our pre-filled message right here and just include bash ourselves. So that's now going to make it super clear to Claude itself that, yes, you are inside of a Markdown code block. And inside this code block, you should be writing out bash formatted commands. So let me try running this again and see how I do now. Okay, so that looks better. Now I will tell you that from this point, there are probably two additional errors that you might want to address. The first is, sometimes you will get back a single command, which is kind of an indication that Claude might want to write out three separate markdown code blocks. The other problem that you might run into, because we are now using a bash code block, Claude might try to insert some bash formatted comments in there as well. So it might be something like, This command does XYZ, and you might see that repeated. And so we definitely don't want those comments really just because that was one of the requirements of this exercise. So to get rid of those comments and to also make sure that we get all three commands more reliably, we can use that hint I gave you. Remember the hint was message prefilling isn't just limited to designating characters like backticks or stuff like that. We can also use the message prefill to dramatically guide Claude in how it's going to answer us. So in this case, we could add in something like Here are all three commands in a single block without any comments. And then I'll put in a colon right there and then a new line, just so it starts all the markdown stuff on the next line down. So I'm gonna try running this and we should now get some much more reliable output. Okay, that looks good. And of course I can keep running all day and we're probably gonna see exactly the result we want. Okay, this looks good.

---

## 🎬 トランスクリプト（日本語）

ストップシーケンスとメッセージ事前入力のアイデアが 完全に理解されていることを確認するために、非常に簡単な演習を行いましょう。 この演習では、画面に表示されているコードと全く同じコードを 書いていただきたいと思います。このコードはすべて 見覚えがあるはずです。プロンプトを見ると、 3つの異なるサンプルAWS CLI コマンドを生成するように書かれています。さて、 このコードを実行すると、おそらく ここに表示されているものに似た出力が得られるでしょう。 読みやすくするために、下にマークダウンとしてレンダリングしました。 これが、私が取得したサンプル開始出力です。 ご覧のとおり、3つの異なるサンプルコマンドが提供されていますが、 それらの周りには多くのコメントがあります。 したがって、ヘッダーがあり、 次に各コマンドをリストアップした番号があります。この演習では、 このコードを使用して、メッセージ事前入力のみを使用し、 ストップシーケンスを使用して、3つの 異なるコマンドをすべて単一の応答で、すべて 隣り合わせに、追加のコメントや 説明なしで取得してほしいと思います。 そして、メッセージ事前入力とストップシーケンスのみを使用して これを行ってほしいと思います。したがって、このプロンプトは一切変更しません。 さあ、試してみてください。 ヒントを少しだけ付け加えました。メッセージ事前入力は バッククォートのような文字だけを使用するわけではないことを 思い出してください。どのような事前入力応答でも構いません。 このビデオを一時停止して、この演習を試してみることをお勧めします。 そうでない場合は、すぐに解決策を説明します。 では、始めましょう。 これを解決するには、まず 事前入力やストップシーケンスなどを何もなしで 出力を見てみることをお勧めします。 だから、ここに何があるか見てみると、 3つのコマンドすべてが 一連の3つのバッククォートで囲まれていることがわかります。 ですから、良い出発点は 3つのバッククォートの事前入力メッセージを挿入することでしょう。 Claudeに、すぐにコマンド作成に入り、 初期コメントをスキップするように指示するために。 そして、ストップシーケンスも 3つのバッククォートにするかもしれません。どこまで行くか見てみましょう。 では、アシスタントメッセージを挿入します。 そして、すべての開始を3つのバッククォートで始めます。 そして、ストップシーケンスを 閉じられた3つのバッククォートにします。実行して どこまで行くか見てみましょう。私の最初の 出力はまともなようですが、まだ完璧ではありません。 3つのコマンドを取得しました。1つ、2つ、3つです。 しかし、先頭に「bash」という単語も付いていることがわかります。 さて、その単語は正確にどこから来たのでしょう？ Claudeがここで何をしているのか見てみましょう。 3つのバッククォートのアシスタントメッセージを初期に提供しました。 3つのバッククォートを配置すると、 マークダウンを記述していることを示しています。 そして、バッククォートでマークダウンコードブロックを書いている場合、 オプションで言語識別子をここに配置できます。 1つを選択すると、それをマークダウンとしてレンダリングするとき、 バッククォート内のコンテンツは、 その言語の構文ハイライトを使用してレンダリングされます。 したがって、この場合、Claudeはここでbashを挿入することを選択しました。 これは、これらのものをレンダリングするときにbashスタイルを 使用すべきであることを示すためです。 私たちにとっては、それはまったく望ましくないことです。 これを解決する方法の1つは、 この事前入力メッセージをここに調整し、 bash自体を挿入することです。これで Claude自身に明確になります。はい、あなたは マークダウンコードブロックの中にいます。そして このコードブロックの中に、bash形式のコマンドを書くべきです。 もう一度実行して、どうなるか見てみましょう。はい、 これで良くなりました。さて、この 時点から、対処したいであろう2つの追加のエラーがあります。 1つ目は、単一のコマンドが返されることがあるということです。 これは、Claudeが3つの 別々のマークダウンコードブロックを書きたいと考えている兆候です。 もう1つの問題は、bashコードブロックを使用しているため、 Claudeがbash形式のコメントを 挿入しようとすることです。 例えば、「この コマンドはXYZを実行します」といったもので、 それが繰り返されている可能性があります。ですから、私たちは絶対に これらのコメントを望んでいません。なぜなら、それがこの演習の要件の1つだったからです。 ですから、それを取り除くために そして、3つのコマンドをより確実に取得するために、 私が与えたヒントを使用できます。 ヒントは、メッセージ事前入力がバッククォートなどの文字を指定するだけではないことを 覚えてください。 また、メッセージ事前入力を使用して、Claudeが どのように回答するかを劇的にガイドすることもできます。 ですから、この場合、次のようなものを追加できます。 ここに3つのコマンドすべてを 単一のブロックで、コメントなしで追加します。 そしてコロンを置き、改行します。 そうすれば、マークダウンのすべてのものが次の行から始まります。 したがって、これを実行してみます。これで より信頼性の高い出力が得られるはずです。はい、 それは良いですね。そして、もちろん、私は一日中すべてを実行できます。 そしておそらく、私たちが望む結果を正確に見ることができます。 はい、これは良いですね。
