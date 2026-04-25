# 02. Overview of Claude models

**URL:** https://anthropic.skilljar.com/claude-with-the-anthropic-api/287722
**Section:** 02 Anthropic overview

---

## 📄 Page Content

Anthropic Academy
    
  

  
    
      Courses
    
  

    

    
      
      

      
        
          My Profile
        
        
      

      
      

      
        Sign Out
      
    
  

  

  

    
    
    
        
            
    
        
    

            
    
        
        
            
            
                
                
                
                    Overview of Claude models
                    
                
                
                    
                        
                            
                                
                                    

    
    

    
    
        
            
        
        
            
                
                This video is still being processed. Please check back later and refresh the page.
            
        
        
            
                Uh oh! Something went wrong, please try again.

---

## 🎬 Transcript (English)

In this video, we are going to examine Claude's three model families and understand which one is right for your specific use case. To help you understand how these models differ, I'm going to walk you through each model's key characteristics and then show you a simple framework for picking the right one. Before we dive into the specifics, let me make one thing clear. All three of these models share Claude's core capabilities, so they can all handle text generation, coding, image analysis, and many other tasks. The real difference between them is how they are optimized. One is built to focus on intelligence, one for speed and cost efficiency, and one for more of a balance between intelligence and speed. The first is Opus. Opus is Claude's most capable model. And when I say capable, I need to say that this is a model that delivers the highest level intelligence that you can get out of Claude. In practice, that means that Opus is designed for scenarios where you have complex requirements that need a high level of intelligence and planning to complete. It can work independently on complex projects for a long period of time, like a task that can run on for several hours where the model needs to manage multi-step processes and navigate a lot of different requirements on its own without a lot of human intervention. Opus supports what we call reasoning, which means it can provide a quick response for simple tasks or it can spend some time thinking for a more complex task. The downside is that Opus has a moderate latency and a higher cost, and that's really the trade-off that you are making. While you get really high intelligence, it also takes a little bit more time and cost for every request that you make. Next up is Sonnet. Sonnet sits in a kind of sweet spot in Claude's lineup. It has a good balance of intelligence, speed, and cost that makes it really useful for most practical use cases. What makes Sonnet great is its strong coding ability, along with its fast text generation. Many developers like its ability to make precise edits to complex code bases, meaning it can make changes to a project without breaking a lot of existing functionality. Finally, we have Haiku. Haiku is Claude's fastest model, and it's made specifically for applications where response time is really important. One important thing to note around Haiku is that it doesn't support the reasoning capabilities that Opus and Sonnet have. Instead, Haiku is optimized for speed and cost efficiency. And this makes Haiku a really good choice for user-facing apps that need some real-time interactions. Now let's talk about how you decide which of these three models to use for your particular application. The way to think about model selection really comes down to understanding the trade-off between these different models. On the one hand side you've got really high intelligence and on the other side you've got more cost and speed. Opus sits on the intelligence side. It's really intelligent, more expensive, and also has higher latency. Haiku sits on the cost and speed side. It has moderate intelligence, low cost, and the highest speed. And Sonnet is right there in the middle, striking a good balance between these different qualities. So here's how you decide which model to use. You really need to identify or figure out what matters most for your specific use case. If intelligence is your top priority, meaning you have a complex task that needs really strong reasoning, then you probably want to make use of Opus. You are choosing quality, over speed, and cost. If speed is your priority, meaning you have real-time user interactions, or you've got some high-volume processing, where you need to get some responses back as fast as possible, then you want to choose Haiku. If you need more of a balance between intelligence, speed, and cost, which is often the case for most applications, then Sonnet is probably your best choice. One important thing to note here is that many teams don't just pick one model and stick with it. Instead, you might use multiple different models in the same application. You might use Haiku for user-facing interactions where speed is really important, maybe Sonnet for your main business logic, and Opus for the really complex tasks that need some deeper reasoning. So that covers Claude's three model families and how to choose between them. Just so you know, we are most often going to use Claude Sonnet in this course just because it gives us a really fantastic balance of these three different qualities.

---

## 🎬 トランスクリプト（日本語）

