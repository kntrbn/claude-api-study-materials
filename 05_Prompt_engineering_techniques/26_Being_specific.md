# 26. Being specific

**URL:** https://anthropic.skilljar.com/claude-with-the-anthropic-api/287740
**Section:** 05 Prompt engineering techniques

---

## 📄 Page Content

Anthropic Academy
    
  

  
    
      Courses
    
  

    

    
      
      

      
        
          My Profile
        
        
      

      
      

      
        Sign Out
      
    
  

  

  

    
    
    
        
            
    
        
    

            
    
        
        
            
                
                    
                        
                            
                                
                            

                            
                                details
                            

                            
                        
                    
                
            
            
                
                
                
                    Being specific
                    
                
                
                    
                        
                            
                                
                                    

    
    

    
    
        
            
        
        
            
                
                This video is still being processed. Please check back later and refresh the page.
            
        
        
            
                Uh oh! Something went wrong, please try again.
            
        
    

    

                                
                            
                        
                    
                
            
        
        
            

    
        
            
                
                    
                        
                            
                        
                    
                
            
            
                
                    Summary
                

                

            
        

        
            
                
                    
                        
                            Summary

                            
                                When working with Claude, one of the most effective ways to improve your results is to be specific about what you want. Instead of leaving everything up to the model's interpretation, you can provide clear guidelines or steps that direct Claude toward the kind of output you're looking for.

Think about it this way: if you ask Claude to "write a short story about a character who discovers a hidden talent," Claude could go in countless directions. The story might be 200 words or 2,000 words. It might have one character or five. It could focus on any type of talent discovery scenario.

By adding specific guidelines, you give Claude a clearer target to aim for. This dramatically improves both the consistency and quality of the output.

Two Types of Guidelines

There are two main approaches to being specific in your prompts, and you'll often see them used together in professional applications.

Output Quality Guidelines

The first type focuses on listing qualities that your output should have. These guidelines help you control:

Length of the response
Structure and format
Specific attributes or elements to include
Tone or style requirements

For example, you might specify that a story should be under 1,000 words, include a clear action that reveals the character's talent, and feature at least one supporting character.

Process Steps

The second type provides specific steps for Claude to follow. This approach is particularly useful when you want Claude to think through a problem systematically or consider multiple perspectives before arriving at a final answer.

Instead of jumping straight to writing, you might ask Claude to:

Brainstorm three talents that would create dramatic tension
Pick the most interesting talent
Outline a pivotal scene that reveals the talent
Brainstorm supporting character types that could increase the impact

Real-World Impact

The difference that specificity makes is dramatic. In testing a meal planning prompt, adding guidelines improved the evaluation score from 3.92 to 7.86 - more than doubling the quality of the output simply by telling Claude exactly what elements to include.

Guidelines:
1. Include accurate daily calorie amount
2. Show protein, fat, and carb amounts  
3. Specify when to eat each meal
4. Use only foods that fit restrictions
5. List all portion sizes in grams
6. Keep budget-friendly if mentioned

When to Use Each Approach

Here's a practical guide for when to use each type of specificity:

Always Use Output Guidelines

You should include quality guidelines in almost every prompt you write. They're your safety net for getting consistent, useful results.

Use Process Steps For Complex Problems

Add step-by-step instructions when you're dealing with:

Troubleshooting complex problems
Decision-making scenarios
Critical thinking tasks
Any situation where you want Claude to consider multiple angles

For instance, if you're asking Claude to analyze why a sales team's performance dropped, you'd want to guide it through examining market metrics, industry changes, individual performance, organizational changes, and customer feedback - rather than letting it focus on just one potential cause.

Combining Both Approaches

In professional prompting, you'll often see both techniques used together. You might have guidelines that control the format and content of your output, plus steps that ensure Claude thinks through the problem thoroughly before responding.

This combination gives you both consistency in your results and confidence that Claude has considered all the important factors in reaching its conclusion.

---

## 🎬 Transcript (English)

