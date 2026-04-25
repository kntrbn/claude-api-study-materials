# 76. Agents and workflows

**URL:** https://anthropic.skilljar.com/claude-with-the-anthropic-api/287796
**Section:** 11 Agents and workflows

---

## 📄 Page Content

Anthropic Academy
    
  

  
    
      Courses
    
  

    

    
      
      

      
        
          My Profile
        
        
      

      
      

      
        Sign Out
      
    
  

  

  

    
    
    
        
            
    
        
    

            
    
        
        
            
                
                    
                        
                            
                                
                            

                            
                                details
                            

                            
                        
                    
                
            
            
                
                
                
                    Agents and workflows
                    
                
                
                    
                        
                            
                                
                                    

    
    

    
    
        
            
        
        
            
                
                This video is still being processed. Please check back later and refresh the page.
            
        
        
            
                Uh oh! Something went wrong, please try again.
            
        
    

    

                                
                            
                        
                    
                
            
        
        
            

    
        
            
                
                    
                        
                            
                        
                    
                
            
            
                
                    Summary
                

                

            
        

        
            
                
                    
                        
                            Summary

                            
                                Workflows and agents are strategies for handling user tasks that can't be completed by Claude in a single request. You've actually been creating both throughout this course - when you used tools and let Claude figure out how to complete tasks, that was an agent.

When to Use Workflows vs Agents

The decision comes down to how well you understand the task:

Use workflows when you can picture the exact flow or steps that Claude should go through to solve a problem, or when your app's UX constrains users to a set of tasks
Use agents when you're not sure exactly what task or task parameters you'll give to Claude

Workflows are a series of calls to Claude meant to solve a specific problem through a predetermined series of steps. Agents give Claude a goal and a set of tools, expecting Claude to figure out how to complete the goal through the provided tools.

Example: Image to CAD Workflow

Let's look at a practical workflow example. Imagine building a web app where users drag and drop an image of a metal part, and you create a STEP file (an industry standard for 3D models) from it.

Since we have a pretty good idea of exactly what to do when a user supplies an image file, and we can easily write all of this out with code as a predefined series of steps, this makes a perfect workflow candidate.

Here's how the workflow breaks down:

Feed an image into Claude, asking it to describe the object
Based on the description, ask Claude to use the CadQuery library to model the object
Create a rendering
Ask Claude to grade the rendering against the original image. If there are issues, fix them

The Evaluator-Optimizer Pattern

This modeling workflow is an example of an evaluator-optimizer pattern. Here's how it works:

Producer: Takes input and creates output (Claude using CadQuery to model the part and create a rendering)
Grader: Evaluates the output against some criteria
Feedback loop: If the grader doesn't accept the output, feedback goes back to the producer for improvement
Iteration: The cycle repeats until the grader accepts the output

Why Learn Workflow Patterns

The goal of identifying different workflows is to give you a set of repeatable recipes for implementing your own features. The Evaluator-Optimizer is one workflow pattern that has worked well for other engineers - consider using it in your own app!

Remember, identifying workflows doesn't inherently do anything for us - we still have to write the actual code to implement them. But these patterns have proven successful for many engineers, so they're worth understanding and applying to your own projects.

---

## 🎬 Transcript (English)

