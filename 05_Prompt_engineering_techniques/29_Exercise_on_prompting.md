# 29. Exercise on prompting

**URL:** https://anthropic.skilljar.com/claude-with-the-anthropic-api/287748
**Section:** 05 Prompt engineering techniques

---

## 📄 Page Content

Anthropic Academy
    
  

  
    
      Courses
    
  

    

    
      
      

      
        
          My Profile
        
        
      

      
      

      
        Sign Out
      
    
  

  

  

    
    
    
        
            
    
        
    

            
    
        
        
            
            
                
                
                
                    Exercise on prompting
                    
                
                
                    
                        
                            
                                
                                    

    
    

    
    
        
            
        
        
            
                
                This video is still being processed. Please check back later and refresh the page.
            
        
        
            
                Uh oh! Something went wrong, please try again.

---

## 🎬 Transcript (English)

Let's test your knowledge of prompt engineering by going through a quick exercise. Now for this exercise, I made a new notebook called 003 underscore exercise. You do not have to download this one. All I did was replace the task description, the prompt input spec, and then adjusted some of the extra criteria down here. So if you want to, you could manually change all the stuff in the notebook you're working out of, or alternatively just download this 003 exercise and get caught up with exactly where I am. Your goal in this exercise is to improve an existing prompt using all the prompt engineering topics we've learned about inside this module. The dataset you're going to be working with is going to create a series of passages of text from a scholarly article. The goal of your prompt is to take in that passage of text and extract all the topics from it into a JSON array of strings. And when I say topic, I really just mean, well, what does this article talk about? So if it's an article about, say, solar panels, I would want to get back a JSON array of strings that contains solar panels inside of it, only with any other topics mentioned inside that text. The only input to the prompt is going to be a content property. So that's going to be one paragraph of text. Now, in my notebook that I've opened right now, I have already executed the cell and generated a dataset. I have already put together a starter prompt for you, and right now it's a very poor prompt that can definitely be improved quite a bit. So go ahead and play around with this prompt and use some of the different techniques we have learned about. In order to evaluate your progress, go ahead and run the cell down here. I've already included a couple of extra criteria to make sure that you're kind of achieving the correct result. Remember, whenever you run the evaluation, you can always open up that report.html file and get a better understanding of what's going on. By default, with that really simple prompt, I've got an average score of 2.8. And so I'm hoping we can at least get that average score over maybe seven or so. As usual, I would encourage you to pause the video right here and go ahead and give this exercise a shot. Otherwise, if you want to stick around, I'm gonna go over a solution right away. All right, so to solve this, we know without a doubt all the work we're going to be doing is focused on this variable right here. We need to improve this prompt in some way to get back some better outputs. The first thing we might do here is make sure you run the evaluation at least one time to generate that output.html file. And then once you have created that file, I would encourage you to open it up and take a look at some of the reasoning on why the output has been graded so poorly. You'll notice a common theme between each of these. A real common theme right away that we can see is that, well, it doesn't like the fact that we are not returning a JSON array of strings. To solve this problem, let's make use of that technique of being simple and direct inside of our prompt. If we expect to get back a JSON array of strings that contains all the topics out of this content, well, we need to be very simple and direct with Claude and tell it exactly what we want. So I'm going to update the first line of the prompt right here and I'll say extract key topics mentioned from a passage of text from a scholarly journal into a JSON array of strings as simple as I can phrase it and as direct as I can possibly make it. And right away, if I rerun the prompt with the evaluation, I will see that I get up to a kind of shocking 9.5 almost immediately. So I kind of didn't really expect it to go that well because there are still some other techniques we might want to try out here. But if we take a look at the report now, I'm definitely getting back this JSON containing all the different topics mentioned. And it looks like the model grader is extremely happy with this output. Now, I don't really want to leave it here. Obviously, there are some other techniques we can add in to make sure that we get the correct kind of output. So the next technique we might add in is structuring our prompt a little bit better by using some XML tags. Before and after the content that we're going to interpolate in right here, I'm going to add in some XML tags and I'm going to give them the name of simply text. Now in this case, I'm choosing to call these tags text because I earlier referred to some text inside of the first line of the prompt. So now we have just a little bit more clear connection between us talking about a passage of text right here and us providing the text right here. Another improvement that we might add in is to be very specific in what we want Claude to do. So I could put in a series of steps for Claude to follow. Let's try that out. I might say follow these steps and then list out exactly what I want Claude to do step by step. So we might say closely examine the provided text. Identify each topic mentioned, add each topic to a JSON array, and then finally respond with the JSON array. Do not provide any other text or commentary. Now, if you wanted to also add in an example using one shot or multi-shot prompting, absolutely feel free to do so. But we already have some pretty good scores, so I think this is probably enough. I'm going to read on this prompt. I'll then run the evaluation again and I end up getting a 9.5 again. So I would say that this is a pretty strong prompt and I would definitely trust it to extract a list of topics from an article.

---

## 🎬 トランスクリプト（日本語）

