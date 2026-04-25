# 78. Chaining workflows

**URL:** https://anthropic.skilljar.com/claude-with-the-anthropic-api/287800
**Section:** 11 Agents and workflows

---

## 📄 Page Content

Anthropic Academy
    
  

  
    
      Courses
    
  

    

    
      
      

      
        
          My Profile
        
        
      

      
      

      
        Sign Out
      
    
  

  

  

    
    
    
        
            
    
        
    

            
    
        
        
            
                
                    
                        
                            
                                
                            

                            
                                details
                            

                            
                        
                    
                
            
            
                
                
                
                    Chaining workflows
                    
                
                
                    
                        
                            
                                
                                    

    
    

    
    
        
            
        
        
            
                
                This video is still being processed. Please check back later and refresh the page.
            
        
        
            
                Uh oh! Something went wrong, please try again.
            
        
    

    

                                
                            
                        
                    
                
            
        
        
            

    
        
            
                
                    
                        
                            
                        
                    
                
            
            
                
                    Summary
                

                

            
        

        
            
                
                    
                        
                            Summary

                            
                                Chaining workflows might seem obvious at first, but they're actually one of the most useful patterns you'll encounter when working with Claude. This approach becomes especially valuable when you're dealing with complex tasks or long prompts that Claude struggles to handle consistently.

What is Workflow Chaining?

A chaining workflow breaks down a large, complex task into smaller, sequential subtasks. Instead of asking Claude to do everything at once, you split the work into focused steps that build on each other.

Here's a practical example: imagine you're building a social media marketing tool that creates and posts videos automatically. Rather than asking Claude to handle everything in one massive prompt, you could break it down like this:

Find related trending topics on Twitter
Select the most interesting topic (using Claude)
Research the topic (using Claude)
Write a script for a short format video (using Claude)
Use an AI avatar and text-to-speech to create a video
Post the video to social media

Why Chain Instead of One Big Prompt?

You might wonder why not just combine all the Claude tasks into a single prompt. The key benefit is focus - when you give Claude one specific task at a time, it can concentrate on doing that task well rather than juggling multiple requirements simultaneously.

The chaining approach offers several advantages:

Split large tasks into smaller, non-parallelizable subtasks
Optionally do non-LLM processing between each task
Keep Claude focused on one aspect of the overall task

The Long Prompt Problem

Here's where chaining becomes really valuable. You'll often encounter situations where you need Claude to write content with many specific constraints. Let's say you want Claude to write a technical article, and you specify that it should:

Not mention that it's written by an AI
Avoid using emojis
Skip clichéd or overly casual language
Write in a professional, technical tone

Even with all these constraints clearly stated, Claude might still produce content that violates some of your rules. You might get back an article that still uses emojis, mentions AI authorship, or sounds unprofessional.

The Chaining Solution

Instead of fighting with one massive prompt, use a two-step chaining approach:

Step 1: Send your initial prompt and accept that the first result might not be perfect. Claude will generate an article, but it might violate some of your constraints.

Step 2: Make a follow-up request that focuses specifically on fixing the issues. Provide the article Claude just wrote and give it targeted revision instructions:

Revise the article provided below.

Follow these steps to rewrite the article:
1. Identify any location where the text identifies the author as an AI and remove them
2. Find and remove all emojis  
3. Locate any cringey writing and replace it with text that would be written by a technical writer

This approach works because Claude can focus entirely on the revision task rather than trying to balance content creation with constraint adherence.

When to Use Chaining

Chaining workflows are particularly useful when:

You have complex tasks with multiple requirements
Claude consistently ignores some constraints in long prompts
You need to process or validate outputs between steps
You want to keep each interaction focused and manageable

While chaining might seem like extra work, it often produces better results than trying to cram everything into a single prompt. The key is recognizing when a task is complex enough to benefit from being broken down into focused, sequential steps.

---

## 🎬 Transcript (English)