The next topic we're going to discuss in the world of prompt engineering is the idea of being specific. To be specific, we want our prompts to list out some sort of guidelines or steps to somehow direct our model in a particular direction. For example, consider the prompt to have on the left-hand side of the screen. In this prompt, I'm asking Claude to write out a short story about a character who discovers a hidden talent. If I just put that prompt by itself into Claude, Claude can go any of an infinite number of directions. It can decide to vary the story length significantly. It can decide to add in extra elements or remove elements from the story. It might have just one character, it might introduce five different characters. If I want to ensure that I'm going to get a particular kind of output, I might decide to put in a list of guidelines, as you see on the right-hand side. These guidelines will provide some high-level guidance or kind of direct Claude in a specific way when it starts generating the response. So for example, I might decide to add in some guidelines of keeping the story under a thousand words, add in some rising actions, and including at least one supporting character. Now I've provided a little bit of guidance to direct Claude towards writing a particular kind of short story. Now there are two kinds of guidelines you're going to see very often in prompts. Type A on the left hand side is kind of like what I just showed you in the previous diagram. You might decide to put in a list of guidelines and those are going to list out some qualities that you want your output to have. So you might try to control maybe the length of the output or the structure of the output or maybe list out some different attributes that the output should have. On the right hand side, the second type of guidelines that we can provide are to provide some actual steps that the model should follow, with the intent of making the model think about specific things or choose between different directions that would hopefully increase the quality of our output. So for example, we might instruct Claude to maybe first brainstorm three special talents that would be really interesting and then pick the most interesting one. We might then ask Claude to try to outline or think about some kind of interesting scene that would reveal that talent, and then think about different kinds of supporting characters that could make the story a little bit more interesting. So on the left hand side, we're really guiding attributes in the output. On the right hand side, we're trying to be a little bit more specific in how Claude arrives at the final product. You can absolutely, and you're gonna see this very often in professional prompts, you'll absolutely, very often see these two techniques mixed together. So you might have a list of guidelines that intend to control some attributes of the output, and then a list of steps that the model should follow as well. Both of these are examples of being specific in your prompting. So now we've seen some idea around what it means to be specific. Let's go back over to our prompt in progress and see if we can incorporate this idea of being specific. All right, so back over here, I'm taking a look at my run prompt function. Now, just to save a little bit of time, I'm going to first paste in a list of guidelines. So this is kind of like that first type of being specific, where I include a list of attributes that I really want to see inside of the output. I'm going to run that cell and then go down and run the eval again. And let's see what we get here. So after a quick pause, I'm going to get back a final score of 7.86. That is an incredible improvement over our previous 3.92, just by adding in a little bit of guidance and telling Claude precisely what things we want to see inside of the output. Now I'm going to try to put in a little variant of this where I use that second variation of being specific. So I'm going to provide some steps that Claude should follow when deciding exactly how to build up this meal plan. So now in this scenario, I'm telling Claude to first do a calculation and then think about this and then do a little bit of planning. You kind of get the idea. I'm providing some steps that Claude should go through. I'm going to run this cell again. And then run down here, and I'm going to remember that score of 7.86, that is really, really high, might be a little bit of a statistical anomaly. And now we get 7.3. So still a dramatic improvement, but not quite as good as listing out some attributes that we would want to see inside the output. So for me, I'm going to revert and go back to listing out some guidelines. So when would you want to use one technique versus the other? Well, I would generally recommend almost always listing out qualities that the output should have as I'm showing on the left hand side on just about any prompt you ever work on. And you will usually want to provide steps that the model should follow, as shown on the right-hand side, any time you're asking Claude to work on a more complex problem, where you want to kind of force Claude to consider a wider view or some extra topics beyond what it naturally might want to consider. For example, consider the prompt on the right-hand side of the screen, where I ask Claude to figure out why a sales team's numbers have dropped in the last quarter. In this scenario, we might want to force Claude to consider some extra viewpoints or extra pieces of data that it might not otherwise immediately consider. All right, so now that we've got a better idea of what it really means to be specific and this idea of adding guidelines or steps as the situation warrants, let's take another break right here and then move on to our next prompt engineering topic in just a moment.

---

## 🎬 トランスクリプト（日本語）

