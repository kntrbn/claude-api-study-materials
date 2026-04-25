# 79. Routing workflows

**URL:** https://anthropic.skilljar.com/claude-with-the-anthropic-api/287801
**Section:** 11 Agents and workflows

---

## 📄 Page Content

Anthropic Academy
    
  

  
    
      Courses
    
  

    

    
      
      

      
        
          My Profile
        
        
      

      
      

      
        Sign Out
      
    
  

  

  

    
    
    
        
            
    
        
    

            
    
        
        
            
                
                    
                        
                            
                                
                            

                            
                                details
                            

                            
                        
                    
                
            
            
                
                
                
                    Routing workflows
                    
                
                
                    
                        
                            
                                
                                    

    
    

    
    
        
            
        
        
            
                
                This video is still being processed. Please check back later and refresh the page.
            
        
        
            
                Uh oh! Something went wrong, please try again.
            
        
    

    

                                
                            
                        
                    
                
            
        
        
            

    
        
            
                
                    
                        
                            
                        
                    
                
            
            
                
                    Summary
                

                

            
        

        
            
                
                    
                        
                            Summary

                            
                                Routing workflows solve a common problem in AI applications: different types of user requests need different handling approaches. Instead of using a one-size-fits-all prompt, you can categorize incoming requests and route them to specialized processing pipelines.

The Problem with Generic Prompts

Consider a social media marketing tool that generates video scripts from user topics. A user might enter "programming" or "surfing" as their topic, but these should produce very different types of content:

Programming topics call for educational content with clear explanations and definitions. Surfing topics work better with entertainment-focused scripts that emphasize excitement and visual appeal. A single generic prompt can't handle both effectively.

Setting Up Content Categories

The first step is defining the different types of content your application might need to generate. You might categorize requests into genres like:

Entertainment - High-energy, culturally relevant content with trendy language
Educational - Clear, engaging explanations with relatable examples
Comedy - Sharp, unexpected content with clever observations and timing
Personal vlog - Authentic, intimate content with conversational storytelling
Reviews - Decisive, experience-based content highlighting strengths and weaknesses
Storytelling - Immersive content using vivid details and emotional connection

Each category gets its own specialized prompt template. For example, the educational prompt might ask Claude to "develop a clear, engaging script that transforms complex information into digestible insights using relatable examples and thought-provoking questions."

How Routing Works in Practice

The routing process happens in two steps:

Categorization - Send the user's topic to Claude with a request to categorize it into one of your predefined genres
Specialized Processing - Use the category result to select the appropriate prompt template and generate content

For example, if a user enters "Python functions" as their topic, you'd first ask Claude to categorize it:

Categorize the topic of a video into one of the listed categories:
<topic>Python functions</topic>

<categories>
- Educational
- Entertainment  
- Comedy
- Personal vlog
- Reviews
- Storytelling
</categories>

Claude responds with "Educational", so you then use the educational prompt template to generate the actual script content.

Routing Workflow Architecture

A routing workflow follows this pattern:

User input goes to a router component first
The router categorizes the request using an initial Claude call
Based on the category, the input gets forwarded to one specific processing pipeline
Each pipeline can have its own workflow, prompts, or tools optimized for that category

The key insight is that user input only goes to one specialized pipeline, not all of them. This allows each pipeline to be highly optimized for its specific use case.

When to Use Routing

Routing workflows work well when:

Your application handles diverse types of requests that need different approaches
You can clearly define categories that cover your use cases
The categorization step can be handled reliably by Claude
The performance benefit of specialized processing outweighs the overhead of the routing step

This pattern is especially valuable for customer service bots, content generation tools, and any application where the "right" response depends heavily on understanding the type of request being made.

---

## 🎬 Transcript (English)

Our next workflow is going to show us one way of improving this social media marketing tool. So once again, we'll imagine that a user is going to enter in a topic, we're then going to produce some videos somehow, and post them to a user's social media account. Now, there's something I really want you to think about about the script generation process. In other words, the actual tone and language used in these different videos. Given two different topics, such as programming on the left hand side, and maybe surfing on the right hand side, we would really expect to get video scripts that are very, very different in nature. So on the left hand side with programming, we would want to get a lot of information, carefully explain definitions, and probably just overall a video that is meant to be educational in nature. And if user entered in surfing as a topic, we would probably want to get back a very different video script. Probably something that is much less educational in nature and doesn't have a long definition on what surfing is or anything like that. So let me show you a workflow that we could use to make sure that a given topic will result in a video script that fits the nature of that topic really well. First, we would sit down and think about all the different possible genres of videos that users might ask us to create. So we might decide that the topics that users are going to give to us are going to fit into one of six different genres. Entertainment, educational, comedy, and so on. So in our example back over here, programming might be educational and surfing might be entertainment. Then for each of these different genres, we might write out a script generation prompt. So if someone asks for a topic that we categorize as being educational in nature, we would ask Claude to write a script using this prompt right here. And the prompt is asking Claude to make a clear, engaging script that has some interesting examples and interesting questions and so on. If the user gives us a topic of surfing, we might categorize that as being entertainment. So then we would take this prompt right here, put in the topic as surfing and feed the whole prompt into Claude and ask Claude to write a script about surfing that maybe has some trendy language and engaging hooks and so on. So let me show you what this entire flow would look like in practice. We would initially send a request off to Claude that contained just the topic the user had entered, maybe something like Python functions, and ask Claude to categorize this topic into one of our different categories that we just came up with. In this scenario, Python functions might be most closely related to the category of educational. So then we would take this response from Claude and then make a follow up request asking Claude to write a script that has some clear, engaging information about Python functions that has thought provoking examples. And then presumably we would get back some script with those different qualities and a tone appropriate for an educational video. This is an example of a routing workflow. In a routing workflow, we are going to take the user's original input and feed it into a routing step. This routing step will probably be a call to Claude itself, asking Claude to categorize the user input or task in some way. Then, depending upon Claude's answer, we're going to forward the user's input onto some very particular follow up processing pipeline. So maybe this one right here, or this one right here, or this one right here, and so on. But probably only one of these different three. Each of these different routing options might have a different workflow implemented inside of it or a customized prompt or a customized set of tools that are specialized for handling the exact task that the user is asking for.