The next workflow that we're going to take a look at is going to seem a little bit obvious and simple, but trust me, this actually ends up being one of the most useful workflows around, specifically in one particular situation that you're going to run into very often. So let's get to it. Let's change up our application a little bit once again. We'll imagine that we are building a social media marketing tool. Users will be asked to enter a topic for when their social media accounts, kind of what the focus of their account is. Then the goal of our application is to generate and post some videos to their account. So here's how we might actually implement this. We don't really need a fancy agent with a ton of fancy tools to implement this. We can build out a workflow that will just go through a series of predefined steps one by one. So in step one, we might take whatever topic the user entered into that form and do a search for trending topics on Twitter. We could then take the list of topics and feed them all into Claude and ask Claude to select the most interesting topic. Then we could do a follow-up request to Claude asking to do some web research on the topic. Then once the research is complete, we could ask Claude to write a script for a short format video. Once we have the script, we could then use an AI avatar and some text-to-speech program to create an actual video and finally post that video off to social media. This is an example of a chaining workflow. In a chaining workflow, we take one large task, which was initially to generate some videos and post them to social media, and we break it up into a series of distinct steps. In our case, the subtasks were the individual calls that we sent off to Claude. We could have attempted to accomplish all three of these tasks inside of a single call off to Claude. So we could have just fed in a list of topics to Claude, asked it to select the most interesting topic, and research the topic, and write a script inside of a single prompt. But by breaking this up into three separate calls, we allow Claude to focus on just one individual task at a time. Now, like I said, this probably seems like a kind of simple and obvious workflow, maybe not even worth discussing because it might be something you've already implemented in the past. But there's one very particular reason that I point out this workflow in particular because it actually ends up being on the most important workflow to understand to get quality outputs out of Claude consistently when using rather large prompts. So let me walk you through a little scenario. You might not have encountered this before, but I can almost guarantee that you will at some point in time. Let's imagine that you are making use of Claude to write an article on some given topic. You might initially just send in a very simple prompt to Claude and ask it to write an article, and then you might get back some results, and although it might be okay, there might be some aspects to it that you don't like. So you might initially find that Claude might be mentioning the fact that it is an AI authoring the article, which you probably don't want. It might make excessive use of emojis, which you might not want. And it might use a little bit cliched language all over the place, which, again, you might not want. And so over time, as you start to develop this prompt, you might eventually set up a big long list of things that you tell Claude to just not do it all. But inevitably, Claude might eventually, no matter how many times you repeat these items, Claude might give you back a response that seems to somehow always use emojis, mention the fact that it has been written by an AI, and just generally have kind of a cringey, non-professional tone to it. And Claude might persist in writing an article like this, no matter how many times you repeat these constraints or things that Claude should not do. So to address this problem, you can use a very simple prompt-chaining workflow. Here's what you might do. You might feed in that initial long prompt that has all these constraints in it, and then just accept that you are going to get back some initial article that doesn't really fit the bill of what you're looking for. Claude might inevitably decide to violate some of the different constraints you laid out. To fix those issues, you could then make a follow-up request back to Claude, providing the article that Claude just wrote. And underneath the article, you could ask Claude to rewrite the article in some particular way. So you could say, find any location where the author identifies as an AI and remove that mention, find and remove all emojis, and then write the text in a way that a professional technical writer would do it. By using this chaining workflow and breaking the task up into multiple steps, you allow Claude to focus much more on each individual task presented to it. So even though it might not really satisfy all the requirements you put into the long prompt originally, the follow-up prompt allows Claude to focus on just the restrictions that you really care about, and will hopefully rewrite the article in a style that you are really looking for. So once again, even though prompt chaining seems like something kind of obvious and simple, this does end up being something that you're going to use rather often, anytime that you have a task for Claude with many constraints, and Claude doesn't seem to be always following those constraints as much as you might expect.

---

## 🎬 トランスクリプト（日本語）