次にプロンプトエンジニアリングの世界で議論するトピックは、 具体性を重視することです。具体的に言うと、 プロンプトでは何らかのガイドライン やステップをリストアップして、モデルを特定の方向へ 誘導したいのです。例えば、画面の左側に あるプロンプトを考えてみてください。このプロンプトでは、 クロードに隠された才能を発見するキャラクターについての 短い物語を書くように依頼しています。もしこの プロンプトだけをクロードに入力した場合、クロードは 無限に多くの方向へ行くことができます。 物語の長さを大幅に変えることもできます。 追加要素を入れたり、要素を削除したりすることもできます。 登場人物は一人かもしれませんし、5人の異なる登場人物を 登場させるかもしれません。もし特定の種類の出力を 確実に得たいのであれば、 ガイドラインのリストを入れることを検討するかもしれません。右側に あるように。これらのガイドラインは、 ある程度の高レベルなガイダンスを提供し、クロードを特定の 方法で誘導するでしょう。例えば、物語を1000語未満にする、 上昇するアクションを入れる、 少なくとも一人の補助的なキャラクターを含める、といった ガイドラインを追加することを検討するかもしれません。これで、特定の 種類の短編小説を書くようにクロードを誘導するための ガイダンスを少し提供しました。 プロンプトでよく見かけるガイドラインは2種類あります。 左側のタイプAは、先ほどの図で示したようなものです。 ガイドラインのリストを入れ、それが出力に含んでほしい いくつかの品質をリストアップします。例えば、 出力の長さや構造を制御しようとしたり、 出力が持つべきいくつかの異なる属性をリストアップしたりするかもしれません。 右側、 2番目の種類のガイドラインは、 モデルが従うべき実際の手順を提供することです。 モデルに特定の事柄について考えさせたり、 異なる方向の中から選択させたりすることで、出力の質を高めることを 期待しています。例えば、クロードにまず 非常に興味深い特別な才能を3つブレインストーミングさせ、 それから最も興味深いものを選ぶように指示するかもしれません。 次に、その才能を明らかにする興味深いシーンの 概要を考えさせたり、物語をより面白くするための 様々な補助的なキャラクターについて考えさせたりするかもしれません。 ですから、左側では出力の属性を誘導しています。 右側では、クロードが最終製品に どのようにたどり着くかについて、もう少し具体的に しようとしています。あなたは間違いなく、 プロフェッショナルなプロンプトでは、 これらの2つのテクニックを組み合わせて使用することになるでしょう。 つまり、出力の属性を制御することを目的としたガイドラインのリストと、 モデルが従うべきステップのリストを持つことができます。 これら両方とも、プロンプトで具体的にすることの 例です。 具体的にすることの意味について、ある程度のアイデアを得ました。 プロンプトの作成に戻って、具体性を具体化できるか 見てみましょう。 はい、こちらに戻って、実行中のプロンプト関数を見ています。 少し時間を節約するために、まずガイドラインのリストを 貼り付けます。これは、私が出力内に含めたい 属性のリストを具体的にすることの、最初の種類に似ています。 そのセルを実行して、 そして評価を再度実行します。 ここで何が得られるか見てみましょう。 少し待った後、最終スコアは7.86になります。 これは、単に少しのガイダンスを追加し、 出力内に含めたいものを正確に伝えるだけで、 以前の3.92から信じられないほどの改善です。 今度は、これの少しバリエーションを試して、 具体性を重視する第2のバリエーションを使用します。 具体的にどのようにこの食事プランを構築するかを決定する際に、 クロードに従うべき手順を提供します。 このシナリオでは、まず計算を行い、 そしてこれを考え、そして少し計画を実行するように クロードに指示しています。あなたはアイデアを理解しました。 クロードが通過すべきステップを提供しています。 このセルを再度実行します。 そして、下に実行します。そして、スコア7.86を覚えておきます。 これは非常に、非常に高く、統計的な異常かもしれません。 そして、7.3が得られました。 まだ劇的な改善ですが、 出力に含んでほしい属性をリストアップするほどではありません。 なので、私はガイドラインをリストアップすることに戻ります。 では、どちらかのテクニックをいつ使用すべきでしょうか？ まず、左側にあるように、ほぼ常に 出力に含んでほしい品質をリストアップすることを 推奨します。これはあなたが取り組むほぼ全てのプロンプトで 行います。そして、右側にあるように、モデルに 従うべき手順を提供することを、 より複雑な問題に取り組む際には、 より広い視野や、通常は考慮しないであろう追加的なトピックを 強制したい場合に、常に含めたいでしょう。 例えば、画面の右側にあるプロンプトを 考えてみてください。営業チームの数字が 先四半期に減少した理由を、クロードに 調べさせます。このシナリオでは、 クロードに、そうでなければ 直ちに考慮しないであろう、 追加的な視点や追加的なデータを 考慮するように強制したいかもしれません。 さて、具体的にすることと、 必要に応じてガイドラインや手順を追加するという考え方について、 より良いアイデアを得たので、 ここでまた休憩を取り、プロンプトエンジニアリングの 次のトピックに移りましょう。 すぐに。 わかりました。 具体的にすることと、 必要に応じてガイドラインや手順を追加するという考え方について、 より良いアイデアを得たので、 ここでまた休憩を取り、プロンプトエンジニアリングの次のトピックに移りましょう。