In this module, we are going to focus on workflows and agents. Let's dive in immediately and understand what these things are. Workflows and agents are strategies that we use to handle the user tasks that can't be completed by Claude in a single request. Believe it or not, you have already been creating workflows and agents throughout this course. For example, when learning about tools, we fed tasks into Claude and relied upon Claude to figure out how to complete them using some provided tools. That was an example of an agent. Now here's the rule of thumb that we use whenever we are trying to decide whether to create a workflow or an agent. If we have a very precise idea of the task we need to complete and we know the exact series of steps that are used to complete it, we'll use a workflow. Otherwise, if we're not really sure about the details of a task that Claude needs to solve, we'll use an agent. In this video and the next couple, we're going to be 100% focused on workflows. I'm going to show you several examples of workflows, so let's take a look at our first one right now. Let's imagine that we are building a small web application. The goal of this app is to allow a user to drag and drop an image of some metal part onto the screen. We're then going to take that image and then somehow build a 3D model out of it. We're then going to get the user back, something called a step file. Now, if you're not familiar with a step file, toy fine, step file is just an industry standard way of communicating or sharing 3D models. So essentially, we're making a 3D model out of an image. Now, even if you are not very familiar with 3D modeling, with a little bit of help and a little bit of time, I bet you could figure out a way to implement this application. Here's how we might do it. We might take the image that the user uploaded and feed into Claude and ask Claude to describe this object in great detail. Then we could take that description, feed it back into Claude separately, and ask Claude to use a Python library called CAD Query to model the object. CAD Query is a Python library that allows you to do 3D solid modeling, and you can output a step file from that process. Now, it's entirely possible that Claude is not going to get this model entirely accurate the first time around. So once we build out this initial model, we might decide to add in a little error checking step, where we could create a rendering as a plain image, and then feed that image back into Claude and ask it how well this image represents the original image that the user uploaded. And if Claude decides that there are major issues in our rendering, we can then go back to the second step and ask Claude to attempt to render the part again. We can then repeat this process over and over again until hopefully we eventually end up with some kind of accurate model of the original part. Now the important thing to understand here is that this is an entire flow of steps that we can kind of imagine ahead of time. We can sit down and design out this entire process. We could easily write out some code to implement it. As a matter of fact, I have previously implemented something almost exactly like this. Because we can explicitly list out and detail all these steps ahead of time, we would refer to this as a workflow. Remember, we define a workflow as a series of calls off to Claude meant to solve some very specific problem, where we really know exactly what those steps are supposed to be ahead of time. This modeling workflow that I've described is an example of something we call an evaluator optimizer. The idea behind this workflow is that we push some input into something called a producer. In our case, the producer is Claude using the CAD Query library to model a part and then creating a rendering out of it. This output, the rendering, is fed into something called a grader. The grader will look at the output and decide if it meets some criteria. If it does, then the workflow ends. Otherwise, if the output doesn't meet some criteria, feedback is given back into the producer, which gets an opportunity to improve the output in some way. This cycle is then going to keep on repeating until eventually the grader accepts the output. Now, at this point in time, you've probably got a somewhat reasonable idea of what this evaluator optimizer thing is all about. But you're probably wondering, OK, what exactly is going on with these workflows? So there's just something I want to clarify here really quickly. Identifying workflows doesn't really inherently do anything for us. We still have to write down and write out the actual code to implement these things. The only reason that we are discussing workflows and the reason that you're going to see workflows as a popular discussion topic is that many other engineers have implemented workflows using these exact same patterns and found a lot of success. So the reason I'm showing you these different workflows is so that you can use these same patterns on your own projects and hopefully find some success with them because they have worked well for other engineers.

---

## 🎬 トランスクリプト（日本語）

