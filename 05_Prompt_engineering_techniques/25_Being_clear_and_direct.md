# 25. Being clear and direct

**URL:** https://anthropic.skilljar.com/claude-with-the-anthropic-api/287744
**Section:** 05 Prompt engineering techniques

---

## 📄 Page Content

Anthropic Academy
    
  

  
    
      Courses
    
  

    

    
      
      

      
        
          My Profile
        
        
      

      
      

      
        Sign Out
      
    
  

  

  

    
    
    
        
            
    
        
    

            
    
        
        
            
                
                    
                        
                            
                                
                            

                            
                                details
                            

                            
                        
                    
                
            
            
                
                
                
                    Being clear and direct
                    
                
                
                    
                        
                            
                                
                                    

    
    

    
    
        
            
        
        
            
                
                This video is still being processed. Please check back later and refresh the page.
            
        
        
            
                Uh oh! Something went wrong, please try again.
            
        
    

    

                                
                            
                        
                    
                
            
        
        
            

    
        
            
                
                    
                        
                            
                        
                    
                
            
            
                
                    Summary
                

                

            
        

        
            
                
                    
                        
                            Summary

                            
                                The first line of your prompt is the most important part of your entire request. This is where you set the stage for everything that follows, and getting it right can dramatically improve your results.

Being Clear and Direct

When crafting that crucial first line, you want to focus on two key principles: clarity and directness. This means using simple language that leaves no room for ambiguity about what you want Claude to do.

Clear Communication

Being "clear" means:

Use simple language that anyone can understand
State exactly what you want without beating around the bush
Lead with a straightforward statement of Claude's task

Instead of writing something vague like "I need to know about those things people put on their roofs that use sun - those solar panel things, I think they're called," be direct and write: "Write three paragraphs about how solar panels work."

Direct Instructions

Being "direct" focuses on how you structure your request:

Use instructions, not questions
Start with direct action verbs like "Write," "Create," or "Generate"

Rather than asking "I was reading about renewable energy and geothermal energy sounds neat. What countries use it?" try: "Identify three countries that use geothermal energy. Include generation stats for each."

Putting It Into Practice

Let's see this technique in action. Starting with a weak prompt that simply asked "What should this person eat?" we can apply our clear and direct approach.

The improved version becomes: Generate a one-day meal plan for an athlete that meets their dietary restrictions.

This revision immediately tells Claude:

What action to take (generate)
What to create (a meal plan)
Key constraints (one day, for an athlete, meeting dietary restrictions)

Results Matter

This simple change can have a significant impact on performance. In our example, the evaluation score jumped from 2.32 to 3.92 - a substantial improvement from just restructuring that opening line.

The key takeaway is that Claude responds best when you treat it like a capable assistant who needs clear direction rather than someone who has to guess what you want. Start strong with a direct action verb, be specific about the task, and you'll see better results right away.

---

## 🎬 Transcript (English)

With a starting grade of 2.32, we can definitely only go up. So with that in mind, let's take a look at our first prompt engineering technique that we're going to use to improve our prompt. Alright, so we're going to be discussing the idea of being clear and direct. These two rules are really talking about the very first line of your prompt. The first line of your prompt tends to be the most important. In that first line, you want to use simple and direct language, until Claude, with a kind of action verb, exactly what its task is. So for example, we might want to have a first line of a prompt be something like write three paragraphs about how solar panels work. that tells Claude that it's going to have a job and use to write or generate or create something. It also clarifies a little bit of information about the expected output and exactly what that output should contain. So we're really setting an action and providing a task in that very first line. Another great example would be identify three countries that use geothermal energy and for each include generation stats. Again, we are telling Claude to do something or give it an immediate task and a little bit of information about the expected output. Let's take this idea of being clear and direct in the very first line of our prompt and see if we can't use it to improve the outcomes of our prompt that we're currently working on. Using that rule that we just learned, I might update this line to say something like, generate a one day meal plan, for an athlete that meets their dietary restrictions. So again, I'm being direct by making use of an action verb at the very start, and then in very simple language, I'm providing a direct task for Claude to fulfill. Now let's rerun the cell to get our updated prompt and then rerun the Eval itself. And see if this does anything to improve our score. And I bet as you can guess, yeah, we're probably going to do a little bit better than we did previously. So I think before I had a 2.32, now I'm up to a 3.92. Definitely an improvement, but still not great. So let's move on to the next video and take a look at our next prompt engineering topic in order to improve our prompt a little bit more.

---

## 🎬 トランスクリプト（日本語）

開始のスコアが2.32なので、 明らかに上がるしかありません。その点を念頭に置いて、 プロンプトを改善するために使う最初のプロンプトエンジニアリングテクニックを 見ていきましょう。さて、 次に議論するのは、明確かつ直接的であるという考え方です。 この2つのルールは、プロンプトの最初の行について 話しています。プロンプトの最初の行は、 最も重要である傾向があります。その最初の行では、 シンプルで直接的な言葉遣いを使い、 Claudeに、アクション動詞を用いて、そのタスクが 何であるかを正確に伝えます。例えば、 プロンプトの最初の行は、「太陽光パネルの仕組みについて3つの段落で書く」のようなものに したいかもしれません。 それはClaudeに、書く、 生成する、あるいは作成するという仕事があることを伝えます。また、期待される出力に関する 情報と、その出力に何が含まれるべきかを 少し明確にします。ですから、 私たちは最初の行でアクションを設定し、 タスクを提供しているのです。もう一つの素晴らしい例は、 地熱エネルギーを使用している3つの国を特定し、 それぞれについて発電量を含めることです。 ここでも、Claudeに何かをしてもらうよう指示したり、 即時のタスクと期待される出力に関する情報を 少し提供したりしています。プロンプトの最初の行で 明確かつ直接的であるという考え方を取り入れて、 現在取り組んでいるプロンプトの結果を改善できるかどうか見てみましょう。 学んだばかりのルールを使って、この行を 「アスリート向けの1日の食事プランを作成し、 食事制限を満たす」のように更新するかもしれません。 ですので、ここでも直接的な アクション動詞を最初に使用することで直接的になり、 そして非常にシンプルな言葉で、 Claudeに実行させる直接的なタスクを提供しています。 それでは、セルを再実行して更新されたプロンプトを取得し、 そして評価自体も再実行して、 スコアが改善されるかどうか見てみましょう。 おそらく皆さんも推測できると思いますが、以前よりも 少し良くなるでしょう。以前は2.32でしたが、 今は3.92まで上がりました。 間違いなく改善ですが、 まだ十分ではありません。ですから、 次のビデオに進み、プロンプトをさらに改善するために 次のプロンプトエンジニアリングのトピックを見ていきましょう。
