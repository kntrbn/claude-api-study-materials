# 82. Workflows vs agents

**URL:** https://anthropic.skilljar.com/claude-with-the-anthropic-api/287794
**Section:** 11 Agents and workflows

---

## 📄 Page Content

Anthropic Academy
    
  

  
    
      Courses
    
  

    

    
      
      

      
        
          My Profile
        
        
      

      
      

      
        Sign Out
      
    
  

  

  

    
    
    
        
            
    
        
    

            
    
        
        
            
                
                    
                        
                            
                                
                            

                            
                                details
                            

                            
                        
                    
                
            
            
                
                
                
                    Workflows vs agents
                    
                
                
                    
                        
                            
                                
                                    

    
    

    
    
        
            
        
        
            
                
                This video is still being processed. Please check back later and refresh the page.
            
        
        
            
                Uh oh! Something went wrong, please try again.
            
        
    

    

                                
                            
                        
                    
                
            
        
        
            

    
        
            
                
                    
                        
                            
                        
                    
                
            
            
                
                    Summary
                

                

            
        

        
            
                
                    
                        
                            Summary

                            
                                When building AI-powered applications, you'll often need to choose between two different architectural approaches: workflows and agents. Each has distinct advantages and trade-offs that make them suitable for different scenarios.

What Are Workflows?

Workflows are a predefined series of calls to Claude designed to solve a known problem or set of problems. You use workflows when you can picture the flow of steps ahead of time - essentially when you know the exact sequence needed to complete a task.

Think of workflows as breaking down a big task into much smaller, more specific subtasks. Each step focuses on a single area, which allows Claude to work more precisely.

What Are Agents?

With agents, Claude gets a set of basic tools and is expected to formulate a plan to use these tools to complete a task. Unlike workflows, you don't know exactly what tasks will be provided, so the system needs to be more adaptive.

Agents can creatively figure out how to handle a wide variety of challenges by combining tools in unexpected ways.

Benefits of Workflows

Claude can focus on one subtask at a time, generally leading to higher accuracy
Far easier to evaluate and test, since you know each exact step
More predictable and reliable execution
Better suited for solving specific, well-defined problems

Benefits of Agents

Allow for more flexible user experience
Far more flexible task completion - Claude can combine tools in unexpected ways to complete a wide variety of tasks
Can handle novel situations that weren't anticipated during development
Can ask users for additional input when needed

Downsides of Workflows

Far less flexible - dedicated to solving specific types of tasks
Generally more constrained user experience - you need to know the exact inputs to the flow
Require more upfront planning and design work

Downsides of Agents

Lower successful task completion rate compared to workflows
More challenging to instrument, test, and evaluate since you often don't know what series of steps an agent will execute
Less predictable behavior

When to Use Each Approach

Your primary goal as an engineer is to solve problems reliably. Users probably don't care that you've built a fancy agent - they want a product that works consistently.

The general recommendation is to always focus on implementing workflows where possible, and only resort to agents when they are truly required. Workflows provide the reliability and predictability that most production applications need, while agents offer flexibility for scenarios where the exact requirements can't be predetermined.

Consider workflows when you have well-defined processes and agents when you need to handle unpredictable, varied user requests that require creative problem-solving.

---

## 🎬 Transcript (English)

Let's wrap up by comparing and contrasting some different aspects of workflows and agents. First, recall that workflows are a predefined series of calls to Claude. We often use workflows when we have a good idea of the exact series of steps that are needed to complete a task. With agents, on the other hand, we don't know exactly what task will be provided, so we instead provide a solid set of basic tools and expect Claude to combine these tools together to complete a given task. You might have noticed that a common theme around workflows is that we take a big task and we divide it up into much smaller tasks. Each of these smaller tasks are much more specific in nature, allowing Claude to focus on a single area at a time. This increased focus generally leads to higher accuracy for completing a task compared to agents. Because we know the exact series of steps that a workflow executes, they're also far easier to test and evaluate. With Agents, we aren't constrained to a series of steps etched in stone. Instead, Claude can creatively figure out how to handle a wide variety of challenges. Along with this flexibility, we also get flexibility in the user experience. While workflows expect to receive a very particular set of inputs, Agents can create their own inputs based on queries received from the user, and Agents can also ask user for more input when it's needed. The downside to agents is that they generally have a lower successful task completion rate compared to workflows because we are delegating so much work to Claude. In addition, they're also harder to test and evaluate, since we often don't have a good idea of what series of steps an agent will execute to complete a given task. At the end of the day, agents are really interesting, but remember, your primary goal as an engineer is to solve problems reliably. Users probably don't care that you've made a fancy agent. They really just want a product that's going to work 100% of the time. So with this in mind, the general recommendation is to always focus on implementing workflows where possible and only resort to agents when they are truly required.

---

## 🎬 トランスクリプト（日本語）

それでは、ワークフローとエージェントのいくつかの 異なる側面を比較対照してまとめましょう。まず、 ワークフローとは、事前に定義された一連の呼び出し であることを思い出してください。ワークフローは、タスクを完了するために 必要な手順が正確にわかっている場合に よく使用します。一方、エージェントでは、 どのようなタスクが提供されるかは正確にはわかりません。そのため、 代わりに、堅実な基本ツールのセットを提供し、 Claudeがこれらのツールを組み合わせて指定されたタスクを 完了することを期待します。ワークフローにおける一般的な テーマとして、大きなタスクを分解して より小さなタスクに分割することがあります。 これらの小さなタスクはそれぞれ、より具体的な性質を持っており、 Claudeは一度に1つの領域に集中することができます。この 集中力の向上は、一般的に、エージェントと比較して タスク完了の精度を高めます。 ワークフローは、実行される手順が正確にわかっているため、 テストと評価もはるかに容易です。 エージェントの場合、石板に刻まれた一連の手順に 制約されません。代わりに、Claudeは さまざまな課題にどのように対処するかを創造的に考え出すことができます。 この柔軟性に加えて、ユーザーエクスペリエンスの 柔軟性も得られます。ワークフローは非常に特定の 入力セットを受け取ることを期待しますが、 エージェントはユーザーからのクエリに基づいて 独自の入力を作成できます。また、エージェントは必要に応じて ユーザーに追加の入力を求めることもできます。エージェントの欠点は、 ワークフローと比較してタスク完了の成功率が低い傾向があることです。これは、 Claudeに多くの作業を委任しているためです。さらに、 テストと評価も困難です。なぜなら、 エージェントが指定されたタスクを完了するために実行する手順の シーケンスを正確に把握していないことが多いためです。 結局のところ、エージェントは非常に興味深いですが、 エンジニアとしての主な目標は、 問題を確実に解決することであることを忘れないでください。ユーザーは、 あなたが派手なエージェントを作成したことなど気にしないでしょう。彼らは 本当に100%機能する製品を求めているだけです。 したがって、これを念頭に置いて、一般的な 推奨事項は、可能な限り常にワークフローの実装に焦点を当て、 エージェントは本当に必要な場合にのみ使用することです。