このビデオでは、Claudeの 3つのモデルファミリーを調べ、どのモデルがお客様の 特定のユースケースに適しているかを理解します。どのように これらのモデルが異なるかを理解するために、各モデルの 主要な特徴を順を追って説明し、最適なモデルを選択するための シンプルなフレームワークをご紹介します。詳細に入る前に、 1つの点を明確にさせてください。これら3つのモデルすべてが Claudeのコア機能を共有しているため、テキスト生成、コーディング、画像 分析、その他多くのタスクを実行できます。 これらのモデルの本当の違いは、最適化の方法です。 1つはインテリジェンスに焦点を当てて構築され、 1つは速度とコスト効率、そしてもう1つはインテリジェンスと速度の バランスを重視して構築されています。最初のモデルは Opusです。OpusはClaudeで最も高性能なモデルです。 そして、高性能と言ったとき、これはClaudeから得られる 最高のインテリジェンスを提供するモデルであると 言う必要があります。実際には、これは複雑な 要件があり、高いレベルのインテリジェンスと 計画が必要なシナリオのためにOpusが設計されていることを意味します。 完了する必要があります。モデルが 数時間続くタスクのように、長時間にわたって複雑なプロジェクトで 独立して作業できます。そこでは、モデルは 複数ステップのプロセスを管理し、 多くの異なる要件を、あまり人間による介入なしに 自分で処理する必要があります。Opusは、いわゆる 推論をサポートしており、これは、簡単なタスクに対して 迅速な応答を提供できるか、または より複雑なタスクのために時間をかけて考えることができるかを意味します。 欠点は、Opusは中程度の遅延と より高いコストを持つことです。そして、それが本当にあなたがしているトレードオフです。 非常に高いインテリジェンスが得られる一方で、 リクエストごとに少し多くの時間とコストがかかります。 次にご紹介するのはSonnetです。Sonnetは Claudeのラインナップにおいて、ある種のスイートスポットに位置しています。 インテリジェンス、速度、コストの優れたバランスを備えており、 ほとんどの実用的なユースケースで非常に役立ちます。 Sonnetを素晴らしいものにしているのは、その強力なコーディング能力と、 高速なテキスト生成能力です。多くの開発者は 複雑なコードベースへの正確な編集能力を気に入っています。 つまり、既存の機能を大きく壊すことなくプロジェクトに変更を加えられるということです。 最後に、Haikuがあります。HaikuはClaudeで最も高速な モデルであり、応答時間が非常に重要なアプリケーションのために特別に作られています。 Haikuに関して重要な点は、それがOpusやSonnetが持つ 推論能力をサポートしていないことです。代わりに、 Haikuは速度とコスト効率に最適化されています。 そして、これはHaikuをリアルタイムのインタラクションが必要な ユーザー向けのアプリにとって非常に良い選択肢にします。 さて、これらの3つのモデルの中から、お客様の特定のアプリケーションに どれを使用するかを決定する方法について説明しましょう。モデルを選択する際に 考慮すべき点は、これらの異なるモデル間のトレードオフを理解することです。 一方では非常に高いインテリジェンスがあり、 もう一方ではコストと速度があります。 Opusはインテリジェンス側に位置しています。非常にインテリジェントで、 より高価で、遅延も大きいです。Haikuは コストと速度側に位置しています。中程度のインテリジェンス、 低コスト、そして最高の速度を備えています。そして Sonnetはちょうどその真ん中に位置し、これらの異なる品質のバランスを うまく取っています。したがって、使用するモデルを決定する方法は次のとおりです。 特定のユースケースにとって最も重要なのは何かを特定または把握する必要があります。 インテリジェンスが最優先事項である場合、つまり、 非常に強力な推論を必要とする複雑なタスクがある場合、 その場合はOpusを利用することをお勧めします。 品質を速度とコストよりも優先しています。速度が 優先事項である場合、つまり、リアルタイムのユーザーインタラクションがある場合、 または、可能な限り迅速に応答を得る必要がある高頻度の処理がある場合、 その場合はHaikuを選択する必要があります。インテリジェンス、 速度、コストのバランスが必要な場合、これはほとんどの アプリケーションでそうであるように、Sonnetはおそらく最良の選択肢です。 ここで重要なのは、多くのチームが1つのモデルを選択してそれに固執するわけではないということです。 代わりに、同じアプリケーションで複数の異なるモデルを使用する場合があります。 速度が非常に重要なユーザー向けのインタラクションにはHaikuを、 メインのビジネスロジックにはおそらくSonnetを、そして より深い推論を必要とする非常に複雑なタスクにはOpusを使用するかもしれません。 これで、Claudeの3つのモデルファミリーと、それらの間で選択する方法についての説明は終わりです。 念のためお伝えしておくと、このコースでは、これら3つの異なる品質の 優れたバランスを提供してくれるため、Claude Sonnetを最も頻繁に使用する予定です。 この優れたバランスを提供してくれるため、Claude Sonnetを最も頻繁に使用する予定です。
