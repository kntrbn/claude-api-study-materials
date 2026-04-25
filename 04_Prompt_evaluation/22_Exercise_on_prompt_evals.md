# 22. Exercise on prompt evals

**URL:** https://anthropic.skilljar.com/claude-with-the-anthropic-api/287738
**Section:** 04 Prompt evaluation

---

## 📄 Page Content

Anthropic Academy
    
  

  
    
      Courses
    
  

    

    
      
      

      
        
          My Profile
        
        
      

      
      

      
        Sign Out
      
    
  

  

  

    
    
    
        
            
    
        
    

            
    
        
        
            
                
                    
                        
                            
                                
                            

                            
                                details
                            

                            
                                
                                    
                                    1
                                    download
                                
                            
                        
                    
                
            
            
                
                
                
                    Exercise on prompt evals
                    
                
                
                    
                        
                            
                                
                                    

    
    

    
    
        
            
        
        
            
                
                This video is still being processed. Please check back later and refresh the page.
            
        
        
            
                Uh oh! Something went wrong, please try again.
            
        
    

    

                                
                            
                        
                    
                
            
        
        
            

    
        
            
                
                    
                        
                            
                        
                    
                
            
            
                
                    Summary
                

                

            
        

        
            
                
                    

                    
                        
                            Downloads
                            
                                
                                    
                                        
                                            
                                            
                                                001_prompt_evals_complete.ipynb
                                                (opens in new tab)

---

## 🎬 Transcript (English)

Let's try out an exercise to improve our prompt evaluation workflow. So here's the task I'm going to give you. I want to improve our model greater a little bit by providing it with more context on what a good solution should actually look like. Now, at first glance, that might sound a little bit challenging, but it turns out you only really have to go through two steps to add in this additional context. So in step one, I would encourage you to go back to the prompt where we generate our data set. And inside that prompt, try asking it for some solution criteria to be included in every test case. So ideally, our test cases that could output should now have some additional solution criteria key, which might look like what you see right here. So it might say something about what a good solution would look like. Maybe you say, well, a good solution would include this characteristic and this characteristic and this characteristic. Once we have this additional solution criteria, we can then insert that into our grade by model prompt. So you might find the existing area of that prompt where we put in our solution to evaluate, and then right after it, you might add in that newly generated solution criteria. And that's all it would really take to give our model greater a little bit better idea of what a good solution would actually look like. As usual, I would encourage you to pause the video right now and give this exercise a shot. Otherwise, we're going to go through a solution right now. So the solution really is just going to be these two separate steps. Should be pretty straightforward. To get started, back inside my notebook, I'm going to find our generate dataset function. And inside there, I'll find the really big prompt we put in. And then when we ask for each of these different test cases, I'm going to say in addition to a task in the output format, I also want to get some solution criteria. And then I'll put in a string right here just to give our model an indication of what this key should actually be. So I'm going to ask for some key criteria for evaluating the solution. And that's pretty much it. So I'm going to rerun the cell. I'm going to go to the cell underneath it and regenerate the data set. Okay, just a couple of seconds, it should be done. There we go. So now we should have an updated data set.json file. I'm gonna open that file up. And I should now see some updated tasks in here, still with the format, but now I've also got some solution criteria. So the solution criteria, we can read over, of course yours is gonna look different than mine, but it's gonna get going to give some idea on, again, what a good solution will actually look like. Next up is step number two. We're going to find our grade by model function and specifically the prompt inside there. And we're going to include this newly generated solution criteria. Again, just to tell the model grader what a good solution looks like. So for that, I will go back to the notebook. I will scroll down and find that grade by model function. Here it is right here. So I'm going to find the prompt. We are already putting in the original task, the output that was generated. And then right after that, I'm going to put in some note to the model and just say, here's some criteria that you should use to evaluate the solution. So criteria you should use to evaluate the solution. I'm going to put in some tags. And I'll tell you why we are adding in these tags very shortly as we start to discuss prompt engineering. And then I'm going to interpolate in from the test case, our solution criteria. And that key right there, remember our test case is really these objects, each of these objects one by one. So we know because we see it right here inside this file, there is a key inside that dictionary of solution criteria. So we're taking that sentence right there and putting it right here. All right, so now time to run the cell. And we're going to rerun our pipeline and see how everything is working. So I'll go down to the run eval function. And then right after that is where we actually execute everything. So I'm going to run that. And then we get our updated score back. Now, I want to print out the results really quickly, just so we can see how this is going to affect the actual output. So we'll do another print of JSON, dumps, results with an indent of two. So now we can see the output from our model, so that's the actual produced output. Here's our test case, so we can take a look at the task in the solution criteria. Here's the score, in this case it was 9, and now hopefully our reasoning section, which is produced by the model grater, is going to be a little bit more fleshed out than it was before because we are including that solution criteria.