---

## 🎬 トランスクリプト（日本語）

次のワークフローでは、この改善方法を ソーシャルメディアマーケティングツールで見ていきます。再度、私たちが想像するのは ユーザーがあるトピックを入力すること、そしてそれから 何らかの方法でビデオを生成し、それを ユーザーのソーシャルメディアアカウントに投稿することです。さて、 スクリプト生成プロセスについて、皆さんにぜひ考えてほしいことがあります。 つまり、これらの異なるビデオで使用される実際のトーンや言語です。 例えば、左側がプログラミング、右側が サーフィンといった2つの異なるトピックがあった場合、 ビデオスクリプトは性質が大きく異なるものを 期待するでしょう。左側のプログラミングでは、 多くの情報や注意深く説明された定義、そして おそらく全体的に教育的な性質を持つビデオを 期待するでしょう。そしてもし ユーザーがトピックとしてサーフィンを入力した場合、 まったく異なるビデオスクリプトを期待するでしょう。おそらく 教育的な性質は少なく、サーフィンが 何であるかについての長い定義などを含まない 何かでしょう。そこで、与えられたトピックが そのトピックの性質に非常によく合うビデオスクリプトを 生成することを保証するために使用できる ワークフローを示しましょう。まず、私たちは ユーザーが作成を依頼する可能性のある、 さまざまなビデオジャンルについてすべて考えます。 つまり、ユーザーが提供するトピックは、6つの異なる ジャンルのいずれかに分類されると決定するかもしれません。 エンターテイメント、教育、コメディ、 などです。私たちの例に戻ると、プログラミングは 教育的であり、サーフィンはエンターテイメントかもしれません。 次に、これらの異なるジャンルごとに、 スクリプト生成プロンプトを作成するかもしれません。教育的だと 私たちが見なすトピックをリクエストした場合、 Claudeにこのプロンプトを使用してスクリプトを作成するように 依頼します。そしてそのプロンプトは、Claudeに 明確で魅力的なスクリプトで、興味深い 例や興味深い質問などを含めるように求めています。ユーザーが サーフィンというトピックを提供した場合、それは エンターテイメントに分類されるかもしれません。そのため、このプロンプトを 取り上げ、トピックとしてサーフィンを入力し、 プロンプト全体をClaudeに渡して、 スクリプトを作成するように依頼します。たとえば、トレンドの 言葉や魅力的なフックなどを含んだ サーフィンに関するスクリプトです。この ワークフロー全体が実際にはどのようになるかを示しましょう。 最初に、Claudeにユーザーが入力したトピック、例えば Python関数などだけを含むリクエストを送信し、 Claudeにこのトピックを、私たちが考えた さまざまなカテゴリのいずれかに分類するように依頼します。 このシナリオでは、Python関数は 教育カテゴリに最も近いかもしれません。そのため、このClaudeからの応答を受け取り、 フォローアップリクエストを作成し、Claudeに スクリプトを作成するように依頼します。それは、 Python関数に関する明確で魅力的な情報を含み、 示唆に富む例を含むものです。そしておそらく、 これらの異なる特性を持つスクリプトが 返され、教育ビデオに適したトーンになります。これは ルーティングワークフローの例です。 ルーティングワークフローでは、ユーザーの元の入力を受け取り ルーティングステップに渡します。このルーティング ステップはおそらくClaude自体への呼び出しで、 Claudeにユーザーの入力またはタスクを 何らかの方法で分類するように依頼します。次に、Claudeの 回答に応じて、ユーザーの入力を 特定のフォローアップ処理パイプラインに転送します。つまり、 こちらかもしれませんし、こちら、またはこちらかもしれません。 しかし、おそらくこれら3つのうちの1つだけでしょう。 これらの異なるルーティングオプションのそれぞれには、 異なるワークフローが実装されているか、カスタマイズされたプロンプト、 あるいはユーザーが要求している正確なタスクを 処理するために特化されたツールのセットが 含まれている可能性があります。
