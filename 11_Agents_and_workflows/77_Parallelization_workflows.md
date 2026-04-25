# 77. Parallelization workflows

**URL:** https://anthropic.skilljar.com/claude-with-the-anthropic-api/287804
**Section:** 11 Agents and workflows

---

## 📄 Page Content

Anthropic Academy
    
  

  
    
      Courses
    
  

    

    
      
      

      
        
          My Profile
        
        
      

      
      

      
        Sign Out
      
    
  

  

  

    
    
    
        
            
    
        
    

            
    
        
        
            
                
                    
                        
                            
                                
                            

                            
                                details
                            

                            
                        
                    
                
            
            
                
                
                
                    Parallelization workflows
                    
                
                
                    
                        
                            
                                
                                    

    
    

    
    
        
            
        
        
            
                
                This video is still being processed. Please check back later and refresh the page.
            
        
        
            
                Uh oh! Something went wrong, please try again.
            
        
    

    

                                
                            
                        
                    
                
            
        
        
            

    
        
            
                
                    
                        
                            
                        
                    
                
            
            
                
                    Summary
                

                

            
        

        
            
                
                    
                        
                            Summary

                            
                                When building AI applications, you'll often encounter tasks that seem simple on the surface but become complex when you try to implement them effectively. Let's explore a powerful pattern called parallelization workflows that can help you break down complex tasks into manageable, focused pieces.

The Problem with Complex Single Prompts

Imagine you're building a material designer application where users upload images of parts and receive recommendations for the best material to use. Your first instinct might be to send the image to Claude with a simple prompt asking it to choose between metal, polymer, ceramic, composite, elastomer, or wood.

While this approach might work, you're asking Claude to do a lot of heavy lifting in a single request. Without specific criteria for each material type, the results won't be as reliable as they could be.

You might think to improve this by adding detailed criteria for each material into one massive prompt. But this creates a new problem - Claude has to juggle all these different considerations simultaneously, which can lead to confusion and suboptimal results.

A Better Approach: Parallelization

Instead of cramming everything into one request, you can split the task into multiple parallel requests. Each request focuses on evaluating the part for a single material type with specialized criteria.

Here's how it works:

Send the same image to Claude multiple times simultaneously
Each request includes specialized criteria for one material (metal criteria, polymer criteria, ceramic criteria, etc.)
Claude evaluates the part's suitability for each material independently
Collect all the analysis results and feed them into a final aggregation step

The final step sends all the individual analysis results back to Claude with a request to compare them and make a final material recommendation.

How Parallelization Workflows Work

The parallelization pattern follows a simple structure:

Split a single task into multiple sub-tasks - Break down the complex decision into focused, specialized evaluations
Run the sub-tasks in parallel - Execute all evaluations simultaneously for faster processing
Aggregate the results together - Combine the specialized analyses into a final decision
The parallelized sub-tasks don't need to be identical - Each can have a specialized prompt, set of tools, or evaluation criteria

Benefits of This Approach

Parallelization workflows offer several key advantages:

Focused attention: Claude can concentrate on one specific aspect at a time rather than trying to balance multiple competing considerations simultaneously. This leads to more thorough and accurate analysis for each material type.

Easier optimization: You can improve and test the prompts for each material evaluation independently. If your metal analysis isn't working well, you can refine just that prompt without affecting the others.

Better scalability: Adding new materials to evaluate is straightforward - just add another parallel request. You don't need to rewrite existing prompts or worry about how the new criteria might interfere with existing ones.

Improved reliability: By breaking down the complex task, you reduce the cognitive load on the AI model and get more consistent, reliable results.

When to Use Parallelization

This pattern works well when you have a complex decision that can be broken down into independent evaluations. Look for situations where you're asking an AI to consider multiple criteria, compare several options, or make decisions that involve different domains of expertise.

The key is identifying tasks that can be meaningfully separated - each parallel sub-task should be able to operate independently and contribute a distinct piece of analysis to the final decision.

---

## 🎬 Transcript (English)

Thank you. Let's take a look at another workflow. We're going to change up our application a little bit this time around. We're still going to ask the user to drag and drop an image of a part onto the screen. But this time, we're going to give the user back an analysis, a report that's going to tell the user the best material to build their part out of, depending upon some various criteria. To implement this feature, we might take the user's supplied image and send it off to Claude along with a short prompt. And in the prompt, we might ask Claude to decide whether it would be best to make this part out of metal, polymer ceramic, and so on. Now, this would probably work, but we are really asking a lot out of Claude in this very simple prompt. For example, we haven't really told Claude any of the real considerations that it should take into account when deciding which material to use. So, even though this might work, we might not get the best results. So a natural improvement here would be probably to go back to this prompt and add in a lot more detail. Maybe tell Claude some of the different scenarios in which it should recommend metal or polymer and so on. So we might end up with a really, really large prompt like this. We might give some criteria for deciding when to use metal and then some criteria for deciding when to use polymer and then repeat with ceramic composite last mere wood and so on. We would end up with a really, really large prompt that might end up being a little bit confusing to Claude because it has to do a lot of analysis and a lot of work inside of one single step. So this might not lead to the best results. Let me show you a better way to approach implementing this feature. We could decide to make a series of different requests in parallel off to Claude whenever a user initially submits an image. Each individual request could then include a specialized prompt asking Claude if making this given part would be a good idea using metal or polymer or ceramic or composite and so on. So in each separate request, we are asking Claude for the suitability of building this part in one individual material. With this approach, we could specialize each individual prompt for the given material. And now, Claude doesn't have to worry about all these different materials. It's really just focused on one individual material at a time. Now, when we eventually get some responses back from Claude, I'm going to change the structure of this diagram just a little bit so I can fit everything on one screen. So we're going to get back these individual analysis results from Claude. Each one is going to tell us the suitability of building out the given part in, say, metal, polymer, ceramic, composite, and so on. We can then take each of these analysis results and then feed them back into Claude in a follow request and ask Claude to consider each of the different analysis results and decide upon a final material to use. Now, Claude doesn't really have to worry about comparing all these different materials up front. Instead, it can just take a look at the analysis results that seem to be the most promising. This is an example of a parallelization workflow. The idea behind a parallelization workflow is that we're going to take one task and break it up into multiple different subtasks. Each of these subtasks can be ran in parallel, so at the same time. We will then take the results from all those different subtasks and then join them all together in a final aggregator step. In our case, the aggregator was this final step with Claude right here. So we fed the results of each parallel task into the aggregator and Claude gave us this final recommendation. There are several benefits to this workflow. First, it allows Claude to focus on one task at a time. So remember just a moment ago when I told you that we could feed the original image part into Claude with a really large prompt that listed out some criteria for many different material types. In this scenario, Claude might get a little bit confused or distracted as it tried to consider all the different pros and cons of each material simultaneously. The second benefit is that we can very easily improve and evaluate the prompts that are being used inside of each subtask. Finally, this flow can generally scale very well. We can add in additional subtasks at any point if we want to without really subtracting from the other subtasks that are being executed.