次に紹介するワークフローは、 少し明白で単純に見えるかもしれませんが、信じてください。 これは実際、最も有用なワークフローの1つとなるのです。 特に、非常に頻繁に遭遇する 1つの状況においてです。では、始めましょう。 アプリケーションをもう一度少し変更しましょう。 ソーシャルメディアマーケティングツールを構築していると想像してください。ユーザーは ソーシャルメディアアカウントのトピック、つまりアカウントの焦点は何かを 入力するように求められます。 そして、私たちのアプリケーションの目標は 動画を生成して投稿することです。 では、これをどのように実装するか見ていきましょう。 凝ったツールをたくさん持つ、凝ったエージェントは必要ありません。 事前に定義された一連のステップを 順番に実行するワークフローを構築できます。 ステップ1では、ユーザーが入力した トピックを取り上げ、Twitterでトレンドになっている トピックを検索します。 次に、トピックのリストを取り込み、すべてClaudeに渡し、 最も興味深いトピックを選択するように依頼します。 その後、Claudeに追加でリクエストを送信し、 そのトピックに関するウェブでの調査を行うように依頼します。 調査が完了したら、短いフォーマットの動画の スクリプトをClaudeに作成するように依頼できます。 スクリプトができたら、AIアバターと テキスト読み上げプログラムを使用して、実際の動画を作成し、 最後にその動画をソーシャルメディアに投稿します。 これはチェーンワークフローの例です。 チェーンワークフローでは、最初に 動画を生成してソーシャルメディアに投稿するという1つの大きなタスクを、 一連の個別のステップに分割します。 この場合、サブタスクはClaudeに送信した個々の呼び出しでした。 3つのタスクすべてを1つのClaudeへの呼び出しで実行することもできました。 つまり、トピックのリストをClaudeに渡し、 最も興味深いトピックを選択し、トピックを調査し、 単一のプロンプトでスクリプトを作成するように依頼できたはずです。 しかし、これを3つの別々の呼び出しに分割することで、 Claudeが一度に1つの個別のタスクに集中できるようにします。 さて、先ほども言いましたが、これはおそらく 単純で明白なワークフローであり、 すでに過去に実装したことがあるかもしれないので、 議論する価値もないと思うかもしれません。 しかし、このワークフローを特に取り上げる 非常に重要な理由があります。 それは、品質の高い出力をClaudeから一貫して得るために 理解する必要がある最も重要なワークフローの1つであるからです。 比較的大規模なプロンプトを使用する場合にです。 それでは、少しシナリオを説明しましょう。 まだ経験していないかもしれませんが、私は 皆さんがいつか必ず経験すると保証できます。 Claudeを使って、与えられたトピックについて記事を書かせていると 想像してみてください。 最初にシンプルなプロンプトを送って記事を書くように依頼し、 それから結果を受け取ったとします。それは悪くないかもしれませんが、 気に入らない部分があるかもしれません。 たとえば、Claudeが記事を執筆しているのがAIであると 言及していることに気づくかもしれません。それはおそらく望まないでしょう。 絵文字を使いすぎているかもしれません。それは望まないかもしれません。 そして、どこにでもあるような使い古された言葉を使っているかもしれません。これも、 望まないかもしれません。 したがって、時間が経つにつれて、このプロンプトを開発していくと、 最終的にClaudeに絶対にしないように指示する 長文のリストを設定するかもしれません。 しかし、必然的に、Claudeは これらの項目を何度繰り返しても、なぜか常に 絵文字を使用し、AIによって書かれたことを言及し、 全体的に少しばかり気まずい、専門的でない トーンを持っているように見える応答を返すかもしれません。 そして、Claudeは、これらの制約や Claudeがすべきでないことを何度繰り返しても、 このような記事を書き続けるかもしれません。 この問題に対処するために、 非常にシンプルなプロンプトチェーンワークフローを使用できます。 そこで、あなたはこれらの制約すべてを含む 最初の長いプロンプトを入力し、 目的に合わない最初の記事が返ってくることを受け入れるかもしれません。 Claudeは、設定したさまざまな制約のいくつか を違反する可能性があります。 これらの問題を解決するために、 Claudeに再度フォローアップリクエストを送信し、 Claudeがちょうど書いた記事を提供できます。 そして、記事の下に、特定の方法で記事を 書き直すようにClaudeに依頼できます。 例えば、著者がAIであることを示している場所があれば それを削除するように尋ね、すべての絵文字を検索して削除し、 プロのテクニカルライターが行うような方法でテキストを記述するように 依頼できます。このチェーンワークフローを使用し、タスクを 複数のステップに分割することで、Claudeは 提示された個々のタスクに集中できるようになります。 そのため、元の長いプロンプトに入力した 要件をすべて満たせない場合でも、 フォローアッププロンプトにより、Claudeは 本当に重要な制約にのみ集中でき、 あなたが探しているスタイルで記事を書き直してくれるでしょう。 したがって、プロンプトチェーンは 明白で単純なもののように見えますが、これは 非常に頻繁に使用するものになります。 Claudeに多くの制約があるタスクがあり、 Claudeが期待するほど常にそれらの制約に従っていないように見える場合です。 その場合です。