---

## 🎬 トランスクリプト（日本語）

プロンプト評価ワークフローを改善するための演習を試してみましょう。ここでは、タスク をご紹介します。モデルを改善したいと考えています。 より多くのコンテキストを提供することで、わずかに 良いソリューションが実際にどのように見えるかについて 改善したいと思います。 さて、一見すると、それは少し難しく聞こえるかもしれませんが、実は この追加のコンテキストを挿入するには、2つのステップを踏むだけで済みます。 ステップ1では、 データセットを生成するプロンプトに戻ることをお勧めします。そして、そのプロンプト内で、 テストケースにいくつかソリューション基準を含めるように尋ねてみてください。 そのため、理想的には、 テストケースの出力には、 追加のソリューション基準キーが含まれているはずです。それは ここに表示されているものに似ているかもしれません。だから、それは 良いソリューションがどのように見えるかについて何か言っているかもしれません。例えば、 良いソリューションには、この特性とこの特性が 含まれるでしょう。そしてこの特性。 この追加のソリューション基準を取得したら、それを プロンプトに入力できます。したがって、 グレード付けモデルのプロンプトに それを挿入できます。プロンプト内の既存の領域を見つけるかもしれません 評価するためのソリューションを配置した場所で、 その直後に、新たに生成された ソリューション基準を追加するかもしれません。それがすべてです。 モデルに、わずかに 良いソリューションがどのように見えるかについて、より良い考えを与えるのに役立ちます。 いつものように、ビデオを一時停止して この演習を試してみることをお勧めします。 さもなければ、今すぐ解決策を検討します。 解決策は、これらの2つの別々のステップにすぎません。 非常に簡単なはずです。始めるために、 私のノートブックに戻って、データセット生成 関数を見つけます。そして、そこで大きなプロンプトを 見つけます。そして、これらの異なるテストケースのそれぞれについて尋ねるとき、 タスクと出力形式に加えて、私も ソリューション基準を取得したいと思います。 そして、ここに文字列を入れて、モデルに このキーが実際には何であるかの兆候を与えるでしょう。だから、 私はソリューションを評価するためのいくつかの 主要な基準を求めます。 それで、それで終わりです。セルを再実行します。 次のセルに移動します。 そして、データセットを再生成します。 OK、 数秒で完了するはずです。完了しました。 これで、更新された dataset.json ファイルができたはずです。 そのファイルを開きます。 そして、ここにも更新されたタスクが表示されるはずです。 フォーマットはそのままですが、 ソリューション基準も追加されました。 ソリューション基準については、もちろん あなたのものは私のものとは異なりますが、 良いソリューションがどのように見えるかについてのアイデアを得るでしょう。 次にステップ2です。 グレード付けモデル関数と、特にその中のプロンプトを見つけます。 そして、この新しく生成されたソリューションを 含めます。 モデルグレーダーに 良いソリューションがどのように見えるかを伝えるためです。 それについては、ノートブックに戻り、 グレード付けモデル関数を見つけます。ここに あります。プロンプトを見つけます。元のタスク、 生成された出力はすでに含まれています。 そしてその直後に、モデルにメモを 入れて、この評価に使用する基準を いくつか提供すると言います。 したがって、評価に使用する 基準。タグをいくつか入れます。 そして、プロンプトエンジニアリングについて話し始めるとき、 これらのタグを追加する理由をすぐに説明します。 そして、テストケースから補間します。 ソリューション基準。 そして、そこにあのキー。 テストケースはこれらのオブジェクトであり、 各オブジェクトが一つずつであることを思い出してください。 このファイル内にあるように、ここに表示されているのでわかります。 辞書のソリューション基準内にキーがあります。 だから、私たちはその文をそこに 入れています。さて、 セルを実行する時間です。 パイプラインを再実行して、すべてが どのように機能しているかを確認します。評価関数に移動します。 そしてそのすぐ後にすべてを実行します。 だからそれを実行します。 そして、更新されたスコアが得られます。 結果をすばやく印刷したいのですが、 それが実際の出力にどのように影響するかを見ることができます。 だから、JSONのダンプをもう一度印刷します。 インデント2で結果を表示します。 これでモデルからの出力が表示されます。 それが実際の生成された出力です。こちらがテスト ケースです。タスクとソリューション基準を確認できます。 こちらがスコアです。この場合は9でした。そして今、うまくいけば、 私たちの推論セクションは、モデルグレーダーによって生成されたものですが、 以前よりも少し充実しているはずです。 なぜなら、ソリューション基準を含めているからです。