---

## 🎬 トランスクリプト（日本語）

ありがとうございます。別のワークフローを見てみましょう。今回は アプリケーションを少し変更します。 ユーザーには部品の画像をドラッグ＆ドロップして 画面に配置してもらいますが、今回はユーザーに 分析結果、つまりレコメンドされた 材料に関するレポートを提供します。これは、さまざまな 基準に基づいて部品を作成するための最良の材料を ユーザーに伝えます。この機能を実装するには、ユーザーが提供した 画像をClaudeに送り、短いプロンプトを付けます。 プロンプトでは、Claudeにこの部品を金属、ポリマー、セラミックの どれで作るのが最適か判断するように依頼するかもしれません。 これはおそらく機能するでしょうが、非常に簡単な プロンプトでClaudeに多くのことを求めていることになります。 例えば、Claudeが材料を選択する際に考慮すべき 実際の考慮事項を何も伝えていません。したがって、 これは機能するかもしれませんが、最良の結果が得られない可能性があります。 ですから、ここではプロンプトに戻って、より多くの詳細を追加するのが 自然な改善でしょう。金属やポリマーなどを推奨すべき さまざまなシナリオをClaudeに伝えるかもしれません。 したがって、このような非常に長いプロンプトになる 可能性があります。金属を使用する場合の決定基準をいくつか示し、 次にポリマーを使用する場合の決定基準を示し、 その後、セラミック、コンポジット、 最後の金属や木材などで繰り返します。 非常に長いプロンプトになり、Claudeにとって少し 混乱する可能性があります。なぜなら、1つの ステップで多くの分析と多くの作業を行う必要があるからです。 したがって、これは最良の結果につながらないかもしれません。 この機能を実装するための、より良い方法を紹介します。 ユーザーが画像を提供するたびに、Claudeに複数の リクエストを並行して送信することにします。 各リクエストには、この部品を金属、ポリマー、セラミック、 コンポジットなどで作成することが良い考えかどうかを 尋ねる、特化したプロンプトを含めることができます。 したがって、各個別のリクエストでは、Claudeに 部品を1つの素材で構築する適合性について尋ねます。 このアプローチでは、各個別のプロンプトを 特定の素材に合わせて専門化できます。 そして今、Claudeはこれらのさまざまな材料すべてを 心配する必要はありません。実際には一度に1つの材料に 集中しています。さて、Claudeから応答を受け取ったら、 すべてを1画面に収めるために、このダイアグラムの構造を少し変更します。 したがって、個別の分析結果を受け取ります。それぞれが、この部品を 例えば金属、ポリマー、セラミック、コンポジットなどで 製造することの適合性を伝えます。 その後、これらの各分析結果を取得し、 フォローアップリクエストでClaudeにフィードバックし、 Claudeに各分析結果を考慮して、最終的な材料を 決定するように依頼できます。これにより、Claudeは 最初にすべての異なる材料を比較することを心配する必要はありません。 代わりに、最も有望な分析結果を確認するだけです。 これは並列化ワークフローの例です。並列化 ワークフローのアイデアは、1つのタスクを複数の 異なるサブタスクに分割することです。 これらのサブタスクはそれぞれ並行して実行でき、 同時に実行されます。その後、すべての異なるサブタスクからの結果を 取得し、最終的なアグリゲータステップで結合します。 この場合、アグリゲータはここにあるClaudeによる最終ステップでした。 したがって、各並列タスクの結果をアグリゲータに渡し、 Claudeが最終的な推奨を提供しました。このワークフローにはいくつかの 利点があります。まず、Claudeが一度に1つのタスクに 集中できるようになります。先ほど、元の部品の画像を、 多くの異なる材料タイプの基準をリストした非常に 長いプロンプトとともにClaudeに渡すことができると言いましたが、 このシナリオでは、Claudeはすべての異なる材料の長所と短所を 同時に考慮しようとするときに、少し混乱したり、気が散ったりする可能性があります。 2番目の利点は、各サブタスクで使用されている プロンプトを非常に簡単に改善および評価できることです。 最後に、このフローは一般的に非常によくスケーリングします。 必要に応じていつでも追加のサブタスクを追加できますが、 実行中の他のサブタスクを損なうことはありません。