このモジュールでは、ワークフローと エージェントに焦点を当てます。すぐに飛び込んで理解しましょう これらのものが何であるか。ワークフローとエージェントは 単一のリクエストで完了できないユーザーのタスクを処理するために使用する戦略です。 信じてもらえなくても、あなたはすでにワークフローとエージェントを作成しています。 エージェント。このコース全体で。例えば、ツールの学習時に 、タスクをClaudeに入力し 、提供されたツールを使用してどのように完了するかをClaudeに考えさせました。 それはエージェントの例でした。 ここで、ワークフローまたはエージェントを作成するかどうかを決定しようとするたびに使用する経験則を示します。 ワークフローを作成するかどうかを決定しようとするたびに使用する経験則を示します。 決定するかどうかを決定しようとするたびに使用する経験則を示します。 完了する必要があるタスクについて非常に正確なアイデアがあり、 それを完了するために使用される正確なステップのシーケンスを知っている場合、ワークフローを使用します。そうでなければ それを完了するために使用される正確なステップのシーケンスを知っている場合、ワークフローを使用します。そうでなければ Claudeが解決する必要があるタスクの詳細についてあまり確信がない場合、エージェントを使用します。このビデオでは Claudeが解決する必要があるタスクの詳細についてあまり確信がない場合、エージェントを使用します。このビデオでは 次のいくつかでは、100％ワークフローに焦点を当てます。 私はあなたにいくつかのワークフローの例を示しますので、最初のものをすぐに見てみましょう。 私はあなたにいくつかのワークフローの例を示しますので、最初のものをすぐに見てみましょう。 小さなWebアプリケーションを構築していると想像してみましょう。 このアプリの目標は、ユーザーが金属部品の画像を 画面にドラッグアンドドロップできるようにすることです。 その後、その画像を取得し、何らかの方法で3Dモデルを 構築します。次に、STEPファイルと呼ばれるものをユーザーに戻します。 STEPファイルに慣れていない場合は、STEPファイルを 楽しんでください。STEPファイルは3Dモデルを通信または共有するための業界標準の方法です。 したがって、基本的に、画像から3Dモデルを作成しています。 したがって、基本的に、画像から3Dモデルを作成しています。 3Dモデリングにあまり慣れていない場合でも、少しの助けと少しの時間があれば、 このアプリケーションを実装する方法を見つけられると確信しています。 このように行うかもしれません。ユーザーがアップロードした画像を 取得した画像をClaudeに入力し 、Claudeに詳細に説明するように依頼するかもしれません。 Claudeに詳細に説明するように依頼するかもしれません。 次に、その説明を取得し、Claudeに再度入力し 、CAD QueryというPythonライブラリを使用してオブジェクトをモデリングするように依頼するかもしれません。 CAD Queryは、3Dソリッドモデリングを実行できるPythonライブラリであり 、そのプロセスからSTEPファイルを出力できます。 そのプロセスからSTEPファイルを出力できます。 これで、Claudeが初回でこのモデルを完全に正確に取得できるとは限りません。 これで、Claudeが初回でこのモデルを完全に正確に取得できるとは限りません。 したがって、最初のモデルを構築したら、エラーチェックのステップを少し追加することを決定するかもしれません。 したがって、最初のモデルを構築したら、エラーチェックのステップを少し追加することを決定するかもしれません。 そこで、レンダリングをプレーンな画像として作成し 、その画像をClaudeに再度入力し 、この画像がユーザーがアップロードした元の画像をどれだけよく表しているかを尋ねることができます。 この画像がユーザーがアップロードした元の画像をどれだけよく表しているかを尋ねることができます。 Claudeがレンダリングに重大な問題があると判断した場合 、2番目のステップに戻り、Claudeに再度部品をレンダリングするように依頼できます。 そして、このプロセスを何度も繰り返して 、最終的に元の部品の正確なモデルを入手できることを願っています。 最終的に元の部品の正確なモデルを入手できることを願っています。 ここで重要なのは、これが事前に想像できる一連のステップであるということです。 これが事前に想像できる一連のステップであるということです。 座ってこのプロセス全体を設計できます。 それを実装するためにコードを書くことも簡単です。 事実、私は以前にこれとほぼ同じものを実装しました。 事実、私は以前にこれとほぼ同じものを実装しました。事前にすべてのステップを明示的にリストアップして詳細に説明できるため 、これをワークフローと呼びます。 ワークフローは、非常に特定の問題を解決することを意図した一連のClaudeへの呼び出しとして定義することを覚えておいてください。 ワークフローは、非常に特定の問題を解決することを意図した一連のClaudeへの呼び出しとして定義することを覚えておいてください。 ワークフローは、非常に特定の問題を解決することを意図した一連のClaudeへの呼び出しとして定義することを覚えておいてください。 これらのステップが何であるか正確にわかっている場合。 このモデリングワークフローは、評価者オプティマイザーと呼ばれるものの例です。 このモデリングワークフローは、評価者オプティマイザーと呼ばれるものの例です。 このワークフローの背後にある考え方は、 入力プロデューサーと呼ばれるものにプッシュすることです。 私たちの場合は、プロデューサーはCAD Queryライブラリを使用して部品をモデリングし 、その後レンダリングを作成するClaudeです。 この出力、レンダリングはグレーダーと呼ばれるものに入力されます。 この出力、レンダリングはグレーダーと呼ばれるものに入力されます。 グレーダーは出力を確認し、特定の基準を満たしているかどうかを判断します。 満たしている場合は、ワークフローは終了します。そうでない場合 、出力が特定の基準を満たさない場合、フィードバック がプロデューサーに与えられ、プロデューサーは改善する機会を得ます。 改善する機会を得ます。このサイクル は、グレーダーが出力を受け入れるまで繰り返されます。 グレーダーが出力を受け入れるまで繰り返されます。現時点で、あなたはおそらく この評価者オプティマイザーについてある程度理解しているでしょう。 この評価者オプティマイザーについてある程度理解しているでしょう。しかし、あなたはたぶん、さて、ワークフローでは具体的に何が起こっているのですか？と考えているでしょう。 ワークフローでは具体的に何が起こっているのですか？と考えているでしょう。そこで、ここに簡単に明確にしたいことがあります。 ワークフローを特定しても、私たちにとって何も本質的に意味はありません。 ワークフローを特定しても、私たちにとって何も本質的に意味はありません。 それでも、これらのものを実装するための実際のコードを書き出す必要があります。 それでも、これらのものを実装するための実際のコードを書き出す必要があります。 ワークフローについて話し、ワークフローが人気のある議論トピックである理由は 、多くの他のエンジニアがこれらのまったく同じパターンを使用してワークフローを実装し、多くの成功を見出しているからです。 、多くの他のエンジニアがこれらのまったく同じパターンを使用してワークフローを実装し、多くの成功を見出しているからです。 したがって、これらのさまざまなワークフローを示しているのは、 これらの同じパターンを自分のプロジェクトで使用し、それらで成功を見つけてもらうためです。 これらの同じパターンを自分のプロジェクトで使用し、それらで成功を見つけてもらうためです。 なぜなら、それらは他のエンジニアにとってうまく機能したからです。 なぜなら、それらは他のエンジニアにとってうまく機能したからです。