プロンプトエンジニアリングの知識を、 簡単な演習を通してテストしてみましょう。この演習のために、 003アンダースコアという新しいノートブックを作成しました。 これをダウンロードする必要はありません。 私がやったことは、タスクの説明、 プロンプト入力仕様を置き換えて、 そしてここにある追加の基準をいくつか調整しただけです。もしよろしければ、 作業しているノートブック内のすべての項目を 手動で変更することもできますし、あるいはこの003 エクササイズをダウンロードして、私がいる場所に追いつくこともできます。 この演習でのあなたの目標は、既存の プロンプトを、このモジュールで学んだすべてのプロンプトエンジニアリングのトピックを使用して改善することです。 あなたが取り組むデータセットは、学術記事からの 一連のテキストの抜粋を作成するものです。 あなたのプロンプトの目標は、 そのテキストの抜粋を入力として受け取り、 そこからすべてのトピックを抽出して、 文字列のJSON配列にすることです。 そしてトピックと言うとき、私は本当に単に この論文は何について書かれているのか、ということです。 たとえば、太陽光パネルに関する論文であれば、 太陽光パネルが含まれる文字列のJSON配列を返すことを期待しています。 そして、そのテキスト内で言及されている他のすべてのトピックを含めます。 プロンプトへの唯一の入力は、コンテンツプロパティになります。 つまり、テキストの1つの段落になります。 さて、今開いている私のノートブックでは、 すでにセルを実行してデータセットを生成しました。 すでに開始プロンプトを用意しましたが、 現時点では非常に貧弱なプロンプトで、 大幅に改善の余地があります。 ですから、自由にこのプロンプトをいじって、 学んだ様々なテクニックを使用してください。 進捗を評価するために、ここにあるセルを実行してください。 正しい結果を達成していることを確認するために、 いくつか追加の基準を含めました。 評価を実行するときはいつでも、 report.htmlファイルを開いて、 何が起こっているのかをより深く理解することができます。 デフォルトでは、その非常に単純なプロンプトで、平均スコアは2.8でした。 なので、最低でも平均スコアを7程度まで 上げられることを期待しています。 いつものように、このビデオを一時停止して、 この演習を試してみることをお勧めします。 そうでなければ、もしお付き合いいただけるなら、すぐに解決策を説明します。 さて、これを解決するために、 我々が行うすべての作業が、この変数に焦点を当てていることは 間違いありません。 このプロンプトを何らかの方法で改善して、より良い出力を得る必要があります。 まず最初に、評価を少なくとも1回実行して output.htmlファイルを生成したことを確認しましょう。 そして、そのファイルを作成したら、 それを開いて、出力がなぜこれほど低く評価されたのか、 その理由をいくつか確認することをお勧めします。 これらのそれぞれの間には、一般的なテーマがあることに気づくでしょう。 すぐに気づく一般的なテーマは、JSON配列の文字列を返していないという事実です。 この問題を解決するために、 プロンプト内でシンプルかつ直接的であるというテクニックを活用しましょう。 コンテンツからすべてのトピックを含む文字列のJSON配列を返すことを期待しているなら、 Claudeに非常にシンプルかつ直接的に、 何を求めているかを正確に伝える必要があります。 そこで、プロンプトの最初の行を更新して、 学術雑誌の抜粋から重要なトピックを抽出し、 それを文字列のJSON配列にしてください。 できる限りシンプルに、そして可能な限り直接的に述べます。 プロンプトを評価と共に再度実行すると、 なんと驚くべきことに、ほとんどすぐに9.5というスコアが得られます。 なぜなら、試すことができる他のテクニックもまだいくつかあるからです。 しかし、レポートを見ると、 すべての言及されているトピックを含むJSONが返されていることがわかります。 そして、モデルグレーダーはこの出力に非常に満足しているようです。 さて、私はここで止めたいわけではありません。明らかに、 正しい種類の出力を得るために追加できる他のテクニックがいくつかあります。 次のテクニックは、XMLタグを使用して プロンプトを少し整理することです。 補間するコンテンツの前後に テキストという名前のXMLタグを追加します。 この場合、これらのタグをテキストと呼ぶことにしたのは、 以前にプロンプトの最初の行でテキストについて言及したからです。 これにより、ここでテキストの抜粋について話していることと、 ここでテキストを提供していることとの間により明確なつながりができました。 また、追加できる改善点は、 Claudeに何をしてもらいたいかについて、 非常に具体的にすることです。例えば、Claudeが従うべきステップを いくつか含めることができます。 それを試してみましょう。 次のステップに従ってください、と述べて、 Claudeに何をしてもらいたいかを ステップごとにリストアップします。 提供されたテキストを注意深く調べ、 言及されている各トピックを特定し、 各トピックをJSON配列に追加し、 最後にJSON配列を応答として提供します。 他のテキストやコメントは提供しないでください。 もし、ワンショットまたはマルチショットのプロンプティングの例を追加したい場合は、 遠慮なく行ってください。 しかし、すでにかなり良いスコアが出ているので、 これで十分でしょう。 このプロンプトを読み込んでから、評価を再度実行します。 そして、再び9.5というスコアが得られました。 これはかなり強力なプロンプトと言え、 記事からトピックのリストを抽出するために 間違いなく信頼できるでしょう。
